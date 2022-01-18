from random import random, randint
from datetime import datetime
from studentInfo import StudentInfo
from reportCard import ReportCard
import timeit
import csv

# THIS FILE IS USED TO GATHER EMPIRCAL DATA FROM SORTING & SEARCHING ALGORITHMS
# main.py INCLUDES USER INPUTS, PREVENTING FOR AUTOMATED DATA COLLECTION

def selectionSort(a):
    min = 0
    temp = 0

    for i in range(len(a)-1):
        min = i

        for j in range(i+1,len(a)):
            if a[j].mark < a[min].mark:
                min = j

        temp = a[min].mark
        a[min].mark = a[i].mark
        a[i].mark = temp

    return a

def linearSearch(a,num):
    for i in range(len(a)):
        if (a[i].mark == num):
            return i

    return -1

def binarySearch(a,num):
    a.sort(key=lambda x: x.mark)
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

# From: https://fossbytes.com/tools/random-name-generator
with open("names.txt", "r") as names:
    nameList = names.readlines()

# From: https://data.ontario.ca/en/dataset/ministry-defined-courses
with open("courses.txt", "r") as courses:
    courseList = courses.readlines()

with open("runtimes/linear.csv","a",newline="") as lin:
    linear = csv.writer(lin)
    linear.writerow(["Objects", "Runtime"])

with open("runtimes/binary.csv","a",newline="") as bin:
    binary = csv.writer(bin)
    binary.writerow(["Objects", "Runtime"])

with open("runtimes/selection.csv","a",newline="") as sel:
    selection = csv.writer(sel)
    selection.writerow(["Objects", "Runtime"])

for i in range(len(courseList)):
    courseList[i] = courseList[i].strip()

# Loop through the different students to instintaniate the classes
for count in range(1,501):
    # Will contain all the students and their attributes

    studentList = []
    
    for i in range(count*100):

        # Gathering student info using data from text files or random integers/floats
        studentInfo = StudentInfo(nameList[i][0], nameList[i][1], randint(9, 12))
        course = courseList[randint(0, len(courseList)-1)]
        mark = round(random() * 99, 2)
        teacher = "JFSS"
        genDate = datetime.now().strftime("%Y-%m-%d %H:%M")

        # Adding each student to the list as a ReportCard object
        studentList.append(ReportCard(studentInfo, course, mark, teacher, genDate))

    selectionSortTime = timeit.timeit(lambda:selectionSort(studentList),number=1) # Uses timit function to find the runtime of the function
    with open("runtimes/selection.csv","a",newline="") as sel:
        selection = csv.writer(sel)
        selection.writerow([len(studentList),selectionSortTime])

    markSearch = round(random() * 99, 2)

    linearSearchTime = timeit.timeit(lambda:linearSearch(studentList,markSearch),number=1) # Uses timit function to find the runtime of the function
    with open("runtimes/linear.csv","a",newline="") as lin:
        linear = csv.writer(lin)
        linear.writerow([len(studentList),linearSearchTime])

    binarySearchTime = timeit.timeit(lambda:binarySearch(studentList,markSearch),number=1) # Uses timit function to find the runtime of the function
    with open("runtimes/binary.csv","a",newline="") as bin:
        binary = csv.writer(bin)
        binary.writerow([len(studentList),binarySearchTime])