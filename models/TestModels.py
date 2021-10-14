from Course import Course
from Class import Class
import datetime

spm_course = Course("Software Project Management", "IS212")
spm_course.add_class(Class("Software Project Management", "G1", 23, datetime.date(2021, 1, 1), datetime.date(2021, 12, 31), datetime.time(8, 15), datetime.time(11, 30), "Chris"))
spm_course.add_class(Class("Software Project Management", "G2", 45, datetime.date(2021, 1, 1), datetime.date(2021, 12, 31), datetime.time(12), datetime.time(3, 15), "Swapna"))
for spm_class in spm_course.get_class_list():
    print(str(spm_class.get_course_name()) + " " + str(spm_class.get_class_id()) + ": " + str(spm_class.get_class_size()))

g1 = Class("SPM", "G1", 23, datetime.date(2021, 1, 1), datetime.date(2021, 12, 31), datetime.time(8, 15), datetime.time(11, 30), "Chris")

print(g1.get_start_time())
print(g1.get_end_time())
print(g1.get_start_date())
print(g1.get_end_date())