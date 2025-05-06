from test import get_info
from generateImage import generate_image
from outpaint import outpaint
from addText import overlay_text_on_image
import time
# def main(company, color, product):
#     while True:
#         try:
#             tagline, adv1, adv2, adv3 = get_info(company)
#             print("get_info returned:", product, tagline, adv1, adv2, adv3)
#             break
#         except:
#             time.sleep(1)

#     image = generate_image(product, color, company)
#     print("gen_image returned")
#     image = outpaint(product)
#     print("outpaint returned")
#     image = overlay_text_on_image("outpaint.png", product, tagline, adv1, adv2, adv3,  "overlayed_image.png")
#     print("add_text returned")
#     #image.show()
#     print("done")

# company = input("Enter company name: ")
# color = input("Enter color: ")
# main(company, color)

outpaint(load_image_path="static/output1.png", width_ratio=0.5, height_ratio=0.75, width=768, height=1408, bg_color="white", product="shoes")  # Example usage
