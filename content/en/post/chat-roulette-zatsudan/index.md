---
title: "Spin the Wheel: Never Run Out of Things to Say on Stream"
slug: "chat-roulette-zatsudan"
date: 2026-04-04T10:00:00+09:00
draft: false
description: "Add a spinning wheel to OBS and let it pick your chat topics. Includes 30 ready-to-use prompts and hosting tips."
categories:
  - haishin-neta
tags:
  - small-talk
  - audience-participation
  - OBS
  - first-time-viewers
---

Every streamer knows the feeling. Chat slows down, your mind goes blank, and you catch yourself thinking, "What do I talk about next?"

Regulars will sometimes carry the conversation, but on nights with lots of newcomers, silence creeps in fast.

That's where a **chat roulette wheel** helps. Drop it into OBS as a browser source, spin it, and the topic picks itself.

**What you'll learn**

- Why "zatsudan" (free-talk streams) stall and how to outsource topic selection
- 30 ready-to-use prompts in 3 tiers
- How to set it up in OBS and keep the flow going

---

## Why picking your own topic kills the momentum

Silence on stream usually isn't about running out of things to say. It's about **choosing which thing to say** — that split-second hesitation is the real conversation killer.

Here are the three patterns that cause dead air.

| Pattern | What happens | What's really going on |
|---|---|---|
| Too many options | You have ideas but can't pick one | Decision fatigue |
| Chat went quiet | A comment lull = instant silence | You're reacting, not driving |
| Self-censoring | "Is this interesting? Is it okay?" | Overthinking kills the vibe |

Every pattern traces back to one thing: the cost of choosing. Remove that cost and the conversation flows on its own.

### Outsource the choice to a wheel

Instead of picking a topic yourself, let the wheel decide. The moment you swap "I have to choose" for "the wheel chose," the mental load drops hard.

**Before (you choose)**
> "Okay, what next... oh, I could talk about yesterday... nah, is that boring...?"
> (5 seconds of dead air)

**After (the wheel chooses)**
> "Alright, spinning the wheel! It landed on 'best thing you bought recently.' Okay, I got this electric toothbrush last week and it changed my life."

---

## How it works and what you need

A chat roulette is just a **browser-based spinning wheel displayed through an OBS browser source**. That's it.

You need three things:

1. **A free wheel tool** (Wheel of Names works great)
2. **OBS** (for the browser source)
3. **A prompt list** (use the one in this article)

There are three ways to spin:

| Method | How | Best for |
|---|---|---|
| Manual | You click the button | Small crowds, laid-back vibes |
| Chat command | Viewers type `!spin` | When you want more interaction |
| StreamElements | Bot triggers the wheel | Established communities |

Start with manual. It's the most reliable while you're getting used to the flow.

---

## 30 prompts in 3 tiers

Mix and match based on the room's energy. Having "light," "deep," and "today-only" layers means you're ready for anything.

### Tier 1: Icebreakers (light, 10 prompts)

Anyone can answer these in under a second. Use them right after going live or on nights with lots of new viewers.

1. Favorite season?
2. Go-to drink lately?
3. Dogs or cats?
4. Favorite color?
5. Last thing that made you laugh?
6. What do you do before falling asleep?
7. Go-to convenience store snack?
8. One thing you really want right now?
9. Best recent purchase?
10. Favorite ice cream flavor?

### Tier 2: Go a little deeper (10 prompts)

These are about you, the streamer. Mix them in once regulars start sticking around.

1. What made you start streaming?
2. Childhood dream?
3. Scariest thing that ever happened to you?
4. Best comment you've ever received on stream?
5. Something you want to try but haven't yet?
6. An anime you loved growing up?
7. A hobby outside of streaming?
8. A motto or phrase you live by?
9. Longest-running hobby?
10. Where do you see yourself in 5 years?

### Tier 3: Today-only (realtime, 10 prompts)

These change every stream because they're about right now. They stay fresh no matter how many times you reuse the list.

1. Today's mood as a weather forecast?
2. Name one thing you can see from where you're sitting.
3. Best moment on stream today so far?
4. What are you eating after this?
5. What's your phone wallpaper right now?
6. Rate today out of 10.
7. A news story catching your eye?
8. What's on your schedule tomorrow?
9. Brag about one thing you did today.
10. What's sitting next to you right now?

A good mix for a one-hour free-talk stream: pick 4 light + 3 deep + 3 today-only = 10 prompts total. That's enough to fill the whole hour.

---

## Setting up the wheel in OBS

Here's how to do it with Wheel of Names. Setup takes about five minutes.

### Step 1: Enter your prompts

1. Open Wheel of Names in your browser.
2. Type each prompt on its own line in the left panel.
3. Tweak the colors and font to match your channel's vibe.

### Step 2: Add a browser source in OBS

1. In OBS, add a new **Browser** source.
2. Paste the Wheel of Names URL into the URL field.
3. Set the size to roughly 800 x 600.
4. Leave "Local file" unchecked and hit OK.

### Step 3: Position it on screen

Place the wheel where it won't block your main content — usually a corner.

| Position | Suggested size | Works well for |
|---|---|---|
| Bottom-right | 300 x 300 | Gaming or work streams |
| Bottom-left | 300 x 300 | If your camera is on the right |
| Center | 600 x 600 | Pure free-talk streams |

Create a dedicated OBS scene for free-talk mode. That way you can switch from your game scene and the wheel is already there.

### Step 4: Save the URL

Wheel of Names turns your customized wheel into a shareable link. Bookmark it so you can reload the same wheel next time without re-entering anything.

---

## Hosting tips for when the wheel is live

Just having the wheel on screen isn't enough — you might forget to spin, or brush past the result too quickly. Here are three tips to make it work.

### Tip 1: The "one minute per prompt" rule

Commit to talking about whatever the wheel lands on for at least **one full minute**. If you still have more to say after that, keep going. When you run dry, spin again.

> "It landed on 'go-to drink lately.' Okay, I've been on a huge latte kick. Every morning I grab a matcha latte from the convenience store — the less-sweet kind, you know? Last week I tried a different brand and..."

A tiny prompt can carry a surprisingly long riff.

### Tip 2: Let viewers add their own prompts

When you accept topic suggestions from chat, the stream becomes participatory by nature. Say something like this at the start:

> "We're doing the chat wheel today! Drop your prompt ideas in chat and I'll add the best ones to the wheel."

Viewer-submitted prompts tend to be things you'd never think of yourself. That unpredictability is what makes it fun.

### Tip 3: Don't spin too fast

Rapid-fire spins feel rushed. You end up skimming topic after topic without actually talking about any of them. Aim for **2-3 minutes of conversation per spin**.

For a one-hour free-talk stream, 15 to 20 spins is a comfortable pace.

---

## Wrapping up

- Dead air comes from the cost of choosing, not a lack of topics — let the wheel handle it
- Stock three tiers of prompts (light / deep / today-only) and you'll never be stuck
- Setup is just an OBS browser source pointing at a URL — try it tonight

Start with just the 10 icebreaker prompts. One spin and you'll notice the silences shrink fast.

> **Related** — [Five Chat Openers That Help New Viewers Settle In](../ice-breaker-intro-5min/) — Templates for the first five minutes of any stream.
