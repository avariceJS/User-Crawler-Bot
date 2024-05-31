# coding: utf-8
import re  # noqa: F401

from yookassa.domain.common import BaseObject
from yookassa.domain.models.payment_data.request.merchant_customer_bank_account import MerchantCustomerBankAccount


class FraudData(BaseObject):

    __topped_up_phone = None

    __merchant_customer_bank_account = None

    @property
    def topped_up_phone(self):
        return self.__topped_up_phone

    @topped_up_phone.setter
    def topped_up_phone(self, value):
        if value is not None and not re.search(r'^[0-9]{4,15}$', value):  # noqa: E501
            raise ValueError(r"Invalid value for `topped_up_phone`, must be a follow pattern or equal to `/[0-9]{4,15}/`")  # noqa: E501
        self.__topped_up_phone = value

    @property
    def merchant_customer_bank_account(self):
        return self.__merchant_customer_bank_account

    @merchant_customer_bank_account.setter
    def merchant_customer_bank_account(self, value):
        if isinstance(value, dict):
            self.__merchant_customer_bank_account = MerchantCustomerBankAccount(value)
        elif isinstance(value, MerchantCustomerBankAccount):
            self.__merchant_customer_bank_account = value
        else:
            raise TypeError('Invalid merchant_customer_bank_account data type in FraudData.merchant_customer_bank_account')  # noqa: E501
