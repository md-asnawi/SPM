# Learning Material
class LearningMaterial:
    def __init__(self, documents, videos, hyperlinks):
        self.documents = documents
        self.videos = videos
        self.hyperlinks = hyperlinks

    def get_documents(self):
        return self.documents

    def set_documents(self, documents):
        self.documents = documents

    def get_videos(self):
        return self.videos

    def set_video(self, video):
        self.video = video

    def get_hyperlinks(self):
        return self.hyperlinks

    def set_hyperlinks(self, hyperlinks):
        self.hyperlinks = hyperlinks