---
name: vtuber-post-translate
description: Use this skill when the user wants to translate an existing Japanese VTuber blog post to English — triggers include "〈slug〉を英訳して", "この記事を英語にも", "/vtuber-post-translate". Rewrites (does not direct-translate) the post to natural English and saves to content/en/post/<slug>/index.md.
---

# VTuber ネタ帳 — 英訳 (リライト)

日本語記事の英語版を作るスキル。**直訳ではなく、英語話者に刺さるリライト**が前提。

## 起動条件

- 「〈slug〉を英訳して」
- 「この記事を英語にも」
- `/vtuber-post-translate` が入力された

## 事前準備

1. `CLAUDE.md` を Read
2. `content/ja/post/<slug>/index.md` を Read
3. 既存の `content/en/post/<slug>/index.md` が無いことを確認 (上書き防止)
4. 参考に既存英語記事 (`content/en/post/hello-vtuber/index.md` 等) をざっと眺めてトーンを合わせる

## 入力

| 項目 | 必須 | 備考 |
|---|---|---|
| slug | ✅ | 日本語版と同じ slug を使う |
| トーン指定 | 省略可 | "casual" / "neutral" / "practitioner" など |

## 手順

### 1. メタ情報の書き換え

フロントマターは下記のみ書き換える。`slug` `date` `categories` `image` は**そのままコピー**。

| フィールド | 扱い |
|---|---|
| `title` | 英語の自然な言い回しにリライト。直訳 ✕ |
| `description` | 英語で書き直し。120 字目安 |
| `tags` | 英語タグに置換 (例: `雑談` → `small-talk`, `初見向け` → `first-time-viewers`) |

### 2. 本文のリライト方針

- **直訳しない**。同じ主旨を英語話者が書くならどう書くかで書き直す
- 日本語より **10〜20% 短めでよい** (日本語の冗長さを削る)
- **日本固有の配信文化**は最初に 1 行の補足を入れる:
  - スパチャ → "Super Chats (paid highlighted comments)"
  - 同時視聴 → "sync-watch streams (watching a movie together on-stream)"
  - 歌枠 → "karaoke streams"
  - 箱/事務所 → "VTuber agencies"
- 見出しレベル (H2/H3) は揃える

### 3. 保存と検証

1. `content/en/post/<slug>/index.md` に Write
2. `hugo --gc --minify` を実行。warning 0 / error 0 を確認
3. ユーザ報告:
   - 保存 path
   - ワードカウント
   - プレビュー URL: `https://vtblog.vvil.jp/en/p/<slug>/`
   - 日本語版との差分サマリ (短くした箇所、追加した文化脚注)

## スタイル指針 (英語)

- 一文は 20〜25 語を目安
- 能動態を優先
- カジュアル寄りだがふざけすぎない (ブログとしての信頼感を保つ)
- 「you」で読者に語りかけてよい
- 絵文字は使わない
- "literally", "basically", "actually" などのフィラーは削る

## 禁止

- 機械翻訳そのまま貼る
- 日本語版の文化脚注を英語で落とす
- CTA 文言を日本語版からコピーしたまま (例: 「最後まで読んでいただきありがとうございました」の直訳)
- 日本語の固有表現 (推し活、同接) をローマ字のまま放置
