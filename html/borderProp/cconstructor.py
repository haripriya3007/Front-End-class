class students:
    def __init__(self,name="",rollno=0,age=0,address="",phno=0):
        self.name=name
        self.rollno=rollno
        self.age=age
        self.address=address
        self.phno=phno
    def show_details(self):
        print(f"Name={self.name}\nRollno={self.rollno}\nAge={self.age}\nAddress={self.address}\nPh:no{self.phno}")  
print("\n****First student details****")         
student_info1=students("siva",1001,20,"pondy",37262874)
student_info2=students("priya",1002,17,"chennai",64262846)
student_info1.show_details() 
print("\n****Second student details****")  
student_info2.show_details()          

        