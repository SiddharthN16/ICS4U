from gradeBook import GradeBook
class ReportCard(GradeBook):
    '''
    The object that creates the report card

    Attributes
    ----------
    studentInfo : class
        Uses the studentInfo object for the students personal information
    course : str
        The course the student is in
    mark : int
        The mark the student has in the course
    teacher : str
        The name of the teacher administrating the documents
    genDate : str
        The date the documents were generated

    Methods
    -------
    generateReport() -> str
        Generates the students report card
    '''

    def __init__(self,studentInfo,course,mark,teacher,genDate):
        '''
        Constructor to create the report card object

        Parameters
        ----------
        studentInfo : class
            Uses the studentInfo object for the students personal information
        course : str
            The course the student is in
        mark : int
            The mark the student has in the course
        teacher : str
            The name of the teacher administrating the documents
        genDate : str
            The date the documents were generated
        '''
        super().__init__(studentInfo,course,mark,teacher,genDate)

    def generateReport(self):
        '''
        Generates the students report card

        Returns
        -------
        str
            The formatted report card for the students
        '''
        return f"Hello {self.studentInfo.firstName}, Your Report Card is Attatched Below:\n|{self.studentInfo.lastName}, {self.studentInfo.firstName}|Grade: {self.studentInfo.grade}|Course: {self.course}|Mark Received: {self.mark}|\n{self.signature()}\n\n"