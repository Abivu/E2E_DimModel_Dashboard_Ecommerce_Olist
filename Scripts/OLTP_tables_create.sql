-- The script creates tables in OLTP database
-- used to manually populate tables through GUI
USE olist_oltp;

CREATE TABLE IF NOT EXISTS olist_customers_dataset 
(   customer_id varchar(1024),
    customer_unique_id varchar(1024),
    customer_zip_code_prefix varchar(1024),
    customer_city varchar(1024),
    customer_state varchar(1024)
);

CREATE TABLE IF NOT EXISTS olist_geolocation_dataset
(   geolocation_zip_code_prefix varchar(1024),
    geolocation_lat varchar(1024),
    geolocation_lng varchar(1024),
    geolocation_city varchar(1024),
    geolocation_state varchar(1024)
);

CREATE TABLE IF NOT EXISTS olist_order_items_dataset
(   order_id varchar(1024),
    order_item_id varchar(1024),
    product_id varchar(1024),
    seller_id varchar(1024),
    shipping_limit_date varchar(1024),
    price varchar(1024),
    freight_value varchar(1024)
);

CREATE TABLE IF NOT EXISTS olist_order_payments_dataset
(   order_id varchar(1024),
    payment_sequential varchar(1024),
    payment_type varchar(1024),
    payment_installments varchar(1024),
    payment_value varchar(1024)
);


CREATE TABLE IF NOT EXISTS olist_order_reviews_dataset
(   review_id varchar(1024),
    order_id varchar(1024),
    review_score varchar(1024),
    review_comment_title varchar(1024),
    review_comment_message varchar(1024),
    review_creation_date varchar(1024),
    review_answer_timestamp varchar(1024)
);

CREATE TABLE IF NOT EXISTS olist_orders_dataset
(   order_id varchar(1024),
    customer_id varchar(1024),
    order_status varchar(1024),
    order_purchase_timestamp varchar(1024),
    order_approved_at varchar(1024),
    order_delivered_carrier_date varchar(1024),
    order_delivered_customer_date varchar(1024),
    order_estimated_delivery_date varchar(1024)    
);

CREATE TABLE IF NOT EXISTS olist_products_dataset
(   product_id varchar(1024),
    product_category_name varchar(1024),
    product_name_lenght varchar(1024),
    product_description_lenght varchar(1024),
    product_photos_qty varchar(1024),
    product_weight_g varchar(1024),
    product_length_cm varchar(1024),
    product_height_cm varchar(1024),
    product_width_cm varchar(1024)
);

CREATE TABLE IF NOT EXISTS olist_sellers_dataset
(   seller_id varchar(1024),
    seller_zip_code_prefix varchar(1024),
    seller_city varchar(1024),
    seller_state varchar(1024)
);

CREATE TABLE IF NOT EXISTS product_category_name_translation
(   product_category_name varchar(1024),
    product_category_name_english varchar(1024)
);


-- Scripts to bulk load data sample

LOAD DATA LOCAL INFILE 'D:/personal_projects/E2E_DimModel_Dashboard_Ecommerce_Olist/Olist/olist_order_reviews_dataset.csv' 
INTO TABLE olist_order_reviews_dataset
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
;




