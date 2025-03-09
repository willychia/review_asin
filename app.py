from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    asin_list = []
    if request.method == "POST":
        asin_input = request.form.get("asin_input")
        if asin_input:
            asin_list = [asin.strip() for asin in asin_input.replace("\n", ",").split(",") if asin.strip()]
    return render_template("index.html", asin_list=asin_list)

if __name__ == "__main__":
    app.run(debug=True)