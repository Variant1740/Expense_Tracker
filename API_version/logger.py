from loguru import logger  
import sys  
import os  

# Create logs folder
os.makedirs("logs", exist_ok=True)

# Remove default handler
logger.remove()

# Colorful terminal output
logger.add(
    sys.stderr,
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <level>{message}</level>",
    colorize=True,
    level="INFO"
)

# Save to daily log file
logger.add(
    "logs/app_{time:YYYY-MM-DD}.log",
    rotation="500 MB",
    retention="10 days",
    compression="zip",
    level="INFO"
)

__all__ = ["logger"]
