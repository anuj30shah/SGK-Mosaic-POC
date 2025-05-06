from flask import Flask, render_template, request, send_file, jsonify
import os
import time
from test import get_info
from generateImage import generate_image
from outpaint import outpaint
from addText import overlay_text_on_image

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        company = request.form.get("company")
        color = request.form.get("color")
        product = request.form.get("product")
        bg_color = request.form.get("bg_color")
        model = request.form.get("model")

        tagline, adv1, adv2, adv3 = process_image(company, color, product, bg_color, model)
        
        return jsonify({
            "images": ["static/output1.png", "static/output2.png", "static/output3.png", "static/output4.png", "static/output5.png", "static/output6.png", "static/output7.png", "static/output8.png", "static/output9.png"],
            "tagline": tagline,
            "adv1": adv1,
            "adv2": adv2,
            "adv3": adv3
        })
    
    return render_template("index.html")

@app.route("/outpaint", methods=["POST"])
def outpaint_image():
    image_path = request.form.get("image_path")
    product = request.form.get("product")
    bg_color = request.form.get("bg_color")

    outpaint_scale = float(request.form.get("outpaint-scale"))
    orientation = request.form.get("orientation")

    if orientation == "landscape":
        width = 1408
        height = 768
        width_ratio = outpaint_scale
        height_ratio = 0.5
    else:
        width = 768
        height = 1408
        width_ratio = 0.5
        height_ratio = outpaint_scale


    
    outpaint_one(product, bg_color, image_path, width_ratio=width_ratio, height_ratio=height_ratio, width=width, height=height)
    
    return jsonify({"outpainted_image": "static/outpaint.png"})

def process_image(company, color, product, bg_color, model):
    while True:
        try:
            tagline, adv1, adv2, adv3, ang1, ang2, ang3, ang4, ang5, ang6, ang7, ang8, ang9 = get_info(company, product=product)
            break
        except:
            time.sleep(1)

    image1 = generate_image(product, color, company, bg_color=bg_color, angle=ang1, image_path="static/output1.png", model_choice=model)
    image2 = generate_image(product, color, company, bg_color=bg_color, angle=ang2, image_path="static/output2.png", model_choice=model)
    image3 = generate_image(product, color, company, bg_color=bg_color, angle=ang3, image_path="static/output3.png", model_choice=model)
    image4 = generate_image(product, color, company, bg_color=bg_color, angle=ang4, image_path="static/output4.png", model_choice=model)
    image5 = generate_image(product, color, company, bg_color=bg_color, angle=ang5, image_path="static/output5.png", model_choice=model)
    image6 = generate_image(product, color, company, bg_color=bg_color, angle=ang6, image_path="static/output6.png", model_choice=model)
    image7 = generate_image(product, color, company, bg_color=bg_color, angle=ang7, image_path="static/output7.png", model_choice=model)
    image8 = generate_image(product, color, company, bg_color=bg_color, angle=ang8, image_path="static/output8.png", model_choice=model)
    image9 = generate_image(product, color, company, bg_color=bg_color, angle=ang9, image_path="static/output9.png", model_choice=model)
    
    return tagline, adv1, adv2, adv3

def outpaint_one(product, bg_color, image_path, width_ratio, height_ratio, width, height):
    image = outpaint(product, bg_color=bg_color, load_image_path=image_path, width_ratio=width_ratio, height_ratio=height_ratio, width=width, height=height)
    image.save("static/outpaint.png")
    return "image"

if __name__ == "__main__":
    app.run(debug=True)
