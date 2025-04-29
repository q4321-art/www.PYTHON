from flask import Flask, render_template_string

app = Flask(__name__)

# Class Utama
class Hewan:
    def __init__(self, nama, gambar, suara_teks, audio):
        self.nama = nama
        self.gambar = gambar
        self.suara_teks = suara_teks
        self.audio = audio

    def suara(self):
        return self.suara_teks

# Subclass Inheritance (5 hewan)
class Anjing(Hewan):
    pass

class Kucing(Hewan):
    pass

class Burung(Hewan):
    pass

class Kuda(Hewan):
    pass

class Sapi(Hewan):
    pass

# Daftar semua hewan
hewan_list = [
    Anjing("Doggy", "static/foto anjink.jpg", "static/sounds/Guk guk!", "static/sounds/anjing_gukguk.mp3"),
    Kucing("Kitty", "static/kucing .jpg", "static/sounds/cat_Meong!", "static/sounds/cat_Meong!.mp3"),
    Burung("Tweety","static/burung.jpg", "static/sounds/Cuit cuit!", "static/sounds/burung.mp3"),
    Kuda("Horsey", "static/kuda.jpg", "static/sounds/Hiiih!", "static/sounds/kuda.mp3"),
    Sapi("MooMoo", "static/sapi terbang.jpg", "static/sounds/sapi_Moo!", "static/sounds/Sapi_Mooo.mp3"),
]

# Template HTML Langsung di Python
html_template = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SUARA HEWANI</title>
    <style>
        body {
            background: linear-gradient(to right, #64b3f4, #c2e9fb);
            font-family: 'Arial', sans-serif;
            color: #333;
            text-align: center;
            margin: 0;
            padding: 0;
        }
        h1 {
            padding: 20px;
            color: #fff;
            font-size: 40px;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
        }
        .container {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 30px;
            padding: 40px;
        }
        .card {
            background: #fff;
            border-radius: 20px;
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
            padding: 20px;
            text-align: center;
            transition: all 0.3s ease-in-out;
            height: 300px;
        }
        .card:hover {
            transform: scale(1.05);
            box-shadow: 0 12px 24px rgba(0, 0, 0, 0.2);
        }
        .card img {
            width: 120px;
            height: 120px;
            object-fit: cover;
            border-radius: 50%;
            margin-bottom: 20px;
        }
        .nama {
            font-size: 24px;
            font-weight: bold;
            color: #555;
            margin-bottom: 10px;
        }
        .suara {
            font-size: 18px;
            color: #888;
            margin-bottom: 10px;
        }
        audio {
            margin-top: 15px;
            background-color: #f4f4f4;
            border: none;
            padding: 5px;
            border-radius: 10px;
            width: 90%;
        }
    </style>
</head>
<body>
    <h1>SUARA HEWAN</h1>
    <div class="container">
        {% for hewan in hewan_list %}
        <div class="card">
            <img src="{{ hewan.gambar }}" alt="{{ hewan.nama }}">
            <div class="nama">{{ hewan.nama }}</div>
            <div class="suara">{{ hewan.suara() }}</div>
            <audio controls>
                <source src="{{ hewan.audio }}" type="audio/mpeg">
                Browser kamu tidak mendukung audio.
            </audio>
        </div>
        {% endfor %}
    </div>
</body>
</html>
'''

@app.route('/')
def index():
    return render_template_string(html_template, hewan_list=hewan_list)

if __name__ == '__main__':
    app.run(debug=True)
