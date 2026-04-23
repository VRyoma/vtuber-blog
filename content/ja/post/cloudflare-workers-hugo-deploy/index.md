---
title: "Cloudflare Workers + Hugo で配信サイトを無料公開する手順"
slug: "cloudflare-workers-hugo-deploy"
date: 2026-04-04T10:00:00+09:00
draft: false
description: "独自ドメインのサイトを持ちたいがサーバー代を払いたくない人向けに、Hugoで作った静的サイトをCloudflare Workers Assetsに無料で載せる手順を解説します。"
categories:
  - unei-tips
tags:
  - Hugo
  - Cloudflare
  - 静的サイト
  - デプロイ
---

「独自ドメインのサイトが欲しいけど、月額サーバー代は払いたくない」と思っていませんか。

ブログやお知らせページを HTTPS で公開するだけなら、レンタルサーバーは不要です。Hugo で作った静的サイトを **Cloudflare Workers Assets** に載せれば、月額 0 円で独自ドメインのサイトを運営できます。

この記事では、Hugo サイトのビルドから Cloudflare へのデプロイ、カスタムドメインの設定までを一通り解説します。

**この記事で分かること:**

- Cloudflare Workers Assets を選ぶ理由と他サービスとの比較
- Hugo のビルド設定と `wrangler.toml` の書き方
- カスタムドメインを HTTPS で公開する手順と注意点

---

## なぜ Cloudflare Workers なのか — 無料・高速・手軽

Cloudflare Workers Assets は、静的ファイル（HTML・CSS・JS・画像）を Cloudflare の世界中にあるサーバーに配置し、高速に配信する仕組みです。個人ブログの運用では、無料プランで十分に賄えます。

### 無料プランでどこまで使えるか

Cloudflare Workers の Free プランでは、**1 日あたり 100,000 リクエスト**まで無料で処理されます。1 日的に数〜数十アクセスの個人ブログであれば、余裕を持って収まります。仮に 1 ページあたり 10 リクエスト（HTML + CSS + JS + 画像類）と見積もっても、1 日 10,000 ページビューまで対応可能です。

サーバーの OS アップデートやセキュリティパッチも不要です。Hugo が生成する静的 HTML を配置するだけなので、PHP やデータベースの脆弱性を気にする必要がありません。

### 他サービスとの比較

無料で静的サイトをホストできるサービスはいくつかあります。代表的なものを比較しました。

| 項目 | Cloudflare Workers | GitHub Pages | Vercel | Netlify |
|---|---|---|---|---|
| 無料リクエスト数 | 100,000 件/日 | 制限なし（公平利用） | 100 GB/月転送 | 100 GB/月転送 |
| カスタムドメイン | 対応 | 対応 | 対応 | 対応 |
| SSL 証明書 | 自動 | 自動 | 自動 | 自動 |
| 日本からの速度 | 〇（東京エッジ） | 〇 | 〇 | △（遅め） |
| ビルド機能 | なし（外部で実行） | GitHub Actions 連携 | 自動ビルド | 自動ビルド |
| CLI デプロイ | `wrangler` | `git push` | `vercel` | `netlify deploy` |

Cloudflare の強みは、**世界 300 以上のエッジロケーション**でコンテンツを配信する点です。日本国内にも複数のエッジがあるため、閲覧者にとってページの読み込みが速くなります。

ただし、Workers Assets には自動ビルド機能がありません。Hugo のビルドは手元または GitHub Actions で行い、生成された `public/` ディレクトリをデプロイする流れになります。このあとはその具体的な手順を見ていきます。

---

## Hugo サイトのビルド設定

デプロイの前に、Hugo でサイトを正しくビルドできる状態を整えます。前提として、**Hugo (extended 版)** がインストール済みで、すでにサイトのファイルがあるものとします。

### Hugo のバージョン確認

まずはターミナルで Hugo のバージョンを確認します。

```bash
hugo version
```

