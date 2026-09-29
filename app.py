from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
  return "Blog de Noticias"

@app.route("/noticias")
def noticias():
  return "Aqui estarão as noticias"

@app.route("/sobre")
def sobre():
  return "Sobre o blog de noticias"

if __name__ == "__main__":
  app.run(debug=True)