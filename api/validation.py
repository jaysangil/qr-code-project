from dotenv import load_dotenv
import os

# Load .env file
dotenv_loaded = load_dotenv()
print(f"Dotenv loaded: {dotenv_loaded}")

# Print environment variables
print(f"AWS_ACCESS_KEY: {os.getenv('AWS_ACCESS_KEY')}")
print(f"AWS_SECRET_KEY: {os.getenv('AWS_SECRET_KEY')}")
print(f"BUCKET_NAME: {os.getenv('BUCKET_NAME')}")
