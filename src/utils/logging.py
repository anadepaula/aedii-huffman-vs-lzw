import sys
from loguru import logger

logger.remove()
STDOUT_FORMAT = "[<g>{time:YYYY-MM-DD HH:mm:ss}</g> <lvl>{level}</lvl>] <b>{message}</b> <d><c>({file}:{line})</c></d>"
logger.add(sys.stdout, format=STDOUT_FORMAT, level="DEBUG")

FILE_FORMAT = "[{time:YYYY-MM-DD HH:mm:ss} {level} {name}] {message} ({file}:{line})"
filename = "logs.log"
logger.add(
    filename,
    format=FILE_FORMAT,
    level="DEBUG",
    encoding="utf8",
    rotation="1 day",
    retention=14,
)