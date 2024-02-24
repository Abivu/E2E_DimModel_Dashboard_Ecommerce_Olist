DimCustomer = """
                INSERT INTO olist_olap.DimCustomer( CustomerID,
                                                    CustomerUniqueID, 
                                                    CustomerState, 
                                                    CustomerCity, 
                                                    CustomeZIPCode, 
                                                    ValidFrom, 
                                                    ValidTo, 
                                                    IsCurrent)
                SELECT 
                    customer_id,
                    customer_unique_id,
                    customer_state,
                    customer_city,
                    customer_zip_code_prefix,
                    now(),
                    '9999-12-31 23:59:59',
                    1
                FROM olist_oltp.olist_customers_dataset 
                LIMIT %s OFFSET %s ;
"""
DimCustomer_script = """SELECT COUNT(*) FROM olist_oltp.olist_customers_dataset"""


DimSeller = """
                INSERT INTO olist_olap.DimSeller( SellerID,
                                                    SellerState, 
                                                    SellerCity, 
                                                    SellerZIPCode, 
                                                    ValidFrom, 
                                                    ValidTo, 
                                                    IsCurrent)
                SELECT
                    sel.seller_id,
                    sel.seller_state,
                    sel.seller_city,
                    sel.seller_zip_code_prefix,
                    now(),
                    '9999-12-31 23:59:59',
                    1
                FROM olist_oltp.olist_sellers_dataset sel
                LIMIT %s OFFSET %s ;
"""
DimSeller_script = """SELECT COUNT(*) FROM olist_oltp.olist_sellers_dataset"""


DimProduct = """
                INSERT INTO olist_olap.DimProduct( ProdID,
                                                    ProdCatName,
                                                    ProdCatNameEng,
                                                    ProdNameLgth,
                                                    ProdPhotoQty,
                                                    ProdWeightG,
                                                    ProdLengthCM,
                                                    ProdHeightCM,
                                                    ProdWidthCM,
                                                    ValidFrom,
                                                    ValidTo,
                                                    IsCurrent)
                SELECT
                    prod.product_id,
                    prod.product_category_name,
                    cat.product_category_name_english,
                    COALESCE(CHAR_LENGTH(prod.product_name_lenght)>1, 0) AS product_name_lenght,
                    COALESCE(CHAR_LENGTH(prod.product_photos_qty)>1, 0) AS product_photos_qty,
                    COALESCE(CHAR_LENGTH(prod.product_weight_g)>1, 0) AS product_weight_g,
                    COALESCE(CHAR_LENGTH(prod.product_length_cm)>1, 0) AS product_length_cm,
                    COALESCE(CHAR_LENGTH(prod.product_height_cm)>1, 0) AS product_height_cm,
                    COALESCE(CHAR_LENGTH(prod.product_width_cm)>1, 0) AS product_width_cm,
                    now(),
                    '9999-12-31 23:59:59',
                    1
                FROM olist_oltp.olist_products_dataset prod
                LEFT JOIN olist_oltp.product_category_name_translation cat
                ON prod.product_category_name = cat.product_category_name
                LIMIT %s OFFSET %s ; 
"""
DimProduct_script = """SELECT COUNT(*) FROM olist_oltp.olist_products_dataset"""


DimOrderStatus = """
                INSERT INTO olist_olap.DimOrderStatus( OrderStatus )
                SELECT
                    DISTINCT order_status
                FROM olist_oltp.olist_orders_dataset
                LIMIT %s OFFSET %s ;
"""
DimOrderStatus_script = """SELECT COUNT(DISTINCT(order_status)) FROM olist_oltp.olist_orders_dataset"""


DimPayMethod = """
                INSERT INTO olist_olap.DimPayMethod( PaymentType )    
                SELECT
                    DISTINCT payment_type
                FROM olist_oltp.olist_order_payments_dataset
                LIMIT %s OFFSET %s;
"""
DimPayMethod_script = """SELECT COUNT(DISTINCT(payment_type)) FROM olist_oltp.olist_order_payments_dataset"""


