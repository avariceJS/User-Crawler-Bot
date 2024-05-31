# -*- coding: utf-8 -*-
from yookassa.domain.common.type_factory import TypeFactory
from yookassa.domain.models.refund_data.refund_data_class_map import RefundDataClassMap


class RefundDataFactory(TypeFactory):
    """
    Factory for payment data objects
    """

    def __init__(self):
        super(RefundDataFactory, self).__init__(RefundDataClassMap())
