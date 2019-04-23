import requests
import json
import random
students = ['Prithvi', 'Ziv', 'Josh', 'John', 'Jake', 'James', 'Bill', 'Jack', 'Duke', 'Challen', 'Aaron', 'Emily', 'Allison', 'Jennifer']
#YOU HAVE TO CHANGE THE ENDPOINT HERE TO YOUR EC2 ENDPOINT
endpoint = 'http://127.0.0.1:5000'
def add_students():
	for student in students:
		data = {'student_name': student}
		response = requests.post(endpoint + '/add_student', data = data, auth = None)
		if response.content != 'Added student':
			print('failed to add student ' + str(student) + ' server response: ' + response.content)


def add_assignments():
	for student in students:
		for i in range(1, 15):
			data = {'student_name': student, 'name': 'Exam ' + str(i), 'date':'2/' + str(i*2) + '/19', 'score': str(random.randint(0, 101)), 'total':'100'}
			response = requests.post(endpoint + '/add_assignment', data = data, auth = None)
			if response.content != 'Assignment added':
				print('failed to add assignment ' + str(i) + ' for student ' + str(student) + ' server response: ' + response.content)




def get_score(student = 'Nobody', assignment = 'Nothing'):
	response = requests.get(endpoint + '/assignment_grade?student_name=' + student + '&assignment_name=' + assignment, auth = None)
	info = json.loads(response.content)
	if info.get('name', '') != assignment:
		print('Failed to get assignment ' + assignment + ' Server response ' + response.content)


if __name__ == "__main__":
	add_students()
	add_assignments()
	get_score('Prithvi', 'Exam 4')