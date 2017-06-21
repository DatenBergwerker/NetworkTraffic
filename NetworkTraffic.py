import time
import re
import psutil
import logging

logging.basicConfig(filename="psutil_report.log",
                    level=logging.INFO,
                    format="%(asctime)s %(message)s",
                    datefmt="%d.%m.%Y %H:%M:%S")
output = re.compile(pattern=r"\((.*)\)")

while True:
    logging.info(output.search(str(psutil.net_io_counters(pernic=True)["devicename"])).group(1))
    time.sleep(1)
