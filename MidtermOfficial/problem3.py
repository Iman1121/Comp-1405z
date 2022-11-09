def print_sorted_list(data):
    #clearing files used for the function
    file = open("sorted_list.txt","w")
    file.write("")
    file.close()

    file = open(data,"r")
    line = file.readline()
    count = 1
    names = 0
    string = ""
    while line !="":
        string = string + line
        if(count == 6):
            names +=1 
            count = 0
        line = file.readline()
        count += 1
    file.close()
    file = open("list.txt","w")
    file.write(string)
    file.close()
    
    for x in range(names):
        file = open(data,"r")
        line = file.readline().strip()
        count = 1
        highest_grade = 0
        highest_grade_name = ""
        first_name1 = ""
        last_name1 = ""
        assignment1 = ""
        midterm1 = ""
        exam1 = ""
        student_number1 = ""
        #searching for the highest mark

        while line != "":
            if(count == 1):
                first_name = line
            elif(count == 2):
                last_name = line
            elif(count == 3):
                student_number = line
            elif(count == 4):
                assignment = line
            elif(count ==5):
                midterm = line
            elif(count == 6):
                exam = line
                grade = int(assignment)*0.25 + int(midterm)*0.3 + int(exam)*0.45
                name = first_name + last_name
                if(grade>highest_grade):
                    highest_grade = grade
                    highest_grade_name = name
                    first_name1 = first_name
                    last_name1 = last_name
                    assignment1 = assignment
                    midterm1 = midterm
                    exam1 = exam
                    student_number1 = student_number
                count = 0
            
            count+= 1
            line = file.readline().strip()
        file.close()
            

#pasting the given file into a new file which doesn't include the person witht he highest grade
        file = open("list.txt","r")
        line = file.readline().strip()
        string = ""
        while line != "":
            if(line.strip() == first_name1):
                pass
            elif(line.strip() == last_name1):
                pass
            elif(line.strip() == student_number1):
                pass
            elif(line.strip() == assignment1):
                pass
            elif(line.strip() == midterm1):
                pass
            elif(line.strip() == exam1):
                pass
            else:
                string = string + line
            line = file.readline()
        file.close()
        file = open("list.txt","w")
        file.write(string)
        file.close()

        file = open("sorted_list.txt", "a")
        file.write(highest_grade_name + "\n" + str(highest_grade) + "\n")
        file.close()

    file = open("sorted_list.txt", "r")
    line = file.readline()
    string = ""
    while line != "":
        string = string + line
        line = file.readline()
    file.close()
    return string
print(print_sorted_list("studentinfo1.txt"))

            

