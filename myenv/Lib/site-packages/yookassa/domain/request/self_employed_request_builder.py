# -*- coding: utf-8 -*-
from yookassa.domain.request import SelfEmployedRequest


class SelfEmployedRequestBuilder(object):
    def __init__(self):
        self.__request = SelfEmployedRequest()

    def set_itn(self, value):
        self.__request.itn = value
        return self

    def set_phone(self, value):
        self.__request.phone = value
        return self

    def set_description(self, value):
        self.__request.description = value
        return self

    def set_confirmation(self, value):
        self.__request.confirmation = value
        return self

    def set_metadata(self, value):
        self.__request.metadata = value
        return self

    def build(self):
        return self.__request
