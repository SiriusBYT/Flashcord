# This is Flashcord.
## The most advanced Discord Theme to date.
![](https://raw.githubusercontent.com/SiriusBYT/flashcord/main/FC-PREVIEW/FC-LMH.gif)
## Flashcord is currently in Early Alpha.
[Available for Repluged](https://replugged.dev/install?identifier=SiriusBYT/flashcord&source=github) Clients, BetterDiscord support will come later as it causes issue with certain things as it injects extra classes which somehow interfere with Flashcord.

# Flashcord is all about Maximising your Chat Space.
![](https://raw.githubusercontent.com/SiriusBYT/flashcord/main/FC-PREVIEW/FC-DKM.gif)
# While also being the pinacle of Customisable Eye Candy.
![](https://raw.githubusercontent.com/SiriusBYT/flashcord/main/FC-PREVIEW/FC-CBGR.gif)

## 🔄️ Flashcord Version Status
🦺 Flashcord Stable: [aSTB-230714] | **0 Updates Behind Flashcord SID.** | 🌐 Root Code Base: aSID-230714-HF1

🔥 Flashcord SID: [aSID-230714-HF1] | **0 Days without an Emergency Hotfix Update.**

## 💡 Instructions and Tips
ℹ️ It is not recommended to use Flashcord on Low-End Systems, you could, but in that case, disable animations, transitions and especially blur with the variables provided.

Flashcord recommends using **Discord Canary** as it was made on it.

### ⚠️ Flashcord requires the "Channel Emojis" Discord Experiment for the best experience.
Flashcord can work without this experiment, however without it, Flashcord looks more dead and less full of life, it is very recommended to enable that experiment.

### 🛑 NOTICE ABOUT CUSTOM IMAGE BACKGROUNDS: Requires "LegalDiscordBypass" or Discord Nitro
Due to the complexity of Flashcord, it is better to seperate the Custom Background Image Theme into another one, problem is that the only other "it just works" theme is a Discord Nitro theme. 
Using the plugin [LegalDiscordBypasses by @loneweeb.tsx](https://replugged.dev/install?identifier=dev.tharki.LegalDiscordBypasses) is thus necessary if you wanna use said feature without Nitro.
![](https://raw.githubusercontent.com/SiriusBYT/flashcord/main/FC-PREVIEW/DiscordCanary_6RUcvA0asO.png)
Choosing any of those themes will activate the Custom IMG mode. It is recommended to use a dark themed one for visibility reasons.

### 🎉 Flashcord Chat Effects

Adding any of these URLs at the end of your Discord message will add a special effect to your message.
```
Rainbow Text Effect: http://flashcord/rainbow
Small Text Effect: http://flashcord/small
Shake Effect: http://flashcord/shake
Dramatic Effect: http://flashcord/dramatic

You can use markdown to hide the link to non-flashcord users. Example: [This message has a Flashcord Chat Effect. Install it to view the effect.](http://flashcord/rainbow)
```
If these effects cause way too much lag, **consider disablming them using the variable provided below**.

### 🔁 User Variables
The following variables can be changed to improve your Flashcord Experience. The values specified for each variable are their default values. 

If you are running Flashcord SID, your variables **must be after the "@import" line**.
```
* {
  /* Control Blur Intensity, recommended to set to 0px on low end systems. */
  --BlurInt-Big: 16px;
  --BlurInt-Med: 8px;
  --BlurInt-Sma: 4px;

  /* Control the Transition Speed of Elements. Set to 0 to Disable.*/
  --AnimMult-Fast: 1;
  --AnimMult-Normal: 1;
  --AnimMult-Slow: 1;

  /* Self Explanatory, set to 0 to Disable. [!] DOES NOT DISABLE CHAT EFFECTS */
  --Enable-Animations: 1;

  /* Custom Background Customisation */
  --CustomBGR-IMG: url("https://sirio-network.com/flashcord/bgr-test.jpg");
  --CustomBGR-Filter: blur(16px) brightness(0.5);

  /* If you are having severe issues in the friends tab because you have too many friends, set this to block */
  --Friend-Redesign: flex; 

  /* Setting this to 0 disables most of the Flashcord Swag for specific users. */
  --Brand-Mode: 1;

  /* High End Systems Only. Puts a bunch more random crap that looks cool but blows computers up */
  --Iridescent-Mode: 0;

  /* Enable Chat Effects, disabling them will stop their animations. (Set to 0 to disable) */
  --Enable-ChatEffects: 1;

}
```

### 💉 Plugin Support

Flashcord supports many pretty cool Repluged Plugins such as:

[Platform Indicators by @puyodead1](https://replugged.dev/install?identifier=me.puyodead1.PlatformIndicators)

[Staff Tags (in Crown Mode) by @puyodead1](https://replugged.dev/install?identifier=me.puyodead1.StaffTags)

[Statistic Counter by @harley.0](https://replugged.dev/install?identifier=griefmodz/statistic-counter&source=github)

[Badges Everywhere by @12944qwerty](https://replugged.dev/install?identifier=dev.kingfish.BadgesEverywhere)

[ShowHiddenChannels by @loneweeb.tsx](https://replugged.dev/install?identifier=dev.tharki.ShowHiddenChannels)

[ReMessageLogger by @sammcheese](https://replugged.dev/install?identifier=SammCheese/ReMessageLogger&source=github)

[Channel Typing by @asportnoy](https://replugged.dev/install?identifier=dev.albertp.ChannelTyping)

Plugin support ranges from simple alignment fixes to complete visual overhaul.

More plugins are expected to be supported in the future.

## 🔥 Switching from Stable to Flashcord SID
Flashcord SID is the very much unstable version of Flashcord. **Unlike Flashcord Stable, who's getting updates every week, SID gets updated every night** on average around 21:30 UTC+01.

⚠️ You cannot decide if you wanna update or not with Flashcord SID, it updates as soon as your client fetches for Flashcord's code.
### It is SERIOUSLY NOT recommended to switch to SID. The Closed Alpha testers can tell you that when aSID-230703 came out, everyone died in pain and agony.
To switch to Flashcord SID, please **Paste the Following Line** into your **Quick CSS** and then click on **"Apply Changes"**
```
Instructions are currently not available. The SID branch is under closed invite.
```
To force update Flashcord SID, open the **DevTools** (CTRL + SHIFT + I), head over to the **Network** Tab, then check **"Disable Cache"** and click on **"Apply Changes"**.

ℹ️ Make sure to also not have Flashcord Stable still enabled after switching to SID to prevent code conflicts.

## ✅ Platform Compatibility

| Platform      | Replugged                | BetterDiscord             |
|:-------------|:--------------------------|:--------------------------|
| 🪟 Windows   | ✅ Perfect Compatibility | ❓Unknown Compatibility   |
| 🍎 MacOS     | ☑️ Seems Perfectly Fine  | ❓Unknown Compatibility   |
| 🐧 GNU/Linux | ❓Unknown Compatibility  | ⚠️ Minor Issues           |

| 📱 Enmity (iOS)     | ☎️ Android             |
|:--------------------|:------------------------|
| [⛔ Color Theme Only](https://github.com/SiriusBYT/flashcord-ios) | ⛔ Unsupported for now |

##### [Flashcord](https://github.com/SiriusBYT/flashcord) © 2023 by [SiriusBYT](https://sirio-network.com) is licensed under [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/).
