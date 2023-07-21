# This is Flashcord.
## The most advanced Discord Theme to date.
![](https://raw.githubusercontent.com/SiriusBYT/flashcord/main/FC-PREVIEW/FC-LMH.gif)
# Flashcord is all about Maximising your Chat Space.
![](https://raw.githubusercontent.com/SiriusBYT/flashcord/main/FC-PREVIEW/FC-DKM.gif)
# While also being the pinacle of Customisable Eye Candy.
![](https://raw.githubusercontent.com/SiriusBYT/flashcord/main/FC-PREVIEW/FC-CBGR.gif)
## Notice: Flashcord is still in very early Alpha.

# 📑 Summary & Important Tabs
- [⬇️ Installing Flashcord](https://github.com/SiriusBYT/flashcord/tree/main#-installing-flashcord-stable)
- [💡 Configuring Flashcord](https://github.com/SiriusBYT/flashcord/tree/main#-configuring-flashcord)
- [🔁 User Variables](https://github.com/SiriusBYT/flashcord/tree/main#-user-variables)
- [🎉 Flashcord Chat Effects](https://github.com/SiriusBYT/flashcord/tree/main#-flashcord-chat-effects)

# ⬇️ Installing Flashcord
Before we can start, decide which version of Flashcord you would like to install, the Stable version gets updates every week or more while the "SID" versions gets updated daily. SID can be unstable at times so if you want a theme that just works then install Stable.
## 🦺 Installing Stable:
[For Replugged Users, simply click here](https://replugged.dev/install?identifier=SiriusBYT/flashcord&source=github), this will open a page that will communicate with your client to install Flashcord.
### You can install Flashcord Stable on other clients such as BetterDiscord or Vencord by adding this to your QuickCSS, please note that Flashcord doesn't fully support other clients!
⚠️ You cannot decide if you wanna update or not with this method, it updates as soon as your client fetches for Flashcord's code.
```
@import url("https://raw.githubusercontent.com/SiriusBYT/flashcord/main/src/main.css");
```
## 🔥 Installing SID:
⚠️ You cannot decide if you wanna update or not with Flashcord SID, it updates as soon as your client fetches for Flashcord's code.
To switch to Flashcord SID, please **Paste the Following Line** into your **Quick CSS** and then click on **"Apply Changes"**
```
@import url("https://sirio-network.com/flashcord/fc-sndl.css");
```
To force update Flashcord SID, open the **DevTools** (CTRL + SHIFT + I), head over to the **Network** Tab, then check **"Disable Cache"** and click on **"Apply Changes"**.

ℹ️ Make sure to also not have Flashcord Stable still enabled after switching to SID to prevent code conflicts.

## 🔄️ Flashcord Version Status
🦺 Flashcord Stable: [aSTB-230714_HF1] | **7 Feature Updates Behind SID.** | 🌐 Root Code Base: aSID-230714-HF1

🔥 Flashcord SID: [aSID-230721-HF1] | **0 Days without an Emergency Hotfix Update.**


# 💡 Configuring Flashcord
## ⚠️ Flashcord requires the "Channel Emojis" Discord Experiment for the best experience.
Refer to your client's way of enabling Experiments, then search for **"Channel Emojis"** and set the **Treatment to 2**

## 🛑 NOTICE ABOUT CUSTOM IMAGE BACKGROUNDS: Requires ["LegalDiscordBypasses" by @loneweeb.tsx](https://replugged.dev/install?identifier=dev.tharki.LegalDiscordBypasses) or Discord Nitro
Due to the complexity of Flashcord, it is better to seperate the Custom Background Image Theme into another one, problem is that the only other "it just works" theme is a Discord Nitro theme. 
Using the plugin  is thus necessary if you wanna use said feature without Nitro.
![](https://raw.githubusercontent.com/SiriusBYT/flashcord/main/FC-PREVIEW/DiscordCanary_6RUcvA0asO.png)
Choosing any of those themes will activate the Custom IMG mode. It is recommended to use a dark themed one for visibility reasons. (ℹ️ In aSID-230720+, you no longer have to pick a random theme)

## 🔁 User Variables
The following variables can be changed to improve your Flashcord Experience. The values specified for each variable are their default values. 

If you are running Flashcord using the @import code, your variables **must be after the "@import" line**.
```
:root {
  /* aSID-230707+: Control Blur Intensity, recommended to set to 0px on low end systems. */
  --BlurInt-Big: 16px;
  --BlurInt-Med: 8px;
  --BlurInt-Sma: 4px;

  /* aSID-230702+: Control the Transition Speed of Elements. Set to 0 to Disable.*/
  --AnimMult-Fast: 1;
  --AnimMult-Normal: 1;
  --AnimMult-Slow: 1;

  /* aSID-230704+: Self Explanatory, set to 0 to Disable. [!] DOES NOT DISABLE CHAT EFFECTS */
  --Enable-Animations: 1;

  /* aSID-230703+: Custom Background Customisation */
  --CustomBGR-IMG: url("https://sirio-network.com/flashcord/bgr-test.jpg");
  --CustomBGR-Filter: blur(16px) brightness(0.5);

  /* aSID-230704+: If you are having severe issues in the friends tab because you have too many friends, set this to block */
  --Friend-Redesign: flex; 

  /* aSID-230706+: Setting this to 0 disables most of the Flashcord Swag for specific users. */
  --Brand-Mode: 1;

  /* aSID-230712+: High End Systems Only. Puts a bunch more random crap that looks cool but blows computers up */
  --IridescentMode: 0;

  /* aSID-230714+: Enable Chat Effects, disabling them will stop their animations. (Set to 0 to disable) */
  --Enable-ChatEffects: 1;

  /* aSID-230715+: See the Flashcord Benchmark Channel on the SGN Discord Server for more information. This is not very useful honestly. */
  --Flashbench: 0;

  /* aSID-230718+: Edit the Server Unread Glow/Shadow, set to 0 to disable it if it distracts you too much */
  --Server-Glow: 1;
  --Server-Glow_Color: blue;

  /* aSID-230718+: Edit the Channel Unread Glow/Shadow, set to 0 to disable it if it distracts you too much */
  --Channel-Glow: 1;
  --Channel-Glow_Unread_Color: rgba(0,0,255,0.5);
  --Channel-Glow_Mention_Color: rgba(255,0,0,0.5);

  /* aSID-230720+: IridescentMode starting from aSID-230720 no longers disables animations when you're not hovering Discord, set the variable to 1 to re-enable them. */
  --Disable-Idle_Optimizations: 0;

  /* aSID-230720+: Setting this to 0 causes most warnings such as "Flashcord is in Alpha; X Mode is unfinished" to get removed.*/
  --Allow-Warnings: 1;
}
```

## 💉 Plugin Support

Flashcord supports many pretty cool Replugged Plugins, all of which are required if you want the best experience, those plugins are:

[Platform Indicators by @puyodead1](https://replugged.dev/install?identifier=me.puyodead1.PlatformIndicators)

[Staff Tags (in Crown Mode) by @puyodead1](https://replugged.dev/install?identifier=me.puyodead1.StaffTags)

[Statistic Counter by @harley.0](https://replugged.dev/install?identifier=griefmodz/statistic-counter&source=github)

[Badges Everywhere by @12944qwerty](https://replugged.dev/install?identifier=dev.kingfish.BadgesEverywhere)

[ShowHiddenChannels by @loneweeb.tsx](https://replugged.dev/install?identifier=dev.tharki.ShowHiddenChannels)

[ReMessageLogger by @sammcheese](https://replugged.dev/install?identifier=SammCheese/ReMessageLogger&source=github)

[Channel Typing by @asportnoy](https://replugged.dev/install?identifier=dev.albertp.ChannelTyping)

Plugin support ranges from simple alignment fixes to complete visual overhaul.

More plugins are expected to be supported in the future.

# 🎉 Flashcord Chat Effects
Adding any of these URLs at the end of your Discord message will add a special effect to your message. These also work for attachements.
```
(aSID-230714+) Rainbow Text Effect: http://flashcord/rainbow
(aSID-230714+) Small Text Effect: http://flashcord/small
(aSID-230714+) Shake Effect: http://flashcord/shake
(aSID-230714+) Dramatic Effect: http://flashcord/dramatic

(aSID-230715+) Red Background Message: http://flashcord/background/red
(aSID-230715+) Green Background Message: http://flashcord/background/green
(aSID-230715+) Blue Background Message: http://flashcord/background/blue

(aSID-230717+) Loud Effect: http://flashcord/loud
(aSID-230717+) Quiet Effect: http://flashcord/quiet

(aSID-230719+) Rainbow Shadow Effect: http://flashcord/rainbow-shadow
(aSID-230719+) Spin Effect: http://flashcord/spin
(aSID-230719+) Fade from Bottom Effect: http://flashcord/fade-bottom
(aSID-230719+) Splash Text Effect: http://flashcord/splash

(aSID-230720+) Debug Information: http://flashcord/debug

You can use markdown to hide the link to non-flashcord users. Example: [This message has a Flashcord Chat Effect. Install it to view the effect.](http://flashcord/rainbow)
```
If these effects cause way too much lag, **consider disablming them using the variable "--Enable-ChatEffects**.


## ✅ Platform Compatibility

| Platform     | Replugged                 | BetterDiscord                                    | Vencord                                          |
|:-------------|:--------------------------|:-------------------------------------------------|:-------------------------------------------------|
| 🪟 Windows   | ✅ Perfect Compatibility | ⚠️ Missing & Incompatible Plugins, seems fine    | ⚠️ Missing Plugins, some compatible, seems fine |
| 🍎 MacOS     | ☑️ Seems Perfectly Fine  | ❓Unknown Compatibility                          | ❓Unknown Compatibility                         |
| 🐧 GNU/Linux | ☑️ Seems Perfectly Fine  | ⚠️ Missing & Incompatible Plugins + Weird Issues | ❓Unknown Compatibility                         |

| 📱 Enmity (iOS)     | ☎️ Android             |
|:--------------------|:------------------------|
| [⛔ Color Theme Only](https://github.com/SiriusBYT/flashcord-ios) | ⛔ Unsupported for now |


## 💾 Flashcord Archive
Older versions of Flashcord are available on the [Sirio Network Website](https://sirio-network.com).
To use an older version of Flashcord, add this to your QuickCSS while replacing [Branch] by either STB (Stable) or SID and [Version Number].
```
@import url("https://sirio-network.com/flashcord/archive/[Status][Branch]-[Version Number].css");

Valid Example:
@import url("https://sirio-network.com/flashcord/archive/aSID-230715.css");
```
To view the available versions, please look at https://sirio-network/flashcord/archive (Warning: Currently not Working)

##### [Flashcord](https://github.com/SiriusBYT/flashcord) © 2023 by [SiriusBYT](https://sirio-network.com) is licensed under [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/).
