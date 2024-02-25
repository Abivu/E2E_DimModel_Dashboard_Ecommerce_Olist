CREATE VIEW OverviewOrders AS

SELECT *,
        CASE
            WHEN    OrderStatus = 'delivered' AND
                    DeliveredCustomerDate < EstimatedDeliverDate THEN 1
            ELSE 0
        END AS OntimeFlag
FROM
    (SELECT
         oi.PurchaseTimestamp
        ,oi.OrderItemId
        ,oi.orderid
        ,prod.ProdCatNameEng
        ,cust.CustomerKey
        ,oi.PaymentValue
        ,os.OrderStatus
        ,orev.reviewscore
        ,CAST (oi.DeliveredCustomerDate AS DATE) AS DeliveredCustomerDate
        ,CAST (oi.EstimatedDeliverDate AS DATE) AS EstimatedDeliverDate
        
    FROM olist_olap.factorderitem oi
    LEFT JOIN olist_olap.factorderreview orev
    ON oi.orderid = orev.orderid
    LEFT JOIN olist_olap.dimproduct prod
    ON oi.ProdKey = prod.Prodkey
    LEFT JOIN olist_olap.dimorderstatus os
    ON os.OrderStatusKey = oi.OrderStatusKey
    LEFT JOIN olist_olap.dimcustomer cust
    ON cust.CustomerKey = oi.CustomerKey) main;
