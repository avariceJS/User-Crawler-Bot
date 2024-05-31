# -*- coding: utf-8 -*-
from yookassa.domain.common.payment_method_type import PaymentMethodType
from yookassa.domain.models.payment_data.payment_data import ResponsePaymentData


class PaymentDataSbp(ResponsePaymentData):

    __sbp_operation_id = None

    def __init__(self, *args, **kwargs):
        super(PaymentDataSbp, self).__init__(*args, **kwargs)
        if self.type is None or self.type is not PaymentMethodType.SBP:
            self.type = PaymentMethodType.SBP

    @property
    def sbp_operation_id(self):
        return self.__sbp_operation_id

    @sbp_operation_id.setter
    def sbp_operation_id(self, value):
        self.__sbp_operation_id = value
