# -----------------------------------------------------------------------------
# Name:        Algorithms Assignment Assignment
# Purpose:     Learning to design, write and analyze complex algorithms and subprograms
#
# Author:      Siddharth Nema
# Created:     15-Nov-2021
# Updated:     19-Nov-2021
# -----------------------------------------------------------------------------
from random import random, randint
from datetime import datetime
from studentInfo import StudentInfo
from reportCard import ReportCard

def update(info, changes, update):
    '''
    Updates the student's mark or course

    Adds the update to a list which contains all the updates to make. Depending on what the change is, it will take the most recent update to make, and perform change the value to the updated one

    Parameters
    ----------
    info : class
        The class which holds the current student's information, which is used to modify the mark or course
    changes : list
        Provides the name of what the change is
    update : list
        Proivdes the values of the for what the changes should be updated to

    Raises
    ------
    ValueError
        If the mark is less than 0 or greater than 100
    '''
    # Adds the Updates to a list
    updateList = []
    for i in update:
        updateList.append(i)

    # Checks if mark values are beyond its boundary
    if (str(type(updateList[0])) == "int" and (updateList[0] < 0 or updateList[0] > 100)):
        raise ValueError("The Mark cannot be below 0 or above 100")

    if (changes[0] in ["Mark", 'mark']):
        info.updatedMark(updateList[0])
        print(f"{info.studentInfo.firstName}'s Mark has been Updated to {info.mark}!")

    if (changes[-1] in ["Course", "course"]):
        info.changeCourse(updateList[-1])
        print(f"{info.studentInfo.firstName}'s Course has been Updated to {info.course}!")

def selectionSort(a):
    min = 0
    temp = 0

    for i in range(len(a)-1):
        min = i

        for j in range(i+1,len(a)):
            if a[j].mark < a[min].mark:
                min = j

        temp = a[min]
        a[min] = a[i]
        a[i] = temp

    return a

def linearSearch(a,num):
    for i in range(len(a)):
        if (a[i].mark == num):
            return i

    return -1

def binarySearch(a,num):
    low = 0
    high = len(a)-1

    while (low <= high):
        mid = int((low + high) / 2)

        if (a[mid].mark < num):
            low = mid + 1
        elif (a[mid].mark > num):
            high = mid - 1
        else:
            return mid

    return -1

# Will contain all the students and their attributes
studentList = []

# From: https://fossbytes.com/tools/random-name-generator
with open("names.txt", "r") as names:
    nameList = names.readlines()

# From: https://data.ontario.ca/en/dataset/ministry-defined-courses
with open("courses.txt", "r") as courses:
    courseList = courses.readlines()

for i in range(len(courseList)):
    courseList[i] = courseList[i].strip()

# Loop through the different students to instintaniate the classes
for i in range(100):
    nameList[i] = nameList[i].strip().split()

    # Gathering student info using data from text files or random integers/floats
    studentInfo = StudentInfo(nameList[i][0], nameList[i][1], randint(9, 12))
    course = courseList[randint(0, len(courseList)-1)]
    mark = round(random() * 99, 2)
    teacher = "JFSS"
    genDate = datetime.now().strftime("%Y-%m-%d %H:%M")

    # Adding each student to the list as a ReportCard object
    studentList.append(ReportCard(studentInfo, course, mark, teacher, genDate))

# ------------------------------------------------------------------------------------------------------------
# Select number of students to modify or change
manageCount = int(input(f"There are {len(studentList)} Students. How many Would you Like to Manage? "))

