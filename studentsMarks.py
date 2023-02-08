print ("========================================")
print       ("| Welcome to student portal |")
print ("========================================")
print ("Please enter your full name:")
name = input()
print ("Please enter your registration number:")
regNo = input()
print ("Please enter your course name:")
courseName = input()

import csv
myFile=open('studentResults.txt','a')
excel=open('studentResults.csv','a')
students=csv.writer(excel)
students.writerow(['name,studentNumber,registrationNumber,test1,test2,courseWork'])

print("=============================================")
print("Welcome to Makerere University Student Portal")
print("=============================================")

# An empty list to store the information entered
marks=[]
studentDetails=[]
# Global variables 
name=studentNumber=registrationNumber=test1=test2=courseWork=examMark=''
# A Function that prompts a student to enter their personal details
def register(name,studentNumber,registrationNumber,test1,test2,courseWork):
    name=input("Please enter your name: ")
    studentNumber=input("Please enter your student number:")
    registrationNumber=input("Please enter your registration number:")
    test1=int(input("Please enter your test one marks:"))
    test2=int(input("Please enter your test two marks:"))
    courseWork=int(input("Please enter your course work marks:"))
    
    marks.append(test1)
    marks.append(test2)
    marks.append(courseWork)
    studentDetails.append(name)
    studentDetails.append(studentNumber)
    studentDetails.append(registrationNumber)

    
    
def marksCalculation():
    register(name,studentNumber,registrationNumber,test1,test2,courseWork)
    largest=max(marks)
    largestMark=str(largest)
    marks.remove(largest)
    secondLargest=max(marks)
    secondLargestMark=str(secondLargest)
    averageScore=str((largest+secondLargest)/2)
    scoreOutOfForty=int((((largest+secondLargest)/100)/2)*40)
    scoreOfCourseWork=str(scoreOutOfForty)
    examMark=int(input("Please enter your exam marks:"))
    exam=str(examMark)
    scoreOutOfSixty=((examMark/100)*60)
    scoreOfExam=str(scoreOutOfSixty)
    finalScore=scoreOutOfForty+scoreOutOfSixty
    realScore=str(finalScore)
    # A dictionary to store details for each student
    regDictionary={'Name':name, 'Student Number':studentNumber, 'Registration Number':registrationNumber, 'Test one marks':test1, 'Test two marks':test2, 'Course work marks':courseWork, 'Exam marks':examMark,'First best done':largest,'Second best done':secondLargest,'Average Score of the best two done':averageScore,"Final score out of forty":scoreOutOfForty,'Final score out of Sixty':scoreOutOfSixty,'Final Score for the course unit':finalScore}
    studentDetails.append(exam)
    studentDetails.append(largestMark)
    studentDetails.append(secondLargestMark)
    studentDetails.append(averageScore)
    studentDetails.append(scoreOfCourseWork)
    studentDetails.append(scoreOfExam)
    studentDetails.append(realScore)
    
    
    print(studentDetails)
def printDetailsToFile():
    f = open('studentResults.txt', 'w')
    for x in studentDetails:
        f.write(x)
        f.write('\n')
marksCalculation()
printDetailsToFile()
    
    
>>>>>>> 7100d9a61d5033f0bf00f9dd3978a20c14ac2c6b
