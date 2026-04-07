class CRUD:
    def __init__(self):
        print("Student Management System")
        self.studentId=[]
        self.studentName=[]
        self.studentRollNo=[]
        self.studentCity=[]
    
    def takeChoice(self):
        print("1.Add Student")
        print("2.Show Student")
        print("3.Update Student")
        print("4.Delete Student")
        print("5.Exit")

        choice=int(input("Select your choice :"))

        if choice is 1:
            obj.addStudent()
            obj.takeChoice()
        elif choice is 2:
            obj.showStudent()
            obj.takeChoice()
        elif choice is 3:
            obj.updateStudent()
            obj.takeChoice()
        elif choice is 4:
            obj.deleteStudent()
            obj.takeChoice()
        else:
            exit()

    def addStudent(self):
        self.studentId.append(input("Enter Student Id : "))
        self.studentName.append(input("Enter Student Name : "))
        self.studentRollNo.append(input("Enter Student Roll No : "))
        self.studentCity.append(input("Enter Student City : "))
        print("Data added successfully")
    
    def showStudent(self):
        print()
        print("Id\tName\tRoll No\tCity")
        print("--------------------------------------------------------------- ")
        for i in range(len(self.studentId)):
            print(self.studentId[i],"\t",self.studentName[i],"\t",self.studentRollNo[i],"\t",self.studentCity[i])
        print("----------------------------------------------------------------")

    def updateStudent(self):
        print("Select the data you want to update :")
        obj.showStudent()
        for i in range(len(self.studentId)):
            self.studentId[i]=int(input("Enter the Student Id you want to Update"))
            print("Student Name : ",self.studentName[i])
            print("Student Roll no : ",self.studentRollNo[i])
            print("Student City : ",self.studentCity[i])
            val=int(input("Enter what you want to update"))
            if val is 1:
                new_studentName=input("Enter Student Name : ")
                self.studentName[i]=new_studentName
            if val is 2:
                new_studentRollNo=input("Enter Student RollNo : ")
                self.studentRollNo[i]=new_studentRollNo
            if val is 3:
                new_studentCity=input("Enter Student City : ")
                self.studentCity[i]=new_studentCity
    
    def deleteStudent(self):
        obj.showStudent()
        val=int(input("Enter the Student Id you want to Delete"))
        for i in range(len(self.studentId)):
            if self.studentId[i] == val:
                confirm=input("Do you really want to delete data : y/n")
                if confirm.islower()=='y':
                    del self.studentId[i]
                    del self.studentName[i]
                    del self.studentRollNo[i]
                    del self.studentCity[i]
                    print("Record deleted")
                else:
                    print("Delete Cancelled")
                return
obj=CRUD()
obj.takeChoice()




