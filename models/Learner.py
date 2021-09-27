from Engineer import Engineer

# Learner inherits from Engineer
class Learner(Engineer):

    def __init__(self, name = "", engineer_id = "", learner_id = ""):
        super().__init__(name, engineer_id)
        self.learner_id = learner_id

    def get_learner_id(self):
        return self.learner_id

    def set_learner_id(self, learner_id):
        self.learner_id = learner_id