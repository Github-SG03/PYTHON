from pyspark.sql.functions import col

def clean_data(df):
    # Example: filter active customers
    return df.filter(col("status") == "active")
