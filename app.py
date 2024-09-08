from flask import Flask, render_template, redirect, url_for
from form import StudentForm, BankForm
from model import db, Student, Bank
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

# Home route to accept student and bank details
@app.route('/', methods=['GET', 'POST'])
def index():
    student_form = StudentForm()
    bank_form = BankForm()

    if student_form.validate_on_submit() and bank_form.validate_on_submit():
        # Create new Student and Bank records
        new_student = Student(
            name=student_form.name.data,
            age=student_form.age.data,
            course=student_form.course.data
        )
        new_bank = Bank(
            bank_name=bank_form.bank_name.data,
            account_number=bank_form.account_number.data,
            ifsc_code=bank_form.ifsc_code.data,
            student=new_student  # Link bank details with the student
        )

        db.session.add(new_student)
        db.session.add(new_bank)
        db.session.commit()

        return redirect(url_for('student_details'))

    return render_template('index.html', student_form=student_form, bank_form=bank_form)

# Route to display student details with bank information
@app.route('/student_details')
def student_details():
    students = Student.query.all()
    return render_template('student_details.html', students=students)

if __name__ == '__main__':
    app.run(debug=True)
