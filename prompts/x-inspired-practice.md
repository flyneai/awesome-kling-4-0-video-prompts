# Four practical prompts inspired by X testing methods

[Home](../README.md) · [Videos and original creator posts](../docs/X-VIDEOS.md) · [Test record](../docs/TEST-RECORD.md)

These are new Flyne AI exercises, not the authors’ prompts or reproductions of their videos. They have **not been render-tested**. Use only the duration, reference and audio controls available in your selected model. Source links explain the testing method; each exercise uses a different scene and directing brief.

以下 4 条是 Flyne AI 新写的练习，借鉴的是测试方法，并非作者原提示词或原视频复刻，均未生成实测。英文代码块可直接复制；先按账户实际支持的时长、参考图和声音设置调整。完整原提示词仍请查看作者原帖。

<a id="long-take"></a>
## 1. A continuous route through a flower shop / 花店连续跟拍

**Learn from:** [Min Choi’s single-prompt example](https://x.com/minchoi/status/2104634610629980283). The author does not publish the prompt. Our exercise tests visible route continuity, not the model’s maximum duration.

**Use:** a 10-second, 16:9 scene with no reference required. 适合测试一镜到底：明确起点、路线、终点，以及途中不应变化的物体。

```text
10-second photoreal continuous shot inside a small flower shop at dawn. One florist in a plain olive apron carries one yellow watering can in her right hand. Begin beside the open entrance, with the florist two steps ahead of the camera. Track behind her at walking speed as she passes a wooden counter, turns left around its end, and stops beside one white orchid on the windowsill. Keep the turn and the same watering can visible. She tilts the can once, waters the orchid, then lowers it without setting it down. Finish behind her right shoulder, holding the orchid and watering can in frame. Soft window light; quiet footsteps and pouring water. No dialogue, music, cuts, time jumps, extra people or changing shop layout.
```

**Check / 检查：** Does the left turn connect the same spaces? Does the can stay in the same hand? Is the final frame held? / 左转前后是否为同一空间，水壶是否换手，结尾是否停稳？

**Revise / 修改：** If an unrequested cut appears, remove the turn and first test a straight route. If the final action is rushed, shorten the walk. / 若自动切镜，先改直线路线；浇水太仓促就缩短行走距离。

<a id="casting"></a>
## 2. Fictional casting with one small action / 虚构人物与细微动作

**Learn from:** [Ozan Sihay’s unnamed-actor test](https://x.com/ozansihay/status/2104676090233151927) and [a creator’s short-test cost report](https://x.com/agi_aibusi/status/2104690941194100858). Neither supplies a full prompt. This exercise describes visible traits instead of celebrity or show names.

**Use:** 5 seconds, 16:9, text to video. 适合低成本试写人物，检查外形和小动作，费用以实际账户为准。

```text
5-second live-action medium close-up of a fictional middle-aged bicycle repairer in a quiet workshop. Short curly grey hair, round clear glasses, a plain navy work shirt with rolled sleeves. He stands behind a bench with a single brass bicycle bell fixed to a handlebar. Begin with his eyes on the bell. He presses the bell lever once with his right thumb, listens to the ring, then gives one small satisfied smile. Keep both eyes and the bell visible in the same static composition. Natural skin texture, soft side light from a high window, muted workshop colors. One bell ring, faint room tone, no speech or music. No cuts, costume changes, extra fingers, text or logos.
```

**Check / 检查：** One press, one ring, then one reaction; glasses and hands should remain stable. / 动作与铃声是否对应，眼镜、手指是否变化？

**Revise / 修改：** If the face changes, test the same action with an authorized character reference. Compare results using the same duration and framing. Record actual credits, including failed attempts. / 人脸不稳时可加入有使用权的人物参考图；比较时固定时长和景别，并计入失败生成的花费。

<a id="references"></a>
## 3. One character sheet, one character / 一份三视图只对应一人

**Learn from:** [Ozan Sihay’s reference test](https://x.com/ozansihay/status/2104687711525490961) and [partial prompt screenshot](https://x.com/ozansihay/status/2104687714800992598). The visible instructions assign one identity to each sheet. [Towya’s longer Japanese production](https://x.com/towya_aillust/status/2104600267887145254) also discusses character and voice references; it does not establish that every Flash account supports those controls.

**Prepare:** upload a sheet showing front, side and back views of one original character wearing a plain orange raincoat. Bind it using your tool’s actual reference selector; “Reference A” below means that one uploaded sheet. Do not paste guessed special tokens. / 准备同一原创角色的正、侧、背三视图，通过界面的参考图选择器关联。没有此功能时不要把文字标签当作接口指令。

```text
10-second single shot, 16:9. Reference A shows different views of ONE person, not three people. Use that person as the only character. Preserve their face, short hair, orange raincoat and dark boots; do not copy the reference sheet layout or studio background. Place the character alone in a small greenhouse after rain. They lift one empty terracotta pot from a waist-high shelf, turn it slowly to inspect a crack, then put it back in the same place. Camera stays at chest height in a gentle three-quarter view, keeping face, hands and pot visible. Diffused daylight, soft rain tapping the glass, no dialogue or music. No duplicated character, costume change, montage, extra pots appearing or sudden camera movement.
```

**Check / 检查：** One person throughout, stable coat and face, the same pot returned to the same shelf. / 是否只出现一个人，服装和面部是否稳定，花盆是否放回原位？

**Revise / 修改：** If the sheet creates duplicates, use a single clear portrait and simplify the turn. Test voice references separately after visual consistency works. / 若三视图被当作多人，换单张清晰角色图；人物稳定后再单独测试声音参考。

<a id="dialogue-comparison"></a>
## 4. Timed dialogue with a persistent object / 带固定道具的分镜对白

**Published creator prompt:** [Pan’s complete timed dialogue brief and Kling clip](https://x.com/sebatheepan/status/2104706256963244436). [The parent comparison](https://x.com/sebatheepan/status/2104706252131725372) shows Seedance first. The original brief separates cast, props, timed shots and sound. Its “one take” wording refers to one generation despite multiple planned cuts. The exercise below is a different story, not a transcription.

**Use:** 15 seconds, 16:9, three shots; reduce dialogue if your mode is shorter. / 重点是台词轮流说、道具位置和结尾反应，不是堆砌镜头数量。

```text
15-second live-action scene with three planned shots in a quiet community radio booth. LEAH, an older presenter in a plain burgundy sweater, sits on the left. OMAR, a younger technician in a grey shirt, sits on the right. One small blue notebook lies closed between them. Keep these identities, seats and the notebook unchanged.
0–5 seconds: static wide two-shot. Omar looks at Leah and says calmly, "The recording is ready." Leah listens without speaking. The notebook stays closed on the table.
5–10 seconds: medium shot of Leah, from the same side of the table. She opens the notebook with her left hand, pauses, then says, "Then let's begin." Omar remains silent off camera.
10–15 seconds: return to the original wide composition. The notebook remains open. Leah looks toward the microphone; Omar gives one small nod. Hold the final two seconds without dialogue.
Natural conversational English, synchronized mouth movement, faint ventilation and one page rustle. Warm practical light, restrained expressions. No music, overlapping speech, subtitles, extra people, reversed seating or disappearing notebook.
```

**Check / 检查：** Compare the last five seconds as carefully as the opening: notebook state, seating, mouth movement and the final silence. / 尤其检查最后五秒，道具不能复原、人物不能换位、停顿时不能继续说话。

**Revise / 修改：** If speech overlaps, test the two-shot without cuts before restoring close-ups. For model comparisons, keep the prompt, references and supported settings the same, and record more than one attempt. / 台词重叠时先取消切镜；跨模型对比要固定条件并记录多次尝试，不以单次优胜作结论。
