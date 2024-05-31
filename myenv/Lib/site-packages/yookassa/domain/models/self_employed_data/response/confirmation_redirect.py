# -*- coding: utf-8 -*-
from yookassa.domain.models.self_employed_data.confirmation import SelfEmployedConfirmation, \
    SelfEmployedConfirmationType


class SelfEmployedConfirmationRedirect(SelfEmployedConfirmation):
    """
    Class representing redirect confirmation data object
    """
    __confirmation_url = None

    def __init__(self, *args, **kwargs):
        super(SelfEmployedConfirmationRedirect, self).__init__(*args, **kwargs)
        if self.type is None or self.type is not SelfEmployedConfirmationType.REDIRECT:
            self.type = SelfEmployedConfirmationType.REDIRECT

    @property
    def confirmation_url(self):
        return self.__confirmation_url

    @confirmation_url.setter
    def confirmation_url(self, value):
        self.__confirmation_url = value
