# coding: utf-8
from yookassa.domain.common.response_object import ResponseObject
from yookassa.domain.models import CancellationDetails


class PersonalDataResponse(ResponseObject):
    """Информация о персональных данных"""  # noqa: E501

    __id = None

    __type = None

    __status = None

    __cancellation_details = None

    __created_at = None

    __expires_at = None

    __metadata = None

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, value):
        self.__type = value

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = value

    @property
    def cancellation_details(self):
        return self.__cancellation_details

    @cancellation_details.setter
    def cancellation_details(self, value):
        self.__cancellation_details = CancellationDetails(value)

    @property
    def created_at(self):
        return self.__created_at

    @created_at.setter
    def created_at(self, value):
        self.__created_at = value

    @property
    def expires_at(self):
        return self.__expires_at

    @expires_at.setter
    def expires_at(self, value):
        self.__expires_at = value

    @property
    def metadata(self):
        return self.__metadata

    @metadata.setter
    def metadata(self, value):
        self.__metadata = value
