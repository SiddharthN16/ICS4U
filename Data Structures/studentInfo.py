class StudentInfo():
    '''
    A student info object that is used to hold the Student's personal information, which can be used in other objects

    Attributes
    ----------
    firstName : str
        The students first name
    grade : int
        The grade teh student is in
    lastName : str
        The students last name
    '''

    def __init__(self, firstName, lastName, grade):
        '''
        Constructor to build the studentInfo object

        Parameters
        ----------
        firstName : str
            The students first name
        lastName : str
            The students last name
        grade : int
            The grade the student is in
        '''
        self.firstName = firstName
        self.lastName = lastName
        self.grade = grade