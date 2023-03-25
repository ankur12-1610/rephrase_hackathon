import requests
import os
import sys
from dotenv import load_dotenv

load_dotenv()
bearer_token = os.getenv('REPHRASE_API_KEY')
campaign_id = os.getenv('CAMPAIGN_ID') # From previous script


url = f"https://personalized-brand.api.rephrase.ai/v2/campaign/{campaign_id}/export"

headers = {
    "accept": "application/json",
    "Authorization": bearer_token,
}

response = requests.post(url, headers=headers)

print(response.text)