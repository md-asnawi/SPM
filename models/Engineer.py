# Engineer
class Engineer:
    
    def __init__(self, name = "", engineer_id = "", course_completed = ""):
        self.name = name
        self.engineer_id = engineer_id
        self.course_completed = course_completed

    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name

    def get_engineer_id(self):
        return self.engineer_id

    def set_engineer_id(self, engineer_id):
        self.engineer_id = engineer_id

    def get_course_completed(self):
        return self.course_completed 

    def set_course_completed(self, course_completed):
        self.course_completed = course_completed

    