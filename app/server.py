from flask import Flask, render_template

app = Flask(__name__) # Tells flask that everything it needs is in the current directory. In this case, inside /app

@app.route("/") # @ adds functionalities to the function we define below
def index():
    return render_template("index.html")

if __name__ =="__main__":
    app.run(host="0.0.0.0", port=3000, debug=True) # 0.0.0.0 is localhost, aka your computer
