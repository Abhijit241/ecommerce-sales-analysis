import pandas as pd
import numpy as np
from db_connection import engine

#SQL query
query= "SELECT * FROM Tsales"

#Load data into pandas DataFrame
df= pd.read_sql(query,engine)

# print pandas Dataframe head, shape, information, description for 
# understanding actual dataframe

print(df.head(2),"\n")
print(df.info(),"\n")
print(df.describe(include="all"),"\n")
print(df.shape)

# checking is any null value present
null=df.isnull().sum()
print(null)

# postalcode contains 6 null values
# keeping them as they do not significantly affect analysis
null_value= df[df["postalcode"].isnull()]
print(null_value)


# ::::::::::::Data Analysis::::::::::::

# 1.calculating total sales
total_sales=df["sales"].sum()
print(total_sales)


# 2.sales distribution
print(df["sales"].describe().round(2))


# 3.top sales categories 
top_categories= df.groupby("category")["sales"].sum()
print("top sales categories:",top_categories,"\n")



# 4.top 5 customers list 
customer_list= (df.groupby("customername")["sales"].sum()
                .sort_values(ascending=False).head(5))
print("highest perchased customers list \n",customer_list,"\n")



# 5.top region to region wise total sales
top_region=(df.groupby("region")["sales"].sum()
            .sort_values(ascending=False))
print("highest sales by region \n",top_region,"\n")



# 6.top 10 cities by total sales
top_cities=(df.groupby("city")["sales"].sum()
            .sort_values(ascending=False).head(10))
print("top cities by total sales \n",top_cities,"\n")



# 7.monthly sales trend of the total sales 
# first grouped all the sales month wise
df["orderdate"]= pd.to_datetime(df["orderdate"])
monthly_sales = (df.groupby(df["orderdate"].dt.month)
                 ["sales"].sum().reset_index())

#converting month number to month name 
monthly_sales["orderdate"]= (pd.to_datetime(monthly_sales["orderdate"],
                                            format="%m").dt.month_name())

# columns select and showing the monthly sales table
monthly_sales= monthly_sales[["orderdate","sales"]]
print(monthly_sales)



# 8.top selling product
top_product=(df.groupby("productname")["sales"].sum())
top_product=top_product.idxmax()
print("top selling products: ",top_product)



# 9.total sales grouped by segment
segment_sales=(df.groupby("segment")["sales"]
               .sum().sort_values(ascending=False))
print(segment_sales)

# 10.average sales by segment
avg_segment_sales=(df.groupby("segment")["sales"]
                   .mean().sort_values(ascending=False))
print(avg_segment_sales)



# 11.which segment has highest sales
top_segment_sales= segment_sales.idxmax()
print("top segment:",top_segment_sales)



# 12.segment wise order count
order_count= (df.groupby("segment")["orderid"].count())
print(order_count)



# 13.highest sales month/order distribution by month
top_sales_month=(df.groupby(df["orderdate"].dt.month_name())["sales"].sum()
                 .sort_values(ascending=False).head(1))
print(top_sales_month)


# 14.most frequent customers
customer_order=(df["customername"].value_counts().head(10))
print(customer_order)

# 15.average sales per customers
avg_customer_sales=(df.groupby("customername")["sales"].mean().round(2)
                    .sort_values(ascending=False).head(10))
print(avg_customer_sales)


# 16. yearly sales trends
yearly_sales=(df.groupby(df["orderdate"].dt.year)["sales"].sum().round(2)
              .sort_values())
print(yearly_sales)










