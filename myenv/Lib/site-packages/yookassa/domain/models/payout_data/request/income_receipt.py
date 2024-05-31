# coding: utf-8
import re  # noqa: F401

from yookassa.domain.common import BaseObject
from yookassa.domain.models import Amount


class IncomeReceiptData(BaseObject):
    """Данные для формирования чека в сервисе Мой налог. Необходимо передавать, если вы делаете выплату %[самозанятому](/developers/payouts/scenario-extensions/self-employed). Только для обычных выплат. """  # noqa: E501

    __service_name = None

    __amount = None

    @property
    def service_name(self):
        return self.__service_name

    @service_name.setter
    def service_name(self, value):
        if value is None:  # noqa: E501
            raise ValueError("Invalid value for `service_name`, must not be `None`")  # noqa: E501
        if value is not None and len(value) > 50:
            raise ValueError("Invalid value for `service_name`, length must be less than or equal to `50`")  # noqa: E501
        self.__service_name = value

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
            raise TypeError('Invalid amount data type in IncomeReceiptData.amount')
