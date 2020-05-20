from functools import wraps
import datetime

import hashids


class ParamsProcess:

    def __init__(self):
        self.hash_func = hashids.Hashids(salt="test", min_length=8)

    def __encode_id(self, common_id):
        return self.hash_func.encode(common_id)

    def __decode_id(self, common_id):
        return self.hash_func.decode(common_id)

    def auto_decode(self, *args, **kwargs):
        """
        参数自动解密
        :return: 解密后的json数据
        """
        try:
            for params in args[0]:
                encode_id = kwargs.get(params)
                if encode_id is None:
                    pass
                else:
                    kwargs['params'] = self.__decode_id(encode_id)
        except IndexError:
            raise IndexError("Need parse key list")
        return kwargs

    def auto_encode(self, *args, **kwargs):
        """
        参数自动加密
        :return: 解密后的json数据
        """
        try:
            for params in args[0]:
                decode_id = kwargs.get(params)
                if decode_id is None:
                    pass
                else:
                    kwargs['params'] = self.__encode_id(decode_id)
        except IndexError:
            raise IndexError("Need parse key list")
        return kwargs


class TimeRelation:

    @staticmethod
    def get_today(time_status):
        if isinstance(time_status, datetime.time):
            return datetime.datetime.combine(datetime.datetime.today(), time_status)
        if time_status == 'midnight':
            return datetime.datetime.combine(datetime.datetime.today(), datetime.time.min)
        elif time_status == 'over':
            return datetime.datetime.combine(datetime.datetime.today(), datetime.time.max)
        else:
            return None

    @staticmethod
    def get_someday(abs_num, time_status):
        if isinstance(time_status, datetime.time):
            return datetime.datetime.combine(datetime.datetime.today() + datetime.timedelta(abs_num), time_status)
        if time_status == 'midnight':
            return datetime.datetime.combine(datetime.date.today() + datetime.timedelta(abs_num), datetime.time.min)
        elif time_status == 'over':
            return datetime.datetime.combine(datetime.date.today() + datetime.timedelta(abs_num), datetime.time.min)
        else:
            return None
