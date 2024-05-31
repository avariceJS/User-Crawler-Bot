# coding: utf-8
import datetime
import re  # noqa: F401

from yookassa.domain.common import BaseObject


class FiscalizationData(BaseObject):
    """Настройки магазина для %[отправки чеков в налоговую](/developers/payment-acceptance/receipts/basics).  Присутствует, если вы запрашивали настройки магазина и этот магазин использует решения ЮKassa для отправки чеков. Отсутствует, если магазин еще не включал отправку чеков через ЮKassa. """  # noqa: E501

    __enabled = None
    """В настройках магазина включена отправка чеков. Возможные значения:  * ~`true` — магазин отправляет данные для чеков через ЮKassa; * ~`false` — магазин выключил отправку чеков через ЮKassa. """  # noqa: E501

    __provider = None

    @property
    def enabled(self):
        return self.__enabled

    @enabled.setter
    def enabled(self, value):
        self.__enabled = value

    @property
    def provider(self):
        return self.__provider

    @provider.setter
    def provider(self, value):
        self.__provider = value
