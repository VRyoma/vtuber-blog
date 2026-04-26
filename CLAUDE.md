# Virtual Village — 執筆ガイド

このリポジトリは Hugo で作る VTuber 向けのネタ共有ブログです。
Claude Code で記事を書くときは **このドキュメント** と `.claude/skills/` のスキル定義に従ってください。

## サイト基本情報

- **タイトル**: Virtual Village
- **URL**: https://vvil.jp/
- **言語**: 日本語メイン / 英語併設 (英語は任意。質の高い日本語を優先)
- **スタック**: Hugo (extended) + hugo-theme-stack v3 / Cloudflare Workers Assets

## 読者像

- 週 3〜5 回配信している個人勢 VTuber が中心
- 登録者 1,000〜50,000 人規模
- プログラミングは不得意だが OBS / Streamlabs / VTuber Studio は使える
- 「今日すぐ使えるネタ」を探しに来ている
- 副次的読者: デビュー予定者、裏方・マネージャー

## 声・文体

- **ですます調**を基本
- **具体的な数字**を入れる (「5 分ごとに」「3 人集めて」など)
- **抽象論で終わらない**。「〜が重要です」で終わらず必ず具体例を添える
- 一方的な断定 (「完全に」「すべて」「絶対」「必ず」) は避ける
- 一文は 60 字以内を目安
- 英語は自然な書き言葉 (カジュアル寄り)。日本語からの直訳は避ける

## やらないこと (編集方針)

- **個別の VTuber や事務所を貶める / 比較評価する**。名指しの是非論は一切書かない
- 未確認情報・噂の掲載
- 主語の大きい表現 (「みんな配信者は〜」「○○勢は〜」)
- 違法・規約違反を誘発する内容 (収益化ガイドライン違反、権利侵害など)
- AI 生成画像を本人写真のように扱う
- 特定サービスへの過度なアフィリエイト誘導

実在 VTuber の公開情報を引用するときは、**企画構造の参考例としてのみ**、肯定的/中立的な文脈で扱う。

## カテゴリ

| slug | 日本語 | English | 扱う内容 |
|---|---|---|---|
| `haishin-neta` | 配信ネタ・企画 | Stream Ideas | 雑談テーマ、参加型、コラボ企画 |
| `game-ideas` | ゲーム実況アイデア | Gaming Ideas | タイトル選定、縛り、切り口 |
| `utawaku` | 歌枠・歌ってみた | Singing Streams | 選曲、構成、機材 |
| `unei-tips` | 運営・裏方Tips | Creator Tips | 技術、SNS、サムネ、収益化 |
| `ai-tips` | AI活用 | AI Tools | ChatGPT/Claude 等の活用法、プロンプト、自動化 |

1 記事 1 カテゴリが原則。複数タグは OK。

## 記事の置き場所

- 日本語記事: `content/ja/post/<slug>/index.md`
- 英語記事: `content/en/post/<slug>/index.md`
- slug は kebab-case 英数字 (例: `ice-breaker-topics-5min`)
- 同じ記事の ja / en は **同じ slug** を使う (Hugo 多言語リンク用)
- カバー画像があれば同じディレクトリに `cover.jpg`

## フロントマター (標準)

```yaml
---
title: "記事タイトル"
slug: "kebab-case-slug"
date: 2026-04-17T10:00:00+09:00
draft: false
description: "120 字以内の記事要約。メタディスクリプションにも使われる。"
categories:
  - haishin-neta
tags:
  - 雑談
  - 初見向け
image: "cover.jpg"  # あれば
---
```

## 本文の長さ目安

- 通常記事: **2,500〜4,000 字**
- 深掘り解説: 5,000〜7,000 字
- ネタリスト系 (箇条書き主体): 2,000〜3,000 字

## 記事の型 (推奨)

1. **リード (150〜300 字)** — 読者の「困った」を 1 行で描写 → この記事で得られるもの
2. **本文 (H2 × 3〜5)** — 各 H2 に「何を / どうやって / 具体例」を必ず 1 セット
3. **まとめ** — 要点 3 つを箇条書き → 関連記事への導線 (あれば)

## 画像・素材

- カバー画像は 1200×630 以上を推奨 (OGP 用)
- 本文中画像は `image.png` `image2.png` のように同じディレクトリに置き、相対パスで参照

## ビルド / 公開フロー

```bash
hugo --gc --minify                          # ビルド確認
hugo server -D                              # ローカル確認 (draft 含む)
git checkout -b content/<slug>              # 記事用ブランチ
git add content/ja/post/<slug>/ && git commit -m "Add post: <title>"
git push -u origin content/<slug>           # PR → main マージで自動デプロイ
```

## スキル一覧

| コマンド | 役割 |
|---|---|
| `/vtuber-post-ideas` | カテゴリ指定で記事アイデアを 10 個生成 |
| `/vtuber-post-write` | 構成→本文→Hugo ファイル保存まで一気通貫 |
| `/vtuber-post-translate` | 既存の日本語記事を英語にリライト |
| `/vtuber-post-polish` | 下書き記事を公開品質までブラッシュアップ |
