# URL -> 기사(제목,본문,날짜) 수집

def get_news(url: str):
    import requests
    from bs4 import BeautifulSoup
    result = requests.get(url)
    doc = BeautifulSoup(result.text, "html.parser")
    title = doc.select("span.num_date")[0].get_text()
    print(f"날짜: {title}")
    title = doc.select("h3.tit_view")[0].get_text()
    print(f"제목: {title}")
    content_list = doc.select("div.article view p")
    content = ""
    for p in content_list:  # content = content + p.get_text()
        content += p.get_text()  # 반복1: content = "" + "본문1"
    print(f"본문:{content}")  # 반복2: content = "본문2" + "본문2"
    pass