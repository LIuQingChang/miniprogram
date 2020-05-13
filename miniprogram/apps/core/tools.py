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

    def auto_decode(self, params_json, json_key_list):
        """
        参数自动解密
        :param params_json: 参数字典
        :param json_key_list: 需要解密json的key列表
        :return: 解密后的json数据
        """
        for params in json_key_list:
            encode_id = params_json.get(params)
            if encode_id is None:
                pass
            else:
                params_json['params'] = self.__decode_id(encode_id)
        return params_json

    def auto_encode(self, params_json, json_key_list):
        """
        参数自动加密
        :param params_json: 参数字典
        :param json_key_list: 需要加密json的key列表
        :return: 解密后的json数据
        """
        for params in json_key_list:
            decode_id = params_json.get(params)
            if decode_id is None:
                pass
            else:
                params_json['params'] = self.__encode_id(decode_id)
        return params_json


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