出力に `extended` と含まれていれば問題ありません。SCSS を使うテーマでは extended 版が必要です。含まれていない場合は、[Hugo のリリースページ](https://github.com/gohugoio/hugo/releases) から extended 版をインストールし直してください。

### 設定ファイルの確認

`hugo.toml`（または `config.toml`）の `baseURL` を、実際のドメインに合わせます。

```toml
baseURL = "https://vtblog.vvil.jp/"
```

`baseURL` が合っていないと、CSS や画像のパスがずれてページが崩れる原因になります。デプロイ先の URL を確認してから設定しましょう。

### ビルドの実行

次のコマンドでサイトをビルドします。

```bash
hugo --gc --minify
```

- `--gc` は、使われていないキャッシュファイルを整理するオプションです
- `--minify` は、HTML・CSS・JS の余分な空白を削ってファイルサイズを小さくします

ビルドが成功すると、プロジェクト直下に `public/` ディレクトリが生成されます。この中に、サイトを構成するすべての HTML・CSS・画像ファイルが入っています。

```bash
# 生成されたファイルの確認例
ls public/
# index.html  p/  categories/  tags/  ...
```

ビルドエラーが出た場合は、テーマのインストール漏れやフロントマターの書き間違いが多いです。エラーメッセージに沿って修正してください。

---

## Cloudflare へのデプロイ手順

Hugo のビルドができたら、次は Cloudflare Workers Assets にデプロイします。Wrangler という公式 CLI ツールを使って進めます。

### 手順 1: Cloudflare アカウントを作成する

[Cloudflare のサインアップページ](https://dash.cloudflare.com/sign-up) からアカウントを作成します。メールアドレスとパスワードだけで登録でき、クレジットカードの入力は不要です。

### 手順 2: Wrangler CLI をインストールする

Wrangler は Cloudflare Workers のコマンドラインツールです。Node.js がインストール済みの環境で、次のコマンドを実行します。

```bash
npm install -g wrangler
```

Node.js が入っていない場合は、[Node.js の公式サイト](https://nodejs.org/) から LTS 版をインストールしてください。バージョン 18 以降を推奨します。

### 手順 3: Wrangler でログインする

```bash
wrangler login
```

ブラウザが開き、Cloudflare アカウントへのアクセス許可を求められます。「Allow」をクリックすれば、ターミナルにログイン完了のメッセージが表示されます。

### 手順 4: wrangler.toml を作成する

プロジェクトのルートディレクトリに `wrangler.toml` を作成します。このファイルは Workers Assets に「どのディレクトリをデプロイするか」を伝える設定ファイルです。

```toml
name = "vtuber-blog"
compatibility_date = "2026-04-17"

[assets]
directory = "./public"
not_found_handling = "404-page"
```

各項目の意味は次の通りです。

- `name` — Workers のプロジェクト名。任意の英数字を指定します
- `compatibility_date` — ランタイムの互換性日付。今日の日付で問題ありません
- `directory` — デプロイするディレクトリ。Hugo の出力先である `./public` を指定します
- `not_found_handling` — 存在しないパスへのアクセス時に 404 ページを返す設定です

このプロジェクトでは JSON フォーマット（`wrangler.jsonc`）を使うこともできます。TOML と JSON、どちらでも動作は同じです。

### 手順 5: デプロイを実行する

Hugo のビルドと Wrangler の設定が揃ったら、デプロイします。

```bash
# まずビルド
hugo --gc --minify

# デプロイ
npx wrangler deploy
```

初回デプロイ時は、プロジェクトが Cloudflare 上に新規作成されます。数秒で完了し、`https://<project-name>.<account>.workers.dev` という URL が発行されます。

```bash
# デプロイ成功時の出力例
# Uploaded vtuber-blog
# Published vtuber-blog (x.xx sec)
#   https://vtuber-blog.<your-account>.workers.dev
```

ブラウザでこの URL を開き、サイトが表示されるか確認してください。以降の更新も、同じ `hugo --gc --minify && npx wrangler deploy` を実行するだけで反映されます。

---

## カスタムドメインの設定と注意点

Workers のデフォルト URL（`*.workers.dev`）でもサイトは公開できますが、独自ドメインを当てるとブランド感が高まります。Cloudflare でドメインを管理する場合の手順を解説します。

### 手順 1: ドメインを Cloudflare に追加する

Cloudflare のダッシュボードで「Add a site」をクリックし、所有しているドメインを入力します。Cloudflare が提示するネームサーバーに変更するよう求められるので、ドメイン取得元の管理画面（お名前.com や Google Domains など）で設定します。

### 手順 2: Workers にカスタムドメインを紐付ける

Cloudflare ダッシュボードの「Workers & Pages」から、デプロイしたプロジェクトを開きます。「Settings」→「Domains & Routes」→「Custom Domains」でドメインを追加します。

Cloudflare 上でドメインが管理されていれば、DNS レコードは自動で設定されます。手動でレコードを書く必要はありません。

### 手順 3: SSL 証明書の確認

Cloudflare は、カスタムドメインに対して**無料の SSL 証明書を自動発行**します。通常は数分で有効になり、`https://` でアクセスできるようになります。Let's Encrypt などの外部サービスを使う必要はありません。

### DNS 反映の注意点

ネームサーバーの変更直後は、**最大 24 時間**かけて世界中に反映されます。この間は古いサーバーを見にいく地域と新しいサーバーを見にいく地域が混在します。焦らず、半日ほど待ってから確認しましょう。

### ドメイン設定のチェックリスト

- [ ] ネームサーバーが Cloudflare 指定のものに変更されている
- [ ] Workers のカスタムドメイン設定でドメインが追加されている
- [ ] `https://` でアクセスして鍵マークが表示される
- [ ] `http://` でアクセスすると `https://` にリダイレクトされる

リダイレクトの設定は、Cloudflare ダッシュボードの「SSL/TLS」→「Edge Certificates」で「Always Use HTTPS」をオンにするだけで有効になります。

---

## まとめ

- Cloudflare Workers Assets は **100,000 リクエスト/日**まで無料で、個人ブログに十分な余裕がある
- Hugo の `public/` ディレクトリを `wrangler deploy` で数秒で公開できる
- カスタムドメインも SSL 証明書込みで無料設定可能。サーバー運用の手間がない

まずは手持ちの Hugo サイト（または `hugo new site` で新規作成したサイト）を、`hugo --gc --minify && npx wrangler deploy` の 2 コマンドで Cloudflare に上げてみてください。数分で `https://` 付の URL が手に入り、サーバー代 0 円のブログ運営が始まります。
