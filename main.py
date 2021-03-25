from flask import Flask, render_template, url_for

app = Flask(__name__)
app.secret_key = "any-string-you-want-just-keep-it-secret"

@app.route('/')
def get_all_posts():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)