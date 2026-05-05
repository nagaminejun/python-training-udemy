import datetime
from pymongo import MongoClient

# 1. MongoDBクライアントの作成
# localhostのデフォルトポート(27017)に接続します
client = MongoClient('mongodb://localhost:27017/')

# 2. データベースの選択 (なければ自動作成されます)
db = client['test_database']

# 3. スタック（データ）の定義
# Pythonの辞書型（JavaでいうMap）がそのまま保存できるのがMongoDBの強みです
stack1 = {
    'name': 'customer1',
    'pip': ['python', 'java', 'go'],
    'info': {'os': 'mac'},
    'data': datetime.datetime.utcnow()
}

stack2 = {
    'name': 'customer2',
    'pip': ['python', 'java'],
    'info': {'os': 'windows'},
    'data': datetime.datetime.utcnow()
}

# 4. コレクション（テーブルに相当）の取得とデータ挿入
db_stacks = db.stacks
stack_id = db_stacks.insert_one(stack1).inserted_id

# 5. 結果の表示
print(stack_id, type(stack_id))
print("###########")

# 6. IDを指定してデータの検索
print(db_stacks.find_one({'_id': stack_id}))
