from PyQt6.QtWidgets import *
from Project_1_GUI import *
import csv
import math

class Students(QMainWindow, Ui_Grade_Tracker):
    LIST_OF_STUDENTS = []
    STUDENT_SCORES = {}
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.load_grades_button.clicked.connect(lambda : self.get_scores())
        self.save_grades_button.clicked.connect(lambda : self.calculate_grade())
        
    def calculate_grade(self):
        name = self.student_name_input.text()
        score = self.score_input.text()
        grade = ''
        try:
            if not score.isdigit():
                raise TypeError
            score = int(score)
            if score < 0 or score > 100:
                raise ValueError
            if score >= 90:
                grade = 'A'
            elif score <= 89 and score >= 80:
                grade = 'B'
            elif score <= 79 and score >= 70:
                grade = 'C'
            elif score <= 69 and score >= 60:
                grade = 'D'
            else:
                grade = 'F'
            self.student_label.setText(name)
            grade = str(grade)
            score = str(score)
            self.student_1_grade_output.setText(grade)
            self.student_1_grade_output.setReadOnly(True)
            self.student_1_score_output.setText(score)
            self.student_1_score_output.setReadOnly(True)
            self.append_scores(name, score, grade)
        except ValueError:
            self.error_display.setText("Score Must Be Between 0 and 100")
        except TypeError:
            self.error_display.setText("Score Must Contain Only Numbers")
        
    
    def calculate_overall_grades(self):
        student_scores = {}
        for student in Students.LIST_OF_STUDENTS:
            if student[0] not in student_scores:
                student_scores[student[0]] = int(student[1])
            elif student[0] in student_scores:
                student_scores[student[0]] += int(student[1])
        for key in student_scores:
            count = 0
            for student in Students.LIST_OF_STUDENTS:
                if student[0] == key:
                    count += 1
            student_scores[key] = math.ceil(student_scores[key] / count)
        self.display_grades(student_scores)
            
    
    def get_scores(self):
        Students.LIST_OF_STUDENTS = []
        with open('student_scores.csv', 'r', newline='') as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                Students.LIST_OF_STUDENTS.append([row[0], row[1]])
        self.calculate_overall_grades()
        

    def append_scores(self, name, score, grade):
        with open('student_scores.csv', 'a', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            to_file = [name, score, grade]
            csv_writer.writerow(to_file)
        self.get_scores()
        
    def display_grades(self, student_scores):
        scores_list = list(student_scores.items())
        self.error_display.setText("Please Enter a Name and Score")
        self.student_1_label.setText(f"{scores_list[0][0]}")
        self.student_2_label.setText(f"{scores_list[1][0]}")
        self.student_3_label.setText(f"{scores_list[2][0]}")
        self.student_4_label.setText(f"{scores_list[3][0]}")
        self.student_1_overall_grade_output.setText(f"{scores_list[0][1]}")
        self.student_1_overall_grade_output.setReadOnly(True)
        self.student_2_overall_grade_output.setText(f"{scores_list[1][1]}")
        self.student_2_overall_grade_output.setReadOnly(True)
        self.student_3_overall_grade_output.setText(f"{scores_list[2][1]}")
        self.student_3_overall_grade_output.setReadOnly(True)
        self.student_4_overall_grade_output.setText(f"{scores_list[3][1]}")
        self.student_4_overall_grade_output.setReadOnly(True)
        

        
    

