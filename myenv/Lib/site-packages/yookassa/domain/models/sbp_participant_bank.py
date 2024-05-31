# coding: utf-8
from yookassa.domain.common import BaseObject


class SbpParticipantBank(BaseObject):
    """Участник СБП (Системы быстрых платежей ЦБ РФ)"""  # noqa: E501

    __bank_id = None

    __name = None

    __bic = None

    @property
    def bank_id(self):
        return self.__bank_id

    @bank_id.setter
    def bank_id(self, value):
        self.__bank_id = str(value)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = str(value)

    @property
    def bic(self):
        return self.__bic

    @bic.setter
    def bic(self, value):
        self.__bic = str(value)
