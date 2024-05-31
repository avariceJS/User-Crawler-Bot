# coding: utf-8

from yookassa.domain.common import BaseObject
from yookassa.domain.models import Amount
from yookassa.domain.models.settings import FiscalizationData, FiscalizationProvider


class Me(BaseObject):
    """Информация о настройках магазина или шлюза. """  # noqa: E501

    __account_id = None
    """Идентификатор магазина или шлюза."""

    __status = None
    """Статус магазина или шлюза. Возможные значения:  * ~`enabled` — подключен к ЮKassa, может проводить платежи или выплаты; * ~`disabled` — не может проводить платежи или выплаты (еще не подключен, закрыт или временно не работает). """  # noqa: E501

    __test = None
    """Это тестовый магазин или шлюз. """  # noqa: E501

    __fiscalization = None
    """Настройки магазина для отправки чеков в налоговую."""

    __fiscalization_enabled = None
    """Устаревший параметр, который раньше использовался для определения настроек отправки чеков в налоговую. Сохранен для поддержки обратной совместимости, в новых версиях API может быть удален.  Используйте объект ~`fiscalization`, чтобы определить, какие у магазина настройки отправки чеков. """  # noqa: E501

    __payment_methods = None
    """Список %[способов оплаты](/developers/payment-acceptance/getting-started/payment-methods#all), доступных магазину. Присутствует, если вы запрашивали настройки магазина. """  # noqa: E501

    __itn = None
    """ИНН магазина (10 или 12 цифр). Присутствует, если вы запрашивали настройки магазина."""

    __payout_methods = None
    """Список способов получения выплат, доступных шлюзу. Возможные значения:  * ~`bank_card` — выплаты на банковские карты; * ~`yoo_money` — выплаты на кошельки ЮMoney; * ~`sbp` — выплаты через СБП.  Присутствует, если вы запрашивали настройки шлюза. """  # noqa: E501

    __name = None
    """Название шлюза, которое отображается в личном кабинете ЮKassa. Присутствует, если вы запрашивали настройки шлюза."""  # noqa: E501

    __payout_balance = None
    """Баланс вашего шлюза. Присутствует, если вы запрашивали настройки шлюза."""

    @property
    def account_id(self):
        return self.__account_id

    @account_id.setter
    def account_id(self, value):
        self.__account_id = value

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = value

    @property
    def test(self):
        return self.__test

    @test.setter
    def test(self, value):
        self.__test = value

    @property
    def fiscalization(self):
        return self.__fiscalization

    @fiscalization.setter
    def fiscalization(self, value):
        if isinstance(value, dict):
            self.__fiscalization = FiscalizationData(value)

    @property
    def fiscalization_enabled(self):
        return self.__fiscalization_enabled

    @fiscalization_enabled.setter
    def fiscalization_enabled(self, value):
        self.__fiscalization_enabled = value

    @property
    def payment_methods(self):
        return self.__payment_methods

    @payment_methods.setter
    def payment_methods(self, value):
        self.__payment_methods = value

    @property
    def itn(self):
        return self.__itn

    @itn.setter
    def itn(self, value):
        self.__itn = value

    @property
    def payout_methods(self):
        return self.__payout_methods

    @payout_methods.setter
    def payout_methods(self, value):
        self.__payout_methods = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def payout_balance(self):
        return self.__payout_balance

    @payout_balance.setter
    def payout_balance(self, value):
        if isinstance(value, dict):
            self.__payout_balance = Amount(value)
