BEGIN;
--1.total sales 
SELECT 
    ROUND(SUM(sales)::NUMERIC,2)
AS Total_sales
FROM Tsales;


--2.Region wise sales
SELECT
    region, ROUND(SUM(sales)::NUMERIC,2)
AS Total_sales
FROM Tsales
GROUP BY region
ORDER BY Total_sales DESC;


--3.top 5 cities by total sales
SELECT
     city,ROUND(SUM(sales)::NUMERIC,2) AS Topcity_sales
FROM Tsales
GROUP BY city
ORDER BY topcity_sales DESC
LIMIT 5;


--4.under 1000 rupees sales in cities
SELECT 
    city,ROUND(SUM(sales)::NUMERIC,2) AS lowest_sales
FROM Tsales
GROUP BY city
HAVING SUM(sales) <1000
ORDER BY lowest_sales ASC;


--5.Find average sales for cities where total sales under 1000
SELECT
   city,
   ROUND(SUM(sales)::NUMERIC,2) AS total_sales,
   ROUND(AVG(sales)::NUMERIC,2) AS avg_sales
FROM Tsales
GROUP BY city
HAVING SUM(sales)<1000
ORDER BY avg_sales ASC
LIMIT 10;


--6.Find average sales in cities
SELECT
    city,
	ROUND(SUM(sales)::NUMERIC,2) AS total_sales,
	ROUND(AVG(sales)::NUMERIC,2) AS avg_sales
FROM Tsales
GROUP BY city
ORDER BY avg_sales DESC
LIMIT 10;


--7.product category wise total sales
SELECT
    category,
	ROUND(SUM(sales):: NUMERIC,2) AS Total_sales
FROM Tsales
GROUP BY category
ORDER BY total_sales DESC;


--8.top customer, who spend highest amout of money in terms of total sales
SELECT 
    customerid,
	customername,
	city,
	state,
	region,
	ROUND(SUM(sales)::NUMERIC,2) as total_sales
FROM Tsales
GROUP BY customerid, 
         customername,
		 city,
		 state,
		 region
ORDER BY total_sales DESC
LIMIT 5;


--9.find customer details who perchased the highest sales product
SELECT 
    orderid,
	orderdate,
    customerid,
	customername,
	city,
	state,
	region,
	productname,
	productid,
	category,
	subcategory,
    ROUND(sales:: NUMERIC,2) AS sales_amount 
FROM Tsales
ORDER BY sales:: NUMERIC DESC
LIMIT 1;


--10.find the customer details,who perchased the second highest sales product
SELECT 
    orderid,
    orderdate,
    customerid,
    customername,
    city,
    state,
    region,
    productname,
    productid,
    category,
    subcategory,
    ROUND(sales::NUMERIC, 2) AS total_sales
FROM Tsales
WHERE sales = (
        SELECT MAX(sales)
        FROM Tsales
        WHERE sales <(
                SELECT MAX(sales)
                FROM Tsales 
        )
);


--11.find the customer details, who perchased minimun of sales product

SELECT 
    orderid,
    orderdate,
    customerid,
    customername,
    city,
    state,
    region,
    productname,
    productid,
    category,
    subcategory,
    ROUND(sales::NUMERIC, 2) AS total_sales
FROM Tsales
WHERE sales =(
           SELECT MIN (sales)
           FROM Tsales);


--12.find top five(5) sales month  
SELECT
    TO_CHAR(DATE_TRUNC('month', orderdate), 'Mon YYYY') AS month,
    ROUND(SUM(sales)::NUMERIC,2) AS total_sales
FROM Tsales
GROUP BY month
ORDER BY total_sales DESC
LIMIT 5;

--13.find second highest sales month
SELECT
    TO_CHAR(DATE_TRUNC('month', orderdate), 'Mon YYYY') AS month,
    ROUND(SUM(sales)::NUMERIC,2) AS total_sales
FROM Tsales
GROUP BY month
ORDER BY total_sales DESC
OFFSET 1
LIMIT 1;


COMMIT;






