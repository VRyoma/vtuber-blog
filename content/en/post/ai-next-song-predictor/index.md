---
title: "Let AI Predict Your Next Song from Viewer Reactions"
slug: "ai-next-song-predictor"
date: 2026-04-29T10:00:00+09:00
draft: false
description: "Feed your past karaoke stream data into AI and get data-backed next-song suggestions. Includes a copy-paste prompt and a decision flow for combining AI picks with chat requests."
categories:
  - utawaku
tags:
  - AI
  - karaoke
  - song-selection
  - audience-analytics
---

Midway through a karaoke stream (utawaku -- a stream where you sing songs for your audience), the comments slow down and you freeze: "What should I sing next...?"

Requests dry up, archive views plateau, or new viewers suddenly pour in. Any of these can leave you second-guessing your song choice. The good news: if you feed your past stream data to an AI, it can suggest the next song with real evidence behind it.

What you will learn in this post:

- Three moments when song selection stalls and why
- A copy-paste AI prompt that predicts your best next song from past reaction data
- A decision flow that combines AI suggestions with live chat requests

---

## 1. Three Moments When Song Choice Stalls

If you rely on gut feeling alone, these three situations slow you down every time.

| Moment | Timing | What happens |
|---|---|---|
| Mid-stream slump | 30-45 minutes in | Requests have cycled through; you run low on candidates |
| Encore pick | Right before ending | You cannot decide on the final song |
| Viewer spike | Concurrent viewers jump suddenly | You are unsure what will keep the new viewers around |

### Moment 1: Mid-stream, requests dry up

About 30 minutes in, the initial flood of requests fades. Your candidate list shrinks, and you spend longer picking the next track.

Picture this: you have five songs left and you just sang two high-energy tracks back to back. You want tempo but your throat needs a break. If you could quickly find a song that performed well at this same point in past streams, you could decide in under 30 seconds.

### Moment 2: Picking the encore

You say "One more song!" and then go silent trying to pick one. Fifteen seconds of dead air is enough to kill the momentum you built.

**Example:** Looking back at your last five karaoke streams, encore ballads averaged 18 comments. Upbeat encore tracks averaged 12. That data gives you a clear reason to go with a ballad tonight.

### Moment 3: A sudden viewer spike

After a collab ends or a clip goes viral, your concurrent viewers jump. Now you are wondering which songs will match these new listeners' tastes.

New viewers often decide whether to follow you within the first one or two songs. If you know which tracks have driven follows right after past viewer spikes, you can pick with confidence.

**Example:** Over three past viewer-spike moments, well-known cover songs (one million+ views on YouTube) averaged 22 comments each. Niche tracks averaged 8. Familiar songs win with new audiences.

---

## 2. Two Steps to Get AI-Powered Song Predictions

Feed the AI data on which songs pulled comments and which songs lost concurrent viewers. It will suggest your next song backed by numbers.

### Step 1: Organize your past reaction data

Pull comment counts from YouTube Studio and note concurrent-viewer changes from your archives. Three to five streams is enough to spot patterns.

Record four things for each song:

1. **Song title and artist**
2. **Position in the set** (which song number)
3. **Comment count** during that song
4. **Concurrent viewer change** (up / flat / down)

Format it like this:

```
[Apr 12 karaoke stream (60 min, 12 songs)]
1. Idol / YOASOBI -- 18 comments -- viewers +12
2. Marigold / Aimyon -- 22 comments -- viewers +5
3. Zankyou Sanka / Aimer -- 9 comments -- viewers -3
4. Yoru ni Kakeru / YOASOBI -- 25 comments -- viewers +15
...
```

You can find comment counts and concurrent viewer data in YouTube Studio under Analytics > Engagement. Open each archive and note the timestamps so the song order is accurate.

### Step 2: Send the prompt to an AI

Combine your data with your current stream situation and paste the prompt below into ChatGPT or Claude. Replace the `[ ]` sections with your own info.

