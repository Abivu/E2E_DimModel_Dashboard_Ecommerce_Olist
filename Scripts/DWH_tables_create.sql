USE olist_olap;

CREATE TABLE IF NOT EXISTS DimCustomer 
(   CustomerKey Integer auto_increment Primary Key,
    CustomerID varchar(250),
    CustomerUniqueID varchar(250),
    CustomerCity varchar(250),
    CustomeZIPCode varchar(20),
    CustomeLat decimal(18, 15),
    CustomeLng decimal(18, 15),
    ValidFrom datetime,
    ValidTo datetime,
    IsCurrent tinyint
);


CREATE TABLE IF NOT EXISTS DimSeller 
(   SellerKey Integer AUTO_INCREMENT Primary Key,
    SellerID varchar(250),
    SellerCity varchar(250),
    SellerState varchar(250),
    SellerZIPCode varchar(20),
    SellerLat decimal(18, 15),
    SellerLng decimal(18, 15),
    ValidFrom datetime,
    ValidTo datetime,
    IsCurrent tinyint
);


CREATE TABLE IF NOT EXISTS DimProduct 
(   ProdKey Integer AUTO_INCREMENT Primary Key,
    ProdID varchar(250),
    ProdtCatNameEng varchar(250),
    ProdNameLgth Integer,
    ProdPhotoQty Integer,
    ProdLengthCM Integer,
    ProdHeightCM Integer,
    ProdWidthCM Integer,
    ValidFrom datetime,
    ValidTo datetime,
    IsCurrent tinyint
);


CREATE TABLE IF NOT EXISTS DimOrderStatus 
(   OrderStatusKey Integer AUTO_INCREMENT Primary Key,
    OrderStatus varchar(25)
);


CREATE TABLE IF NOT EXISTS DimPayMethod 
(   PayMethodKey Integer AUTO_INCREMENT Primary Key,
    PaymentType varchar(25)
);


CREATE TABLE IF NOT EXISTS DimDate 
(   DateKey varchar(10) Primary Key,
    DayOfWeek Integer,
    DayofMonth Integer,
    DayName varchar(15),
    Mnth Integer,
    MonthName varchar(15),
    Quartr Integer,
    Year Integer,
    WeekendFlag tinyint,
    HolidayFlag tinyint,
    Season varchar(15),
    WeekNumber Integer,
    YearMonth varchar(7)
);


CREATE TABLE IF NOT EXISTS FactOrderItem
(
    OrderItemID varchar(250),
    OrderID varchar(250),
    ProdKey Integer,
    SellerKey Integer,
    CustomerKey Integer,
    Price Float,
    FreightValue Float,
    OrderStatusKey Integer,
    DateKey varchar(10),
    PayMethodKey Integer,
    PaymentValue Float,
    PurchaseTimestamp datetime,
    ApprovedAt datetime,
    DeliveredCarrierDate datetime,
    DeliveredCustomerDate datetime,
    EstimatedDeliverDate datetime,
    Vversion Integer
);


CREATE TABLE IF NOT EXISTS FactOrderReview
(
    ReviewID varchar(250) Primary Key,
    OrderID varchar(250),
    ReviewScore Integer,
    ReviewTitle varchar(250),
    ReviewMsg varchar(500),
    ReviewCreationDate datetime,
    ReviewAnswerTimestamp datetime
);