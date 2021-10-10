# Learning Material
class LearningMaterial:
    def __init__(self, id, name, format, type, uploader):
        self.id = id
        self.name = name
        self.format = format
        self.type = type
        self.uploader = uploader

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_format(self):
        return self.format

    def set_format(self, format):
        self.format = format

    def get_type(self):
        return self.type

    def set_type(self, type):
        self.type = type

    def get_uploader(self):
        return self.uploader

    def set_uploader(self, uploader):
        self.uploader = uploader
