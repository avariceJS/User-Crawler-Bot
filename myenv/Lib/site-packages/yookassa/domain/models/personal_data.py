# -*- coding: utf-8 -*-
import re  # noqa: F401

from yookassa.domain.common import BaseObject


class PayoutPersonalData(BaseObject):
    """Персональные данные получателя выплаты. Необходимо передавать, если вы делаете выплату с [проверкой получателя](/developers/payouts/scenario-extensions/recipient-check). Только для обычных выплат. """  # noqa: E501

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


class PersonalDataType(object):
    """Тип персональных данных — цель, для которой вы будете использовать данные. Возможное значение: `sbp_payout_recipient` — выплаты с %[проверкой получателя](/developers/payouts/scenario-extensions/recipient-check). """  # noqa: E501

    SBP_PAYOUT_RECIPIENT = "sbp_payout_recipient"


class PersonalDataStatus(object):
    """Статус персональных данных. Возможные значения:  * ~`waiting_for_operation` — данные сохранены, но не использованы при проведении выплаты; * ~`active` — данные сохранены и использованы при проведении выплаты; данные можно использовать повторно до срока, указанного в параметре `expires_at`; * ~`canceled` — хранение данных отменено, данные удалены, инициатор и причина отмены указаны в объекте cancellation_details (финальный и неизменяемый статус)."""  # noqa: E501

    WAITING_FOR_OPERATION = "waiting_for_operation"
    ACTIVE = "active"
    CANCELED = "canceled"
