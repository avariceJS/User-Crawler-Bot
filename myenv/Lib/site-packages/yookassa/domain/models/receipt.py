# -*- coding: utf-8 -*-
from yookassa.domain.common import BaseObject
from yookassa.domain.models.receipt_data.industry_details import IndustryDetails
from yookassa.domain.models.receipt_data.operational_details import OperationalDetails
from yookassa.domain.models.receipt_data.receipt_customer import ReceiptCustomer
from yookassa.domain.models.receipt_data.receipt_item import ReceiptItem


class Receipt(BaseObject):
    """
    Class representing receipt data wrapper object
    """
    __customer = None

    __items = []

    __tax_system_code = None

    __receipt_industry_details = None

    __receipt_operational_details = None

    @property
    def customer(self):
        return self.__customer

    @customer.setter
    def customer(self, value):
        if isinstance(value, dict):
            self.__customer = ReceiptCustomer(value)
        elif isinstance(value, ReceiptCustomer):
            self.__customer = value
        else:
            raise TypeError('Invalid customer value type')

    @property
    def items(self):
        return self.__items

    @items.setter
    def items(self, value):
        if isinstance(value, list):
            items = []
            for item in value:
                if isinstance(item, dict):
                    items.append(ReceiptItem(item))
                elif isinstance(item, ReceiptItem):
                    items.append(item)
                else:
                    raise TypeError('Invalid item type in receipt.items')

            self.__items = items
        elif value is None:
            self.__items = []
        else:
            raise TypeError('Invalid items value type in receipt')

    @property
    def tax_system_code(self):
        return self.__tax_system_code

    @tax_system_code.setter
    def tax_system_code(self, value):
        if isinstance(value, int):
            self.__tax_system_code = value
        else:
            raise TypeError('Invalid tax_system_code value type')

    @property
    def email(self):
        return self.__customer.email if self.__customer is not None else None

    @email.setter
    def email(self, value):
        if self.__customer is None:
            self.__customer = ReceiptCustomer()
        self.__customer.email = str(value)

    @property
    def phone(self):
        return self.__customer.phone if self.__customer is not None else None

    @phone.setter
    def phone(self, value):
        if self.__customer is None:
            self.__customer = ReceiptCustomer()
        self.__customer.phone = str(value)

    def has_items(self):
        return bool(self.items)

    @property
    def receipt_industry_details(self):
        return self.__receipt_industry_details

    @receipt_industry_details.setter
    def receipt_industry_details(self, value):
        if isinstance(value, list):
            items = []
            for item in value:
                if isinstance(item, dict):
                    items.append(IndustryDetails(item))
                elif isinstance(item, IndustryDetails):
                    items.append(item)
                else:
                    raise TypeError('Invalid receipt_industry_details data type in ReceiptData.receipt_industry_details')
            self.__receipt_industry_details = items
        else:
            raise TypeError('Invalid receipt_industry_details value type in ReceiptData')

    @property
    def receipt_operational_details(self):
        return self.__receipt_operational_details

    @receipt_operational_details.setter
    def receipt_operational_details(self, value):
        if isinstance(value, dict):
            self.__receipt_operational_details = OperationalDetails(value)
        elif isinstance(value, OperationalDetails):
            self.__receipt_operational_details = value
        else:
            raise TypeError('Invalid receipt_operational_details data type in ReceiptData.receipt_operational_details')
