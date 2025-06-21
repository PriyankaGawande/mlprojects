"""import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}.log"
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok=True)
LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format='[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
)

if __name__=="__main__":
    logging.info("logging has started")"""
from datetime import datetime
import os

# Format the timestamp safely for file names
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
logs_dir = "logs"
logs_path = os.path.join(logs_dir, f"{timestamp}.log")

# Make sure only the directory part is created
os.makedirs(logs_dir, exist_ok=True)

# Now you can create/use the log file
with open(logs_path, "w") as f:
    f.write("Log initialized.\n")
