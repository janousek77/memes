from flask import Flask, render_template, request
import joke
import meme

app = Flask(__name__)

@app.route("/")
def landing():
    return render_template("index.html", joke=joke.get_joke())

@app.route('/make_meme', methods=['GET', 'POST'])
def make_meme():
    top = request.form.get('top')
    bottom = request.form.get('bottom')
    filename = meme.make_meme(top, bottom)
    print(filename)
    return render_template('index.html', filename="./static/"+filename, joke=joke.get_joke())


if __name__ == "__main__":
    app.run(debug=True)
