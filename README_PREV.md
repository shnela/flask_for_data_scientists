# Flask-WTF - revision

[README_PREV.md](./README_PREV.md)
(I'm cheating - it's readme_prev_prev, but haven't done anything interesting recently)

[Flask - Uploading Files][]
1. A `<form>` tag is marked with `enctype=multipart/form-data` and an `<input type=file>` is placed in that form.
1. The application accesses the file from the files dictionary on the request object.
1. use the save() method of the file to save the file permanently somewhere on the filesystem.


## Current dir
Instruction in `auxiliary_code/python_path.py`

## Problem with `regexp_validator`
Replace it with
```python
def validate_input_data(self, field):
    data = field.data
    if not data or not data.filename.endswith('.csv'):
        raise ValidationError('Only csv files allowed')
```

## Save file
```python
file = form.input_data.data
filename = secure_filename(file.filename)
file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
```

Where I got it from? Show debugger.


## Assignment
Save recently uploaded `filename` in session and display it's name in index.  
Add new view `download` which will use [Flask - send_from_directory] and returns the file.  
Add `<a>` in `index` which will be responsible for downloading csv.
```html
<a href="{{ url_for('download') }}">download file ({{ session.filename }})</a>
```


[Flask - Uploading Files]: https://flask.palletsprojects.com/en/1.1.x/patterns/fileuploads/
[Flask - send_from_directory]: https://flask.palletsprojects.com/en/1.1.x/api/#flask.send_from_directory
