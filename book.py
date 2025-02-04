
class Book():
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages
        
    def display_info(self):
        print(f"Title:{self.title}")
        print(f"author:{self.author}")
        print(f"pages:{self.pages}")
    
    def title_and_author(self):
        return (f"Title: {self.title}, Author: {self.author}")

my_book = Book('Tarnished are the stars','Rosiee Thor',398)
print(my_book.title_and_author())   
    
