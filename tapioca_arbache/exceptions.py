from tapioca.exceptions import TapiocaException


class ConflictException(TapiocaException):
    def __init__(self, message='', client=None):
        super(ConflictException, self).__init__(message, client=client)


class MissingUrlExeption(TapiocaException):
    def __init__(self, message='A url a se requisitar não foi especificadas', client=None):
        super().__init__(message, client)
