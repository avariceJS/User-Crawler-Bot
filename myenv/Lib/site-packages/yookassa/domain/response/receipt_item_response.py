# -*- coding: utf-8 -*-
from decimal import Decimal

from yookassa.domain.common import ResponseObject
from yookassa.domain.models import Amount, ReceiptItemSupplier
from yookassa.domain.models.receipt_data.industry_details import IndustryDetails
from yookassa.domain.models.receipt_data.mark_code_info import MarkCodeInfo
from yookassa.domain.models.receipt_data.mark_quantity import MarkQuantity


class ReceiptItemResponse(ResponseObject):

    __description = None

    __quantity = None

    __amount = None

    __vat_code = None

    __payment_subject = None

    __payment_mode = None

    __country_of_origin_code = None

    __customs_declaration_number = None

    __excise = None

    __supplier = None

    __agent_type = None

    __mark_code_info = None

    __measure = None

    __payment_subject_industry_details = None

    __product_code = None

    __mark_mode = None

    __mark_quantity = None

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, value):
        self.__description = value

    @property
    def quantity(self):
        """
        :return Decimal:
        """
        return self.__quantity

    @quantity.setter
    def quantity(self, value):
        self.__quantity = Decimal(str(float(value)))

    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self, value):
        self.__amount = Amount(value)

    @property
    def vat_code(self):
        return self.__vat_code

    @vat_code.setter
    def vat_code(self, value):
        self.__vat_code = int(value)

    @property
    def payment_subject(self):
        return self.__payment_subject

    @payment_subject.setter
    def payment_subject(self, value):
        self.__payment_subject = str(value)

    @property
    def payment_mode(self):
        return self.__payment_mode

    @payment_mode.setter
    def payment_mode(self, value):
        self.__payment_mode = str(value)

    @property
    def country_of_origin_code(self):
        return self.__country_of_origin_code

    @country_of_origin_code.setter
    def country_of_origin_code(self, value):
        self.__country_of_origin_code = value

    @property
    def customs_declaration_number(self):
        return self.__customs_declaration_number

    @customs_declaration_number.setter
    def customs_declaration_number(self, value):
        self.__customs_declaration_number = value

    @property
    def excise(self):
        """
        :return Decimal:
        """
        return self.__excise

    @excise.setter
    def excise(self, value):
        self.__excise = Decimal(str(value))

    @property
    def supplier(self):
        return self.__supplier

    @supplier.setter
    def supplier(self, value):
        if isinstance(value, dict):
            self.__supplier = ReceiptItemSupplier(value)
        else:
            self.__supplier = value

    @property
    def agent_type(self):
        return self.__agent_type

    @agent_type.setter
    def agent_type(self, value):
        self.__agent_type = str(value)

    @property
    def mark_code_info(self):
        return self.__mark_code_info

    @mark_code_info.setter
    def mark_code_info(self, value):
        if isinstance(value, dict):
            self.__mark_code_info = MarkCodeInfo(value)
        else:
            self.__mark_code_info = value

    @property
    def measure(self):
        return self.__measure

    @measure.setter
    def measure(self, value):
        self.__measure = str(value)

    @property
    def payment_subject_industry_details(self):
        return self.__payment_subject_industry_details

    @payment_subject_industry_details.setter
    def payment_subject_industry_details(self, value):
        if isinstance(value, list):
            self.__payment_subject_industry_details = [IndustryDetails(item) for item in value]
        else:
            self.__payment_subject_industry_details = []

    @property
    def product_code(self):
        return self.__product_code

    @product_code.setter
    def product_code(self, value):
        self.__product_code = str(value)

    @property
    def mark_mode(self):
        return self.__mark_mode

    @mark_mode.setter
    def mark_mode(self, value):
        self.__mark_mode = str(value)

    @property
    def mark_quantity(self):
        return self.__mark_quantity

    @mark_quantity.setter
    def mark_quantity(self, value):
        if isinstance(value, dict):
            self.__mark_quantity = MarkQuantity(value)
        else:
            self.__mark_quantity = value
