# coding: utf-8
import re  # noqa: F401

from yookassa.domain.common import BaseObject
from yookassa.domain.models import Amount


class IncomeReceipt(BaseObject):
    """Данные чека, зарегистрированного в ФНС. Присутствует, если вы делаете выплату [самозанятому](/developers/payouts/scenario-extensions/self-employed). """  # noqa: E501

    __service_name = None

    __npd_receipt_id = None

    __url = None

    __amount = None

    @property
    def service_name(self):
        return self.__service_name

    @service_name.setter
    def service_name(self, value):
        self.__service_name = value

    @property
    def npd_receipt_id(self):
        return self.__npd_receipt_id

    @npd_receipt_id.setter
    def npd_receipt_id(self, value):
        self.__npd_receipt_id = value

    @property
    def url(self):
        return self.__url

    @url.setter
    def url(self, value):
        self.__url = value

    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self, value):
        if isinstance(value, dict):
            self.__amount = Amount(value)
        elif isinstance(value, Amount):
            self.__amount = value
        else:
            raise TypeError('Invalid amount data type in IncomeReceipt.amount')
