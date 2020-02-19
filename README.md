# Awesomemory
旅などの思い出を 写真アルバムとして保存でき、いつでも思い出を振り返れるアプリケーション。
写真アルバムを作成するだけでなく、簡単なスケジュールも作成することもできます。

#背景
Djangoの勉強を深めるため、ポートフォリオとして初めてWebアプリケーションを作成しました。
自分の趣味である旅と関連したものを作りたいと考え、思い出となる写真を保存できるアルバム集というコンセプトで開発を進めました。

# 実装し学んだこと
CRUD機能、ページネーション、サーチ機能、画像アップロード機能、カスタムユーザモデル、
signalを使用してアカウント作成時にプロフィールを自動生成する機能、userや他のモデルとのリレーション、
formsetを使用し複数の画像を一括でアップロードする機能を実装しました。
特に苦労した所は、複数の写真をアップロードする機能を実装する時で、ひたすらグーグルやYoutubeで調べ、
最終的に、imageモデルを作成しpostモデルにFreignkeyで紐付け、formsetのmodelformset_factoryを使用しなんとか実装出来ました。


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
ログイン画面に切り替わり、先ほど作成したアカウントでログインして下さい。
#### 3. Memory一覧
ログイン後ホーム画面であるMemory一覧が表示されます。Create Memoryボタンをクリックします。
#### 4. Memory作成フォーム
Title, Category, Thumbnail, Textを記入し Saveをクリックします。
#### 5. 作成したMemoryの表示
Memory一覧画面に戻ります、先ほど作成した Memoryが表示されています。クリックすると詳細画面に切り替わります。
#### 6. Memory詳細画面
詳細画面の左下にあるボタンでサムネイルやテキストなどの変更や、削除を行なうことができます。
#### 7. 複数の画像をアップロード
右上にある (Update Image)をクリックして複数の画像をアップロードすることができます。
画像の追加や変更、削除が可能です。
#### 8. Schedule画面
ヘッダーのScheduleをクリックすると、Schedule管理画面にいき、簡易なスケジュールを作成することができます。
日付が古い順に表示されます。右上にある(New Schedule)で新しいスケジュールを作成できます。
#### 10. Scheduleの更新と削除
作成後Schedule画面で更新や削除ボタンをクリックして行えます。
#### 11. Profile画面
ヘッダーのProfileをクリックして Profile画面に切り替わります。Profile画面ではパスワードの変更とProfileの更新が可能です。

# 使用方法
#### 1. git cloneでリポジトリーをクローン
```
$ git clone https://github.com/Yuji5117/awesomemory.git
```
#### 2. awesomemory ディレクトリーに移動し、以下のコマンドを実行し仮想環境を有効化
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



