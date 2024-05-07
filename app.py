from flask import Flask, render_template, request, redirect, url_for
import Student_data as sd

app = Flask(__name__)

def get_db():
    db = sd.Data()
    return db

@app.route('/')
def index():
    db = get_db()
    data = db.return_data()
    return render_template('index.html', data=data)

@app.route('/add', methods=['POST'])
def add_data():
    db = get_db()
    id = request.form['student_id']
    name = request.form['student_name']
    branch = request.form['student_branch']
    semester = request.form['student_sem']
    marks = request.form['student_marks']
    result = db.add_data(id, name, branch, semester, marks)
    if result is not True:
        data = db.return_data()
        return render_template('index.html', message = result, data=data)
    return redirect(url_for('index'))

@app.route('/delete/<id>', methods=['GET', 'POST'])
def delete_data(id):
    if request.method == 'POST':
        db = get_db()
        result = db.delete_data(id)
        return redirect(url_for('index'))
    

@app.route('/update/<id>', methods=['POST'])
def update_data(id):
    db = get_db()
    new_name = request.form['update_student_name']
    new_branch = request.form['update_student_branch']
    new_semester = request.form['update_student_sem']
    new_marks = request.form['update_student_marks']
    result = db.update_data(id, new_name, new_branch, new_semester, new_marks)
    if result is not True:
        data = db.return_data()
        return render_template('index.html', message = result, data=data)
    return redirect(url_for('index'))



if __name__ == '__main__':
    app.run(debug=True)
