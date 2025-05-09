import pytest
from pyspark.sql import SparkSession
from src.transform import clean_data

@pytest.fixture
def spark():
    return SparkSession.builder.appName("Test").getOrCreate()

def test_clean_data(spark):
    df = spark.createDataFrame([(1, "A"), (None, "B")], ["id", "name"])
    cleaned = clean_data(df)
    assert cleaned.count() == 1
