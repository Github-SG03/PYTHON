from dotenv import load_dotenv
from src.extract import extract_data
from src.transform import clean_data
from src.load import save_data
from src.logger import logger

def main():
    load_dotenv()
    try:
        df = extract_data()
        cleaned = clean_data(df)
        save_data(cleaned)
        logger.info("✅ ETL completed.")
    except Exception as e:
        logger.error(f"❌ ETL failed: {e}")

if __name__ == "__main__":
    main()
