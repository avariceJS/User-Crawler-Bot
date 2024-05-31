# coding: utf-8
import re  # noqa: F401

from yookassa.domain.common import BaseObject


class AdditionalUserProps(BaseObject):
    """Дополнительный реквизит пользователя (тег в 54 ФЗ — 1084). <br/>Можно передавать, если вы отправляете данные для формирования чека по сценарию %[Сначала платеж, потом чек](/developers/payment-acceptance/receipts/54fz/other-services/basics#receipt-after-payment) """  # noqa: E501

    __name = None

    __value = None

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if value is not None and len(value) > 64:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `64`")  # noqa: E501
        self.__name = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        if value is None:  # noqa: E501
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501
        if value is not None and len(value) > 234:
            raise ValueError("Invalid value for `value`, length must be less than or equal to `234`")  # noqa: E501
        self.__value = value
