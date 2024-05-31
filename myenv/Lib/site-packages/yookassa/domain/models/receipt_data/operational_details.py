# -*- coding: utf-8 -*-
from yookassa.domain.common import BaseObject


class OperationalDetails(BaseObject):

    __operation_id = None

    __value = None

    __created_at = None

    @property
    def operation_id(self):
        return self.__operation_id

    @operation_id.setter
    def operation_id(self, value):
        if value is None:  # noqa: E501
            raise ValueError("Invalid value for `operation_id`, must not be `None`")  # noqa: E501
        if not isinstance(value, int):  # noqa: E501
            raise TypeError("Invalid value type for `operation_id`, must be `int`")  # noqa: E501
        if value is not None and value > 255:  # noqa: E501
            raise ValueError("Invalid value for `operation_id`, must be a value less than or equal to `255`")  # noqa: E501
        if value is not None and value < 0:  # noqa: E501
            raise ValueError("Invalid value for `operation_id`, must be a value greater than or equal to `0`")  # noqa: E501
        self.__operation_id = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        if value is None:  # noqa: E501
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501
        if value is not None and len(value) > 64:
            raise ValueError("Invalid value for `value`, length must be less than or equal to `64`")  # noqa: E501
        self.__value = value

    @property
    def created_at(self):
        return self.__created_at

    @created_at.setter
    def created_at(self, value):
        if value is None:  # noqa: E501
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501
        self.__created_at = value
