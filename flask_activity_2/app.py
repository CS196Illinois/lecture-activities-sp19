from flask import Flask, request, send_file, render_template, redirect
app = Flask(__name__)

assignments = dict()
assignments['Example Name'] = {'name': 'Impossible Assignment', 'date': '10/3/2019', 'score': '90', 'total': '100'}

@app.route('/')
def home():
    # TODO: Make this endpoint redirect to the /directory endpoint
    pass


@app.route('/directory')
def directory():
    return render_template('student_list.html', student_names=assignments.keys())


@app.route('/report/<name>')
def report(name):
    # TODO: Render the report card template for the given student
    # (Hint: you'll need to give the template student_name and student_assignments)
    # See the /directory endpoint below for an example of how templates works
    return "YOU SHOULD RENDER A TEMPLATE HERE :)"


@app.route('/add_assignment', methods=['POST'])
def add_assignment():
    student_name = request.form['student_name']
    if student_name not in assignments:
        assignments[student_name] = list()

    # TODO: Fill in Nones below to add the assignment (Hint: Use request.form)
    new_assignment = dict()
    new_assignment['name'] = None # The name of the assignment
    new_assignment['date'] = None # The date of the assignment
    new_assignment['score'] = None # The score of the assignment
    new_assignment['total'] = None # The total points of the assignment
    assignments[student_name].append(new_assignment)

    return "Assignment added."

# TODO: Make the error page (static/404.html) show up!

if __name__ == "__main__":
    app.run()
