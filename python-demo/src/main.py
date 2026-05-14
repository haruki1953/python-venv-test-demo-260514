# hello.py
import requests

#
print("Hello Python 3.11")

# 发起 GET 请求
response = requests.get("https://httpbin.org/get")

# 打印状态码
print("Status:", response.status_code)

# 打印返回内容（JSON）
print("Response JSON:")
print(response.json())
