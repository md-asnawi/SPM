# Class, part of Course
class Class:

    def __init__(self, course_name, class_id, class_size, start_date, end_date, start_time, end_time, trainer_name):
        self.course_name = course_name
        self.class_id = class_id
        self.class_size = class_size
        self.start_date = start_date
        self.end_date = end_date
        self.start_time = start_time
        self.end_time = end_time
        self.trainer_name = trainer_name

    def get_course_name(self):
        return self.course_name

    def set_course_name(self, course_name):
        self.course_name = course_name      

    def get_class_id(self):
        return self.class_id

    def set_class_id(self, class_id):
        self.class_id = class_id      

    def get_class_size(self):
        return self.class_size

    def set_class_size(self, class_size):
        self.class_size = class_size

    def get_start_date(self):
        return self.start_date

    def set_start_date(self, start_date):
        self.start_date = start_date

    def get_end_date(self):
        return self.end_date

    def set_end_date(self, end_date):
        self.end_date = end_date

    def get_start_time(self):
        return self.start_time

    def set_start_time(self, start_time):
        self.start_time = start_time

    def get_end_time(self):
        return self.end_time

    def set_end_time(self, end_time):
        self.end_time = end_time

    def get_trainer_name(self):
        return self.trainer_name

    def set_trainer_name(self, trainer_name):
        self.trainer_name = trainer_name