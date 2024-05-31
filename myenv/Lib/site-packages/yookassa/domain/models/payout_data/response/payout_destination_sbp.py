# -*- coding: utf-8 -*-
from yookassa.domain.common.payment_method_type import PaymentMethodType
from yookassa.domain.models.payout_data.payout_destination import PayoutDestination


class PayoutDestinationSbp(PayoutDestination):
    """Данные для выплаты через СБП на счет в банке или платежном сервисе."""  # noqa: E501

    __phone = None

    __bank_id = None

    __recipient_checked = None

    def __init__(self, *args, **kwargs):
        super(PayoutDestinationSbp, self).__init__(*args, **kwargs)
        if self.type is None or self.type is not PaymentMethodType.SBP:
            self.type = PaymentMethodType.SBP

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, value):
        self.__phone = value

    @property
    def bank_id(self):
        return self.__bank_id

    @bank_id.setter
    def bank_id(self, value):
        self.__bank_id = value

    @property
    def recipient_checked(self):
        return self.__recipient_checked

    @recipient_checked.setter
    def recipient_checked(self, value):
        self.__recipient_checked = value
