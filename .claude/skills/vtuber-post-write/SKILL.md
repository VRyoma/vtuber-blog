---
name: vtuber-post-write
description: Use this skill when the user wants to write a full VTuber blog post — triggers include "記事を書いて", "この案で書いて", "/vtuber-post-write", specifying a slug from an earlier idea list, or asking for a complete article draft. Produces outline → body → Hugo front matter and saves to content/ja/post/<slug>/index.md.
---

# VTuber ネタ帳 — 記事執筆

構成 → 本文 → Hugo ファイル保存までを 1 スキルで完結させる。
途中で **必ずユーザに構成の承認を取る** ため、勝手に長文を書き切らない。

## 起動条件

- 「この案で記事書いて」「〈slug〉で書いて」
- `vtuber-post-ideas` からの案を指定されたとき
- `/vtuber-post-write` が入力された

## 事前準備

1. `CLAUDE.md` を Read
2. 指定 slug の既存ファイル `content/ja/post/<slug>/index.md` が無いことを確認 (上書き防止)
3. 参考として類似カテゴリの既存記事を 1 本 Read してトーンを揃える

## 入力

| 項目 | 必須 | 備考 |
|---|---|---|
| slug | ✅ | kebab-case 英数字 |
| カテゴリ | ✅ | `haishin-neta` / `game-ideas` / `utawaku` / `unei-tips` の 1 つ |
| 読者の悩み | ✅ | 1 行 |
| 核になる価値 | ✅ | 1 行 |
| 希望の長さ | 省略可 | 既定 3,000 字前後 |
| 英語版も作るか | 省略可 | 既定は作らない。作る場合は Phase 4 へ |

不足があれば `AskUserQuestion` で確認してから Phase 1 に入る。

## Phase 1 — 構成案の提示 (ユーザ承認必須)

以下をチャットに出力する:

```markdown
## タイトル案
1. 〜
2. 〜
3. 〜

## リード (150〜300 字・下書き)
…

## H2 構成
### H2-1: 〜
- 核心: 〜 (1 行)
- H3-a / H3-b
- 具体例の型: 数字リスト / ステップ / ミニ対話

### H2-2 …

## まとめの要点 3 つ
- 〜
- 〜
- 〜
```

そのあと `AskUserQuestion` で:
- どのタイトルを採用するか
- 構成のまま進めてよいか / 修正希望があるか

を確認する。**承認が取れるまで本文を書かない。**

## Phase 2 — 本文執筆

CLAUDE.md の「声・文体」「本文の長さ目安」「記事の型」に厳密に従う。

**必須要件**:
- 一文 60 字以内目安
- 各 H2 に数字入りの具体例が最低 1 つ
- 「〜が重要です」で段落を締めない → 必ず直後に「具体的には〜」を続ける
- CLAUDE.md の「やらないこと」を遵守

**推奨**:
- H2 の中で小さなテーブル / 箇条書きを 1 つ以上使う (読みやすさ)
- コードブロックが似合う箇所 (OBS 設定、CSV、コマンド等) では遠慮しない
- リード末尾に「この記事で分かること」を箇条書き 3 つ

## Phase 3 — Hugo ファイル作成

1. ディレクトリ作成: `content/ja/post/<slug>/`
2. `index.md` を Write。フロントマター例:

```yaml
---
title: "採用したタイトル"
slug: "<slug>"
date: 2026-04-17T10:00:00+09:00  # 実行時刻 (JST, ISO 8601)
draft: false
description: "<120 字以内の要約>"
categories:
  - <カテゴリ>
tags:
  - <2〜5 個>
---
```

3. 本文を挿入
4. `hugo --gc --minify` を実行して warning/error 0 を確認
5. ユーザへの報告:
   - 保存 path
   - ワードカウント
   - プレビュー URL: `https://vtblog.vvil.jp/p/<slug>/`
   - カバー画像を置く場所の案内: `content/ja/post/<slug>/cover.jpg`

## Phase 4 (任意) — 英語版

ユーザが「英語も作る」と言った場合のみ実行:

1. `/vtuber-post-translate` スキルに委譲することを推奨
2. 直接書く場合は `content/en/post/<slug>/index.md` に保存し、**直訳を避け**リライト

## 禁止

- プレースホルダ (「ここに具体例を入れる」「TBD」) のまま保存
- 未確認情報・噂の記述
- 個別 VTuber / 事務所への批評
- 実在 VTuber 名の許可なき引用
- Phase 1 の承認を取らずに Phase 2〜3 を実行

## 失敗時の挙動

- `hugo --gc --minify` が失敗した場合は、エラー内容を貼って修正案を提示する。**ファイルは残したまま** ユーザに相談する
- 既存 slug と衝突したら、別 slug 候補を 3 つ提示してユーザに選ばせる
