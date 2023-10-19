""" Module for object tracking in raspberry pi """

import os
from dotenv import load_dotenv # pip install python-dotenv

load_dotenv()

print(os.getenv("SECRET_KEY"))
