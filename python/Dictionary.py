if __name__== '__main__':
   #list
    # students= ['truong',45, 'teacher', 'technology','STU']
    # print(students)
    # for student in students:
    #     print(student)
    # # dictionary tap khoa!
    students = {'truong': 45, 'teacher': 36, 'technology': 50}
    print(students['truong'])
    print(students['technology'])
    students['technology']=20
    print(students['technology'])
    del students['technology']
    print(students)
    #Gan gt khoa != mang append
    students['single']=70
    print(students)
    print(len(students))