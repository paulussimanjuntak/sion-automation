from services.serve import app
from flask import redirect, url_for

@app.route('/')
def index():
    return redirect(url_for('sions.sion'))

if __name__ == '__main__':
    app.run()
