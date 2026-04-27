from roboter.models import robot

def talk_about_restaurant():
    # レストラン案内を担当するロボットオブジェクトを生成する
    restaurant_robot = robot.RestaurantRobot()

    # 1. ロボットが挨拶する
    # 2. ユーザー名を入力してもらう
    restaurant_robot.hello()

    # TODO:robotがuserへレストランのおすすめをする
    # 3. CSVに過去のレストランデータがあるか確認する
    # 4. データがあれば、人気順におすすめする
    # 5. ユーザーが Yes と答えたら、そのレストランのカウントを増やす
    # 6. ユーザーが No と答えたら、次のレストランをおすすめする
    # restaurant_robot.recommend_restaurant()

    # TODO:
    # おすすめをランダム表示するロジック教材にはない。
    restaurant_robot.recommend_restaurant()

    # TODO:
    # 7. おすすめが終わったら、好きなレストランを聞く
    # 8. 入力されたレストランをCSVに保存する
    restaurant_robot.ask_user_favorite()


    # 9. お礼を言って終了する
    restaurant_robot.thank_you()
