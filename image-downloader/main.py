
from flask import Flask, render_template, request
from random import randint
import requests


def download_image(image_url):
    if not image_url.startswith("http"):
        return "Invalid URL"

    filename = randint(100, 99999)
    local_filename = f"{filename}.png"

    with requests.get(image_url, stream=True) as r:
        if r.status_code == 200:
            with open(f"C:/Users/Owner/Desktop/{local_filename}", "wb") as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)
            return "Image Downloaded!"
        else:
            return "Failed to download image"


app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        urlval = request.form.get("url")
    else:
        urlval = "404"

    progress = download_image(urlval)
    return render_template('index.html', progress=progress)


if __name__ == "__main__":
    app.run(debug=True)
