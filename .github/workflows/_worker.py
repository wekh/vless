import requests

# 定义要获取内容的URL
url_worker = "https://gh.wekh.eu.org/https:/raw.githubusercontent.com/yonggekkk/Cloudflare_vless_trojan/main/Vless_workers_pages/_worker.js"
url_proxyip = "https://gh.wekh.eu.org/https:/raw.githubusercontent.com/yonggekkk/Cloudflare_vless_trojan/main/ProxyIP.txt"

# 发起请求并获取页面内容
response_worker = requests.get(url_worker)
response_proxyip = requests.get(url_proxyip)

# 将内容分别保存到文件中
with open("_worker.js", "w") as file_worker:
    file_worker.write(response_worker.text)

with open("ProxyIP.txt", "w") as file_proxyip:
    file_proxyip.write(response_proxyip.text)

print("内容已保存到文件中：_worker.js 和 ProxyIP.txt")
