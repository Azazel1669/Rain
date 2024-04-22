from flask import Flask, url_for, request
from flask import render_template


app = Flask(__name__)

@app.route('/text')
def news():
    if request.method == 'GET':
        return render_template('site.html')
    elif request.method == 'POST':
        return render_template('site.html')
        print(request.form['about'])



if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')