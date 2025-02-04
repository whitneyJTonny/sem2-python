#Create a class for the author

class Author:
    def __init__(self,name,email,contact):
        self.name = name
        self.email = email
        self.contact = contact
        
    def display_info(self):
        print(f"Name:{self.name}")
        print(f"Email:{self.email}")
        print(f"Contact:{self.contact}")
    
    def name_email_and_contact(self):
        return (f"Name: {self.name}, Email: {self.email}")
    
    def __str__(self):
       return f"Author(Name: {self.name}, Email: {self.email}, Contact: {self.contact})"

        
my_author = Author('Whitney Josephin','whitneyjosephin042@gmail.com',707980632)

print(my_author)

my_author.display_info()
print(my_author.name_email_and_contact)
