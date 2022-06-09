from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def hello():
    main_data = {
        'a': "aaa",
        'b': "BBBB",
        'c': "CCCCC",
    }
    return render_template("index.html", main_data=main_data)


@app.route("/contacts/")
def contacts():
    dev_name = "KAPTOWE4KA"
    return render_template("contacts.html", name=dev_name)


@app.route("/results/")
def results():
    #data = ['python', 'js', 'java', 'rust', 'ruby', 'sql']
    data = []
    return render_template("results.html", data=data)


@app.route("/run/", methods=['GET'])
def run_get():
    with open("main.txt", 'r', encoding="utf-8") as f:
        text = f.read()
        data = text.split("\n")
    return render_template("form.html", data=data)


@app.route("/run/", methods=['POST'])
def run_post():
    text = request.form['input_text']
    print(text)
    with open("main.txt", 'a', encoding="utf-8") as f:
        f.write(f"{text}\n")
    return render_template("good.html")


if __name__ == "__main__":
    app.run(host="192.168.0.177", port="80", debug=True)
