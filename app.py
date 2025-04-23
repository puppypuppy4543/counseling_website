from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add', methods=['GET', 'POST'])
def add_form():
    if request.method == 'POST':
        # Access form fields
        session = request.form.get('session')
        form_number = request.form.get('form_number')
        date = request.form.get('date')
        name = request.form.get('name')
        admission_class = request.form.get('admission_class')
        father_name = request.form.get('father_name')
        father_occupation = request.form.get('father_occupation')
        address = request.form.get('address')
        referred_by = request.form.get('referred_by')
        last_school = request.form.get('last_school')
        phone = request.form.get('phone')
        school_visited = request.form.get('school_visited')
        comments = request.form.get('comments')
        counseled_by = request.form.get('counseled_by')
        principal_comments = request.form.get('principal_comments')

        # For now, just print it or later write to Excel
        print("Form submitted:")
        print(f"{session=}, {form_number=}, {date=}, {name=}, {admission_class=}, {father_name=}, {father_occupation=}")
        print(f"{address=}, {referred_by=}, {last_school=}, {phone=}, {school_visited=}, {comments=}, {counseled_by=}, {principal_comments=}")

        # Redirect or thank you page later
        return redirect(url_for('home'))

    return render_template('add.html')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
