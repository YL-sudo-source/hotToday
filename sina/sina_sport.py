import requests
import pyquery
def get_sina_sport_data():
    url = "https://sports.sina.com.cn/"
    res = requests.get(url)
    doc = pyquery.PyQuery(res.content.decode("utf-8"))
    h3_items = doc("div[node-type=\"tianYiList\"] h3>a").items()
    li_items = doc("div[node-type=\"tianYiList\"] li>a").items()
    data = []
    check = set()
    for item in li_items:
        title = item.text()
        link = item.attr("href")
        if "ai/app/download" in link:
            continue
        if check.issuperset({link}):
            continue
        result = check.add(link)
        hotScore = 0
        data.append({
            "title": title,
            "url": link,
            "hotScore": hotScore
        })
    for item in h3_items:
        title = item.text()
        link = item.attr("href")
        if "ai/app/download" in link:
            continue
        if check.issuperset({link}):
            continue
        result = check.add(link)
        hotScore = 0
        data.append({
            "title": title,
            "url": link,
            "hotScore": hotScore
        })
    return {"data":data}