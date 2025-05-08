from src.extract import extract_data
from src.transform import clean_data
from src.load import save_data
from config.settings import get_spark_session

def main():
    # Initialize Spark session
    spark = get_spark_session()

    # Extract data
    df = extract_data("data/raw/customers.csv")

    # Transform data
    cleaned_df = clean_data(df)

    # Load data
    save_data(cleaned_df, "data/output/cleaned_data.csv")

if __name__ == "__main__":
    main()
