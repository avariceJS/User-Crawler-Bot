# -*- coding: utf-8 -*-
from yookassa.domain.common.confirmation_type import ConfirmationType
from yookassa.domain.models.confirmation.request.confirmation_request import ConfirmationRequest


class ConfirmationQr(ConfirmationRequest):
    """
    Class representing qr confirmation data object
    """

    __return_url = None
    """URL, на который вернется пользователь после подтверждения или отмены платежа на веб-странице. Не более 1024 символов."""

    def __init__(self, *args, **kwargs):
        super(ConfirmationQr, self).__init__(*args, **kwargs)
        if self.type is None or self.type is not ConfirmationType.QR:
            self.type = ConfirmationType.QR

    @property
    def return_url(self):
        return self.__return_url

    @return_url.setter
    def return_url(self, value):
        cast_value = str(value)
        if cast_value:
            self.__return_url = cast_value
        else:
            raise ValueError('Invalid returnUrl value')
