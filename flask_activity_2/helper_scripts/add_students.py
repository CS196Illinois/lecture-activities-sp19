import requests
requests.post('http://127.0.0.1:5000/add_assignment',
              data = {
                'student_name':'Prithvi',
                'assignment_name': 'Exam 1',
                'assignment_date':'2/22/19',
                'assignment_score':'90',
                'assignment_total':'100',
              })


requests.post('http://127.0.0.1:5000/add_assignment',
              data = {
                'student_name':'Prithvi',
                'assignment_name': 'Exam 2',
                'assignment_date':'2/26/19',
                'assignment_score':'95',
                'assignment_total':'100',
              })


requests.post('http://127.0.0.1:5000/add_assignment',
              data = {
                'student_name':'James',
                'assignment_name': 'Exam 1',
                'assignment_date':'2/22/19',
                'assignment_score':'100',
                'assignment_total':'100',
              })


requests.post('http://127.0.0.1:5000/add_assignment',
              data = {
                'student_name':'James',
                'assignment_name': 'Exam 2',
                'assignment_date':'2/26/19',
                'assignment_score':'85',
                'assignment_total':'100',
              })
