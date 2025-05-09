from config.config import Config
from src.logger import logger

def save_data(df):
    logger.info(f"Saving data to {Config.OUTPUT_PATH}")
    df.coalesce(1).write.mode("overwrite").csv(Config.OUTPUT_PATH, header=True)
    logger.info("Data saved.")
