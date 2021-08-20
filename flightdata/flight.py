from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("flight").master("local[*]").getOrCreate()
flightdata = spark.read.option("inferSchema", True).option("header", True).csv("2015-summary.csv")
flightdata.createOrReplaceTempView("flight_data_view")
sqlway = spark.sql("""SELECT DEST_COUNTRY_NAME, COUNT(1) FROM flight_data_view GROUP BY DEST_COUNTRY_NAME """)
sqlway.show(10)
dataframeway = flightdata.groupby('DEST_COUNTRY_NAME').sum("count").withColumnRenamed("sum(count)", "destination_total").sort("destination_total", ascending=False).limit(5).show()
print("hello")