code_2_session = ("GET",
                  "https://api.weixin.qq.com/sns/jscode2session?appid=APPID&secret=SECRET&js_code=JSCODE&grant_type"
                  "=authorization_code")
get_paid_union_id = ("GET",
                     "https://api.weixin.qq.com/wxa/getpaidunionid?access_token={access_token}&openid={"
                     "open_id}&transaction_id={transaction_id}")
get_access_token = (
    "GET", "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={app_id}&secret={app_secret}")
get_unlimited_code = ("POST", "https://api.weixin.qq.com/wxa/getwxacodeunlimit?access_token={access_token}")
img_sec_check = ("POST", "https://api.weixin.qq.com/wxa/img_sec_check?access_token={access_token}")
msg_sec_check = ("POST", "https://api.weixin.qq.com/wxa/msg_sec_check?access_token=ACCESS_TOKEN")
send_subscribe_message = ("POST", "https://api.weixin.qq.com/cgi-bin/message/subscribe/send?access_token=ACCESS_TOKEN")
