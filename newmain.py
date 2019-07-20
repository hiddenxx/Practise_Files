import os,re
student_text_path = "Resources/students.txt"
students_folder = "Resources/Students/"

class Student():
    def __init__(self,id=None,name=None,subject=None,marks=None):
        self.id = id
        self.name = name
        self.subject = subject
        self.marks = marks
        self.file_name = self.id+"_"+ self.name +".txt"
        self.file_path = students_folder+self.file_name

    def display_all(self):
        return ("{" + f'Id : {self.id} , Name : {self.name} , Subject : {self.subject} , Marks : {self.marks}' + "}")

    def create_files(self):
        if not os.path.exists(self.file_path) :
            with open(self.file_path,mode='a+') as fp :
                print("Initializing Template.")
                lines = []
                template = '{Id : $id , Name : $name , Subject : $subject , Marks : $marks}'
                total = f"\nTotal : 0"
                lines.insert(len(lines),template)
                lines.insert(len(lines),total)
                fp.writelines(lines)

    def check_studentfile(self):
        with open(self.file_path , mode='r') as fp :
            lines = fp.readlines()

        with open(self.file_path , mode ='w') as fp :
            lines.insert(len(lines)-1,self.display_all())
            value = int(lines[-1].split(":")[1])
            value += self.marks
            lines.pop(len(lines)-1)
            lines.insert(len(lines),f"\nTotal : {value}")
            fp.writelines(lines)

def initialize_student_file():
    student_list = []
    with open(student_text_path,mode='r') as student_textfile :
        for lines in student_textfile :
            line = lines.rstrip().split(",")
            student_list.append(Student(line[0],line[1],line[2],int(line[3])))
    return student_list



def main():
    student_list = initialize_student_file()
    for index , line in enumerate(student_list) :
        line.create_files()
        line.check_studentfile()

if __name__ == '__main__':
    main()
