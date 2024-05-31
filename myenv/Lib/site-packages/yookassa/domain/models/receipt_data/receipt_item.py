# -*- coding: utf-8 -*-
import re
from decimal import Decimal

from yookassa.domain.common import BaseObject
from yookassa.domain.models.amount import Amount
from yookassa.domain.models.receipt_data.industry_details import IndustryDetails
from yookassa.domain.models.receipt_data.mark_code_info import MarkCodeInfo
from yookassa.domain.models.receipt_data.mark_quantity import MarkQuantity


class ReceiptItem(BaseObject):
    """
    Class representing receipt item data wrapper object

    Used in Receipt
    """
    __description = None

    __amount = None

    __vat_code = None

    __quantity = None

    __measure = None

    __mark_quantity = None

    __payment_subject = None

    __payment_mode = None

    __country_of_origin_code = None

    __customs_declaration_number = None

    __excise = None

    __product_code = None

    __mark_code_info = None

    __mark_mode = None

    __payment_subject_industry_details = None

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, value):
        self.__description = str(value)

    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self, value):
        if isinstance(value, dict):
            self.__amount = Amount(value)
        elif isinstance(value, Amount):
            self.__amount = value
        else:
            raise TypeError('Invalid amount value type')

    @property
    def vat_code(self):
        return self.__vat_code

    @vat_code.setter
    def vat_code(self, value):
        self.__vat_code = int(value)

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
    def measure(self):
        return self.__measure

    @measure.setter
    def measure(self, value):
        self.__measure = value

    @property
    def mark_quantity(self):
        return self.__mark_quantity

    @mark_quantity.setter
    def mark_quantity(self, value):
        if isinstance(value, dict):
            self.__mark_quantity = MarkQuantity(value)
        elif isinstance(value, MarkQuantity):
            self.__mark_quantity = value
        else:
            raise TypeError('Invalid mark_quantity data type in ReceiptItem.mark_quantity')

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
        self.__country_of_origin_code = str(value)

    @property
    def customs_declaration_number(self):
        return self.__customs_declaration_number

    @customs_declaration_number.setter
    def customs_declaration_number(self, value):
        self.__customs_declaration_number = str(value)

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
    def product_code(self):
        return self.__product_code

    @product_code.setter
    def product_code(self, value):
        self.__product_code = str(value)

    @property
    def mark_code_info(self):
        return self.__mark_code_info

    @mark_code_info.setter
    def mark_code_info(self, value):
        if isinstance(value, dict):
            self.__mark_code_info = MarkCodeInfo(value)
        elif isinstance(value, MarkCodeInfo):
            self.__mark_code_info = value
        else:
            raise TypeError('Invalid mark_code_info data type in ReceiptItem.mark_code_info')

    @property
    def mark_mode(self):
        return self.__mark_mode

    @mark_mode.setter
    def mark_mode(self, value):
        if value is not None and not re.search(r'^[0]{1}$', value):  # noqa: E501
            raise ValueError(r"Invalid value for `mark_mode`, must be a follow pattern or equal to `/^[0]{1}$/`")  # noqa: E501
        self.__mark_mode = value

    @property
    def payment_subject_industry_details(self):
        return self.__payment_subject_industry_details

    @payment_subject_industry_details.setter
    def payment_subject_industry_details(self, value):
        if isinstance(value, list):
            items = []
            for item in value:
                if isinstance(item, dict):
                    items.append(IndustryDetails(item))
                elif isinstance(item, IndustryDetails):
                    items.append(item)
                else:
                    raise TypeError(
                        'Invalid payment_subject_industry_details data type in ReceiptItem.payment_subject_industry_details')
            self.__payment_subject_industry_details = items
        else:
            raise TypeError('Invalid payment_subject_industry_details value type in ReceiptItem')


class PaymentMode(object):
    """
    Class representing payment_mode values enum
    """
    FULL_PREPAYMENT = 'full_prepayment'
    PARTIAL_PREPAYMENT = 'partial_prepayment'
    ADVANCE = 'advance'
    FULL_PAYMENT = 'full_payment'
    PARTIAL_PAYMENT = 'partial_payment'
    CREDIT = 'credit'
    CREDIT_PAYMENT = 'credit_payment'


class PaymentSubject(object):
    """
    Class representing payment_subject values enum
    """
    COMMODITY = 'commodity'
    EXCISE = 'excise'
    JOB = 'job'
    SERVICE = 'service'
    GAMBLING_BET = 'gambling_bet'
    GAMBLING_PRIZE = 'gambling_prize'
    LOTTERY = 'lottery'
    LOTTERY_PRIZE = 'lottery_prize'
    INTELLECTUAL_ACTIVITY = 'intellectual_activity'
    PAYMENT = 'payment'
    AGENT_COMMISSION = 'agent_commission'
    COMPOSITE = 'composite'
    ANOTHER = 'another'


class ReceiptItemMeasure(object):
    PIECE = 'piece'
    GRAM = 'gram'
    KILOGRAM = 'kilogram'
    TON = 'ton'
    CENTIMETER = 'centimeter'
    DECIMETER = 'decimeter'
    METER = 'meter'
    SQUARE_CENTIMETER = 'square_centimeter'
    SQUARE_DECIMETER = 'square_decimeter'
    SQUARE_METER = 'square_meter'
    MILLILITER = 'milliliter'
    LITER = 'liter'
    CUBIC_METER = 'cubic_meter'
    KILOWATT_HOUR = 'kilowatt_hour'
    GIGACALORIE = 'gigacalorie'
    DAY = 'day'
    HOUR = 'hour'
    MINUTE = 'minute'
    SECOND = 'second'
    KILOBYTE = 'kilobyte'
    MEGABYTE = 'megabyte'
    GIGABYTE = 'gigabyte'
    TERABYTE = 'terabyte'
    ANOTHER = 'another'
