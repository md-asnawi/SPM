# Administrator
# jenkintest13
class Administrator:

    def __init__(self, name="", administrator_id=""):
        self.name = name
        self.administrator_id = administrator_id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_administrator_id(self):
        return self.administrator_id

    def set_administrator_id(self, administrator_id):
        self.administrator_id = administrator_id
