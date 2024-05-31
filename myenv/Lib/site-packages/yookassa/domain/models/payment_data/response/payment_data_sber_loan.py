# -*- coding: utf-8 -*-
import re

from yookassa.domain.common.payment_method_type import PaymentMethodType
from yookassa.domain.models import Amount
from yookassa.domain.models.payment_data.payment_data import ResponsePaymentData


class PaymentDataSberLoan(ResponsePaymentData):
    __loan_option = None

    __discount_amount = None

    def __init__(self, *args, **kwargs):
        super(PaymentDataSberLoan, self).__init__(*args, **kwargs)
        if self.type is None or self.type is not PaymentMethodType.SBER_LOAN:
            self.type = PaymentMethodType.SBER_LOAN

    @property
    def loan_option(self):
        return self.__loan_option

    @loan_option.setter
    def loan_option(self, value):
        cast_value = str(value)
        if re.match('^loan|installments_([0-9]+)$', cast_value):
            self.__loan_option = cast_value
        else:
            raise ValueError('Invalid loan_option value type')

    @property
    def discount_amount(self):
        return self.__discount_amount

    @discount_amount.setter
    def discount_amount(self, value):
        if isinstance(value, dict):
            self.__discount_amount = Amount(value)
        elif isinstance(value, Amount):
            self.__discount_amount = value
        else:
            raise TypeError('Invalid discount_amount value type')
