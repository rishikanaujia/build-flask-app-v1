import logging


def setup_logging(level: str):
    """Setup logging configuration."""
    logging.basicConfig(
        level=level,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )
    logging.info("Logging is set up with level: %s", level)

    return logging


custom_logger = setup_logging("info")
