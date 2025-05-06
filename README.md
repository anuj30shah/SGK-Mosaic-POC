# Mosaic POC (Flask + Amazon Bedrock)

A lightweight demo web app that creates marketing‑style product renders with Amazon Bedrock image models and lets users *out‑paint* any chosen render onto a larger canvas.

|               |                                                     |
|---------------|-----------------------------------------------------|
| **Backend**   | Flask (Python 3.11)                                 |
| **Front‑end** | Plain HTML + Vanilla JS (Fetch API)                 |
| **Models**    | • Stable Diffusion XL (`stability.stable-diffusion-xl-v1`)  <br>• Nova Canvas (`amazon.nova-canvas-v1:0`) |
| **AWS**       | Bedrock Runtime (image generation)                  |
| **Key files** | `app.py`, `generateImage.py`, `outpaint.py`, `addText.py`, `templates/index.html` |

---

## Features
- **Text‑to‑Image** — supply *company*, *product*, *color*, *background color*, and pick **SD‑XL** or **Nova Canvas**.
- **Nine camera angles** — each request saves `static/output1.png` … `output9.png`.
- **Out‑painting** — extend any render using Titan Image Generator v2 (`static/outpaint.png`).
- **Copy text** — `get_info()` returns a tagline plus three ad blurbs.
- **Text overlays** — `addText.py` can drop branded boxes onto an image.

---

## Folder Structure
├── app.py # Flask routes
├── generateImage.py # Bedrock T2I (SD‑XL or Nova)
├── outpaint.py # Bedrock Titan v2 out‑painting helper
├── addText.py # PIL overlay utility
├── templates/
│ └── index.html # web form + JS
└── static/ # generated PNGs are written here

## Prerequisites
1. **Python 3.11**  
2. **AWS account** with Bedrock enabled (e.g. `us‑east‑1`) and IAM permissions 

