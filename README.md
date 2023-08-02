# This is Flashcord.
## The most advanced Discord Theme to date.
![](https://raw.githubusercontent.com/SiriusBYT/flashcord/main/FC-PREVIEW/FC-LMH.gif)
# Flashcord is all about Maximising your Chat Space.
![](https://raw.githubusercontent.com/SiriusBYT/flashcord/main/FC-PREVIEW/FC-DKM.gif)
# While also being the pinacle of Customisable Eye Candy.
![](https://raw.githubusercontent.com/SiriusBYT/flashcord/main/FC-PREVIEW/FC-CBGR.gif)
## Notice: Flashcord is still very much unfinished.

# 📑 Summary & Important Tabs
- [⬇️ Installing Flashcord](https://github.com/SiriusBYT/flashcord/tree/main#-installing-flashcord-stable)
- [💡 Configuring Flashcord](https://github.com/SiriusBYT/flashcord/tree/main#-configuring-flashcord)
- [🔁 User Variables](https://github.com/SiriusBYT/flashcord/tree/main#-user-variables)
- [🎉 Flashcord Chat Effects](https://github.com/SiriusBYT/flashcord/tree/main#-flashcord-chat-effects)

# ⬇️ Installing Flashcord

### Install instructions have moved to the [Flashcord Wiki](https://github.com/SiriusBYT/flashcord/wiki).

## 🔄️ Flashcord Version Status
🦺 Flashcord Stable: [aSTB-230721] | **4 Feature Updates Behind SID.** | 🌐 Root Code Base: aSID-230721-HF3

🔥 Flashcord SID: [bSID-230802] | **15 Days without an Emergency Hotfix Update.**


# 💡 Configuring Flashcord

## 🔁 User Variables (Flashcord Alpha, does NOT work with Flashcord Beta)
NOTICE: The next major release of Flashcord does not have the same variable names. Please remind yourself that they will change very soon.

The following variables can be changed to improve your Flashcord Experience. The values specified for each variable are their default values. 

If you are running Flashcord using the @import code, your variables **must be after the "@import" line**.

This is a list of all the variables Flashcord has, to edit them, simply put the following block of code in your QuickCSS and remove variables you aren't going to modify, as easy as that!
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
  --CustomBGR-IMG: url("https://sirio-network.com/flashcord/bgr-test.jpg"); /* kiss your default weeb background goodbye soon, will be replaced by something i made instead of this placeholder that just stayed around */
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

  /* aSID-230720+: Setting this to anything causes most warnings such as "Flashcord is in Alpha; X Mode is unfinished" to get removed.*/
  --Allow-Warnings

  /* aSID-230721-HF2+: Setting this to "none" will remove the Debug Text caused by http://flashcord/debug, useful if people are spamming this. */
  --Debug-Text_Display: block;

  /* aSID-230722+: Some dude randomly forked Flashcord and edited the stripe image, you can thank him for this feature now. */
  --Custom-SHC_Stripe: url("https://sirio-network.com/flashcord/elements/stripe.png");
}
```

## 💉 Plugin Support

Flashcord supports many pretty cool Replugged Plugins, all of which are required if you want the best experience.

To see compatible plugins, simply check the plugins tab (REPLUGGED ONLY)

Some required plugins are shown in the [Flashcord WIki](https://github.com/SiriusBYT/flashcord/wiki/Installing-Flashcord-on-Replugged#-required-plugins).

For Flashcord Stable Users: Ignore the message about not getting the full experience because plugins are missing. That message will be gone soon, the real plugins you really need are shown in the wiki.

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
If these effects cause way too much lag, **consider disabling them using the variable "--Enable-ChatEffects**.


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
