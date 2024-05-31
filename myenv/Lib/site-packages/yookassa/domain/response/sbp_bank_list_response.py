# coding: utf-8
from yookassa.domain.common import BaseObject
from yookassa.domain.models import SbpParticipantBank


class SbpBankListResponse(BaseObject):
    """Список участников СБП, отсортированный по идентификатору участника в порядке убывания (desc)"""  # noqa: E501

    __type = None

    __items = None

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, value):
        self.__type = value

    @property
    def items(self):
        return self.__items

    @items.setter
    def items(self, value):
        if isinstance(value, list):
            self.__items = [SbpParticipantBank(receipt) for receipt in value]
        else:
            self.__items = value
