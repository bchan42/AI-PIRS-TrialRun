import os
import json
from dotenv import load_dotenv

def get_api_key():
    load_dotenv()
    email = os.getenv("USER_EMAIL")
    if not email:
        raise ValueError("USER_EMAIL not set in .env")

    with open("config.json") as f:
        config = json.load(f)

    if email not in config.get("allowed_users", []):
        raise PermissionError(f"Access denied for user: {email}")

    return config["api_key"]