DimDate = """
           INSERT INTO olist_olap.DimDate( DateKey,
                                            DayOfWeek,
                                            DayOfMonth,
                                            DayName,
                                            Mnth,
                                            MonthName,
                                            Quartr,
                                            Year,
                                            WeekendFlag,
                                            Season,
                                            WeekNumber,
                                            YearMonth)
SELECT
DISTINCT(Date_format(date_time, '%Y%m%d')) AS DateKey,
        Dayofweek(date_time) AS DayOfWeek,
        Dayofmonth(date_time) AS DayOfMonth,
        Dayname(date_time) AS DayName,
        Month(date_time) AS Mnth,
        Monthname(date_time) AS MonthName,
        Quarter(date_time) AS Quartr,
        Year(date_time) AS Year,
        CASE WHEN Dayofweek(date_time) IN (1, 7) THEN 1 ELSE 0 END AS WeekendFlag,
        CASE WHEN Month(date_time) IN (12, 1, 2) THEN 'Winter'
            WHEN Month(date_time) IN (3, 4, 5) THEN 'Spring'
            WHEN Month(date_time) IN (6, 7, 8) THEN 'Summer'
            WHEN Month(date_time) IN (9, 10, 11) THEN 'Autumn'
            ELSE 'Unknown' END AS Season,
        Weekofyear(date_time) AS WeekNumber,
        Date_format(date_time, '%Y%m') AS YearMonth
FROM
    (SELECT order_purchase_timestamp AS date_time FROM olist_oltp.olist_orders_dataset
    UNION 
    SELECT order_approved_at AS date_time FROM olist_oltp.olist_orders_dataset
    UNION 
    SELECT order_delivered_carrier_date AS date_time FROM olist_oltp.olist_orders_dataset
    UNION 
    SELECT order_delivered_customer_date AS date_time FROM olist_oltp.olist_orders_dataset
    UNION 
    SELECT order_estimated_delivery_date AS date_time FROM olist_oltp.olist_orders_dataset) main
WHERE CHAR_LENGTH(date_time)> 15
LIMIT %s OFFSET %s;
"""
                
DimDate_script = """SELECT COUNT(DISTINCT(Date_format(date_time, '%Y%m%d')))
    FROM
        (SELECT order_purchase_timestamp AS date_time FROM olist_oltp.olist_orders_dataset
        UNION 
        SELECT order_approved_at AS date_time FROM olist_oltp.olist_orders_dataset
        UNION 
        SELECT order_delivered_carrier_date AS date_time FROM olist_oltp.olist_orders_dataset
        UNION 
        SELECT order_delivered_customer_date AS date_time FROM olist_oltp.olist_orders_dataset
        UNION 
        SELECT order_estimated_delivery_date AS date_time FROM olist_oltp.olist_orders_dataset) main;"""


DimGeolocation = """
                INSERT INTO olist_olap.DimGeolocation( GeoZipCode,
                                                        GeoLat,
                                                        GeoLng,
                                                        GeoCity,
                                                        GeoState)
                SELECT 
                    geolocation_zip_code_prefix,
                    geolocation_lat,
                    geolocation_lng,
                    geolocation_city,
                    geolocation_state
                FROM olist_oltp.olist_geolocation_dataset
                LIMIT %s OFFSET %s;"""

DimGeolocation_script = """SELECT COUNT(*) FROM olist_oltp.olist_geolocation_dataset;"""

