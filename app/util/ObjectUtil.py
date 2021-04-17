import datetime


class ObjectUtil:

    @staticmethod
    def isNone(value):
        return False if value is not None else True

    @staticmethod
    def notNone(value):
        return False if value is None else True

    @staticmethod
    def existField(obj, field):
        if field in obj:
            return True
        else:
            return False

    @staticmethod
    def isEmpty(value: str):
        if value.strip() == '':
            return True
        else:
            return False

    @staticmethod
    def notDate(value: str):
        try:
            datetime.datetime.strptime(value, '%Y-%m-%d')
            return False
        except Exception as error:
            return True