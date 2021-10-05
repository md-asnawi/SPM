# Learning Material
class LearningMaterial:
    def __init__(self, type, file_name):
        self.type = type
        self.file_name = file_name

    def get_type(self):
        return self.type

    def set_type(self, type):
        self.type = type

    def get_file_name(self):
        return self.file_name

    def set_file_name(self, file_name):
        self.file_name = file_name