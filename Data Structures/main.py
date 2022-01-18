#-----------------------------------------------------------------------------
# Name:        Data Structures Assignment
# Purpose:     To learn & implement objects, extending objects concepts, file IO, and formal documentation
#
# Author:      Siddharth Nema
# Created:     19-Oct-2021
# Updated:     22-Oct-2021
#-----------------------------------------------------------------------------
import json
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


# Open and read the content of the input json file
with open("input.json") as inputFile:
    inputContent = json.load(inputFile)

# Will contain all the students and their attributes
studentList = []

# Loop through the different students to instintaniate the class
for student in inputContent:
    #Gathering the info required from the json "database"
    studentInfo = StudentInfo(inputContent[student]["firstName"], inputContent[student]["lastName"], int(inputContent[student]["grade"]))
    course, mark, teacher = dict(list(inputContent[student].items())[3:]).values()
    genDate = datetime.now().strftime("%Y-%m-%d %H:%M")

    #Adding each student to the list as a ReportCard object
    studentList.append(ReportCard(studentInfo, course,int(mark), teacher, genDate))

#------------------------------------------------------------------------------------------------------------
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
                    update(currStudentInfo, ['mark', 'course'], [markUpdate, courseUpdate])

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
                #Writes report card to an text file, which stores all the past writes due to append ("a") parameter
                with open("output.txt", "a") as outputFile:
                    outputFile.write(currStudentInfo.generateReport())
                    genState = True

            # breaks from the loop to proceed, if there is another students
            elif (reportGen in ["No", "no"]):
                print("\nMoving onto the Next Student.")
                genState = True

            #Invalid response must try again
            else:
                print("Invalid Reponse")