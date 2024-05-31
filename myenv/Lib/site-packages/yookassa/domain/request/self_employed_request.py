# -*- coding: utf-8 -*-
from yookassa.domain.common.request_object import RequestObject
from yookassa.domain.models.self_employed_data.confirmation import SelfEmployedConfirmation
from yookassa.domain.models.self_employed_data.confirmation_factory import SelfEmployedConfirmationFactory

DESCRIPTION_MAX_LENGTH = 128


class SelfEmployedRequest(RequestObject):
    """Запрос на создание объекта самозанятого. """  # noqa: E501

    __itn = None

    __phone = None

    __confirmation = None

    __description = None

    __metadata = None

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
        if isinstance(value, dict):
            self.__confirmation = SelfEmployedConfirmationFactory().create(value, self.context())
        elif isinstance(value, SelfEmployedConfirmation):
            self.__confirmation = value
        else:
            raise TypeError('Invalid confirmation data type in SelfEmployedRequest.confirmation')

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, value):
        if value is not None and len(value) > DESCRIPTION_MAX_LENGTH:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `{}`".format(DESCRIPTION_MAX_LENGTH))  # noqa: E501
        self.__description = value

    @property
    def metadata(self):
        return self.__metadata

    @metadata.setter
    def metadata(self, value):
        self.__metadata = value

    def validate(self):
        if self.itn is None and self.phone is None:
            self.__set_validation_error('Both itn and phone values are empty in self_employed_request')

    def __set_validation_error(self, message):
        raise ValueError(message)
