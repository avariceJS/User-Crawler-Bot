# -*- coding: utf-8 -*-
from yookassa.domain.common.receipt_type import ReceiptType
from yookassa.domain.common.request_object import RequestObject
from yookassa.domain.models.receipt_data.receipt_customer import ReceiptCustomer
from yookassa.domain.models.receipt_data.additional_user_props import AdditionalUserProps
from yookassa.domain.models.receipt_data.industry_details import IndustryDetails
from yookassa.domain.models.receipt_data.operational_details import OperationalDetails
from yookassa.domain.models.settlement import Settlement
from yookassa.domain.request.receipt_item_request import ReceiptItemRequest


class ReceiptRequest(RequestObject):

    __type = None

    __payment_id = None

    __refund_id = None

    __customer = None

    __items = []

    __send = None

    __tax_system_code = None

    __additional_user_props = None

    __receipt_industry_details = None

    __receipt_operational_details = None

    __settlements = []

    __on_behalf_of = None

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, value):
        self.__type = str(value)

    @property
    def payment_id(self):
        return self.__payment_id

    @payment_id.setter
    def payment_id(self, value):
        self.__refund_id = None
        self.__payment_id = str(value)

    @property
    def refund_id(self):
        return self.__refund_id

    @refund_id.setter
    def refund_id(self, value):
        self.__payment_id = None
        self.__refund_id = str(value)

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
            raise TypeError('Invalid customer value type in ReceiptRequest')

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

    @property
    def items(self):
        return self.__items

    @items.setter
    def items(self, value):
        if isinstance(value, list):
            items = []
            for item in value:
                if isinstance(item, dict):
                    items.append(ReceiptItemRequest(item))
                elif isinstance(item, ReceiptItemRequest):
                    items.append(item)
                else:
                    raise TypeError('Invalid item type in ReceiptRequest.items')
            self.__items = items
        elif value is None:
            self.__items = []
        else:
            raise TypeError('Invalid items value type in ReceiptRequest')

    @property
    def send(self):
        return self.__send

    @send.setter
    def send(self, value):
        if isinstance(value, bool):
            self.__send = value
        else:
            raise TypeError('Invalid send value type in ReceiptRequest')

    @property
    def tax_system_code(self):
        return self.__tax_system_code

    @tax_system_code.setter
    def tax_system_code(self, value):
        if isinstance(value, int):
            self.__tax_system_code = value
        else:
            raise TypeError('Invalid tax_system_code value type in ReceiptRequest')

    @property
    def additional_user_props(self):
        return self.__additional_user_props

    @additional_user_props.setter
    def additional_user_props(self, value):
        if isinstance(value, dict):
            self.__additional_user_props = AdditionalUserProps(value)
        elif isinstance(value, AdditionalUserProps):
            self.__additional_user_props = value
        else:
            raise TypeError('Invalid additional_user_props data type in ReceiptRequest')

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
                    raise TypeError('Invalid receipt_industry_details data type in PostReceiptData.receipt_industry_details')
            self.__receipt_industry_details = items
        else:
            raise TypeError('Invalid receipt_industry_details value type in ReceiptRequest')

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
            raise TypeError('Invalid receipt_operational_details data type in ReceiptRequest')

    @property
    def settlements(self):
        return self.__settlements

    @settlements.setter
    def settlements(self, value):
        if isinstance(value, list):
            items = []
            for item in value:
                if isinstance(item, dict):
                    items.append(Settlement(item))
                elif isinstance(item, Settlement):
                    items.append(item)
                else:
                    raise TypeError('Invalid settlement type in ReceiptRequest.settlements')
            self.__settlements = items
        elif value is None:
            self.__settlements = []
        else:
            raise TypeError('Invalid settlements value type in ReceiptRequest')

    @property
    def on_behalf_of(self):
        return self.__on_behalf_of

    @on_behalf_of.setter
    def on_behalf_of(self, value):
        self.__on_behalf_of = str(value)

    def validate(self):
        if self.type is None:
            self.__set_validation_error('ReceiptRequest.type not specified')

        if self.send is None:
            self.__set_validation_error('ReceiptRequest.send not specified')

        if self.customer is not None:
            email = self.customer.email
            phone = self.customer.phone
            if not email and not phone:
                self.__set_validation_error('Both email and phone values are empty in ReceiptRequest.customer')
        else:
            self.__set_validation_error('ReceiptRequest.customer not specified')

        if not self.has_items():
            self.__set_validation_error('ReceiptRequest.items not specified')

        if not self.has_settlements():
            self.__set_validation_error('ReceiptRequest.settlements not specified')

        if self.type is ReceiptType.PAYMENT and self.payment_id is None:
            self.__set_validation_error('ReceiptRequest.payment_id not specified')

        if self.type is ReceiptType.REFUND and self.refund_id is None and self.payment_id is None:
            self.__set_validation_error('ReceiptRequest.refund_id or ReceiptRequest.payment_id not specified')

    def has_items(self):
        return bool(self.items) and bool(len(self.items))

    def has_settlements(self):
        return bool(self.settlements) and bool(len(self.settlements))

    def __set_validation_error(self, message):
        raise ValueError(message)
