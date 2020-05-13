from django.shortcuts import render
import hashids

salt = "test"

i = hashids.Hashids(salt="sasasa", min_length=8)  # 添加一个salt ，Hashide通过接收salt值支持对散列的散列，可确保唯一性
ensecret = i.encode(12345678)
print(ensecret)
desecret = i.decode(ensecret+'123')
print(desecret)
