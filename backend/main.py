from flask import Flask, render_template
from config import Config  # vi fixar config strax

app = Flask(__name__, template_folder='../webapp/templates', static_folder='../webapp/static')
app.config.from_object(Config)


@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
