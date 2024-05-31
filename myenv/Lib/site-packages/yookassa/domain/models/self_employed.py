# coding: utf-8
import re  # noqa: F401

from yookassa.domain.common import BaseObject


class PayoutSelfEmployed(BaseObject):
    """Данные самозанятого, который получит выплату. Необходимо передавать, если вы делаете выплату %[самозанятому](/developers/payouts/scenario-extensions/self-employed). Только для обычных выплат."""  # noqa: E501

    __id = None

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        if value is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501
        if value is not None and len(value) > 50:
            raise ValueError("Invalid value for `id`, length must be less than or equal to `50`")  # noqa: E501
        if value is not None and len(value) < 36:
            raise ValueError("Invalid value for `id`, length must be greater than or equal to `36`")  # noqa: E501
        self.__id = value


class SelfEmployedStatus(object):
    """Статус подключения самозанятого и выдачи ЮMoney прав на регистрацию чеков"""
    PENDING = "pending"
    """ЮMoney запросили права на регистрацию чеков, но самозанятый еще не ответил на заявку"""
    CONFIRMED = "confirmed"
    """Самозанятый выдал права ЮMoney; вы можете делать выплаты"""
    CANCELED = "canceled"
    """Самозанятый отклонил заявку или отозвал ранее выданные права"""
    UNREGISTERED = "unregistered"
    """Самозанятый с таким ИНН не зарегистрирован в сервисе Мой налог, или пользователь потерял статус самозанятого"""
