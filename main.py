import config  # ここで config.py が「実行」される！

def main():
    print(f"--- main.py の実行開始 ---")

    print(f"--- import 後の処理 ---")
    print(f"main.py の名前は: {__name__}")

    # configの中の関数は呼べる
    print(config.get_db_info())
    print(f"#####################################")

if __name__ == '__main__':
    print(type(__name__))
    main()
