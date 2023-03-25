# Rephrase.ai Hackathon project
# Installation
To run the whole project at one go, run:
- `bash run.sh` 
> Make sure `run.sh` is executable
  
For running individual scripts
- Convert resume to text: `python3 resume_to_text.py`
- Get summary of resume and prompt for stable diffusion: `python3 gpt.py`
- To get the images: `python3 get_image_url.py`
- `python3 campaign.py`
- `python3 campaign_id.py`
- To get the video link for the campaign: `python3 video_url.py`

## Note:
- Create .env file of the credentitals
- Make sure to create blank text files for the output of the scripts: `prompt_text.txt`, `summary.txt`, `resume_text.txt` and `image_url.txt`