# Has to be within the number of students
if (manageCount <= len(studentList)):
    # Creates a new list with only names of students as items in studentList are of class type
    nameList = [str(i) for i in studentList]

    # Used to loop through the number of students selected
    for i in range(manageCount):
        studentSelect = ""

        # Loop Repeats if student is not in the list, else it proceeds
        while studentSelect not in nameList:
            studentSelect = input(f"[Student #{i+1}]: Which Student Would you Like to Manage?\n")

            if (studentSelect not in nameList):
                print(f"Student not Found, Try Again.")

        # Finds the selected student to modify / change from the list of students
        currStudentInfo = studentList[nameList.index(studentSelect)]

        print(f"{studentSelect} Currently has a {currStudentInfo.mark} in {currStudentInfo.course}")

        changes = ""

        try:
            # Options to choose from when modifiying students properties
            while changes not in ["Mark", "mark", "Course", "course", "Both", "both", "None", "none"]:
                changes = input(f"Would you like to change the Student's Mark or Course or Both?\n")

                # Calls the update function to change the students mark
                if (changes in ["Mark", "mark"]):
                    markUpdate = int(input(f"Enter the Student's Updated {changes.capitalize()}: "))
                    update(currStudentInfo, [changes], [markUpdate])

                # Calls the update function to change the students course
                elif (changes in ["Course", "course"]):
                    courseUpdate = input(f"Enter the Student's Updated {changes.capitalize()}: ")
                    update(currStudentInfo, [changes], [courseUpdate])

                # Calls the update function to change both mark & course
                elif(changes in ["Both", "both"]):
                    markUpdate = int(input(f"Enter the Student's Updated Mark: "))
                    courseUpdate = input(f"Enter the Student's Updated Course: ")
                    update(currStudentInfo, ['mark', 'course'], [
                           markUpdate, courseUpdate])

                 # Used to proceed without making any changes
                elif (changes in ["None", "none"]):
                    print(f"No Changes Made.\n")

                # Option selected not valid
                else:
                    print(f"Option Not Available, Please Try Again.\n")
        except TypeError as e:
            print(f"A TypeError has Occurred: {e}")
        except ValueError as e:
            print(f"A ValueError has Occured: {e}")

        # Loops to generate a report card
        genState = False
        while genState == False:
            reportGen = input(f"Would you Like to Generate a Report Card for this Student? ")

            # Generates a report card for the current student using the generateReport method & breaks
            if (reportGen in ["Yes", "yes"]):
                # Writes report card to an text file, which stores all the past writes due to append ("a") parameter
                with open("output.txt", "a") as outputFile:
                    outputFile.write(currStudentInfo.generateReport())
                    genState = True

            # breaks from the loop to proceed, if there is another students
            elif (reportGen in ["No", "no"]):
                print("\nMoving onto the Next Student.\n")
                genState = True

            # Invalid response must try again
            else:
                print("Invalid Reponse")
# ------------------------------------------------------------------------------------------------------------
# Begin Sorting & Searching after marks and courses have been finalized

# Printing the first & last 20 items of the unsorted list
print(f"Before Sorting:\n--------------------------")
first = []
last = []
for i in range(20):
    first.append(studentList[i].mark)
    last.append(studentList[-20+i].mark)
print(f"First 20:\n{first}\nLast 20:\n{last}\n")
print(f"First 20 Names:\n{studentList[:20]}\nLast 20 Names:\n{studentList[-20:]}")

first = []
last = []

print("Now Sorting Every Student's marks in the Peel Region...\n")
selectionSort(studentList) # Calling the selection sort function to sort the list

# Printing the first & last 20 items of the sorted list
for i in range(20):
    first.append(studentList[i].mark)
    last.append(studentList[-20+i].mark)

print(f"After Sorting:\n--------------------------")
print(f"First 20 Marks:\n{first}\nLast 20 Marks:\n{last}\n")
print(f"First 20 Names:\n{studentList[:20]}\nLast 20 Names:\n{studentList[-20:]}")

# Checking if the user wants to search for a mark in the list
searchQuery = input("Would you like to search for a specific mark? ")
while (searchQuery in ["yes","Yes","no","No"]):
    if(searchQuery in ["No","no"]):
        break

    markSearch = float(input("What is the mark that you are searching for? "))

    linearSearchResult = linearSearch(studentList,markSearch) # Calling the linear search function to find the mark

    studentList.sort(key=lambda x:x.mark)
    binarySearchResult = binarySearch(studentList,markSearch) # Calling the binary search function to find the mark
    # If the mark is not in the list
    if (binarySearchResult == -1 or linearSearchResult == -1):
        print(f"No Student has a mark of {markSearch}")
    else:
        # print(f"The first student in the Peel region to get a mark of {markSearch} is #{linearSearchResult or binarySearchResult} in the list of students.")
        break