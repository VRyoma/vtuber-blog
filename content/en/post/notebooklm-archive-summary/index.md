---
title: "Summarize Your Stream Archive with NotebookLM"
slug: "notebooklm-archive-summary"
date: 2026-05-03T10:40:00+09:00
draft: false
description: "Scrubbing through a 3-hour VOD to find the highlights takes just as long as the stream itself. Load the transcript into NotebookLM and ask it to pull clips, moments, and next-stream ideas in minutes."
categories:
  - ai-tips
tags:
  - ai-tools
  - notebooklm
  - stream-archive
  - transcription
  - time-saving
image: "cover.jpg"
---

Watching your own VODs (video-on-demand archives) to find the best moments takes as long as the original stream. Most creators skip it entirely — and leave a lot of clip-worthy content on the table.

Google's NotebookLM changes the math. Load your stream transcript, ask a question, and get an answer based only on what was actually said. Clip candidates, highlight moments, next-stream ideas — minutes, not hours.

**What you will learn**

- What NotebookLM is and why it works well for this
- How to get a transcript from YouTube Studio
- A ready-to-use prompt library for different tasks

---

## What NotebookLM is

NotebookLM is a free Google AI tool. You upload documents — PDFs, text files, Google Docs — and then ask questions. It answers strictly from what you loaded, so it's less likely to hallucinate than a general chat AI. "What happened in this stream?" gets you an answer based on your actual transcript, not AI guesswork.

It's been available in Japanese since late 2024, so it handles Japanese stream transcripts well.

---

## Getting your transcript

### From YouTube Studio (easiest)

YouTube automatically generates captions for uploaded VODs. Here's how to download them:

1. Go to **YouTube Studio → Videos** → click the stream
2. Open the **Subtitles** tab → find "Japanese (auto-generated)"
3. Click the three-dot menu → **Download transcript**

Open the downloaded file in any text editor and you'll have timestamped text.

### When auto-captions are inaccurate

Fast speech, regional accents, and game-specific terms trip up the auto-captions. If accuracy matters for a specific VOD, try a dedicated transcription service. CLOVA Note and Notta both handle Japanese gaming content reasonably well on their free tiers.

---

## Loading into NotebookLM

1. Log in at [notebooklm.google.com](https://notebooklm.google.com/) with your Google account
2. Create a **New notebook**
3. Click **Add source** → **Paste text** or **Upload file**
4. Paste the transcript or upload as a .txt file

You can load multiple transcripts into one notebook. Load ten streams from last month and ask cross-stream questions like "What topics got the best viewer reactions across all these streams?"

---

## Prompt library

### Full-stream summary

```
Summarize what happened in this stream as 5 chronological bullet points.
Include timestamps where available.
```

### Clip and short video candidates

```
Pick 3 moments from this stream that could work as a 30-second to 2-minute short clip.
For each one, give your reasoning and the timestamp.
```

### Audience reaction highlights

```
Identify 3–5 moments where the audience reaction seemed especially strong
(laughter, surprise, emotional moments).
```

### Ideas for next stream

```
Based on the viewer comments and reactions in this transcript,
suggest 3 content ideas worth trying in a future stream.
```

### Social post

```
Write a post for X (Twitter) — under 280 characters — that tells people
"here's what happened in this stream" in a way that makes them want to watch the archive.
```

---

## Things to keep in mind

### Transcript quality affects answer quality

If the auto-captions are a mess, the AI answers will be too. For a stream with a lot of game jargon, skim the transcript first and fix obvious errors before loading it.

### Check for personal info before uploading

NotebookLM sends content to Google's servers. Before uploading, make sure the transcript doesn't contain anything you wouldn't want stored externally — addresses, phone numbers, or anything said off-guard.

### Free plan limits

As of 2026, NotebookLM's free tier allows up to 50 sources per notebook and 500,000 tokens per source. For very long streams, either split the transcript or load just the sections you care about.

---

## Summary

- **NotebookLM turns a 3-hour VOD into a 5-minute review session.** Ask for clips, highlights, social posts, and next-stream ideas — all from one transcript
- **YouTube Studio's subtitle download gives you a free transcript in seconds.** Use CLOVA Note or Notta if auto-captions aren't accurate enough
- **Specific prompts get better results.** Tell it what you want the output for — clip, social post, or next-stream pitch — and the answer will be much more usable

---

*Related posts*

- [Write Today's Stream Script in 10 Minutes with AI](/en/p/ai-stream-script-10min/)
- [Run a 15-Minute Weekly Stream Review with AI](/en/p/ai-stream-weekly-analysis/)
