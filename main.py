# main.py
from app_logger import logger  # <--- This fulfills the requirement!

# Create some dummy variables for the example
circle_name = "Circle A"
square_name = "Square B"

# Use the logger as requested
logger.info("The program has started.")
logger.debug(f"The first var is {circle_name} and the second is {square_name}")