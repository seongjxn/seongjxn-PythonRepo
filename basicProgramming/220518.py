# studentList = []
# deptList = []

# def prepareData() :
#     global studentList, deptList

#     matrials = Dept(100, '신소재공학과')
#     mechanics = Dept(200, '기계공학과')

#     deptList = [matrials, mechanics]

#     studentList = []
#     studentList.append(Student(101, '신철수', matrials))
#     studentList.append(Student(102, '신정철', matrials))
#     studentList.append(Student(201, '기대승', mechanics))
#     studentList.append(Student(202, '기정은', mechanics))

# def main() :
#     prepareData()

#     print('='*10, 'All Departments List')
#     for dept in deptList :
#         print(dept)

#     print('='*10, 'All Student List')





# dList = []

# dLen = int(input('length : '))

# for i in range(dLen) :
#     dList.append(int(input('value : ')))

# for j in range(len(dList)) :
#     print(j, ',', dList[j])





# model

class Contact:
    def __init__(self, name, phone_number, e_mail, addr):
        self.name = name
        self.phone_number = phone_number
        self.e_mail = e_mail
        self.addr = addr

    def print_info(self):
        print("Name: ", self.name)
        print("\tPhone Number: ", self.phone_number)
        print("\tE-mail: ", self.e_mail)
        print("\tAddress: ", self.addr)

def set_contact():
    name = input("Name: ")
    phone_number = input("Phone Number: ")
    e_mail = input("E-mail: ")
    addr = input("Address: ")
    contact = Contact(name, phone_number, e_mail, addr)
    return contact

def print_contact(contact_list):
    for contact in contact_list:
        contact.print_info()

def delete_contact(contact_list, name):
    for i, contact in enumerate(contact_list):
        if contact.name == name:
            del contact_list[i]

def find_contact(contact_list, name):
    for i, contact in enumerate(contact_list):
        if contact.name == name:
            contact_list[i].print_info()

def print_menu():
    print("1. 연락처 입력")
    print("2. 연락처 출력")
    print("3. 연락처 삭제")
    print("4. 연락처 검색")
    print("5. 종료")
    menu = input("메뉴선택: ")
    return int(menu)

#main program

def run():
    contact_list = []
    contact_list.append(Contact("jjh","010-111-1112","jjh@jjh.com","강화군"))
    contact_list.append(Contact("ktr","010-222-2222","ktr@ktr.com","의성군"))
    contact_list.append(Contact("lya","010-222-2222","lya@ktr.com","안성군"))    
    while 1:
        menu = print_menu()
        if menu == 1:
            contact = set_contact()
            contact_list.append(contact)
        elif menu == 2:
            print_contact(contact_list)
        elif menu == 3:
            name = input("Name to delete: ")
            delete_contact(contact_list, name)
        elif menu == 4:
            name = input("Name to find: ")
            find_contact(contact_list, name)
        elif menu == 5:
            break
if __name__ == "__main__":
    run()



