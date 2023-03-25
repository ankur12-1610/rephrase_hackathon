import requests
import json

# accessing prompt_text
with open('prompt_text.txt') as f:
    prompt_text = f.read()

# fetching data from stable diffusion
url = "https://stablediffusionapi.com/api/v3/text2img"

payload = json.dumps({
    "key": "ccrFQTXeJfqopsI6tIypuD8hauilUevAdtsN0DvMXA6JSVkn3EVzZCJXYJ7c",
    "prompt": prompt_text,
    "negative_prompt": "((out of frame)) ((not a person))",
    "width": "512",
    "height": "512",
    "samples": "1",
    "num_inference_steps": "20",
    "safety_checker": "no",
    "enhance_prompt": "yes",
    "seed": None,
    "guidance_scale": 7.5,
    "webhook": None,
    "track_id": None
})
headers = {
    'Authorization': 'Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJkYm1zcHJvamVjdC5sZWxvdHVzZ3JhbmRAZ21haWwuY29tIiwiaWF0IjoxNjY3NzI2NDQ3LCJleHAiOjE2Njc3MzcyNDd9.yfy6cxfqsd8wvcZ-jH3scCy_qglOFINATZ0g3NGpp-bnSuzoIBPgydbdaV6gB0xYUUfD1tB2IDUeGbYYDIxLDQ',
    'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)
data = response.json()
img_url = data['output'][0]
print(data)
print(img_url)

# saving it in `image_url.txt`
f = open("image_url.txt", "w")
f.write(img_url)
f.close()