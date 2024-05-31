# -*- coding: utf-8 -*-
from yookassa.domain.common.payment_method_type import PaymentMethodType
from yookassa.domain.models.payout_data.payout_destination import PayoutDestination


class PayoutDestinationSbp(PayoutDestination):
    """Данные для выплаты на счет в банке через систему быстрых платежей."""  # noqa: E501

    __phone = None

    __bank_id = None

    def __init__(self, *args, **kwargs):
        super(PayoutDestinationSbp, self).__init__(*args, **kwargs)
        if self.type is None or self.type is not PaymentMethodType.SBP:
            self.type = PaymentMethodType.SBP

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, value):
        if value is None:  # noqa: E501
            raise ValueError("Invalid value for `phone`, must not be `None`")  # noqa: E501
        self.__phone = value

    @property
    def bank_id(self):
        return self.__bank_id

    @bank_id.setter
    def bank_id(self, value):
        if value is None:  # noqa: E501
            raise ValueError("Invalid value for `bank_id`, must not be `None`")  # noqa: E501
        if value is not None and len(value) > 12:
            raise ValueError("Invalid value for `bank_id`, length must be less than or equal to `12`")  # noqa: E501
        self.__bank_id = value

