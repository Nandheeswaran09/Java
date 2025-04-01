class book:
    def __init__(self,title,author,avaiable):
        self.title=title
        self.author=author
        self.avaiable=avaiable
    
    def borrow_book(self,borrow):
        self.avaiable -= borrow
        print('BOOK BORROWED SUCCESSFULLY')
        print(f'Book Details{self.title} , {self.author} ,{self.avaiable}')
        
    def return_book(self,ret):
        self.avaiable +=ret
        print('Book Return succesfully')
        print(f'Book Details: {self.title}, {self.author}, {self.avaiable}')
    
    def display_info(self):
        print(f'Book Details: {self.title}, {self.author}, {self.avaiable}')

c1=book('python basics','John doe',5)
c1.borrow_book(1)
c1.return_book(1)
c1.display_info()
