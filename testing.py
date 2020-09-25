from urllib.request import urlopen
url = "https://www.cnn.com/2020/09/25/politics/census-counting-timeline-federal-judge/index.html"
page = urlopen(url)
html_bytes = page.read()
html = html_bytes.decode("utf-8")
print(html)
