from flask import Flask, render_template, request
from google import genai
import os

app = Flask(
    __name__,
    template_folder="../templates",
    static_folder="../static"
)

client = genai.Client(
    api_key=os.environ.get("GEMINI_API_KEY")
)

@app.route("/", methods=["GET", "POST"])
def index():
    hasil = None

    if request.method == "POST":
        fakultas = request.form.get("fakultas")
        prodi = request.form.get("prodi")
        topik = request.form.get("topik")

        prompt = f"""
Buatkan 10 judul skripsi:

Fakultas: {fakultas}
Prodi: {prodi}
Topik: {topik}

Buat yang modern, relevan, dan layak dijadikan penelitian.
"""

        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )

            hasil = response.text

        except Exception as e:
            hasil = f"Error: {str(e)}"

    return render_template("index.html", hasil=hasil)

app = app
