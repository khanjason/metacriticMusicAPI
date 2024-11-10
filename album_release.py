class AlbumRelease():
    def __init__(self,artist,title,date):
        self.artist=artist
        self.title=title
        self.release_date = date

class AnticipatedRelease(AlbumRelease):
    def __init__(self,artist,title,date):
        super().__init__(artist,title,date)

class ConfirmedRelease(AlbumRelease):
    def __init__(self,artist,title,date,notes):
        super().__init__(artist,title,date)
        self.notes = notes
    def convert_date():
        pass


    