```
You are a karaoke stream song-selection advisor.
Based on the past reaction data and current situation below,
suggest the top 5 songs the streamer should sing next.

[Past reaction data]
[Paste the text you prepared above]

[Current situation]
- Time elapsed: [e.g., 35 min]
- Time remaining: [e.g., 25 min]
- Songs sung so far: [e.g., Idol, Marigold, Zankyou Sanka]
- Current concurrent viewers: [e.g., 85]
- Chat vibe: [e.g., comments are light but stamps are frequent]
- Candidate songs: [e.g., Yoru ni Kakeru, Usseewa, Shape of Love,
  Kakurenbo, Shinunoga E Wa, Kaikai Kitan]

Output format:
1. Top 5 song suggestions (ranked)
2. Reason for each pick (which past-data trend supports it)
3. Predicted reaction (estimated comments and viewer change)
4. Any recommended key changes
5. Engagement rate for each candidate (comments / concurrent viewers)
```

### Sample output

The AI might come back with something like this:

1. **Yoru ni Kakeru / YOASOBI** -- 25 comments and +15 viewers when sung mid-stream in the past. Strongest track record among your candidates.
2. **Kaikai Kitan / Eve** -- Upbeat and tends to raise stamp activity during low-comment stretches.
3. **Shape of Love / SEKAI NO OWARI** -- Performed well after ballads in past streams. A good ramp-up from the current calm vibe.
4. **Kakurenbo / Yuuri** -- High new-viewer retention rate. Solid pick when viewer count is flat.
5. **Usseewa / Ado** -- Predicted 15-20 comments and +8-12 viewers. Reliable peak, but given remaining time, it may work better one song later.

Each suggestion comes with a data-backed reason, so you are not choosing at random.

---

## 3. Combining AI Picks with Live Requests

Taking the AI suggestion as-is works, but real streams bring live requests too. Here is a three-step process to blend both.

### Step 1: Check the AI top 3

Before or during the stream, look at the top three AI suggestions so they are fresh in your mind.

### Step 2: Branch by whether a request came in

Use this text-based decision flow:

```
Step 1: Review the AI top 3
    |
    +-- A request came in
    |       |
    |       +-- The requested song is in the AI list
    |               --> Sing it (data and viewer enthusiasm match)
    |
    |       +-- The requested song is NOT in the AI list
    |               --> Check its past engagement rate
    |               Above average? Sing it. Never sung before? Treat it as a trial pick.
    |
    +-- No request
            |
            +-- Go with the AI #1 pick
                --> But if the genre or tempo repeats the last song, swap to #2
```

### Step 3: Walk through an example

**Situation:** 40 minutes in, 20 minutes left, 90 concurrent viewers holding steady.

- AI top pick: Yoru ni Kakeru (25 comments, +15 viewers historically)
- Chat request: Kakurenbo

Kakurenbo ranked fourth in the AI list, so data and viewer energy line up. You can respond right away: "Great request, let's do Kakurenbo!"

If no request came in and you just sang an upbeat track, you might skip the AI's #1 (Yoru ni Kakeru) and go with #2 (Kaikai Kitan) or #4 (Kakurenbo) for a tempo shift. The flow makes that call natural.

### How to calculate engagement rate

Engagement rate = comment count divided by concurrent viewers. Calculate this for each song in your past data and you get a baseline for comparing AI picks against requests.

Formula: `engagement rate = comments / concurrent viewers`

Example: 20 comments with 80 concurrent viewers gives a rate of 0.25. If your stream average is 0.20, any song at 0.25 or above is a strong pick.

Add line 5 in the prompt output format ("Engagement rate for each candidate") and the AI will return these numbers alongside its suggestions.

---

## Wrap-up

- Song selection stalls most often at the **mid-stream slump, encore, and viewer-spike** moments. Gut feeling alone slows you down in all three.
- Feed three to five past streams into the AI and it will **suggest your next song backed by comment and viewer data**. The copy-paste prompt lets you start right now.
- Compare AI picks with live requests using **engagement rate**, and you get a choice that fits both the data and the room.

**Your three-minute action for tonight:** Open YouTube Studio, pull the song titles, comment counts, and concurrent viewer changes from your last three karaoke archives, and paste them into the prompt above. You will have a data-backed song advisor ready for your next stream.

---

*Related: [Build a Karaoke Stream Setlist in 3 Minutes with AI](/post/ai-utawaku-setlist-assistant/) / [Strategies for Growing with Karaoke Streams](/post/utawaku-growth-strategy/) / [How to Pick the Last Song at Your Karaoke Stream](/post/utawaku-last-song-pick/)*
