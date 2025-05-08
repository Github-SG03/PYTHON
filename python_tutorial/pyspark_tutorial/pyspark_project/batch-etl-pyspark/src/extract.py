def extract_data(spark, file_path):
    return spark.read.option("header", "true").csv(file_path)
