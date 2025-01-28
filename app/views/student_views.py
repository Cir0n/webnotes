from flask import Blueprint, render_template, request
from app.controllers.student_controller import StudentController

class StudentViews:
    def __init__(self):
        self.student_bp = Blueprint('student_bp', __name__)
        self.controller = StudentController()
        self.register_routes()

    def register_routes(self):
        @self.student_bp.route('/students/<int:student_id>')
        def student_details(student_id):
            student = self.controller.get_student(student_id)
            if "error" in student:
                return render_template('error.html') 
            return render_template('student/dashboard.html', student=student)
        
        @self.student_bp.route('/students')
        def list_students():
            students = self.controller.list_students()
            return render_template('student/list.html', students=students)
        
        @self.student_bp.route('/students/add', methods=['GET', 'POST'])
        def add_student():
            data = request.form
            self.controller.create_student(
                first_name=data.get('first_name'),
                last_name=data.get('last_name'),
                student_class=data.get('class')
            )
            return render_template('student/add.html')  
        
