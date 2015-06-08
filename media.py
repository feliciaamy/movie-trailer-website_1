import webbrowser

class Movie():
    """This class provides a way to store movie related information"""
    
    def __init__(self,title='',storyline='',poster='',youtube='',rating='',rank=''):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster
        self.trailer_youtube_url = youtube
        self.rating = rating
        self.rank = rank

    def setTitle(self,title):
        self.title = title

    def setStoryline(self,storyline):
        self.storyline = storyline

    def setPoster(self,poster):
        self.poster_image_url = poster

    def setTrailer(self,youtube):
        self.trailer_youtube_url = youtube

    def setRating(self,rating):
        self.rating = rating
        
    def setRank(self,rank):
        self.rank = rank

    def getTitle(self):
        return self.title
        
    def show_trailer(self):
        #Open youtube to show the trailer of the movie
        webbrowser.open(self.trailer_youtube_url)