FactOrderItem = """
                INSERT INTO olist_olap.FactOrderItem( OrderItemID,
                                                        OrderID,
                                                        ProdKey,
                                                        SellerKey,
                                                        CustomerKey,
                                                        price,
                                                        FreightValue,
                                                        OrderStatusKey,
                                                        DateKey,
                                                        PayMethodKey,
                                                        PaymentValue,
                                                        PurchaseTimestamp,
                                                        ApprovedAt,
                                                        ShippingLimitDate,
                                                        DeliveredCarrierDate,
                                                        DeliveredCustomerDate,
                                                        EstimatedDeliverDate,
                                                        Vversion)
                SELECT 
                        CONCAT(oi.order_id, '-', oi.order_item_id) AS OrderItemID,
                        oi.order_id,
                        prod.ProdKey,
                        sell.SellerKey,
                        cust.CustomerKey,
                        oi.price,
                        oi.freight_value,
                        stat.OrderStatusKey,
                        IF(CHAR_LENGTH(order_purchase_timestamp)>5, DATE_FORMAT(order_purchase_timestamp, '%Y%m%d'), NULL),
                        pay.PayMethodKey,
                        paym.payment_value,
                        IF(CHAR_LENGTH(ord.order_purchase_timestamp) > 5, CAST(ord.order_purchase_timestamp AS DATETIME), NULL),
                        IF(CHAR_LENGTH(ord.order_approved_at) > 5, CAST(ord.order_approved_at AS DATETIME), NULL),
                        IF(CHAR_LENGTH(oi.shipping_limit_date) > 5, CAST(oi.shipping_limit_date AS DATETIME), NULL),
                        IF(CHAR_LENGTH(ord.order_delivered_carrier_date) > 5, CAST(ord.order_delivered_carrier_date AS DATETIME), NULL),
                        IF(CHAR_LENGTH(ord.order_delivered_customer_date) > 5, CAST(ord.order_delivered_customer_date AS DATETIME), NULL),
                        IF(CHAR_LENGTH(ord.order_estimated_delivery_date) > 5, CAST(ord.order_estimated_delivery_date AS DATETIME), NULL),
                        1

                FROM olist_oltp.olist_order_items_dataset oi
                LEFT JOIN olist_oltp.olist_orders_dataset ord
                ON oi.order_id = ord.order_id
                LEFT JOIN olist_oltp.olist_order_payments_dataset paym
                ON ord.order_id = paym.order_id
                LEFT JOIN olist_olap.DimCustomer cust
                ON ord.customer_id = cust.CustomerID
                LEFT JOIN olist_olap.DimOrderStatus stat
                ON ord.order_status = stat.OrderStatus
                LEFT JOIN olist_olap.DimProduct prod
                ON oi.product_id = prod.ProdID
                LEFT JOIN olist_olap.DimSeller sell
                ON oi.seller_id = sell.SellerID
                LEFT JOIN olist_olap.DimPayMethod pay
                ON paym.payment_type = pay.PaymentType
                LIMIT %s OFFSET %s;
"""
FactOrderItem_script = """SELECT COUNT(*) FROM olist_oltp.olist_order_items_dataset;"""


FactOrderReview = """
                INSERT INTO olist_olap.FactOrderReview( ReviewID,
                                                    OrderID,
                                                    ReviewScore,
                                                    ReviewTitle,
                                                    ReviewMsg,
                                                    CreationDate,
                                                    ReviewTimestamp)
                SELECT   review_id
                        ,order_id
                        ,review_score
                        ,review_comment_title
                        ,review_comment_message
                        ,IF(CHAR_LENGTH(review_creation_date) > 5, CAST(review_creation_date AS DATETIME), NULL)
                        ,IF(CHAR_LENGTH(review_answer_timestamp) > 5, CAST(review_answer_timestamp AS DATETIME), NULL)  
                FROM
                        (SELECT *, ROW_NUMBER() OVER(PARTITION BY order_id ORDER BY review_answer_timestamp DESC) AS row_num 
                        FROM olist_oltp.olist_order_reviews_dataset) main
                WHERE row_num = 1
                LIMIT %s OFFSET %s;
"""

FactOrderReview_script = """SELECT COUNT(*) FROM olist_oltp.olist_order_reviews_dataset;"""




