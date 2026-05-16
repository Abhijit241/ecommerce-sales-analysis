from db_connection import engine
import matplotlib.pyplot as plt
import pandas as pd
import mplcursors

#SQL query
query= "SELECT * FROM Tsales"

#Load data into pandas DataFrame
df= pd.read_sql(query,engine)

# adding hover values for bars and line points
def format_hover(sel):
    if hasattr(sel.artist, "get_height"):
        value = sel.artist.get_height()
    elif hasattr(sel.artist, "get_width"):
        value = sel.artist.get_width()
    else:
        try:
            _, value = sel.target
        except Exception:
            value = None
    if value is not None:
        sel.annotation.set_text(f"{value:,.2f}")




# **1.monthly sales trend of the total sales
df["orderdate"] = pd.to_datetime(df["orderdate"])
df["month"] = df["orderdate"].dt.month
monthly_sales = (df.groupby("month")["sales"].sum()
                 .reset_index().sort_values("month"))

monthly_sales["month"] =( monthly_sales["month"]
.apply(lambda x: pd.to_datetime(str(x), format="%m").strftime("%B")))

#visualize monthly sales trends by plot-line
#bar chart for better visualization of monthly sales trends
plt.figure(figsize=(12, 6))
ax = monthly_sales.plot(x="month", y="sales", kind="bar", color="steelblue")
monthly_sales.plot(x="month", y="sales", kind="line", ax=ax, color="green", marker="o")
# hover feature
cursor = mplcursors.cursor(list(ax.containers) + ax.lines, hover=True)
cursor.connect("add", format_hover)

plt.title("Monthly Sales Trends")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.savefig("monthly_sales_trends.png")
plt.show()  





# **2. yearly sales trends
yearly_sales=(df.groupby(df["orderdate"].dt.year)["sales"].sum().round(2))
plt.figure(figsize=(10, 6))
ax = yearly_sales.plot(kind="line",color="blue",marker="o")

# hover feature
cursor = mplcursors.cursor(ax.lines, hover=True)
cursor.connect("add", format_hover)

plt.title("Yearly Sales Trends")
plt.xlabel("Year")
plt.ylabel("Sales")
plt.grid(True)
plt.tight_layout()
plt.savefig("yearly_sales_trends.png")
plt.show()


# **3. sales distribution by category
category_sales = (df.groupby("category")["sales"].sum().reset_index())

# visualize sales distribution by category
plt.figure(figsize=(8, 8))
plt.pie(category_sales["sales"], labels=category_sales["category"],
        autopct='%1.1f%%', startangle=140,
        wedgeprops={'edgecolor': 'white', 'linewidth': 2},
        explode=[0.01, 0.01, 0.01],colors=["#AF0C17","#25c15b","#e4c838"])
plt.title("Sales Distribution by Category")
plt.axis('equal')
plt.tight_layout()
plt.savefig("sales_distribution_by_category.png")
plt.show()




# **4. highest revenue state
state_sales = df.groupby("state")["sales"].sum().sort_values(ascending=False)
highest_state = state_sales.idxmax()
highest_revenue = state_sales.max()

plt.figure(figsize=(10, 6))
ax = state_sales.head(10).plot(kind="bar", color="steelblue")
cursor = mplcursors.cursor(list(ax.containers), hover=True)
cursor.connect("add", format_hover)
plt.title(f"Top 10 States by Total Sales\n(Highest: {highest_state} - {highest_revenue:,.2f})")
plt.xlabel("State")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.savefig("top_states_by_sales.png")
plt.show()



# **5. segment-wise sales distribution
segment_sales = df.groupby("segment")["sales"].sum().reset_index()

# visualize segment-wise sales distribution
plt.figure(figsize=(8, 8))
plt.pie(segment_sales["sales"], labels=segment_sales["segment"],
        autopct='%1.1f%%', startangle=140,
        wedgeprops={'edgecolor': 'white', 'linewidth': 2},
        explode=[0.01, 0.01, 0.01],colors=["#8D0808","#cfea48","#5EC27A"])
plt.title("Sales Distribution by Segment")
plt.axis('equal')
plt.tight_layout()
plt.savefig("sales_distribution_by_segment.png")
plt.show()



# **6. top products by sales
product_sales =(df.groupby("productname")["sales"].sum().sort_values(ascending=False).head(10))
# visualize top products by sales
plt.figure(figsize=(12, 6)) 
ax = product_sales.plot(kind="bar", color="steelblue")
cursor = mplcursors.cursor(list(ax.containers), hover=True)
cursor.connect("add", format_hover)
plt.title("Top 10 Products by Sales")
plt.xlabel("Product Name")
plt.ylabel("Sales")
plt.xticks(rotation=20, ha="right")
plt.grid(True)
plt.tight_layout()  
plt.savefig("top_products_by_sales.png")
plt.show()


# **7. sales distribution by region
region_sales = df.groupby("region")["sales"].sum().reset_index()  
# visualize sales distribution by region  
plt.figure(figsize=(8, 8))
plt.pie(region_sales["sales"], labels=region_sales["region"], autopct='%1.1f%%', startangle=140,
        wedgeprops={'edgecolor': 'white', 'linewidth': 2},
        explode=[0.01, 0.01, 0.01, 0.01],colors=["#ABB31F","#67a6e5","#BD4C4C","#43DF49"])
plt.title("Sales Distribution by Region")
plt.axis('equal')
plt.tight_layout()
plt.savefig("sales_distribution_by_region.png")
plt.show()



# **8. sales distribution by city
city_sales = df.groupby("city")["sales"].sum().reset_index()
# visualize sales distribution by city
plt.figure(figsize=(12, 6))
ax = city_sales.sort_values("sales", ascending=False).head(10).plot(x="city",y="sales", 
                                                               kind="bar", color="steelblue")  
cursor = mplcursors.cursor(list(ax.containers), hover=True)
cursor.connect("add", format_hover)
plt.title("Top 10 Cities by Sales") 
plt.xlabel("City")
plt.ylabel("Sales")
plt.xticks(rotation=45, ha="right")
plt.grid(True)
plt.tight_layout()
plt.savefig("sales_distribution_by_city.png")
plt.show()


# **9. top 10 customers by sales
customer_sales = df.groupby("customername")["sales"].sum().reset_index()
plt.figure(figsize=(12, 6))
ax = customer_sales.sort_values("sales", ascending=False).head(10).plot(x="customername", y="sales",
                                                                    kind="barh", color="steelblue")
cursor = mplcursors.cursor(list(ax.containers), hover=True)
cursor.connect("add", format_hover)
plt.title("Top 10 Customers by Sales")
plt.xlabel("Customer Name")
plt.ylabel("Sales")
plt.xticks(rotation=45, ha="right")
plt.grid(True)
plt.tight_layout()
plt.savefig("top_customers_by_sales.png")
plt.show()


