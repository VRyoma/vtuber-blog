---
title: "Fix Your Stream Audio Balance in 5 Minutes — OBS Audio Mixer Basics"
slug: "obs-audio-balance-5min"
date: 2026-04-21T10:00:00+09:00
draft: false
description: "Stop getting 'your game audio is too loud' comments. Learn how to set target dB levels for each audio source in OBS and prioritize your voice."
categories:
  - unei-tips
tags:
  - obs
  - audio-levels
  - streaming-setup
  - audio
image: "cover.jpg"
---

Has a viewer ever told you the game sound is drowning out your voice?

What sounds balanced on your end can feel very different to your audience. When game audio overpowers your mic, your commentary gets lost. Viewers who came for the conversation tend to leave.

This article walks you through the OBS audio mixer. You will learn **target dB levels for each audio source and how to prioritize them**. The whole setup takes about five minutes.

**What you will learn:**

- Target dB levels for mic, game audio, and BGM
- Step-by-step adjustment in the OBS audio mixer
- A one-minute archive check you can do after every stream

---

## What Happens When the Balance Is Off — Three Common Complaints

Audio balance is one of those things you do not notice until someone points it out. Your headphones can trick you into thinking everything sounds fine.

Here are three complaints that show up often in comments.

| Complaint | Cause | Effect |
|---|---|---|
| "Game sound is too loud, I can't hear you" | Game volume is higher than the mic | Viewers who prefer chat-focused streams leave |
| "The BGM is distracting while you talk" | BGM is too loud | The calm vibe of a conversation gets undercut |
| "Your volume keeps changing" | Distance to the mic varies | Hard to follow, and can cause clipping |

"Game audio too loud" comes up especially often in FPS and action game streams. Gunshots and explosions spike suddenly, so average volume settings may not be enough.

## Target dB for Each Audio Source — Mic, Game, BGM

The starting point is deciding **what you want viewers to hear most**. For VTuber streams, that should almost always be your voice.

Here are common targets for three audio sources.

| Source | Target dB | Priority | Role |
|---|---|---|---|
| Mic (voice) | -5 to 0 dB | Highest | Main content of the stream |
| Game audio | -15 to -10 dB | Medium | Adds atmosphere |
| BGM | -25 to -20 dB | Low | Fills silence in the background |

Your mic sits at -5 to 0 dB because **your voice is the star**. Game audio should support without competing. BGM should be at a level where viewers barely notice it while you talk.

### How OBS Volume Sliders Map to dB

OBS shows 0-100% sliders in the audio mixer, but internally it uses dB. Here is a rough guide.

| Slider position | Approximate dB |
|---|---|
| 100% | 0 dB (reference) |
| 70-80% | -5 to -3 dB |
| 50% | Around -10 dB |
| 30% | -15 to -12 dB |
| 10-20% | -25 to -18 dB |

These are rough numbers. **Do a test recording in your own setup and listen back.** Mic sensitivity and room acoustics will shift the sweet spot.

## OBS Audio Mixer — Step-by-Step Adjustment

Once you know the target dB, adjust OBS. Follow these five steps in order.

### Step 1: Open the Audio Mixer

At the bottom of the OBS main window you will find the Audio Mixer panel. Your mic, desktop audio (game sound), and BGM sources should be listed there. This is where all the adjustments happen.

### Step 2: Set the Mic as the Loudest Source

Set the mic slider to 80-100%. This is your baseline. Watch the volume meter — it should bounce steadily in the green-to-yellow range. If it stays red, you risk clipping, so lower it a bit.

### Step 3: Lower Game Audio Below Your Voice

Pull the game audio slider down to about 40-50%. With the game running, speak into your mic at a normal volume. Keep lowering until **your voice is clearly louder than the game**. That is your target.

### Step 4: Make BGM Almost Invisible

Set the BGM slider to about 10-20%. While you talk it should feel like it is "sort of there." It should only become noticeable during pauses in conversation.

### Step 5: Record a 30-Second Test and Listen Back

After the sliders are set, **record about 30 seconds of footage**. Run the game, talk into the mic, then play it back. Use earbuds or headphones — balance issues are easier to catch that way.

### Bonus: Fine-Tuning with Advanced Audio Properties

Right-click any source in the audio mixer to open Advanced Audio Properties. From there you can:

- **Volume (%)**: Adjust in 1% increments instead of dragging the slider
- **Audio Monitoring**: Toggle between "Monitor Only" and "Monitor and Output"
- **Downmix**: Switch between stereo and mono

If sudden sounds like gunshots are too loud, add a **Limiter filter** to the game audio source. Right-click the source, choose Filters, and add a Limiter. This caps volume spikes without changing the overall level.

---

## Post-Stream Check — Listen to One Minute of the Archive

After you finish a stream, try this habit: **skip to the middle of the archive and listen for one minute.** This is often enough to catch audio balance problems.

### How to Check

1. Open the archive near the midpoint (around the 30-minute mark)
2. Listen to 30 seconds of gameplay
3. Listen to 30 seconds of zatsudan (free-talk)
4. Compare how your voice and BGM sound in each section

### What to Listen For

| Check | Pass if... |
|---|---|
| Voice is clear | It is not buried under game audio or BGM |
| BGM stays in the background | It does not draw attention while you talk |
| No clipping | Loud moments do not produce harsh crackling noise |
| No awkward silences | The stream does not go completely silent for long stretches |

Use earbuds or headphones for this check. Speakers add bass resonance that can make game audio sound quieter than it really is. Even cheap earbuds give you a more accurate read on balance.

If you find a problem, adjust the relevant slider before your next stream. Change it in **5% increments** — large jumps tend to create new issues.

---

## Quick Recap

- **Prioritize your mic.** Set game audio and BGM low enough that they never compete with your voice.
- Start with **mic at 80-100%, game audio at 40-50%, BGM at 10-20%** and adjust from there.
- After each stream, **listen to one minute of the archive** to keep improving your balance over time.

Before your next stream, glance at the audio mixer sliders and do a quick 30-second test recording. Even checking two things — "is the mic the loudest source?" and "does game audio overpower my voice?" — is worth the effort.
