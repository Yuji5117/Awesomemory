# Awesomemory
旅などの思い出を 写真アルバムとして保存でき、いつでも思い出を振り返れるアプリケーション。
写真アルバムを作成するだけでなく、簡単なスケジュールも作成することもできます。

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

![demo10](https://user-images.githubusercontent.com/50049575/74825613-92e09380-534d-11ea-9b4e-35eabf50b89e.png)

#### 2. ログイン
ログイン画面に切り替わり、先ほど作成したアカウントでログインして下さい。

![demo11](https://user-images.githubusercontent.com/50049575/74825596-8e1bdf80-534d-11ea-88af-79192d674a92.png)

#### 3. Memory一覧
ログイン後ホーム画面であるMemory一覧が表示されます。Create Memoryボタンをクリックします。

![demo13](https://user-images.githubusercontent.com/50049575/74826927-ca503f80-534f-11ea-9087-e7500f1c13ec.png)

#### 4. Memory作成フォーム
Title, Category, Thumbnail, Textを記入し Saveをクリックします。

![demo14](https://user-images.githubusercontent.com/50049575/74826933-cde3c680-534f-11ea-8ec3-2440d9149d1a.png)

#### 5. 作成したMemoryの表示
作成した Memoryは以下のように表示されます。クリックすると詳細画面に切り替わります。

![demo1](https://user-images.githubusercontent.com/50049575/74826417-e7384300-534e-11ea-99c1-26ac4516e725.png)


#### 6. Memory詳細画面
詳細画面の左下にあるボタンでサムネイルやテキストなどの変更や、削除を行なうことができます。

![demo7](https://user-images.githubusercontent.com/50049575/74825654-a0961900-534d-11ea-8bf8-ba5804b87f94.png)

#### 7. 複数の画像をアップロード
右上にある (Update Image)をクリックして複数の画像をアップロードすることができます。
画像の追加や変更、削除が可能です。

![demo8](https://user-images.githubusercontent.com/50049575/74825635-9bd16500-534d-11ea-9b13-3786c78c08df.png)

#### 8. Schedule画面
ヘッダーのScheduleをクリックすると、Schedule管理画面にいき、簡易なスケジュールを作成することができます。
日付が古い順に表示されます。右上にある(New Schedule)で新しいスケジュールを作成できます。

![demo6](https://user-images.githubusercontent.com/50049575/74827415-c07b0c00-5350-11ea-91c2-50618a08eec1.png)

![demo5](https://user-images.githubusercontent.com/50049575/74826085-595c5800-534e-11ea-90a2-23c989090087.png)

#### 10. Scheduleの更新と削除
作成後Schedule画面で更新や削除ボタンをクリックして行えます。

![demo4](https://user-images.githubusercontent.com/50049575/74826054-4a75a580-534e-11ea-8b1e-ed05daea789e.png)

#### 11. Profile画面
ヘッダーのProfileをクリックして Profile画面に切り替わります。Profile画面ではパスワードの変更とProfileの更新が可能です。

![demo2](https://user-images.githubusercontent.com/50049575/74826004-35007b80-534e-11ea-9aae-31366b1aaab2.png)


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



