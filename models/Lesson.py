from LearningMaterial import LearningMaterial

# Lesson, part of Class
class Lesson:
    def __init__(self, LearningMaterial, ungraded_quiz, completion_status):
        self.learning_material = learning_material
        self.ungraded_quiz = ungraded_quiz
        self.completion_status = completion_status

    def get_LearningMaterials(self):
        return self.LearningMaterial

    def set_learning_materials(self, learning_material):
        self.learning_material = learning_material

    def get_ungraded_quiz(self):
        return self.ungraded_quiz

    def set_ungraded_quiz(self, ungraded_quiz):
        self.ungraded_quiz = ungraded_quiz
