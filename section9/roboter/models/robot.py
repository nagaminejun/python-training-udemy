from roboter.models import ranking
from roboter.views import console

DEFAULT_ROBOT_NAME = 'Roboko'

class Robot(object):
    def __init__(self, name=DEFAULT_ROBOT_NAME):
        self.name = name
        self.user_name = ''
        # pass

    def hello(self):
        # self.user_name = input(f'こんにちは！私は{self.name}です。あなたの名前は何ですか？')
        template = console.get_template('hello.txt')
        self.user_name = input(template.substitute({'robot_name' : self.name}))

    def thank_you(self):
        print(f'{self.name}: {self.user_name}さん。ありがとうございました。')
        print('良い一日を！さようなら')
        # pass

class RestaurantRobot(Robot):
    def __init__(self, name=DEFAULT_ROBOT_NAME):
        super().__init__(name=name)
        self.favorite_restaurant = ''
        self.ranking_model = ranking.RankingModel()

    def ask_user_favorite(self):
        # self.favorite_restaurant = input(f'{self.user_name}さん。どこのレストランが好きですか？\n')
        template = console.get_template('which_restaurant.txt')
        answer = input(template.substitute({'user_name' : self.user_name}))

        # 空文字・スペースだけの入力を保存しない
        if not self.favorite_restaurant.strip():
            print('無効な文字が入力されたため登録できませんでした')
            return

        self.ranking_model.increment(self.favorite_restaurant)

        print(f'確認: 入力されたレストランは{self.favorite_restaurant}です')

    def recommend_restaurant(self):

        """
        人気順におすすめし、Noなら次を出す（ループ版）
        """

        not_list = [] # すでにおすすめしたレストランを記録するリスト

        while True:
            # 人気順にレストラン名をwhileループする
            # restaurant = self.ranking_model.get_most_popular(not_list)

            # ランダムにレストラン名をwhileループする
            restaurant = self.ranking_model.get_random(not_list)

            # 
            if not restaurant:
                break

            # answer = input(
            #     f'私のおすすめのレストランは{restaurant}です。\n'
            #     f'このレストランは好きですか？ [y/n]\n'
            # )

            template = console.get_template('greeting.txt')

            answer = input(template.substitute({'restaurant' : restaurant}))

            # Yesならカウントを増やす
            if answer.lower() in ['yes', 'y']:
                self.ranking_model.increment(restaurant)
                break

            # No → 次の候補へ
            not_list.append(restaurant)
        # """
        # 一番人気のレストランを1つおすすめする
        # """

        # # CSVから一番人気のレストランを取得
        # restaurant = self.ranking_model.get_most_popular()

        # # 何もデータがなければ何もしない
        # if not restaurant:
        #     return
        
        # # ユーザーにおすすめする。
        # answer = input(
        #     f'私のおすすめのレストランは{restaurant}です。\n'
        #     f'このレストランは好きですか？ [y/n]\n')
        
        # # Yesならカウントを増やす
        # if answer.lower() in ['yes', 'y']:
        #     self.ranking_model.increment(restaurant)
        
