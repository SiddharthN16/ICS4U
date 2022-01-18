from abc import ABC, abstractmethod

class Document(ABC):
    '''
    An abstract class which acts as a template for any documents to be created, which all have a signature

    Attributes
    ----------
    genDate : str
        Generates the current date and time when used
    teacher : str
        Name of the teacher creating the document

    Methods
    -------
    signature() -> void
        Abstract method used to create a signature from the teacher
    '''

    def __init__(self,teacher,genDate):
        '''
        Constructor to build the Document object

        Parameters
        ----------
        teacher : str
            Generates the current date and time when used
        genDate : str
            Name of the teacher creating the document
        '''
        self.genDate = genDate
        self.teacher = teacher

    # Abstract method for creating a signature which every document has
    @abstractmethod
    def signature(self):
        '''
        Abstract method to create a template for the signature that every Document has
        '''
        pass