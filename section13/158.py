from bs4 import BeautifulSoup
import requests

# 1. 指定したURLのHTML情報を取得する
url = 'https://www.python.org'
response = requests.get(url)

# 2. 取得したテキスト（HTML）をBeautifulSoupで解析（パース）する
# 'lxml' は高速な解析エンジンです
soup = BeautifulSoup(response.text, 'lxml')

# 3. HTMLの中から <title> タグをすべて探し出す
titles = soup.find_all('title')

# x. HTMLの中から <a> タグをすべて探し出す
# titles = soup.find_all('a')

# 4. 結果を表示する
print(titles)

# おまけ：タグの中の「文字だけ」を綺麗に表示したい場合
# for title in titles:
#     print(title.get_text())
