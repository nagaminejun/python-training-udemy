import smtplib
from email.message import EmailMessage

# 1. メールの内容を作成
msg = EmailMessage()
msg.set_content('これはPythonからのテストメールです。')  # 本文
msg['Subject'] = 'テストメールの件名'              # 件名
msg['From'] = 'あなたのメールアドレス'    # 送信元
msg['To'] = '宛先メールアドレス@example.com'        # 送信先（自分でもOK）

# 2. SMTPサーバーの設定（Gmail用）
smtp_host = 'smtp.gmail.com'
smtp_port = 587  # TLS用のポート
username = 'あなたのメールアドレス'
password = 'ここにアプリパスワードを入れる'  # 普通のパスワードではありません

# 3. メール送信を実行
try:
    # サーバーに接続（JavaのSocket通信のようなもの）
    server = smtplib.SMTP(smtp_host, smtp_port)
    server.ehlo()      # 挨拶
    server.starttls()  # 通信を暗号化
    server.ehlo()      # 再度挨拶
    # ログイン
    server.login(username, password)
    
    # 送信
    server.send_message(msg)
    print("メール送信に成功しました！")
    
    # 終了
    server.quit()
except Exception as e:
    print(f"エラーが発生しました: {e}")
