import hashids
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import RpcRequest


def check_params(
        *args,
        partial=True,
        **kwargs
):
    try:
        params_set = args[0]
    except IndexError:
        raise IndexError("请输入参数列表")

    if partial:
        if set(kwargs.keys()).issubset(params_set):
            return True
        else:
            raise Exception("参数未通过检查")
    else:
        if params_set == kwargs.keys():
            return True
        else:
            raise Exception("参数未通过检查")


class Params2Code:

    def __init__(self, salt):
        self.hash_func = hashids.Hashids(salt=salt, min_length=4)

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
            raise IndexError("请输入要解密的key列表")
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
            raise IndexError("请输入要解密的key列表")
        return kwargs


class SendSMS:
    REGION = "cn-hangzhou"
    PRODUCT_NAME = "Dysmsapi"
    DOMAIN = "dysmsapi.aliyuncs.com"

    def __init__(self, access_key_id, access_key_secret):
        self.acs_client = AcsClient(access_key_id, access_key_secret, self.REGION)

    def send_sms(self, template_param=None, **kwargs):
        check_params({"OutId", "PhoneNumbers", "SignName", "TemplateCode"}, partial=False, **kwargs)
        sms_request = RpcRequest(self.PRODUCT_NAME, '2017-05-25', 'SendSms')

        sms_request.__params = {}
        sms_request.__params.update(**kwargs)

        if template_param is not None:
            sms_request.__params.update({'TemplateParam': template_param})
        sms_request.set_query_params(sms_request.__params)

        sms_response = self.acs_client.do_action_with_exception(sms_request)

        return sms_response
