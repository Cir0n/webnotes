from app.models.class_ import ClassModel


class ClassController:
    def __init__(self):
        self.class_model = ClassModel()

    def get_all_classes(self):
        return self.class_model.get_all_class()

    def add_class(self, name):
        self.class_model.add_class(name)
        return {"success": "Class added successfully"}
    
    def get_one_class(self, class_id):
        return self.class_model.get_one_class(class_id)
