## Chemistry Inventory Sorter App
## Jeff Muday, Wake Forest University
## written with Mike Thompson, Lab Manager, Dept of Chemistry
## For demonstration purposes only
##
import os
from flask import (Flask, render_template,
                   request, redirect, flash,
                   url_for, send_from_directory)

from werkzeug.utils import secure_filename
import sort1

UPLOAD_FOLDER = '/uploads'
ALLOWED_EXTENSIONS = {'txt'}

sample_data = ['sodium chloride','bismuth','phosphoric acid','ferric chloride','1,3-Dimethylamylamine', 'acetic acid'
     'alpha-galactosidase','erythro-dibromide','erythomycin', 'trans-2\'-Bromostyrene',
     'threo-2 3-dibromo-3-phenylpropanoic acid','2,3-Dibromo-3-phenylpropanoic acid']

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file',
                                    filename=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''

def remove_blank_lines(mylist):
    """remove blank lines"""
    newlist = []
    for item in mylist:
        if len(item) != 0:
            newlist.append(item)
    return newlist

@app.route('/login')
def login():
    """render a login page, auth todo"""
    return render_template('login.html')

@app.route('/features')
def features():
    """render a features page"""
    return render_template('features.html')

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)

@app.route('/', methods=['GET','POST'])
def index():
    """The view of the sorter demo"""
    # get action requested 
    action = request.form.get('actionBtn')
    
    # get current state of sorted/unsorted_items textArea
    unsorted_items = request.form.get('unsorted_items')
    sorted_items = request.form.get('sorted_items')
    
    if request.method == "GET":
        # see if list is already populated, if not, get the sample data
        if unsorted_items is None:
            unsorted_items = '\n'.join(sample_data)        
    else:
        # user command submitted.
        if action == 'sort':
            # handle the SORT button
            unsorted_items = request.form.get('unsorted_items')
            mylist = unsorted_items.split('\n')
            mylist = remove_blank_lines(mylist)
            sort1.bubbleSort(mylist)
            sorted_items = '\n'.join(mylist)
        elif action == 'clearSorted':
            # handle clearSorted action
            sorted_items = ''
        else:
            pass
        
    return render_template('index.html', unsorted_items=unsorted_items, sorted_items=sorted_items)

@app.route('/contact')
def contact():
    """render the contact page"""
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=False)