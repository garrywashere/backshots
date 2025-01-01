from flask import Flask, render_template, request

app = Flask(__name__)

round_info = {"lives": 0, "blanks": 0, "probability": ""}


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/new_round")
def new_round():
    return render_template("new_round.html")


@app.route("/current_round", methods=["GET", "POST"])
def current_round():
    if request.method == "POST":
        round_info["lives"] = int(request.form["live"])
        round_info["blanks"] = int(request.form["blank"])

        total = round_info["lives"] + round_info["blanks"]
        round_info["probability"] = f"{round(round_info['lives']/total*100,2)}%"

    return render_template("current_round.html", round_info=round_info)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
