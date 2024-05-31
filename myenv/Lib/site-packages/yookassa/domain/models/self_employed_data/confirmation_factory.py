# -*- coding: utf-8 -*-
from yookassa.domain.common.type_factory import TypeFactory
from yookassa.domain.models.self_employed_data.confirmation_class_map import SelfEmployedConfirmationClassMap


class SelfEmployedConfirmationFactory(TypeFactory):
    def __init__(self):
        super(SelfEmployedConfirmationFactory, self).__init__(SelfEmployedConfirmationClassMap())
