# Awesomemory
旅や日常生活の思い出を 写真アルバムとして保管でき、いつでも思い出を振り返れるアプリケーション。
写真アルバムを作成するだけでなく、簡単なスケジュールも作成することもできます。

# 開発環境
- Python == 3.7.5
- asgiref==3.2.3
- Django==3.0.3
- django-widget-tweaks==1.4.5
- mysqlclient==1.4.6
- Pillow==7.0.0
- pytz==2019.3
- sqlparse==0.3.0

# アプリ機能
#### 1. サインアップ
記入してアカウントを作成します。
#### 2. ログイン
ログイン画面に切り替わり、先ほど作成したアカウントログインして下さい。
#### 3. Memory一覧
ログイン後ホーム画面であるMemory一覧が表示。(Create Memory)を押します。
#### 4. Memory作成フォーム
Title, Category, Thumbnail, Textを記入し Saveします。
#### 5. 作成したMemoryの表示
Memory一覧画面に戻り、先ほど作成した Memoryが表示されています。クリックすると詳細画面に切り替わります。
#### 6. Memory詳細画面
詳細画面の左下にあるボタンでサムネイルやテキストなどの変更や、削除を行なうことができます。
右上にある (Update Image)をクリックして複数の画像をアップロードやすることができます。
画像の追加や変更、削除が可能です。
#### 7. Schedule画面
ヘッダーのScheduleをクリックすると、Schedule管理画面にいき、簡単なスケジュールを作成することができます。
古い日付順位に表示されます。右上にある(New Schedule)で新しいスケジュールを作成できます。
#### 9. 作成後Schedule画面で更新や削除
#### 10. Portfolio画面
ヘッダーのProfileをクリックして Profile画面に切り替わります。Profile画面ではパスワードの変更とProfileの更新が可能です。

# 使用方法
#### 1. git cloneでリポジトリーをクローン
```
$ git clone https://github.com/Yuji5117/awesomemory.git
```
#### 2. awesomemeory ディレクトリーに移動し、以下のコマンドを実行し仮想環境を有効化
```
$ source venv/bin/activate
```
#### 3. その後、runserverを実行
```
$ python manage.py runserver
```
#### 4. 以下が表示されたら、ブラウザで http://127.0.0.1:8000/にアクセス
```
System check identified no issues (0 silenced).
February 19, 2020 - 05:01:09
Django version 3.0.3, using settings 'conf.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```



