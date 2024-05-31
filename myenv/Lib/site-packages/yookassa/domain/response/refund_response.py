# -*- coding: utf-8 -*-
from yookassa.domain.common import PaymentMethodType
from yookassa.domain.common.response_object import ResponseObject
from yookassa.domain.models import CancellationDetails
from yookassa.domain.models.amount import Amount
from yookassa.domain.models.deal import RefundDealInfo
from yookassa.domain.models.refund_data.refund_data_class_map import RefundDataClassMap
from yookassa.domain.models.refund_data.refund_data_factory import RefundDataFactory
from yookassa.domain.models.refund_data.refund_source import RefundSource


class RefundResponse(ResponseObject):
    """
    Class representing response object.

    Contains data
    """
    __id = None

    __payment_id = None

    __status = None

    __cancellation_details = None

    __receipt_registration = None

    __created_at = None

    __amount = None

    __description = None

    __sources = None

    __deal = None

    __refund_method = None

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def payment_id(self):
        return self.__payment_id

    @payment_id.setter
    def payment_id(self, value):
        self.__payment_id = value

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = value

    @property
    def cancellation_details(self):
        return self.__cancellation_details

    @cancellation_details.setter
    def cancellation_details(self, value):
        self.__cancellation_details = CancellationDetails(value)

    @property
    def receipt_registration(self):
        return self.__receipt_registration

    @receipt_registration.setter
    def receipt_registration(self, value):
        self.__receipt_registration = value

    @property
    def created_at(self):
        return self.__created_at

    @created_at.setter
    def created_at(self, value):
        self.__created_at = value

    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self, value):
        self.__amount = Amount(value)

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, value):
        self.__description = value

    @property
    def sources(self):
        return self.__sources

    @sources.setter
    def sources(self, value):
        if isinstance(value, list):
            self.__sources = [RefundSource(item) for item in value]
        else:
            self.__sources = value

    @property
    def deal(self):
        return self.__deal

    @deal.setter
    def deal(self, value):
        self.__deal = RefundDealInfo(value)

    @property
    def refund_method(self):
        return self.__refund_method

    @refund_method.setter
    def refund_method(self, value):
        if isinstance(value, dict) and 'type' in value and value['type'] not in RefundDataClassMap().response:
            value['type'] = PaymentMethodType.UNKNOWN
        self.__refund_method = RefundDataFactory().create(value, self.context())
