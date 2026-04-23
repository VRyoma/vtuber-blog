---
title: "Tame Your OBS Scenes — Switch in Under 3 Seconds"
slug: "obs-scene-switch-3sec"
date: 2026-04-05T10:00:00+09:00
draft: false
description: "Clean up your OBS scenes and sources so you can switch with a single hotkey in under three seconds."
categories:
  -unei-tips
tags:
  - obs
  - streaming-setup
  - hotkeys
  - source-organization
---

Ever panicked mid-stream because you forgot to swap the BGM or missed the right scene?

When your OBS scene list keeps growing, finding the one you need takes a few seconds too long. That kills your pacing, and you stop reading chat. Stream quality drops without you noticing.

This guide shows you how to tidy up scenes and sources so you can **switch with one hotkey in under three seconds**.

**What you will learn:**
- How to cut your scene list down to seven or fewer
- Hotkey assignments that actually work during a live stream
- Concrete settings that prevent common switching mistakes

---

## Why you end up with too many scenes — and why seven is the limit

Over time you add a scene for every new stream idea, a special one for collabs, a test scene here and there. Before long you are staring at ten or more.

Once you pass ten scenes, **finding the right one takes two to three seconds**. During a live stream that is enough time to miss a comment or sit in dead air.

### How to trim down to seven scenes

List every scene you have right now. Split them into "use every week" and "use once a month or less."

**A solid seven-scene setup:**

| # | Scene | Purpose |
|---|---|---|
| 1 | Standby | "Starting soon" screen before and after streams |
| 2 | Game | Main game capture |
| 3 | Chat | Camera-focused zatsudan (free-talk) layout |
| 4 | Singing | Audio source + character art for utawaku (singing streams) |
| 5 | Break | BRB (be-right-back) screen |
| 6 | End | "Thank you for watching" screen |
| 7 | Screen Share | Collab and Discord screen-share layout |

For scenes you use less than once a month, create them when needed and delete them after the stream. One shared "Screen Share" scene covers most collab setups without needing per-partner scenes.

### Before and after

**Before (12 scenes):**
Collab A, Collab B, Game 1, Game 2, Chat, Singing, Break, End, Standby, Announcement, Test, Screen Share

**After (7 scenes):**
Standby, Game, Chat, Singing, Break, End, Screen Share

"Announcement" becomes a source you toggle inside the Chat scene. "Test" lives in a separate OBS profile. That gets you to seven.

---

## Kill duplicate sources with shared (linked) references

Now that scenes are sorted, fix **source duplication**.

If you copy-pasted the same camera frame or text overlay into every scene, you already know the pain. Change the BGM volume once and you are fixing it in five places.

### Common duplicates

- **Camera frame** — same position and size in almost every scene
- **BGM source** — reused across Standby, Break, and End
- **Name and social links** — fixed in a corner at all times

Turn these into shared sources and **you edit once, every scene updates**.

### How to link sources across scenes

1. Right-click a source you want to share
2. Copy it, switch to another scene, and pick **"Paste (Reference)"**
3. Edit the original and all linked copies update instantly

```
Example: Create your camera frame in the Chat scene
  -> Paste (Reference) into Game and Singing scenes
  -> Need to reposition? Edit it once in Chat — done
```

**Important:** Regular "Paste" creates an independent copy. Changes to one will not affect the other. Always use "Paste (Reference)" when you want linked behavior.

---

## Assign hotkeys and switch in under three seconds

Scenes and sources are clean. Now set up **one-keystroke switching** so you stop reaching for the mouse mid-stream.

### Recommended hotkey layout

| Action | Key | Why |
|---|---|---|
| Scene: Standby | F1 | Left edge, easy to hit |
| Scene: Game | F2 | High-frequency scene, keep it close |
| Scene: Chat | F3 | Same |
| Scene: Singing | F4 | Same |
| Scene: Break | F5 | Used every stream |
| Scene: End | F12 | Far from the rest to avoid accidents |
| Mute mic | Ctrl+M | One-hand shortcut |
| Mute desktop audio | Ctrl+D | One-hand shortcut |

### Setup steps

1. Open OBS Settings and go to Hotkeys
2. Scroll to the "Switch to scene" section
3. Click each input field and press the key you want to assign
4. Click OK to save

F6 through F11 tend to clash with other software. The F1 through F5 plus F12 combo avoids most conflicts. If you are playing a game that captures function keys, fall back to Ctrl+number or Alt+number instead.

### No Stream Deck? Use your phone

No Elgato Stream Deck? No problem. Free apps like OBS Remote or Streamlabs Remote turn your phone into a scene-switch controller. Lay your phone next to your keyboard and swap scenes without touching the mouse.

---

## Three tricks to prevent switching mistakes during a stream

Even with everything set up, slip-ups happen live. Here are three **preventive settings** that catch common errors before they reach your viewers.

### 1. Number your scene names

By default OBS sorts scenes alphabetically, which shifts things around every time you rename one. Add a number prefix and the list stays fixed.

```
01_Standby
02_Game
03_Chat
04_Singing
05_Break
06_End
07_ScreenShare
```

A fixed order makes it easier to remember which hotkey maps to which scene.

### 2. Prevent "forgot to unmute" with the audio mixer

Switching scenes and talking with the mic still muted is a classic mistake. The fix: **control muting through the audio mixer, not per-source toggles.**

- Toggle your mic with a dedicated hotkey (Ctrl+M)
- Enable "keep mute state across scenes" in OBS Settings, Audio, Advanced
- Before going live, confirm the mic is unmuted

### 3. A three-item pre-stream checklist

Run through this before every stream. It takes 30 seconds and catches most issues.

| # | Check | How |
|---|---|---|
| 1 | Mic is unmuted | Watch the audio mixer bar for movement |
| 2 | Starting scene is Standby | Confirm "01_Standby" is selected |
| 3 | Hotkeys work | Press F3 then F2 and verify the switch |

Add it to your go-live routine and switching errors drop sharply.

---

## Recap

- Keep scenes at **seven or fewer** — delete anything you do not use weekly
- Use **Paste (Reference)** for shared sources so you edit once, not five times
- Assign **hotkeys** so every switch is one keystroke, zero mouse hunting

Before your next stream, review your scene list. Keep the seven you actually use and cut the rest. That alone gives you more headroom to focus on chat and content instead of OBS menus.
