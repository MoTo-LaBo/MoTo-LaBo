# Django Web Practical App
- GAE (Google App Engine )
  - Google Cloud Storage
- App
  - login 機能
  - Javascript(非同期処理)
  - お問い合わせ page
    - google re CAPTCHA
  - user page
  - 決済 page(demo page)
    - 必要な場合(決済行者に申請)、API(api key)取得・実装
1. Python Django を用いて web app 開発
   - 実用性に重きを置く事が前提
2. Material Design Bootstrap と独自の scss を用いた Design
   - 今後のメンテナンスがしやすように,種別事file分け,変数格納,mixin, 使用
3. Django の template tage と HTML を組み合わせてメンテナンスしやすいようにする
   - file を分けて分かり易く・管理し易くする (include で import)
4. GAE(google app engine), Google Cloud Storage, GitHub を用いて service を公開
   - App 詳細は Development_Manual.md を確認
5. iPhone,Android の home icon 対応
   - 簡易的な SEO, OGP の対策も実施
6. 今後の version は tag を付けて管理
