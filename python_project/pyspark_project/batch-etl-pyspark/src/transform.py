from src.logger import logger

def clean_data(df):
    logger.info("Cleaning data...")
    cleaned_df = df.dropna()
    logger.info(f"Cleaned data: {cleaned_df.count()} rows remain.")
    return cleaned_df
