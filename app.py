from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

# Ensure there's a folder to save the uploads
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files or 'details' not in request.form:
        return 'Missing file or details'

    file = request.files['file']
    details = request.form['details']
    print("Details", details)

    if file.filename == '' or details.strip() == '':
        return 'Both file and details are required'

    if file:
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return details.upper()

if __name__ == '__main__':
    app.run(debug=True)
