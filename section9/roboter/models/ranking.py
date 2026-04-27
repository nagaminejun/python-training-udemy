import csv  # CSVファイルを読み書きするために使う
import os   # ファイルが存在するか確認するために使う
import random

# CSVファイル名を定数として定義する
# あとでファイル名を変えたいとき、ここだけ変えればよい
RANKING_CSV_FILE_PATH = 'ranking.csv'

# CSVの列名を定数として定義する
# 直接 'NAME' や 'COUNT' と何度も書くとタイプミスしやすいため
RANKING_COLUMN_NAME = 'NAME'
RANKING_COLUMN_COUNT = 'COUNT'

class RankingModel(object):
    """
    レストランランキングをCSVで管理するクラス。

    このクラスの役割:
    1. ranking.csv が存在するか確認する
    2. 入力されたレストラン名とカウントを self.data に持つ
    3. self.data の内容をCSVへ保存する
    """
    def __init__(self, csv_file=RANKING_CSV_FILE_PATH):
        self.csv_file = csv_file
        self.data = {}

        if not os.path.exists(self.csv_file):
            # 'w' は書き込みモード
            # newline='' はCSVを書き込むときの空行対策
            with open(self.csv_file, 'w', newline='') as csv_file:
                writer = csv.DictWriter(
                    csv_file,
                    fieldnames=[
                        RANKING_COLUMN_NAME,
                        RANKING_COLUMN_COUNT
                        ]
                )
                # CSVの1行目にヘッダーを書き込む
                # NAME,COUNT
                writer.writeheader()
            
        # CSVファイルの中身を self.data に読み込む
        self.load_data()

    # CSVファイルを読み込んでデータを一時保管する
    def load_data(self):
        """
        CSVファイルの中身を読み込んで、self.data に入れる。

        ranking.csv の例:
            NAME,COUNT
            Japanese Apple,2

        self.data の形:
            {
                'Japanese Apple': 2
            }
        """
        # CSVファイルを読み込みモードで開く
        with open(self.csv_file, 'r', newline='') as csv_file:
            reader = csv.DictReader(csv_file)

            # CSVを1行ずつ読む
            for row in reader:
                # row は辞書のように扱える
                # 例: {'NAME': 'Japanese Apple', 'COUNT': '2'}
                restaurant_name = row[RANKING_COLUMN_NAME]
                count = int(row[RANKING_COLUMN_COUNT])

                self.data[restaurant_name] = count

    def increment(self, restaurant_name):
        """
        レストラン名のカウントを1増やす。
        まだCSV読み込みはせず、まずは1件保存できる形にする。
        """
        restaurant_name = restaurant_name.title() # title()は単語の先頭を大文字する標準メソッド

        if not restaurant_name:
            return

        # すでに self.data に同じレストラン名があるか確認する
        if restaurant_name in self.data:
            self.data[restaurant_name] += 1
        else:
            self.data[restaurant_name] = 1
        
        self.save()

    def save(self):
        with open(self.csv_file, 'w', newline='') as csv_file:
            writer = csv.DictWriter(
                csv_file,
                fieldnames=[
                    RANKING_COLUMN_NAME,
                    RANKING_COLUMN_COUNT
                    ]
                )
            # まずヘッダーを書く
            writer.writeheader()

            for name, count in self.data.items():
                writer.writerow({
                    RANKING_COLUMN_NAME: name,
                    RANKING_COLUMN_COUNT: count
                })

    def get_most_popular(self, not_list=None):
        """
        self.data の中から、COUNTが一番多いレストラン名を返す。

        not_list:
            すでにおすすめ済みのレストランを除外するためのリスト。
        """
        if not_list is None:
            not_list = []
        # self.data が空なら、おすすめできるレストランがない
        if not self.data:
            return None
        
        # self.data をCOUNTの多い順に並べる
        # 例: {'A': 3, 'B': 1} → ['A', 'B']
        sorted_data = sorted(
            self.data, 
            key=self.data.get, 
            reverse=True
        )

        # 人気順に見て、まだおすすめしていないレストランを返す
        for restaurant_name in sorted_data:
            if restaurant_name in not_list:
                continue

            return restaurant_name
        
        return None
    
    # ランダムロジック
    def get_random(self, not_list=None):
        # pass
        """
        ランダムにレストランを1つ返す
        （すでにおすすめしたものは除外）
        """

        if not_list is None:
            not_list = []

        # not_listに含まれていないレストランだけを抽出
        restaurants = [
            name for name in self.data if name not in not_list
        ]

        # 候補がなければ終了
        if not restaurants:
            return None
        
        # 
        return random.choice(restaurants)
    
if __name__ == '__main__':
    ranking_model = RankingModel()
    print(ranking_model.data)
    print(ranking_model.get_most_popular())
