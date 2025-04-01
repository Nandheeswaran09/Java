class employee:
    def __init__(self,name,employee_id,salary,department):
        self.name=name
        self.employee_id=employee_id
        self.salary=salary
        self.department=department
    
    def apply_raise(self,prec):
        increase=(self.salary * prec) /100
        self.salary +=increase
        print(f'Salary Updated : New salary of {self.name}, {self.salary}')
        
    def transfer_department(self,new_department):
        self.department=new_department
        print(f'Department Transferred: New Department of {self.name}, {self.department}')
        
    def display(self):
        print(f'Employee details : Name {self.name} Id : {self.employee_id}, Salary :{self.salary} , {self.department}')
        
        
c1=employee('John',101,50000,'HR')
c1.apply_raise(10)
c1.transfer_department('IT')
c1.display()
