from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
app = Flask(__name__)
bootstrap = Bootstrap5(app)
@app.route('/')
def home():
    return  render_template('index.html')

@app.route('/portfolio')
def test():
    return render_template('portfolio.html')
d
if __name__ == '__main__':
    app.run()