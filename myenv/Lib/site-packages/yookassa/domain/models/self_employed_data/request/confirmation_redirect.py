# -*- coding: utf-8 -*-
from yookassa.domain.models.self_employed_data.confirmation import SelfEmployedConfirmation, \
    SelfEmployedConfirmationType


class SelfEmployedConfirmationRedirect(SelfEmployedConfirmation):
    def __init__(self, *args, **kwargs):
        super(SelfEmployedConfirmationRedirect, self).__init__(*args, **kwargs)
        if self.type is None or self.type is not SelfEmployedConfirmationType.REDIRECT:
            self.type = SelfEmployedConfirmationType.REDIRECT
