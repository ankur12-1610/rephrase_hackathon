import os
import requests
from dotenv import load_dotenv

load_dotenv()

bearer_token = os.getenv('REPHRASE_API_KEY')

url = "https://personalized-brand.api.rephrase.ai/v2/campaign/create"

images = ["https://pub-8b49af329fae499aa563997f5d4068a4.r2.dev/generations/517f8ed3-6953-4e0d-b59d-000b7121a4c3-0.png",
          "https://pub-8b49af329fae499aa563997f5d4068a4.r2.dev/generations/b2d2db8f-c6d7-448f-be84-286e3b1bd9d7-0.png",
          "https://pub-8b49af329fae499aa563997f5d4068a4.r2.dev/generations/188fc34d-4684-4129-90b5-a1fb01bff616-0.png",
          ]

with open('summary.txt') as f:
    summary = f.read()

payload = {
    "videoDimension": {"height": 1080, "width": 1920},
    "scenes": [
        {
            "elements": [
                {
                    "style": {
                        "height": "100%",
                        "width": "100%",
                        "position": "absolute",
                        "zIndex": 1,
                    },
                    "asset": {
                        "kind": "Image",
                        "use": "Background",
                        "url": images[0],
                    },
                },
                {
                    "style": {
                        "position": "absolute",
                        "zIndex": 2,
                        "bottom": "0em",
                        "objectFit": "cover",
                        "height": "37.5em",
                        "width": "66.66666666666667em",
                        "left": "16.666666666666664em",
                    },
                    "asset": {
                        "kind": "Spokesperson",
                        "spokespersonVideo": {
                            "output_params": {
                                "video": {
                                    "resolution": {"height": 720, "width": 1280},
                                    "background": {"alpha": 0},
                                    "crop": {"preset": "MS"},
                                }
                            },
                            "model": "danielle_pettee_look_2_nt_aug_2022",
                            "voiceId": "7bc739a4-7abc-46db-bc75-e24b6f899fa9__005",
                            "gender": "female",
                            "transcript": "<speak>"+summary[0]+"</speak>",
                            "transcript_type": "ssml_limited",
                        },
                    },
                },
            ]
        },
        {
            "elements": [
                {
                    "style": {
                        "height": "100%",
                        "width": "100%",
                        "position": "absolute",
                        "zIndex": 1,
                    },
                    "asset": {
                        "kind": "Image",
                        "use": "Background",
                        "url": images[1],
                    },
                },
                {
                    "style": {
                        "position": "absolute",
                        "zIndex": 2,
                        "bottom": "0em",
                        "objectFit": "cover",
                        "height": "37.5em",
                        "width": "66.66666666666667em",
                        "left": "16.666666666666664em",
                    },
                    "asset": {
                        "spokespersonVideo": {
                            "output_params": {
                                "video": {
                                    "resolution": {"height": 720, "width": 1280},
                                    "background": {"alpha": 0},
                                    "crop": {"preset": "MS"},
                                }
                            },
                            "model": "danielle_pettee_look_2_nt_aug_2022",
                            "voiceId": "7bc739a4-7abc-46db-bc75-e24b6f899fa9__005",
                            "gender": "female",
                            "transcript": "<speak>"+summary[1]+"</speak>",
                            "transcript_type": "ssml_limited",
                        },
                        "kind": "Spokesperson",
                    },
                },
            ]
        },
        {
            "elements": [
                {
                    "style": {
                        "height": "100%",
                        "width": "100%",
                        "position": "absolute",
                        "zIndex": 1,
                    },
                    "asset": {
                        "kind": "Image",
                        "use": "Background",
                        "url": images[2],
                    },
                },
                {
                    "style": {
                        "position": "absolute",
                        "zIndex": 2,
                        "bottom": "0em",
                        "objectFit": "cover",
                        "height": "37.5em",
                        "width": "66.66666666666667em",
                        "left": "16.666666666666664em",
                    },
                    "asset": {
                        "spokespersonVideo": {
                            "output_params": {
                                "video": {
                                    "resolution": {"height": 720, "width": 1280},
                                    "background": {"alpha": 0},
                                    "crop": {"preset": "MS"},
                                }
                            },
                            "model": "danielle_pettee_look_2_nt_aug_2022",
                            "voiceId": "7bc739a4-7abc-46db-bc75-e24b6f899fa9__005",
                            "gender": "female",
                            "transcript": "<speak>"+summary-summary[0]-summary[1]+"</speak>",
                            "transcript_type": "ssml_limited",
                        },
                        "kind": "Spokesperson",
                    },
                },
            ]
        },
    ],
    "title": "Into to MJ",
    "thumbnailUrl": "https://blog.siriusxm.com/wp-content/uploads/2022/11/MichaelJacksonChannel-1117.jpg",
}
headers = {
    "accept": "application/json",
    "Authorization": bearer_token,
    "content-type": "application/json",
}

response = requests.post(url, json=payload, headers=headers)
data = response.json()
campaign_id = data['campaign_id']
print(campaign_id)
f = open(".env", "a")
f.write("CAMPAIGN_ID="+campaign_id)
f.close()