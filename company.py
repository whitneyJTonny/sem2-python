
#Create a company class

class Company:
    #contructor 
    def __init__(self,name,email,contact):
        self.name = name
        self.email = email
        self.contact = contact
        
    def __str__(self):
        return f"(Name: {self.name}, Email: {self.email}, Contact: {self.contact}"    
#creating a new instance
company_one = Company('Whitony Company','whitneyjosephin042@gmail.com',707980632) 
print(company_one) 

     
