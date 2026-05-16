BEGIN;
--create sales table
CREATE TABLE IF NOT EXISTS Tsales(
RowID INT,
OrderID TEXT,
OrderDate DATE,
ShipDate DATE,
ShipMode TEXT,
CustomerID TEXT,
CustomerName TEXT,
Segment TEXT,
Country TEXT,
City TEXT,
State TEXT,
PostalCode INT,
Region TEXT,
ProductID TEXT,
Category TEXT,
SubCategory TEXT,
ProductName TEXT,
Sales FLOAT
);

--import csv file
COPY Tsales
FROM 'C:\data_analyst project\ecommerce_project\data\supersales_cleaned(in)1.csv'
DELIMITER ','
CSV HEADER
QUOTE '"';


--showing sales table
SELECT * FROM Tsales
LIMIT 50;


COMMIT;
