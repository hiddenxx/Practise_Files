import os,re
from string import Template
import csv

student_text_path = "Resources/students.txt"
student_template_path = "Resources/template.txt"
students_folder = "Resources/Students/"

template_student = open(student_text_path).readline().rstrip()
template_student_headers = re.findall(r'<\b\w+\b>', template_student)
template_report = open(student_template_path).readline().rstrip()

class Student():
    def __init__(self,student_data=None,file_name="",file_path="",keylist=[]):
        self.student_data = student_data
        self.file_name = file_name
        self.file_path = students_folder + str(file_name)
        self.keylist = keylist

    def print_data(self):
        print(self.student_data)

    def setKeylist(self,dict):
        return list(dict.keys())

    def set_filename_filepath(self):
        self.keylist = self.setKeylist(self.student_data)
        for l in self.keylist :
            if re.search("roll|name|id",l) :
                self.file_name += self.student_data[l]
                self.file_path = students_folder + str(self.file_name)
    def get_marks(self):
        for l in self.keylist :
            if re.search("mark",l) :
                return int(self.student_data[l])

    def display_all(self):
        pattern = re.compile(r"(<[a-zA-z0-9.]+>)",re.IGNORECASE)
        # matches = re.finditer(pattern, template_report.lower())
        # for matchNum , match in enumerate(matches) :
        #     print(f"{matchNum}.{match.group().strip()}:{match.start()}.{match.end()}")
        matches = pattern.findall(template_report)
        result = re.sub(pattern, r'$[\g<1>]', template_report)
        result1 = re.sub(r'\$\[([^\]]*)\]',lambda x:self.student_data.get(x.group(1)),result)

        return result1


    def file_generation_template(self):
        self.set_filename_filepath()
        if not os.path.exists(self.file_path) :
            with open(self.file_path,mode='a+') as fp :
                print("Initializing Template.")
                lines = []
                total = f"\nTotal : 0"
                lines.insert(len(lines),template_report)
                lines.insert(len(lines),total)
                print(lines)
                fp.writelines(lines)
        else:
            with open(self.file_path,mode='r') as fp:
                line = fp.readline().rstrip()
                if line == template_student :
                    print(f"File with template : {line}")

    def check_studentfile(self):
        with open(self.file_path , mode='r') as fp :
            lines = fp.readlines()
            total = 0
        with open(self.file_path , mode ='w') as fp :
            lines.insert(len(lines)-1,self.display_all())
            value = self.get_marks()
            total = int(lines[-1].split(":")[1])
            total += value
            lines.pop(len(lines)-1)
            lines.insert(len(lines),f"\nTotal : {total}")
            fp.writelines(lines)

def listtodict(keys,values):
    keys = [x.lower() for x in keys]
    values = [x.lower() for x in values]
    return dict(zip(keys,values))

def student_file():
    student_list = []
    with open(student_text_path,mode='r') as student_textfile :
            student_textfile_lines = student_textfile.readlines()[1:]
            for lines in student_textfile_lines :
                line = lines.rstrip().split(",")
                student_list.append(Student(listtodict(template_student_headers,line)))
    return student_list

    # pattern = re.compile(r"<([a-zA-z0-9.]+)>",re.IGNORECASE)
    # matches = re.finditer(pattern, template_report.lower())
    # for matchNum , match in enumerate(matches) :
    #     print(f"{matchNum}.{match.group().strip()}:{match.start()}.{match.end()}")
    # matches = pattern.findall(template_report)
    # print(matches)
    # print(template_student_headers)
    # result = re.sub(pattern, r'$\g<1>', template_report)
    # t = Template(result)
    # print(result)
    # print(t.substitute(marks=1,rollno=101,studname='random',subject='random1'))

def main():
    student_list = student_file()
    for index , line in enumerate(student_list):
        line.file_generation_template()
        line.check_studentfile()
    # print(student_list[i].student_data[template_student_headers[j]])
    # for j in range(0,len(template_student_headers)):
    #     print(f"{template_student_headers[j]} : " + student_list[3].student_data[template_student_headers[j]])


if __name__ == '__main__':
    main()
