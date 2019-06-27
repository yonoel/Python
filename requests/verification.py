import requests
from lxml import etree

def getVerificationCode(invoice):
    request_s = requests.Session()
    url = "https://inv-veri.chinatax.gov.cn/index.html"
    response  = request_s.get(url,verify = False)
    html = etree.HTML(response.text)
    print(response.text)


if __name__ == "__main__":
    getVerificationCode(None)
    # print(dir(fpdm))
