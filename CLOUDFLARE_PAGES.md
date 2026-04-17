# Cloudflare Pages デプロイ手順

このリポジトリを Cloudflare Pages に接続して公開するときの設定メモ。

## 1. プロジェクト作成

1. Cloudflare ダッシュボード → **Workers & Pages** → **Create** → **Pages** → **Connect to Git**
2. GitHub の `vryoma/vtuber-blog` リポジトリを選択
3. Production branch: `main`

## 2. ビルド設定

| 項目 | 値 |
|---|---|
| Framework preset | `None` (手動で設定) |
| Build command | `npm install && npx hugo --gc --minify` |
| Build output directory | `public` |
| Root directory | (空でよい) |
| Deploy command (Workers の場合のみ) | `npx wrangler deploy` または空欄 |

> **重要**: Cloudflare Pages の自動インストールは **非 extended 版** の Hugo しか入れないため、Stack テーマ (SCSS を使う) では SCSS ビルドエラーになります。本リポジトリは `package.json` に `hugo-extended` を入れて `npx hugo` 経由でビルドすることで extended 版を使います。

> **Workers Assets (新方式) で公開される場合**: リポジトリ直下の `wrangler.jsonc` が使われ、`public/` を静的アセットとして配信します。Pages ビルドの場合はこのファイルは無視されるので併存して問題ありません。

## 3. 環境変数

Cloudflare Pages → Settings → Environment variables に以下を追加。

| Key | Value | Scope |
|---|---|---|
| `HUGO_ENV` | `production` | Production |
| `GO_VERSION` | `1.22.0` | Production & Preview |
| `NODE_VERSION` | `20` | Production & Preview |

`GO_VERSION` は Hugo Module を解決するために必要です (Stack テーマを Hugo Module 経由で読み込んでいるため)。`HUGO_VERSION` は `package.json` で固定しているため環境変数では指定しません。

## 4. カスタムドメイン (任意)

Pages プロジェクト → **Custom domains** から独自ドメインを接続。接続後、`hugo.toml` の `baseURL` をそのドメインに書き換えてコミットすると、OG タグ・RSS 等のリンクが揃います。

## 5. プレビュー

PR を作ると Cloudflare Pages が自動で Preview URL (`<hash>.vtuber-blog.pages.dev`) を発行する。GitHub Checks に URL が出るので、そこから確認できます。

## トラブルシュート

- **`module not found`**: `GO_VERSION` が未設定の可能性。環境変数を確認。
- **`TOCSS: ... extended version required`**: ビルドコマンドが素の `hugo` になっている。`npm install && npx hugo --gc --minify` に変更。
- **日本語が文字化け**: `hasCJKLanguage = true` が `hugo.toml` にあるか確認 (本リポジトリでは設定済み)。
