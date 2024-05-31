# -*- coding: utf-8 -*-
import uuid

from yookassa.client import ApiClient
from yookassa.domain.common import HttpVerb
from yookassa.domain.request import PersonalDataRequest
from yookassa.domain.response import PersonalDataResponse


class PersonalData:
    base_path = '/personal_data'

    def __init__(self):
        self.client = ApiClient()

    @classmethod
    def find_one(cls, personal_data_id):
        """
        Get information about personal_data

        :param personal_data_id:
        :return: PersonalDataResponse
        """
        instance = cls()
        if not isinstance(personal_data_id, str) or not personal_data_id:
            raise ValueError('Invalid personal_data_id value')

        path = instance.base_path + '/' + personal_data_id
        response = instance.client.request(HttpVerb.GET, path)
        return PersonalDataResponse(response)

    @classmethod
    def create(cls, params, idempotency_key=None):
        """
        Create personal_data

        :param params: data passed to API
        :param idempotency_key:
        :return: PersonalDataResponse
        """
        instance = cls()
        path = cls.base_path

        if not idempotency_key:
            idempotency_key = uuid.uuid4()

        headers = {
            'Idempotence-Key': str(idempotency_key)
        }

        if isinstance(params, dict):
            params_object = PersonalDataRequest(params)
        elif isinstance(params, PersonalDataRequest):
            params_object = params
        else:
            raise TypeError('Invalid params value type')

        response = instance.client.request(HttpVerb.POST, path, None, headers, params_object)
        return PersonalDataResponse(response)
