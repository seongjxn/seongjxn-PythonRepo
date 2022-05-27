
'''

# 1

class Student : 
    def __init__(self, studentNo, name, gpa, english) :
        self.studentNo = studentNo
        self.name = name
        self.gpa = gpa
        self.english = english

    def __str__(self) :
        result  = self.studentNo + '' + self.name + '' + str(self.gpa) + ''
        result += str(self.english)
        return result

i = Student('S2018001', 'i', 4.5, 990)
you = Student('S2018002', 'you', 1.5, 190)

print(i)
print(you)

print(type(i))
print(type(you))


# 2

class Student : 
    def __init__(self, studentNo, name, gpa, english) :
        self.studentNo = studentNo
        self.name = name
        self.gpa = gpa
        self.english = english

    def __str__(self) :
        result  = self.studentNo + '' + self.name + '' + str(self.gpa) + ''
        result += str(self.english)
        return result

    def canGradute(self) :
        if (self.gpa >= 2.0 and self.english >= 550) :
            print(self.name, "Can Graduate")
        else :
            print(self.name, "Can't Graduate")

i = Student('S2018001', 'i', 4.5, 990)
you = Student('S2018002', 'you', 1.5, 190)

print(i)
print(you)

print(type(i))
print(type(you))

'''

# 3

class Dept :
    def __init__(self, deptNo, name) :
        self.deptNo = deptNo
        self.name = name
    
    def __str__(self) :
        result = "(" + str(self.deptNo) + " " + self.name + ")"
        return result

class Student :
    def __init__(self, studentNo, name, dept) :
        self.studentNo = studentNo
        self.name = name
        self.dept = dept
    
    def __str__(self) -> str:
        result = "(" + str(self.studentNo) + " "
        result += self.name + " " + self.dept.name + ")"
        return result

studentList = []
deptList = []

def prepareData() :
    global deptList, studentList
    matrials = Dept(100, '신소재공학과')
    mechanics = Dept(200, '기계공학과')
    deptList = [matrials, mechanics]
    studentList = []
    studentList.append(Student(101, '신철수', matrials))
    studentList.append(Student(102, '신정철', matrials))
    studentList.append(Student(201, '기대승', mechanics))
    studentList.append(Student(202, '기정은', mechanics))

def main() :
    prepareData()
    print('='*10, 'All Departments List')
    for dept in deptList :
        print(dept)
    print('='*10, 'All Students List')
    for student in studentList :
        print(student)

main()


# 4

class Contact :
    def __init__(self, name, phoneNumber, email, addr) :
        self.name = name
        self.phoneNumber = phoneNumber
        self.email = email
        self.addr = addr

    def printInfo(self) :
        print('Name : ', self.name)
        print('\tPhone Number : ', self.phoneNumber)
        print('\te-Mail', self.email)
        print('\tAddress : ', self.addr)

def setContact() :
    name = input("Name : ")
    phoneNumber = input("Phone Number : ")
    email = input("e-Mail : ")
    addr = input("Address : ")
    contact = Contact(name, phoneNumber, email, addr)
    return contact


