from flask import Flask, render_template
from main import main
app = Flask("anon-web")

@app.route('/')
def home():
    return render_template('home.html', ips=main())

if __name__ == "__main__":
    app.run()
