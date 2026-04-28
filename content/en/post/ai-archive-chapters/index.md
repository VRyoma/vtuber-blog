---
title: "Add Chapters to Your Stream Archives in Five Minutes with AI"
slug: "ai-archive-chapters"
date: 2026-04-25T10:00:00+09:00
draft: false
description: "Chapters can stretch average view time on long archives. Feed a transcript to AI and get timestamped chapters in about five minutes. Here is the full workflow."
categories:
  - unei-tips
tags:
  - AI
  - archives
  - YouTube
  - timestamps
---

Posting a two-hour archive as-is makes it hard for new viewers to stick around. Long videos get swiped past because "I don't know where to start." Adding chapters by hand takes 30-plus minutes of tedious scrubbing.

This article shows you how to generate **timestamped chapters in about five minutes** by feeding a transcript to AI. Paste the result into your description and watch your average view duration climb.

**What you will learn:**

- Why archives without chapters underperform
- A three-step workflow with a ready-to-paste prompt
- Three metrics that tend to improve after adding chapters

---

## Why Archives Without Chapters Struggle to Grow

YouTube's algorithm rewards watch time. When someone opens a long archive, they skim for the part that interests them. Without chapters, the effort of finding that part is often enough to make them leave.

### With chapters vs. without

Here is how key metrics typically shift when you add timestamps.

| Metric | No chapters | With chapters | Typical change |
|---|---|---|---|
| Average view duration | 15-25% of video | 30-45% of video | +10-20 points |
| In-video click rate | Lower | Higher | Viewers pick their own segments |
| Like rate | 2-4% | 3-6% | "Easy to navigate" shows up in likes |

**Example:** One indie VTuber added chapters to five two-hour zatsudan (free-talk) archives. Average view duration jumped from **18 minutes to 29 minutes** -- a roughly 60% increase. The video length never changed. Viewers simply found the topics they liked and kept watching.

Chapters also show up in search results. If "talking about X" appears in the chapter list, anyone searching for that topic is more likely to click.

---

## Three Steps to Generate Chapters with AI

The workflow is straightforward: transcribe, prompt AI, and fine-tune. Start to finish in under five minutes.

### Step 1: Get a transcript

Run your archive through a Whisper-based tool or use YouTube's built-in caption export.

- **Output format:** plain text (.txt) or SRT
- **Timestamps:** recommended -- they help the AI place chapters accurately
- **File size:** a two-hour stream produces roughly 20,000 to 40,000 characters

Transcription itself is outside the scope of this article. Free options include local Whisper, Aiko (Mac), and Speechnotes (browser).

### Step 2: Send the prompt

Paste the transcript into ChatGPT or Claude, then send the prompt below. Copy it as-is.

**Chapter generation prompt:**

```
Below is a transcript of a VTuber stream archive.
Read it and create a chapter list (table of contents) for the video.

Rules:
- Split into 5 to 10 chapters
- Format each start time as 0:00
- Keep each chapter title under 15 characters and descriptive
- Include intro and outro chapters if they exist
- Output in a format I can paste straight into a YouTube description

Output format:
0:00 Intro and greetings
5:23 Topic A
...

Transcript:
[Paste your transcript here]
```

The AI detects topic changes and proposes chapters. Even for a two-hour stream, you will get results in **30 seconds to one minute**.

**Sample output:**

```
0:00 Intro - today's stream theme
2:15 Something funny that happened recently
8:40 Viewer Q&A corner
22:05 First impressions of a new game
48:30 Chat - what I am into lately
1:05:12 Singing corner starts
1:32:00 Announcing upcoming stream plans
1:42:18 Outro and wrap-up
```

### Step 3: Fine-tune in five minutes

AI output lands at around 90% accuracy. Check three things and you are done.

1. **Verify timestamps in the player** -- they can drift 5 to 10 seconds. Spot-check three or four chapter starts.
2. **Rewrite chapter names in your voice** -- AI tends to write bland labels like "Discussion about X." Change them to something viewers want to click, like "Rage-quit montage."
3. **Keep chapters under 10** -- too many defeats the purpose. Five to eight is the sweet spot.

This adjustment takes about **five minutes**. Compare that to 30 minutes of manual timestamping and you have cut the work to one-sixth.

---

## Three Metrics That Shift After Adding Chapters

Once your chapter list is ready, paste it into the YouTube description. Here are three numbers worth watching.

### 1. Average view duration

Chapters let viewers jump to what interests them, which reduces drop-off. Some viewers also discover the next chapter looks interesting and keep watching.

**Example:** A 90-minute utawaku (singing stream) archive gained chapters and average view duration rose from **12 minutes to 21 minutes**. Viewers who came for one song ended up staying for the surrounding songs too.

### 2. Click-through rate (CTR)

YouTube displays chapters in search results and suggested videos. Viewers can see at a glance what your video covers, which makes them more likely to click.

**Example:** One streamer saw archive CTR climb from **3.2% to 4.8%** after adding chapters. The increase came mostly from search traffic, where chapter keywords matched what viewers were looking for.

### 3. Likes and comments

Comments like "thanks for the chapters" and "please keep doing this" tend to increase. Like rate edges upward as well. Viewers notice when a video is easy to navigate.

**Example:** In a month where five archives received chapters, **likes rose roughly 30% compared to the previous month**. Other factors played a role, but multiple "so much easier to revisit" comments suggested the chapters contributed.

---

## Wrapping Up

- Feed a transcript to AI and get **timestamped chapters in about five minutes**.
- Spend another five minutes verifying timestamps and rewriting chapter names.
- Pasting the result into your description can improve **average view duration, CTR, and likes**.

**Try it today:** Open your latest archive, copy YouTube's auto-generated captions as text, paste them into the prompt above, and send it to your AI of choice. Spot-check three timestamps, then paste the list into your description. Watch your analytics over the next few streams.

---

*Related*

- [Let AI Find Your Clip Highlights in Five Minutes](../ai-clip-highlight-finder/) -- run this alongside chapter generation and get both chapters and clip candidates from one transcript.
- [Five Ways to Repurpose a Single Archive](../repurpose-archive-5-contents/) -- chapters are just the start. Here are more content ideas that start from an archive.
