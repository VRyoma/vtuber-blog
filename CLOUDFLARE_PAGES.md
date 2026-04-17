# Cloudflare Pages デプロイ手順

このリポジトリを Cloudflare Pages に接続して公開するときの設定メモ。

## 1. プロジェクト作成

1. Cloudflare ダッシュボード → **Workers & Pages** → **Create** → **Pages** → **Connect to Git**
2. GitHub の `vryoma/vtuber-blog` リポジトリを選択
3. Production branch: `main`

## 2. ビルド設定

| 項目 | 値 |
|---|---|
| Framework preset | `Hugo` |
| Build command | `hugo --gc --minify` |
| Build output directory | `public` |
| Root directory | (空でよい) |

## 3. 環境変数

Cloudflare Pages → Settings → Environment variables に以下を追加。

| Key | Value | Scope |
|---|---|---|
| `HUGO_VERSION` | `0.141.0` | Production & Preview |
| `HUGO_ENV` | `production` | Production |
| `GO_VERSION` | `1.22.0` | Production & Preview |

`GO_VERSION` は Hugo Module を解決するために必要です (このリポジトリは Stack テーマを Hugo Module 経由で読み込んでいるため)。

## 4. カスタムドメイン (任意)

Pages プロジェクト → **Custom domains** から独自ドメインを接続。接続後、`hugo.toml` の `baseURL` をそのドメインに書き換えてコミットすると、OG タグ・RSS 等のリンクが揃います。

## 5. プレビュー

PR を作ると Cloudflare Pages が自動で Preview URL (`<hash>.vtuber-blog.pages.dev`) を発行する。GitHub Checks に URL が出るので、そこから確認できます。

## トラブルシュート

- **`module not found`**: `GO_VERSION` が未設定の可能性。環境変数を確認。
- **`hugo: command not found` / 古い Hugo**: `HUGO_VERSION` を明示。preset だけだと古い版が入ることがある。
- **日本語が文字化け**: `hasCJKLanguage = true` が `hugo.toml` にあるか確認 (本リポジトリでは設定済み)。
