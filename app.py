from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None

    if request.method == "POST":
        a = float(request.form["a"])
        b = float(request.form["b"])

        resultado = {
            "adicao": a + b,
            "subtracao": a - b,
            "multiplicacao": a * b,
            "divisao": a / b
        }

    return render_template("index.html", resultado=resultado)

if __name__ == "__main__":
    app.run(debug=True)
