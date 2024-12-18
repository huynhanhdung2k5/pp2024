students = [] 
courses = [] 
marks = []


def student_info():
    num_students = int(input("Number of students: "))
    for i in range(num_students):
        studentID = input("Student id: ")
        studentName = input("Student name: ")
        dob = input("DoB: ")
        students.append({"Student ID": studentID , "Name": studentName ,"DoB":dob})



def course_info():
    num_courses = int(input("Number of courses: "))
    for i in range(num_courses):
        courseID = input("Course ID: ")
        courseName = input("Course name: ")
        courses.append({"Course ID": courseID,"Course name": courseName })


def set_marks():
    if not students:
        print("No student in the list")
        student_info()

    if not courses:
        print("No course in the list")
        course_info()
    

    courseID = input("Enter course ID: ")
    exist = False
    for course in courses:
        if course["Course ID"] == courseID :
            exist = True
            break
    if not exist: 
        print("Course ID not found")

    for student in students:
        mark = float(input("Enter Student mark {} (ID: {}): " .format(student["Name"] , student["Student ID"])))
        marks.append({"Student ID": student["Student ID"] , "Course ID": courseID, "Mark":mark })



def course_list():
    if not courses:
        print("No course in the list")
        course_info()

    print("\nList of Course: ")
    for course in courses:
        print("Course ID: {0} , Course name {1}".format(course["Course ID"] , course["Course name"]))


def student_list():
    if not students:
        print("No student in the list")
        student_info()
        

    print("\nList of Students: ")
    for student in students:
        print("Student ID: {0} ,Student name {1} ,DoB: {2}".format(student["Student ID"], student["Name"], student["DoB"]))


def show_marks():
    if not students:
        print("No student in the list")
        student_info()

    if not courses:
        print("No student in the course")
        course_info()

    if not marks:
        print("There are no marks")
        set_marks()

    courseID = input("Enter course ID to show marks: ")
    exist = False
    for course in courses:
        if course["Course ID"] == courseID:
            exist = True
            break
    if not exist:
        print("Can not find course ID")
    
    print("\nMark of Student for the course {0}: ".format(courseID))
    for mark in marks:
        if mark["Course ID"] == courseID :
            studentName = next(student["Name"] for student in students if (student["Student ID"] == mark["Student ID"]))
            print("Student {} , Mark {}".format(studentName , mark["Mark"]))

def main():
    while True:
        print("1.Set student infomation")
        print("2.Set course infomation")
        print("3.Set mark for the course")
        print("4.Course list")
        print("5.Student list")
        print("6.Show mark")
        print("7.Exit")

        choice = input("Choose a number: ")
        if choice == "1" :
            student_info()
        elif choice == "2" :
            course_info()
        elif choice == "3" :
            set_marks()
        elif choice == "4" :
            course_list()
        elif choice == "5" :
            student_list()
        elif choice == "6" :
            show_marks()
        elif choice == "7" :
            print("Exit")
            break
        else:
            print("Try again")
    
main()

