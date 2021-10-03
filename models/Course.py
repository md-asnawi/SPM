# Course
# class_list is an attribute which contains all the Class objects
# e.g. Course SPM will have attribute class_list, which contains Class G1, Class G2...
class Course:

    def __init__(self, course_name = "", course_id = "", class_list = [], enrolmentstartdate = "", enrolmentenddate = ""):
        self.course_name = course_name
        self.course_id = course_id
        self.class_list = class_list
        self.enrolmentstartdate = enrolmentstartdate
        self.enrolmentenddate = enrolmentenddate

    def get_course_name(self):
        return self.course_name
    
    def set_course_name(self, course_name):
        self.course_name = course_name

    def get_course_id(self):
        return self.course_id

    def set_course_id(self, course_id):
        self.course_id = course_id

    def get_class_list(self):
        return self.class_list

    def add_class(self, Class):
        self.class_list.append(Class)

    def remove_class(self, Class):
        self.class_list.remove(Class)