from Engineer import Engineer

# Trainer inherits from Engineer
class Trainer(Engineer):

    def __init__(self, name = "", engineer_id = "", trainer_id = ""):
        super().__init__(name, engineer_id)
        self.trainer_id = trainer_id

    def get_trainer_id(self):
        return self.trainer_id

    def set_trainer_id(self, trainer_id):
        self.trainer_id = trainer_id