# coding: utf-8
import re  # noqa: F401

from yookassa.domain.common import BaseObject


class MerchantCustomerBankAccount(BaseObject):

    __account_number = None

    __bic = None

    @property
    def account_number(self):
        return self.__account_number

    @account_number.setter
    def account_number(self, value):
        if value is not None and not re.search(r'^[0-9]{20}$', value):  # noqa: E501
            raise ValueError("Invalid value for `account_number`, must be a follow pattern or equal to `/[0-9]{20}/`")  # noqa: E501
        self.__account_number = value

    @property
    def bic(self):
        return self.__bic

    @bic.setter
    def bic(self, value):
        if value is not None and not re.search(r'^\d{9}$', value):  # noqa: E501
            raise ValueError(r"Invalid value for `bic`, must be a follow pattern or equal to `/\d{9}/`")  # noqa: E501
        self.__bic = value
