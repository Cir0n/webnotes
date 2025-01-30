from app.models.subject import SubjectModel

class SubjectController:
    def __init__(self):
        self.model = SubjectModel()
    
    def get_all_subjects(self):
        return self.model.get_all_subjects()
    