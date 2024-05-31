# coding: utf-8
import re  # noqa: F401

from yookassa.domain.common.request_object import RequestObject


class PersonalDataRequest(RequestObject):

    __type = None

    __last_name = None

    __first_name = None

    __middle_name = None

    __metadata = None

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, value):
        if value is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        self.__type = str(value)

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, value):
        if value is None:  # noqa: E501
            raise ValueError("Invalid value for `last_name`, must not be `None`")  # noqa: E501
        if value is not None and len(value) > 200:
            raise ValueError("Invalid value for `last_name`, length must be less than or equal to `200`")  # noqa: E501
        if value is not None and len(value) < 1:
            raise ValueError("Invalid value for `last_name`, length must be greater than or equal to `1`")  # noqa: E501
        if value is not None and not re.search(r'^[—–‐\-a-zA-Zа-яёА-ЯЁ ]*$', value):  # noqa: E501
            raise ValueError(r"Invalid value for `last_name`, must be a follow pattern or equal to `/^[—–‐\-a-zA-Zа-яёА-ЯЁ ]*$/`")  # noqa: E501
        self.__last_name = value

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, value):
        if value is None:  # noqa: E501
            raise ValueError("Invalid value for `first_name`, must not be `None`")  # noqa: E501
        if value is not None and len(value) > 100:
            raise ValueError("Invalid value for `first_name`, length must be less than or equal to `100`")  # noqa: E501
        if value is not None and len(value) < 1:
            raise ValueError("Invalid value for `first_name`, length must be greater than or equal to `1`")  # noqa: E501
        if value is not None and not re.search(r'^[—–‐\-a-zA-Zа-яёА-ЯЁ ]*$', value):  # noqa: E501
            raise ValueError(r"Invalid value for `first_name`, must be a follow pattern or equal to `/^[—–‐\-a-zA-Zа-яёА-ЯЁ ]*$/`")  # noqa: E501
        self.__first_name = value

    @property
    def middle_name(self):
        return self.__middle_name

    @middle_name.setter
    def middle_name(self, value):
        if value is not None and len(value) > 200:
            raise ValueError("Invalid value for `middle_name`, length must be less than or equal to `200`")  # noqa: E501
        if value is not None and len(value) < 1:
            raise ValueError("Invalid value for `middle_name`, length must be greater than or equal to `1`")  # noqa: E501
        if value is not None and not re.search(r'^[—–‐\-a-zA-Zа-яёА-ЯЁ ]*$', value):  # noqa: E501
            raise ValueError(r"Invalid value for `middle_name`, must be a follow pattern or equal to `/^[—–‐\-a-zA-Zа-яёА-ЯЁ ]*$/`")  # noqa: E501
        self.__middle_name = value

    @property
    def metadata(self):
        return self.__metadata

    @metadata.setter
    def metadata(self, value):
        self.__metadata = value

    def validate(self):
        if self.type is None or self.last_name is None or self.first_name is None:
            self.__set_validation_error('Type, last_name and first_name values cannot be empty in PersonalDataRequest')  # noqa: E501

    def __set_validation_error(self, message):
        raise ValueError(message)
