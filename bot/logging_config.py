# bot/logging_config.py
import logging

logging.basicConfig(
    
    filename="tradingbot.bot",
    level = "INFO",
    format = "%(asctime)s - %(levelname)s - %(message)s"
    
)

logger = logging.getLogger(__name__)
