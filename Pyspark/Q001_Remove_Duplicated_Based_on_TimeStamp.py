# Databricks notebook source
# MAGIC %md
# MAGIC ## **Q001**
# MAGIC ## **While ingesting customer data from an external source, you notice duplicate entries. How would you remove duplicates and retain only the latest entry based on a timestamp column?**

# COMMAND ----------

# MAGIC %md
# MAGIC ## First lets try in SQL

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE TABLE sales_data (
# MAGIC     product_id STRING,
# MAGIC     date DATE,
# MAGIC     sales INT
# MAGIC );
# MAGIC
# MAGIC INSERT INTO sales_data (product_id, date, sales) VALUES
# MAGIC ('101', '2023-12-01', 100),
# MAGIC ('101', '2023-12-02', 150),
# MAGIC ('102', '2023-12-01', 200),
# MAGIC ('102', '2023-12-02', 250);
# MAGIC
# MAGIC SELECT * FROM sales_data;

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC WITH CTE AS (
# MAGIC SELECT *,
# MAGIC row_number() OVER(PARTITION BY product_id ORDER BY date DESC) as rn
# MAGIC FROM sales_data)
# MAGIC
# MAGIC SELECT product_id, date, sales FROM CTE WHERE rn=1;

# COMMAND ----------

# MAGIC %md
# MAGIC ## Pyspark Solution

# COMMAND ----------

from pyspark.sql.functions import * 
from pyspark.sql.types import *

# COMMAND ----------

data = [("101", "2023-12-01", 100), ("101", "2023-12-02", 150), 
        ("102", "2023-12-01", 200), ("102", "2023-12-02", 250)]
columns = ["product_id","date","sales"]

df = spark.createDataFrame(data,columns)
df.display()

# COMMAND ----------

## Casting date column from string to date format

df = df.withColumn('date',col('date').cast(DateType()))
# df = df.withColumn("date", to_date(col("date"),"yyyy-MM-dd")) -- Both would work


## Drop the duplicates
df = df.orderBy("product_id","date",ascending=[1,0]).dropDuplicates(subset=['product_id'])
df.display()

# COMMAND ----------

