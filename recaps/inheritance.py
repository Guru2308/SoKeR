class Page:
    def __init__ (self, heading, body):
        self.heading = heading
        self.body = body

    def create(self):
        html = f"<h1>{self.heading}</h1> <p>{self.body}</p>"
        return html
    

class Contact(Page):
    def __init__ (self, heading, body, email):
        super().__init__(heading, body)
        self.email = email

contact_page = Contact("Hi","Say hi back!","c23@gmail.com")
print(contact_page.email)
print(contact_page.body)
print(isinstance(contact_page,Page))