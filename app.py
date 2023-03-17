from flask import Flask, render_template, request
import os
import datetime as dt

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def upload_file():  # put application's code here
    if request.method == 'GET':
        msg = 'wait for file'
    elif request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            msg = 'No file part'
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            msg = 'No selected file'
        if file:
            filename = file.filename
            file.save(os.path.join(r'C:\\1progr\\1MY\\python\\flaskProject\\rec\\', filename))
            msg = 'got file'
    return render_template('index.html', msg=msg + '\t\t' + str(dt.datetime.now()))


if __name__ == '__main__':
    app.run()
