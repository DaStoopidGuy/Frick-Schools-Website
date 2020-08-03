from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)
data = 0


@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        valueF = request.form["F"]
        global data
        if valueF == "oneF":
            data += 1
        elif valueF == "hundredF":
            data += 100

    print(f"Value: {data}")
    return render_template("index.html", content=data)
    
@app.route("/home")
def homePage():
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)