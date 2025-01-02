from flask import Flask, render_template, request, redirect, url_for

"""
To whom it may concern,

I'm well aware this is a terrible way to implement this, it should've all been done in JavaScript, client-side.
However, I hate JavaScript and this is only a small application to run locally, so I'm not too bothered.

- Garry
"""

app = Flask(__name__)
counters = {"live": 0, "blank": 0, "probability": 0.0}


@app.route("/")
def index():
    return render_template("index.html", header="Backhots.EXE")


@app.route("/input")
def input():
    return render_template("input.html", header="New_Game.DLL")


@app.route("/submit", methods=["POST"])
def submit():
    counters["live"] = int(request.form.get("live"))
    counters["blank"] = int(request.form.get("blank"))
    return redirect(url_for("display"))


@app.route("/subtract", methods=["GET"])
def subtract():
    if request.args.get("type") == "live":
        counters["live"] -= 1
        return redirect(url_for("display"))
    elif request.args.get("type") == "blank":
        counters["blank"] -= 1
        return redirect(url_for("display"))
    else:
        return redirect(url_for("display"))


@app.route("/display")
def display():
    try:
        counters["probability"] = round(
            counters["live"] / (counters["live"] + counters["blank"]) * 100, 2
        )
    except ZeroDivisionError:
        counters["probability"] = 0.0
    return render_template("display.html", header="Current_Game.BIN", counters=counters)


@app.errorhandler(404)
def not_found(error):
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(host="127.0.0.1", port="8080", debug=True)
