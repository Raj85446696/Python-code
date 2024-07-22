import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import mysql.connector

db  = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Raj@708090',
    database='Ecommerce'
)

cur = db.cursor()

# Q.1 List all unique cities where customers are located 
query = '''select distinct customer_city from customers'''
cur.execute(query)
data = cur.fetchall()
print("here list of all unique cities",data)

# Q.2 Count the number of order placed in 2017;
query = '''select count(order_id) from orders  where order_purchase_timestamp regexp ("2017")'''
cur.execute(query)
data = cur.fetchall()
print("Total number of order placed in 2017 are = ",data)

# Q.3 Find the total sales per category 
query = '''SELECT PR.PRODUCT_CATEGORY  , sum(P.PAYMENT_VALUE)  FROM PRODUCTS PR JOIN ORDER_ITEMS O 
ON PR.PRODUCT_ID = O.PRODUCT_ID JOIN PAYMENTS P ON P.ORDER_ID = O.ORDER_ID GROUP BY PRODUCT_CATEGORY'''
cur.execute(query)
data = cur.fetchall()
df = pd.DataFrame(data,columns=["category","total_payment"])
print(df)


# Q.4 Calculate the percentage of order that were paid in installments.
query = '''SELECT (SUM(CASE WHEN payment_installments >=1 THEN 1 ELSE 0 END))/count(*)*100 AS PERCENTAGE FROM PAYMENTS'''
cur.execute(query)
data = cur.fetchall()
df = pd.DataFrame(data,columns=["PERCENTAGE"])
print("the total percentage ",df)


# Q.5 Count the number of customer from each state.
query = '''SELECT CUSTOMER_STATE ,COUNT(customer_id) FROM CUSTOMERS GROUP BY CUSTOMER_STATE'''
cur.execute(query)
data = cur.fetchall()
df = pd.DataFrame(data,columns=["State","total"])
print(df)

#for creating bar plot 
x = df["State"]
y = df["total"]
plt.bar(x,y,color = "r",label="customer")
plt.xlabel("States")
plt.ylabel("Total of Customers")
plt.grid(color="g",alpha = 0.2)
plt.legend()
plt.show()


# Q.6 Calculate the number of order per month in 2018.
query = '''select month(order_purchase_timestamp) as Month ,count(order_id) as no_of_orders from orders where year(order_purchase_timestamp) = 2018 group by month(order_purchase_timestamp)'''
cur.execute(query)
data = cur.fetchall()
df = pd.DataFrame(data,columns=["Months","No of orders"])
print(df)

# For Plotting bar plot using seaborn 
plt.bar(["jan","feb","Mar","Apr","May","June","July","Aug","Sep","Oct"],df["No of orders"],label = "no of orders")
plt.xlabel("Months",color="b",fontsize =15)
plt.ylabel("No of Orders",color="b",fontsize =15)
plt.grid(color ="g",alpha = 0.3)
plt.legend()
plt.show()

# Q.7 Find the average number of products per order, grouped by customer city.
querry =  '''WITH COUNT_PER_ORDER AS(SELECT ORDERS.ORDER_ID,ORDERS.CUSTOMER_ID,COUNT(ORDER_ITEMS.ORDER_ID) AS OC FROM ORDERS JOIN ORDER_ITEMS ON ORDERS.ORDER_ID = ORDER_ITEMS.ORDER_ID
GROUP BY ORDERS.ORDER_ID , ORDERS.CUSTOMER_ID)
SELECT CUSTOMERS.CUSTOMER_CITY , ROUND(AVG(COUNT_PER_ORDER.OC),2) AVERAGE_ORDERS FROM CUSTOMERS JOIN COUNT_PER_ORDER
ON CUSTOMERS.CUSTOMER_ID = COUNT_PER_ORDER.CUSTOMER_ID GROUP BY CUSTOMERS.CUSTOMER_CITY;'''
cur.execute(querry)
data = cur.fetchall()
df = pd.DataFrame(data,columns=["customer_city","average_order"])
print(df.head()) # for getting top 5 values 
print(df.shape) 
print(df.size)


#Q.8 Calculate the percentage of total revenue contributed by each product category.
querry = '''SELECT PR.PRODUCT_CATEGORY , (SUM(P.PAYMENT_VALUE)/(SELECT SUM(PAYMENT_VALUE) FROM PAYMENTS)*100) AS SALES_PERCENTAGE FROM PRODUCTS PR JOIN ORDER_ITEMS O ON PR.PRODUCT_ID = O.PRODUCT_ID JOIN 
PAYMENTS P ON P.ORDER_ID = O.ORDER_ID GROUP BY PRODUCT_CATEGORY ORDER BY SALES_PERCENTAGE DESC'''
cur.execute(querry)
data = cur.fetchall()
df = pd.DataFrame(data,columns=["product_category","sales_percentage"])
print(df)

# for create pi graph 
plt.pie(df.sales_percentage,labels=df.product_category,radius=1,shadow=True,textprops={"fontsize":10},autopct="%0.2f%%")
plt.show()


# Q.9 Identify the correlation between product price and the number of times a product has been purchased.
querry = '''SELECT P.PRODUCT_CATEGORY , COUNT(OD.PRODUCT_ID) AS COUNT,ROUND(AVG(OD.PRICE),3) AS PRICE FROM PRODUCTS P JOIN ORDER_ITEMS OD ON P.PRODUCT_ID = OD.PRODUCT_ID GROUP BY P.PRODUCT_CATEGORY;'''
cur.execute(querry)
data = cur.fetchall()
df = pd.DataFrame(data,columns=["product_category","order_count","price"])
arr1 = df["order_count"]
arr2 = df["price"]
c = np.corrcoef([arr1,arr2])
print("Correlation between price and number of times purchased is = ",c[0][1])


