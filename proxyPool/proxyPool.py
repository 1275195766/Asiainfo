import requests

def get_proxy():
    return requests.get("http://39.100.99.42:5010/get/").json()


def delete_proxy(proxy):
    requests.get("http://39.100.99.42:5010/delete/?proxy={}".format(proxy))


def get_all_proxy():

    return requests.get("http://39.100.99.42:5010/get_all/")


def get_status():
    return requests.get("http://39.100.99.42:5010/get_status")

# your spider code

def getHtml():
    # ....
    retry_count = 5
    proxy = get_proxy().get("proxy")
    while retry_count > 0:
        try:
            html = requests.get('http://www.baidu.com', proxies={"http": "http://{}".format(proxy)}, verify=False)
            # 使用代理访问
            return html
        except Exception:
            retry_count -= 1

    # 删除代理池中代理
    delete_proxy(proxy)
    return None


if __name__ == "__main__":
    print(getHtml().text)