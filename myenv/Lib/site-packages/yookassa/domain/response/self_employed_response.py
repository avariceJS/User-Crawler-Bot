# coding: utf-8
import re  # noqa: F401

from yookassa.domain.common import ResponseObject
from yookassa.domain.models.self_employed_data.confirmation_factory import SelfEmployedConfirmationFactory


class SelfEmployedResponse(ResponseObject):
    """Объект самозанятого. """  # noqa: E501

    __id = None

    __status = None

    __created_at = None

    __itn = None

    __phone = None

    __confirmation = None

    __description = None

    __metadata = None

    __test = None

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = str(value)

    @property
    def created_at(self):
        return self.__created_at

    @created_at.setter
    def created_at(self, value):
        self.__created_at = value

    @property
    def itn(self):
        return self.__itn

    @itn.setter
    def itn(self, value):
        self.__itn = value

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, value):
        self.__phone = str(value)

    @property
    def confirmation(self):
        return self.__confirmation

    @confirmation.setter
    def confirmation(self, value):
        self.__confirmation = SelfEmployedConfirmationFactory().create(value, self.context())

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, value):
        self.__description = value

    @property
    def metadata(self):
        return self.__metadata

    @metadata.setter
    def metadata(self, value):
        self.__metadata = value

    @property
    def test(self):
        return self.__test

    @test.setter
    def test(self, value):
        self.__test = value
