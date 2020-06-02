# coding: UTF-8
import urllib.request, urllib.error
from bs4 import BeautifulSoup

url = "http://www.nikkei.com/markets/kabu/"

html = urllib.request.urlopen(url)

soup = BeautifulSoup(html, "html.parser")

# span要素全てを摘出する
span = soup.find_all("span")

nikkei_heikin = ""
for tag in span:
    try:
        string_ = tag.get("class").pop(0)

        # 摘出したclassの文字列にmkc-stock_pricesと設定されているかを調べる
        if string_ in "mkc-stock_prices":
            nikkei_heikin = tag.string
            break
    except:
        pass

print(nikkei_heikin)
