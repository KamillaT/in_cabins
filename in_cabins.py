from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
@app.route("/distribution")
def distribution():
    pilots = ["Ридли Скотт", "Энди Уир", "Марк Уотни", "Венката Капур", "Тедди Сандерс", "Шон Бин"]
    return render_template("pilots.html", pilots=pilots)


if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")
