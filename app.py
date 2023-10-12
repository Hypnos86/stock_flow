from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def base():
    return render_template('base.html')
@app.route("/main/")
def main():
    return render_template('main.html')


if __name__ == '__main__':
    app.debug = True
    app.run()