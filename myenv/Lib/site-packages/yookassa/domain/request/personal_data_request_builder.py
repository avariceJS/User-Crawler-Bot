# -*- coding: utf-8 -*-
from yookassa.domain.request import PersonalDataRequest


class PersonalDataRequestBuilder(object):
    def __init__(self):
        self.__request = PersonalDataRequest()

    def set_type(self, value):
        self.__request.type = value
        return self

    def set_last_name(self, value):
        self.__request.last_name = value
        return self

    def set_first_name(self, value):
        self.__request.first_name = value
        return self

    def set_middle_name(self, value):
        self.__request.middle_name = value
        return self

    def set_metadata(self, value):
        self.__request.metadata = value
        return self

    def build(self):
        return self.__request
