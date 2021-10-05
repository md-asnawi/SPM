# Course
# class_list is an attribute which contains all the Class objects
# e.g. Course SPM will have attribute class_list, which contains Class G1, Class G2...
class Course:

    def __init__(self, course_name = "", course_id = "", class_list = [], enrolment_start_date = "", enrolment_end_date = ""):
        self.course_name = course_name
        self.course_id = course_id
        self.class_list = class_list
        self.enrolment_start_date = enrolment_start_date
        self.enrolment_end_date = enrolment_end_date

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

    def get_enrolment_start_date(self):
        return self.enrolment_start_date

    def set_enrolment_start_date(self, enrolment_start_date):
        self.enrolment_start_date = enrolment_start_date

    def get_enrolment_end_date(self):
        return self.enrolment_end_date

    def set_enrolment_end_date(self, enrolment_end_date):
        self.enrolment_end_date = enrolment_end_date

    