from dotenv import load_dotenv
import os

load_dotenv()

# Access environment variables using os.environ
secret_key = os.environ.get('SECRET_KEY')
database_url = os.environ.get('DATABASE_URL')
