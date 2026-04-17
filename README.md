# VTuber ネタ帳 (vtuber-blog)

VTuber 向けの配信ネタ・企画アイデア・歌枠構成・運営Tips を蓄えていくブログ。Hugo + [Stack theme](https://github.com/CaiJimmy/hugo-theme-stack) で構築し、Cloudflare Pages で公開する想定。

## 動作環境

- Hugo **extended** 0.128 以降 (推奨: 0.141.0)
- Go 1.20 以降 (Hugo Module 解決のために必要)
- Git

## セットアップ

```bash
git clone <this repo>
cd vtuber-blog
hugo mod get -u
hugo server -D
```

`http://localhost:1313/` を開くと日本語トップ、`http://localhost:1313/en/` で英語トップが表示される。

## 記事の追加

```bash
# 日本語記事
hugo new --kind post content/ja/post/my-new-idea/index.md
# 英語記事
hugo new --kind post content/en/post/my-new-idea/index.md
```

作成されたファイルの `draft: true` を `false` にすると公開対象になる。カバー画像を置く場合は同じディレクトリに `cover.jpg` などを配置して、フロントマターの `image` で指定する。

### カテゴリ

- `haishin-neta` — 配信ネタ・企画 / Stream Ideas
- `game-ideas` — ゲーム実況アイデア / Gaming Ideas
- `utawaku` — 歌枠・歌ってみた / Singing Streams
- `unei-tips` — 運営・裏方Tips / Creator Tips

## ビルド

```bash
hugo --gc --minify
```

成果物は `public/` に出力される。

## デプロイ

Cloudflare Pages での設定手順は [CLOUDFLARE_PAGES.md](./CLOUDFLARE_PAGES.md) を参照。

## ディレクトリ構成

```
.
├── hugo.toml               # サイト全体設定
├── config/_default/        # 言語・メニュー・モジュール定義
├── archetypes/default.md   # 記事テンプレ
├── content/ja/             # 日本語コンテンツ
├── content/en/             # 英語コンテンツ
├── assets/                 # Hugo Pipes 用 (SCSS 等)
├── static/                 # 素のまま配信する静的ファイル
└── layouts/                # テーマ override 用 (必要なら追加)
```
