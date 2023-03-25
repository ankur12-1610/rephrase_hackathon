import requests
import os
import sys
from dotenv import load_dotenv

load_dotenv()

bearer_token = os.getenv('REPHRASE_API_KEY')
campaign_id = os.getenv('CAMPAIGN_ID')

url = f"https://personalized-brand.api.rephrase.ai/v2/campaign/{campaign_id}"

headers = {
    "accept": "application/json",
    "Authorization": bearer_token
}

response = requests.get(url, headers=headers)

print(response.text)
