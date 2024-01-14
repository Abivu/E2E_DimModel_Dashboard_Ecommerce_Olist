[130124]
Had trouble of loading data automatically by Python
Switched to manual for now
Created tables script - default datatypes varchar(1024). In practice, these tables are created and existed with
predefined datatypes
For this project, extra work in ETL to transform data types

[Issues I had]
1. After manual loading, found out data loading issue for table olist_geolocation_dataset
Possible Cause: over a million row!!! 
--> **Solution:** Set ResultSet FetchSize = 0. 
And alternatively, for large tables (> 1mil rows) Use Bulk Loading strategy instead. 

2. During manual loading, in table olist_order_reviews_dataset, encountered an error
"Data too long for column 'review_creation_date' at row 1"
--> Caused by STRICT MODE in MySQL to control invalidated data inserts.
-->**Solution:** Turn off the mode

3. During manual loading, in table olist_order_reviews_dataset, there was malformed data input
like the character "\"
--> Solution: switched to Bulk loading will ignore that row having special character

4. How to handle special characters in dataset?
