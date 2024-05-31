# -*- coding: utf-8 -*-
from yookassa.domain.common.data_context import DataContext
from yookassa.domain.common.payment_method_type import PaymentMethodType
from yookassa.domain.models.refund_data.response.refund_data_sbp import \
    RefundDataSbp as ResponseRefundDataSbp
from yookassa.domain.models.refund_data.response.refund_data_unknown import \
    RefundDataUnknown as ResponseRefundDataUnknown


class RefundDataClassMap(DataContext):
    def __init__(self):
        super(RefundDataClassMap, self).__init__('response')

    @property
    def response(self):
        return {
            PaymentMethodType.SBP: ResponseRefundDataSbp,
            PaymentMethodType.UNKNOWN: ResponseRefundDataUnknown,
        }
