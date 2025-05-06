import boto3
import json
import base64
from PIL import Image
import io

def generate_image(product, color, company, bg_color="white eggshell", angle="front", image_path="output.png", model_choice="sdxl"): 
    bedrock = boto3.client("bedrock-runtime")

    if model_choice == "nova":
        model_id = "amazon.nova-canvas-v1:0"
        prompt   = (f"One full {color} {product} in {angle} shot centered in "
                    f"{bg_color} studio background. Slight shadow")
        payload  = {
            "taskType": "TEXT_IMAGE",
            "textToImageParams": {"text": prompt},
            "imageGenerationConfig": {
                "numberOfImages": 1,
                "height": 768,
                "width": 768,
                "cfgScale": 8.0,
                "seed": 0
            }
        }
    else:                                   # default → SD‑XL
        model_id = "stability.stable-diffusion-xl-v1"
        payload  = {
            "text_prompts": [{
                "text": f"One full {color} {product} in {angle} shot centered "
                        f"in {bg_color} background. Slight shadow",
                "weight": 1
            }],
            "height": 768,
            "width": 768
        }

    body = json.dumps(payload)
    resp = bedrock.invoke_model(
        modelId=model_id, body=body,
        contentType="application/json", accept="application/json"
    )
        # ---- after resp = bedrock.invoke_model(...) -----------------
    resp_json = json.loads(resp["body"].read())

    if model_choice == "nova":                 # images is a list[str]
        base64_img = resp_json["images"][0]    # ← full base‑64 string
    else:                                      # SD‑XL style response
        base64_img = resp_json["artifacts"][0]["base64"]

    image_bytes = base64.b64decode(base64_img.encode("ascii"))
    image       = Image.open(io.BytesIO(image_bytes))
    image.save(image_path)
    return image



#generate_image("leggings", "green", "Lululemon")