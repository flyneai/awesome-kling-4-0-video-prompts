# Four inherited VideoWeb exercises for Flash testing

Inherited unchanged from VideoWeb AI; these four exercises are not newly authored Flyne AI prompts. [Source history](../docs/UPSTREAM.md).

[Home](../README.md) · [52 upstream recipes](README.md) · [X video examples](../docs/X-VIDEOS.md) · [Test record](../docs/TEST-RECORD.md)

Four original, **recipe-only** briefs written by VideoWeb AI on 29 September 2026. They explore problems highlighted by the X tests linked by the upstream project, with different subjects, actions, dialogue and shot plans. They are not the creators' prompts, reproductions of their clips, or verified Kling results. Use a duration and mode available in your account. 中文读者可先看每条的用途与检查方法；英文代码块可直接复制。

## 1. Label card under a moving light

**Use case:** product lettering inspection / 检查产品文字 · **Format:** 5s, 16:9 · **Best mode:** approved start image, one take.

**Why it works:** A stationary package and one moving light isolate text stability from object rotation. Inspired by the testing problem in [Pan's packaging example](https://x.com/sebatheepan/status/2104653409227829496), not its prompt.

```text
[OUTPUT]
Five seconds, 16:9, one locked-off close shot, natural product photography.
[REFERENCE / ANCHORS]
Use an approved photograph of one cream paper tea pouch as the start frame. Its front carries one dark-blue rectangular label with the exact three-letter word "TEA" supplied in the image. Preserve the pouch outline, paper folds, label size and each letter. The pouch never moves.
[WORLD]
A pale oak tabletop against a soft gray backdrop. No other packages or readable text.
[TIMING / CAMERA]
0–1s: Hold the complete label front-on with generous space around all three letters.
1–4s: A soft rectangular studio light moves slowly from camera-left to camera-right. Only illumination and the pouch's cast shadow change; camera and pouch stay still.
4–5s: Light stops. Hold the final label clearly in focus.
[AUDIO]
Quiet room tone, no speech or music.
[CONSTRAINTS]
No camera movement, letter animation, label redesign, added characters, melted paper edges or duplicated pouch. Keep the whole front label in focus.
```

**Swap ideas:** Use your own short approved label and plain packaging; add exact typography in post-production if generation cannot preserve it.

**Failure check / 检查方法：** 比较第 0、2、4 秒和末帧，逐字核对字母、标签边缘和纸袋形状。通过后再单独测试旋转，不同时增加多个变量。

## 2. Lantern reflection in a ceramic studio

**Use case:** changing light and reflections / 检查光源与反射 · **Format:** 8s, 16:9 · **Best mode:** start image, one take.

**Why it works:** One moving practical light gives the viewer a clear cause for changing highlights. [Pan's low-light test](https://x.com/sebatheepan/status/2104653412738666699) motivates the question; this is not a test of encoded HDR bit depth.

```text
[OUTPUT]
Eight seconds, 16:9, a single medium-wide stationary shot.
[ANCHORS / WORLD]
An adult ceramicist in a plain olive apron stands behind a wooden bench at dusk. A tall glazed blue vase stays on the center of the bench. A warm battery lantern sits to the vase's left. A window behind camera provides weak cool ambient light. Preserve the vase's outline and the person's face and clothing.
[TIMING]
0–2s: The ceramicist takes the lantern by its single handle; the vase remains untouched.
2–5s: Lift the lantern slowly to chest height and move it to the vase's right. The warm reflection travels across the glaze in response to the lantern. The vase's shadow moves in the opposite direction.
5–7s: Place the lantern on the right side of the bench and release the handle.
7–8s: Hold on the stationary lantern, vase and ceramicist.
[AUDIO]
Soft room tone, one quiet handle creak and one gentle placement sound. No dialogue or music.
[CONSTRAINTS]
One lantern, one vase, two hands. No floating light, extra light source, self-luminous vase, exposure flashing, camera movement or changing room layout.
```

**Swap ideas:** First remove the person and move only an off-camera light if hand interaction fails.

**Failure check / 检查方法：** 检查亮斑和影子是否随灯移动；灯放下后应停止变化。网页预览无法证明文件是 10-bit HDR，高动态范围编码需要另查输出文件和平台设置。

## 3. Parcel stamp with a persistent mark

**Use case:** action order and object permanence / 检查动作顺序和结果是否保留 · **Format:** 10s, 16:9 · **Best mode:** one take.

**Why it works:** The final stamped mark visibly records the earlier action. The continuity-testing problem comes from [Pan's sequential-action example](https://x.com/sebatheepan/status/2104653416123551799).

```text
[OUTPUT]
Ten seconds, 16:9, one continuous overhead tabletop shot.
[ANCHORS / WORLD]
A small packing desk in daylight. One blank kraft envelope lies flat at center. One plain rubber stamp with a round handle sits to its right; an open red ink pad is above it. Only an adult worker's two hands enter the frame. The stamp makes one solid red circle, without lettering.
[TIMING]
0–3s: The right hand picks up the stamp and presses its rubber face onto the ink pad once.
3–6s: Lift it, move to the envelope's upper-right corner and press once. The left hand holds the envelope flat without covering that corner.
6–8s: Lift the stamp to reveal one red circle. Set the stamp back to the right of the envelope.
8–10s: Both hands withdraw. Hold on the envelope with its single unchanged red mark, the ink pad and the stamp.
[AUDIO]
Two soft contact sounds at the pad and envelope, then quiet paper rustle. No music or speech.
[CONSTRAINTS]
The red mark appears only after contact and remains until the end. No extra marks, moving ink pad, changing envelope size, disappearing stamp, extra fingers or cuts.
```

**Swap ideas:** Change ink color only; keep layout and sequence identical for comparisons.

**Failure check / 检查方法：** 确认印记在接触后才出现，手移开后仍保留；检查印章有没有凭空消失。动作挤在一起时，先只测试“盖章→抬起→保持”。

## 4. Closing-time umbrella exchange

**Use case:** restrained two-person dialogue / 检查双人对白与道具连续性 · **Format:** 15s, 16:9 · **Best mode:** two character references if supported, three shots.

**Why it works:** Two short lines leave room for a visible decision and silent response. Related testing problem: [Pan's dialogue example](https://x.com/sebatheepan/status/2104653420112032191). This is a separate story, not a shortened version of that scene.

```text
[OUTPUT]
Fifteen seconds, 16:9, three shots, grounded live-action drama with native English dialogue where supported.
[ANCHORS / WORLD]
A quiet flower shop at closing time. Mara, an adult florist in a charcoal apron, stands behind the counter on screen-left. Jo, an adult courier in a tan jacket, stands near the door on screen-right. One closed yellow umbrella rests horizontally on the counter. Rain outside; warm shop light inside. Keep these positions and the umbrella's color stable.
[SHOT 1 / 0–5s]
Static medium two-shot. Jo looks at the rain, then back to Mara. JO, quietly: "I can wait." Mara notices his wet sleeve. Only Jo speaks and moves his mouth during the line.
[SHOT 2 / 5–10s]
Close shot of Mara from Jo's side, staying on the same side of their eyeline. Mara slides the closed umbrella across the counter toward Jo. MARA, warmly: "Take this. Bring it tomorrow." Her hand releases it before Jo takes the handle. Only Mara speaks during her line.
[SHOT 3 / 10–15s]
Return to the initial two-shot. Jo holds the closed umbrella at his side and nods once. Mara resumes tying a plain paper bouquet. Hold the final two seconds. No additional dialogue.
[AUDIO]
Continuous rain outside, quiet shop room tone, one fabric slide and paper rustle. No music, subtitles or narrator.
[CONSTRAINTS]
One yellow umbrella throughout; it never opens indoors. No extra speakers, swapped voices, overlapping dialogue, new people, identity changes, reversed screen positions or object teleportation.
```

**Swap ideas:** Replace both lines with equally short lines in a supported language; if the selected mode lacks audio, generate silent visuals and record dialogue separately.

**Failure check / 检查方法：** 对照说话人的嘴型、左右位置和伞的交接；确认每句台词只有指定人物在说。若 15 秒模式不可用，拆为独立镜头并在剪辑中衔接。
