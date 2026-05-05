import sqlite3
import time

# 1. memcacheのインポート（事前に pip install python-memcached が必要です）
import memcache

# 2. memcachedクライアントの作成
# 127.0.0.1:11211 は memcached のデフォルトの場所です
db = memcache.Client(['127.0.0.1:11211'])

# 3. キャッシュの基本操作（コメントアウトを外して試せます）
# 'web_page' というキーで 'value1' を 3秒間だけ保存する
db.set('web_page', 'value1', time=3)
time.sleep(1)
print(db.get('web_page'))

# カウンター機能（インクリメント）
db.set('counter', 0)
db.incr('counter', 1)
db.incr('counter', 1)
db.incr('counter', 1)
db.incr('counter', 1)
print(db.get('counter'))

# 4. SQLiteの基本操作（これまでの復習）
conn = sqlite3.connect('test_sqlite2.db')
curs = conn.cursor()
# curs.execute(
#     'CREATE TABLE persons('
#     'employ_id INTEGER PRIMARY KEY AUTOINCREMENT, name STRING)'
# )
# curs.execute('INSERT INTO persons(name) values("Mike")')
# conn.commit()
# conn.close()

def get_employ_id(name):
    employ_id = db.get(name)
    if employ_id:
        return employ_id
    curs.execute(
        'select * from persons where name = "{}"'.format(name)
    )
    person = curs.fetchone()
    if not person:
        raise Exception('No employ')
    employ_id, name = person
    db.set(name, employ_id, time=60)
    return employ_id

print(get_employ_id("Mike"))
