import os
from dotenv import load_dotenv, find_dotenv
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Print current working directory
logger.info(f"Current working directory: {os.getcwd()}")

# Find .env file
dotenv_path = find_dotenv()
logger.info(f".env file path: {dotenv_path}")

# Load .env file
load_dotenv(dotenv_path)

# Print environment variables
logger.info(f"TAVILY_API_KEY: {os.getenv('TAVILY_API_KEY')}")
logger.info(f"ANTHROPIC_API_KEY: {os.getenv('ANTHROPIC_API_KEY')}")

class Config:
    TAVILY_API_KEY = os.getenv('TAVILY_API_KEY')
    ANTHROPIC_API_KEY = os.getenv('ANTHROPIC_API_KEY')