# `course_name` VARCHAR(45) NOT NULL,
#   `class_id` INT NOT NULL,
#   `engineer_id` INT NOT NULL,
#   `date_assigned` DATETIME NOT NULL,
#   `start_date` DATETIME NOT NULL,
#   `end_date` DATETIME NOT NULL,
#   `progress` INT NOT NULL,
#   `enrolment_status` VARCHAR(45) NOT NULL,
#   `preassigned` BOOLEAN NOT NULL,
#   `withdrawal` BOOLEAN NOT NULL

# Engineer & Class enrolment class
class Enrolment:
    
    def __init__(self, class_id = "", engineer_id = "", date_assigned = "", start_date = "", end_date = "", progress = "", enrolment_status = "", preassigned = "", withdrawal = ""):
        self.class_id = class_id
        self.engineer_id = engineer_id
        self.date_assigned = date_assigned
        self.start_date = start_date
        self.end_date = end_date
        self.progress = progress
        self.enrolment_status = enrolment_status
        self.preassigned = preassigned
        self.withdrawal = withdrawal

    def get_class_id(self):
        return self.class_id

    def set_class_id(self, class_id):
        self.class_id = class_id

    def get_engineer_id(self):
        return self.engineer_id

    def set_engineer_id(self, engineer_id):
        self.engineer_id = engineer_id

    def get_date_assigned(self):
        return self.date_assigned
    
    def set_date_assigned(self, date_assigned):
        self.date_assigned = date_assigned

    def get_start_date(self):
        return self.start_date
    
    def set_start_date(self, start_date):
        self.start_date = start_date

    def get_end_date(self):
        return self.end_date
    
    def set_end_date(self, end_date):
        self.end_date = end_date

    def get_progress(self):
        return self.progress
    
    def set_progress(self, progress):
        self.progress = progress

    def get_enrolment_status(self):
        return self.enrolment_status
    
    def set_enrolment_status(self, enrolment_status):
        self.enrolment_status = enrolment_status

    def get_preassigned(self):
        return self.preassigned
    
    def set_preassigned(self, preassigned):
        self.preassigned = preassigned

    def get_withdrawal(self):
        return self.withdrawal
    
    def set_withdrawal(self, withdrawal):
        self.withdrawal = withdrawal