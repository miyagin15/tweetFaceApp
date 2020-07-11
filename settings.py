import os
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv(verbose=True)

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# nifukura
X_NCMB_Application_Key = os.environ.get('X_NCMB_Application_Key')
X_NCMB_Timestamp = os.environ.get('X_NCMB_Timestamp')
X_NCMB_Signature = os.environ.get('X_NCMB_Signature')

# twitter
TW_CONSUMER_KEY = os.environ.get('TW_CONSUMER_KEY')
TW_CONSUMER_SECRET = os.environ.get('TW_CONSUMER_SECRET')
TW_TOKEN = os.environ.get('TW_TOKEN')
TW_TOKEN_SECRET = os.environ.get('TW_TOKEN_SECRET')
