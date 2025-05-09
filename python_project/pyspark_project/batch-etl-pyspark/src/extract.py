from pyspark.sql import SparkSession
from config.config import Config
from src.logger import logger

def extract_data():
    logger.info("Extracting data...")
    spark = SparkSession.builder.appName("ETL").getOrCreate()
    df = spark.read.csv(Config.DATA_PATH, header=True, inferSchema=True)
    logger.info(f"Extracted {df.count()} rows.")
    return df
