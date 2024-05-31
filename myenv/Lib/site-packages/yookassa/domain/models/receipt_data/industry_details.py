# -*- coding: utf-8 -*-
import re

from yookassa.domain.common import BaseObject


class IndustryDetails(BaseObject):

    __federal_id = None

    __document_date = None

    __document_number = None

    __value = None

    @property
    def federal_id(self):
        return self.__federal_id

    @federal_id.setter
    def federal_id(self, value):
        if value is None:  # noqa: E501
            raise ValueError("Invalid value for `federal_id`, must not be `None`")  # noqa: E501
        if value is not None and not re.search(r'(^00[1-9]{1}$)|(^0[1-6]{1}[0-9]{1}$)|(^07[0-3]{1}$)', value):  # noqa: E501
            raise ValueError(r"Invalid value for `federal_id`, must be a follow pattern or equal to `/(^00[1-9]{1}$)|(^0[1-6]{1}[0-9]{1}$)|(^07[0-3]{1}$)/`")  # noqa: E501
        self.__federal_id = value

    @property
    def document_date(self):
        return self.__document_date

    @document_date.setter
    def document_date(self, value):
        if value is None:  # noqa: E501
            raise ValueError("Invalid value for `document_date`, must not be `None`")  # noqa: E501
        self.__document_date = value

    @property
    def document_number(self):
        return self.__document_number

    @document_number.setter
    def document_number(self, value):
        if value is None:  # noqa: E501
            raise ValueError("Invalid value for `document_number`, must not be `None`")  # noqa: E501
        if value is not None and len(value) > 32:
            raise ValueError("Invalid value for `document_number`, length must be less than or equal to `32`")  # noqa: E501
        self.__document_number = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        if value is None:  # noqa: E501
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501
        if value is not None and len(value) > 256:
            raise ValueError("Invalid value for `value`, length must be less than or equal to `256`")  # noqa: E501
        self.__value = value
