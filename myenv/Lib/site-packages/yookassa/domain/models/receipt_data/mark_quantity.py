# coding: utf-8
import re  # noqa: F401

from yookassa.domain.common import BaseObject


class MarkQuantity(BaseObject):
    """
    Дробное количество маркированного товара (тег в 54 ФЗ — 1291). Обязательный параметр, если одновременно выполняются эти условия:
      * вы используете Чеки от ЮKassa или онлайн-кассу, обновленную до ФФД 1.2;
      * товар нужно [маркировать](http://docs.cntd.ru/document/902192509);
      * поле `measure` имеет значение ~`piece`.

    Пример: вы продаете поштучно карандаши. Они поставляются пачками по 100 штук с одним кодом маркировки.
    При продаже одного карандаша нужно в `numerator` передать ~`1`, а в `denominator` — ~`100`.
    """  # noqa: E501

    __numerator = None

    __denominator = None

    @property
    def numerator(self):
        return self.__numerator

    @numerator.setter
    def numerator(self, value):
        if value is None:  # noqa: E501
            raise ValueError("Invalid value for `numerator`, must not be `None`")  # noqa: E501
        if value is not None and value < 1:  # noqa: E501
            raise ValueError("Invalid value for `numerator`, must be a value greater than or equal to `1`")  # noqa: E501
        self.__numerator = value

    @property
    def denominator(self):
        return self.__denominator

    @denominator.setter
    def denominator(self, value):
        if value is None:  # noqa: E501
            raise ValueError("Invalid value for `denominator`, must not be `None`")  # noqa: E501
        if value is not None and value < 1:  # noqa: E501
            raise ValueError("Invalid value for `denominator`, must be a value greater than or equal to `1`")  # noqa: E501
        self.__denominator = value
