import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    DATA_PATH = os.getenv("DATA_PATH", "data/input/data.csv")
    OUTPUT_PATH = os.getenv("OUTPUT_PATH", "data/output/output.csv")
    ENV = os.getenv("ENV", "dev")
