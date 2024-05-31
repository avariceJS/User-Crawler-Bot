# coding: utf-8
import re  # noqa: F401

from yookassa.domain.common import BaseObject


class SelfEmployedConfirmation(BaseObject):
    """
    Base class confirmation data objects
    """
    __type = None

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, value):
        self.__type = str(value)


class SelfEmployedConfirmationType:
    """Код сценария подтверждения пользователем заявки ЮMoney на получение прав для регистрации чеков в сервисе Мой налог. """  # noqa: E501
    REDIRECT = 'redirect'
