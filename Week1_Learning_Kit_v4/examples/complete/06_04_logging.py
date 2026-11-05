import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s %(message)s",
)
logger = logging.getLogger(__name__)
logger.info("sampling started; interval=%s", 0.5)
try:
    raise OSError("classroom simulated failure")
except OSError:
    logger.exception("report could not be saved")
