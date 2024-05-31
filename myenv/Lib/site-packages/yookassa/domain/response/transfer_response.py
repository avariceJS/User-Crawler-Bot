# -*- coding: utf-8 -*-
from yookassa.domain.common import BaseObject
from yookassa.domain.models.amount import Amount


class TransferResponse(BaseObject):
    """
    Class representing payment transfer wrapper object

    Used in Payment
    """
    __account_id = None

    __amount = None

    __status = None

    __platform_fee_amount = None

    __description = None

    __metadata = None

    __release_funds = None

    __connected_account_id = None

    @property
    def account_id(self):
        return self.__account_id

    @account_id.setter
    def account_id(self, value):
        self.__account_id = str(value)

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
    def status(self):
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = str(value)

    @property
    def platform_fee_amount(self):
        return self.__platform_fee_amount

    @platform_fee_amount.setter
    def platform_fee_amount(self, value):
        if isinstance(value, dict):
            self.__platform_fee_amount = Amount(value)
        elif isinstance(value, Amount):
            self.__platform_fee_amount = value
        else:
            raise TypeError('Invalid platform_fee_amount value type')

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, value):
        self.__description = str(value)

    @property
    def metadata(self):
        return self.__metadata

    @metadata.setter
    def metadata(self, value):
        if type(value) is dict:
            self.__metadata = value

    @property
    def release_funds(self):
        return self.__release_funds

    @release_funds.setter
    def release_funds(self, value):
        self.__release_funds = value

    @property
    def connected_account_id(self):
        return self.__connected_account_id

    @connected_account_id.setter
    def connected_account_id(self, value):
        self.__connected_account_id = value


class TransferStatus(object):
    """
    Class representing transfer.status values enum
    """
    PENDING = 'pending'
    WAITING_FOR_CAPTURE = 'waiting_for_capture'
    SUCCEEDED = 'succeeded'
    CANCELED = 'canceled'
