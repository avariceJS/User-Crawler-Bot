# coding: utf-8
import re  # noqa: F401

from yookassa.domain.common import BaseObject


class MarkCodeInfo(BaseObject):
    """
    Код товара (тег в 54 ФЗ — 1163). Обязательный параметр, если одновременно выполняются эти условия:
      * вы используете Чеки от ЮKassa или онлайн-кассу, обновленную до ФФД 1.2;
      * товар нужно [маркировать](http://docs.cntd.ru/document/902192509).
    Должно быть заполнено хотя бы одно поле.
    """  # noqa: E501

    __mark_code_raw = None

    __unknown = None

    __ean_8 = None

    __ean_13 = None

    __itf_14 = None

    __gs_10 = None

    __gs_1m = None

    __short = None

    __fur = None

    __egais_20 = None

    __egais_30 = None

    @property
    def mark_code_raw(self):
        return self.__mark_code_raw

    @mark_code_raw.setter
    def mark_code_raw(self, value):
        self.__mark_code_raw = value

    @property
    def unknown(self):
        return self.__unknown

    @unknown.setter
    def unknown(self, value):
        if value is not None and len(value) > 32:
            raise ValueError("Invalid value for `unknown`, length must be less than or equal to `32`")  # noqa: E501
        if value is not None and len(value) < 1:
            raise ValueError("Invalid value for `unknown`, length must be greater than or equal to `1`")  # noqa: E501
        self.__unknown = value

    @property
    def ean_8(self):
        return self.__ean_8

    @ean_8.setter
    def ean_8(self, value):
        if value is not None and len(value) > 8:
            raise ValueError("Invalid value for `ean_8`, length must be less than or equal to `8`")  # noqa: E501
        if value is not None and len(value) < 8:
            raise ValueError("Invalid value for `ean_8`, length must be greater than or equal to `8`")  # noqa: E501
        self.__ean_8 = value

    @property
    def ean_13(self):
        return self.__ean_13

    @ean_13.setter
    def ean_13(self, value):
        if value is not None and len(value) > 13:
            raise ValueError("Invalid value for `ean_13`, length must be less than or equal to `13`")  # noqa: E501
        if value is not None and len(value) < 13:
            raise ValueError("Invalid value for `ean_13`, length must be greater than or equal to `13`")  # noqa: E501
        self.__ean_13 = value

    @property
    def itf_14(self):
        return self.__itf_14

    @itf_14.setter
    def itf_14(self, value):
        if value is not None and len(value) > 14:
            raise ValueError("Invalid value for `itf_14`, length must be less than or equal to `14`")  # noqa: E501
        if value is not None and len(value) < 14:
            raise ValueError("Invalid value for `itf_14`, length must be greater than or equal to `14`")  # noqa: E501
        self.__itf_14 = value

    @property
    def gs_10(self):
        return self.__gs_10

    @gs_10.setter
    def gs_10(self, value):
        if value is not None and len(value) > 38:
            raise ValueError("Invalid value for `gs_10`, length must be less than or equal to `38`")  # noqa: E501
        if value is not None and len(value) < 1:
            raise ValueError("Invalid value for `gs_10`, length must be greater than or equal to `1`")  # noqa: E501
        self.__gs_10 = value

    @property
    def gs_1m(self):
        return self.__gs_1m

    @gs_1m.setter
    def gs_1m(self, value):
        if value is not None and len(value) > 200:
            raise ValueError("Invalid value for `gs_1m`, length must be less than or equal to `200`")  # noqa: E501
        if value is not None and len(value) < 1:
            raise ValueError("Invalid value for `gs_1m`, length must be greater than or equal to `1`")  # noqa: E501
        self.__gs_1m = value

    @property
    def short(self):
        return self.__short

    @short.setter
    def short(self, value):
        if value is not None and len(value) > 38:
            raise ValueError("Invalid value for `short`, length must be less than or equal to `38`")  # noqa: E501
        if value is not None and len(value) < 1:
            raise ValueError("Invalid value for `short`, length must be greater than or equal to `1`")  # noqa: E501
        self.__short = value

    @property
    def fur(self):
        return self.__fur

    @fur.setter
    def fur(self, value):
        if value is not None and len(value) > 20:
            raise ValueError("Invalid value for `fur`, length must be less than or equal to `20`")  # noqa: E501
        if value is not None and len(value) < 20:
            raise ValueError("Invalid value for `fur`, length must be greater than or equal to `20`")  # noqa: E501
        self.__fur = value

    @property
    def egais_20(self):
        return self.__egais_20

    @egais_20.setter
    def egais_20(self, value):
        if value is not None and len(value) > 33:
            raise ValueError("Invalid value for `egais_20`, length must be less than or equal to `33`")  # noqa: E501
        if value is not None and len(value) < 33:
            raise ValueError("Invalid value for `egais_20`, length must be greater than or equal to `33`")  # noqa: E501
        self.__egais_20 = value

    @property
    def egais_30(self):
        return self.__egais_30

    @egais_30.setter
    def egais_30(self, value):
        if value is not None and len(value) > 14:
            raise ValueError("Invalid value for `egais_30`, length must be less than or equal to `14`")  # noqa: E501
        if value is not None and len(value) < 14:
            raise ValueError("Invalid value for `egais_30`, length must be greater than or equal to `14`")  # noqa: E501
        self.__egais_30 = value
