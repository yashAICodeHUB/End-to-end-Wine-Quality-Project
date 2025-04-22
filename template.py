import os
from pathlib import Path
import logging

# we create logging for model tracking and debugging
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

#next mention project name 

project_name = "WineQualityPrediction"

#list of folder
list_of_files = [
    # below are the folder inside that, there will we files
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    # below are individual file 
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html",
]

for filepath in list_of_files:
    filepath = Path(filepath) # here as this project we can ru on any os, to handle that we pass to Path funtion, it will automatically detect the os
    filedir, filename = os.path.split(filepath) # using this we actually split folder name and file name different and store into variable

    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating Directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} s already exists")