# -*- coding: utf-8 -*-
from yookassa.domain.common.request_object import RequestObject
from yookassa.domain.models.amount import Amount
from yookassa.domain.models.deal import PayoutDealInfo
from yookassa.domain.models.payout_data.payout_destination import PayoutDestination
from yookassa.domain.models.payout_data.payout_destination_factory import PayoutDestinationFactory
from yookassa.domain.models.payout_data.request.income_receipt import IncomeReceiptData
from yookassa.domain.models.personal_data import PayoutPersonalData
from yookassa.domain.models.self_employed import PayoutSelfEmployed

DESCRIPTION_MAX_LENGTH = 128


class PayoutRequest(RequestObject):
    """
    Class representing PayoutRequest values enum
    """

    __amount = None

    __payout_destination_data = None

    __payout_token = None

    __payment_method_id = None

    __description = None

    __deal = None

    __self_employed = None

    __receipt_data = None

    __personal_data = None

    __metadata = None

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
    def payout_destination_data(self):
        return self.__payout_destination_data

    @payout_destination_data.setter
    def payout_destination_data(self, value):
        if isinstance(value, dict):
            self.__payout_destination_data = PayoutDestinationFactory().create(value, self.context())
        elif isinstance(value, PayoutDestination):
            self.__payout_destination_data = value
        else:
            raise TypeError('Invalid payout_destination_data type')

    @property
    def payout_token(self):
        return self.__payout_token

    @payout_token.setter
    def payout_token(self, value):
        cast_value = str(value)
        if cast_value:
            self.__payout_token = cast_value
        else:
            raise TypeError('Invalid payout_token value')

    @property
    def payment_method_id(self):
        return self.__payment_method_id

    @payment_method_id.setter
    def payment_method_id(self, value):
        self.__payment_method_id = value

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, value):
        cast_value = str(value)
        if len(cast_value) <= DESCRIPTION_MAX_LENGTH:
            self.__description = cast_value
        else:
            raise ValueError('The value of the description parameter is too long. Max length is {}'.format(DESCRIPTION_MAX_LENGTH))  # noqa: E501

    @property
    def deal(self):
        return self.__deal

    @deal.setter
    def deal(self, value):
        if isinstance(value, dict):
            self.__deal = PayoutDealInfo(value)
        elif isinstance(value, PayoutDealInfo):
            self.__deal = value
        else:
            raise TypeError('Invalid deal type')

    @property
    def self_employed(self):
        return self.__self_employed

    @self_employed.setter
    def self_employed(self, value):
        if isinstance(value, dict):
            self.__self_employed = PayoutSelfEmployed(value)
        elif isinstance(value, PayoutSelfEmployed):
            self.__self_employed = value
        else:
            raise TypeError('Invalid self_employed data type in PayoutRequest.self_employed')

    @property
    def receipt_data(self):
        return self.__receipt_data

    @receipt_data.setter
    def receipt_data(self, value):
        if isinstance(value, dict):
            self.__receipt_data = IncomeReceiptData(value)
        elif isinstance(value, IncomeReceiptData):
            self.__receipt_data = value
        else:
            raise TypeError('Invalid receipt_data data type in PayoutRequest.receipt_data')

    @property
    def personal_data(self):
        return self.__personal_data

    @personal_data.setter
    def personal_data(self, value):
        if isinstance(value, list):
            if len(value) > 2:
                raise ValueError("Invalid value for `personal_data`, number of items must be less than or equal to `2`")  # noqa: E501
            if len(value) < 1:
                raise ValueError("Invalid value for `personal_data`, number of items must be greater than or equal to `1`")  # noqa: E501

            personal_data_array = []
            for personal_dataData in value:
                if isinstance(personal_dataData, dict):
                    personal_data_array.append(PayoutPersonalData(personal_dataData))
                elif isinstance(personal_dataData, PayoutPersonalData):
                    personal_data_array.append(personal_dataData)
                else:
                    raise TypeError('Invalid personal_data data type in PayoutRequest.personal_data')
            self.__personal_data = personal_data_array
        else:
            raise TypeError('Invalid personal_data value type in PayoutRequest')

    @property
    def metadata(self):
        return self.__metadata

    @metadata.setter
    def metadata(self, value):
        if type(value) is dict:
            self.__metadata = value

    def validate(self):
        amount = self.amount
        if amount is None:
            self.__set_validation_error('Payout amount not specified')

        if amount.value <= 0.0:
            self.__set_validation_error('Invalid payout amount value: ' + str(amount.value))

        if (self.payout_token and self.payout_destination_data) or \
                (self.payout_token and self.payment_method_id) or \
                (self.payout_destination_data and self.payment_method_id):
            self.__set_validation_error('Both payout_token, payout_destination_data and payment_method_id values are specified')

        elif self.payout_token is None and self.payout_destination_data is None and self.payment_method_id is None:
            self.__set_validation_error('Both payout_token, payout_destination_data and payment_method_id values are not specified')

    def __set_validation_error(self, message):
        raise ValueError(message)
