# Django Web Practical App
### MoTo LaBo site url
> https://moto-labo.dt.r.appspot.com
### GAE (Google App Engine )
  - 下記で管理
    - Google Cloud Platform
    - Google Cloud Storage
    - Google Analytics
### App
  - blog 機能
    - コメント投稿
    - user page
  - login 機能
  - お問い合わせ page
    - Google reCAPTCHA
  - 決済 page(demo page:PAY.jp)
    - 必要な場合(決済行者に申請)、API(api key)取得・実装
  - Javascript(非同期処理)
### 1. Python Django を用いて web app 開発
   - 実用性に重きを置く事が前提
### 2. Material Design Bootstrap と独自の scss を用いた Design
   - 今後のメンテナンスがしやすように,種別事file分け,変数格納,mixin, 使用
### 3. Django の template tage と HTML を組み合わせてメンテナンスしやすいようにする
   - file を分けて分かり易く・管理し易くする (include で import)
### 4. GAE(google app engine), Google Cloud Storage, を用いて service を公開
   - App 詳細は Development_Manual.md を確認
### 5. iPhone,Android の home icon 対応
   - 簡易的な SEO, OGP の対策も実施
### 6. 今後の version は tag を付けて GitHub 管理
