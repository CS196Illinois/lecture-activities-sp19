from flask import Flask, request
import json
app = Flask(__name__)

gradebook = {}



@app.route('/add_student', methods=['POST'])
def add_student():
	student_name = request.form['student_name']
	#see if There are any assignments provided
	assignments = request.form.get('assignments', dict())
	if student_name not in gradebook:
		gradebook[student_name] = assignments
		return 'Added student'
	else:
		return 'Student already exists'


@app.route('/add_assignment', methods=['POST'])
def add_assignment():
    student_name = request.form['student_name']
    if student_name not in gradebook:
        gradebook[student_name] = dict()

    # TODO: Fill in Nones below to add the assignment
    new_assignment = dict()
    new_assignment['name'] = request.form['name'] # The name of the assignment
    new_assignment['date'] = request.form['date'] # The date of the assignment
    new_assignment['score'] = request.form['score'] # The name of the assignment
    new_assignment['total'] = request.form['total'] # The name of the assignment
    gradebook[student_name][request.form['name']] = new_assignment

    return "Assignment added"



@app.route('/assignment_grade', methods = ['GET'])
def get_score():
    student_name = request.args['student_name']
    assignment_name = request.args['assignment_name']
    student = gradebook.get(student_name, dict())
    assignment = student.get(assignment_name, "")
    return json.dumps(assignment)


@app.route('/student_grades', methods = ['GET'])
def get_grades():
	student_name = request.args['student_name']
	student = gradebook.get(student_name, '')
	return json.dumps(student)



@app.route('/assignment_average', methods = ['GET'])
def get_average():
	#TODO: return the average score on the given assignment
	assignment_name = request.args['assignment_name']
	return '0'


@app.route('/assignment_scores', methods = ['GET'])
def get_all_scores():
	assignment_name = request.args['assignment_name']
	#TODO: return a json where the keys are student names and the values are the student's scores on this assignment
	return ""



if __name__ == "__main__":
    # you may want to add a host and port parameter to this when you deploy it on ec2
    app.run()
