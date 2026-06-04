from flask import Flask, render_template, request
from google import genai
import os

app = Flask(__name__)

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
"""

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        hasil = response.text

    return render_template("index.html", hasil=hasil)

if __name__ == "__main__":
    app.run(debug=True)