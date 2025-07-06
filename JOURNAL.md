---
title: "Homeassistant KEYBOWL"
author: "Felix Wittwer (fegolix)"
description: "A keybowl designed for all your keys. But smart."
created_at: "2024-07-06"
---

# Journal

Here you can see a documentation of the entire development process.

**Total hours spent: 7h**

## July 6th (7h)

### Session 1 (2h) getting the idea, researching

After searcing for my keys and not finding them in our "key bowl" I got the idea of a smart solution for our keys. And even better how to integrate that into Homeassistant. Forst of all the concept. So the normal non smart version is preitty simple, just toss all your keys into a borwl/ basket but what if every keychain had an RFID tag on it? This would allow for thracking the keys not neccesarily to spy on wh is home wut to knwo where the keys are. To step it up a bit this could also be integrated into Homeassistant with a small display that shows some data/dashboard per user. Everyone has his own keychain so I can track who tossed his key in or took it out. And based on that information everybody gets shown his own personal dashboard. For one it might be stats about our greenhouse for the othe their timetable and current changes of it right in the morning before school.

<img src="./journal%20files/2025-07-06/smart_keybowl_sketch.png" width="400" />

<br>

I wanted a simple non distracting and simple solution that doesn't uses to much power and in standby mode maybe can be used as a clock. So I opted for a 4.2 inch e-Paper display and a raspberry Pi Zero 2 which is relatively low cost but has enough power to handle all the stuff of the display, additional keys and RFID reader and can render beautiful layouts on the screen. An ESP32-S3 simply cant handel all of that in an easy way. Another chalenge was finding the right module and corresponding RFID Tags. NFC simply wouldn't cut it here. I needed a solution that can read multiple tags at one inside a pile and that without errors. This lead me to the R200 module a UHF RFID Reader.

### Session 2 (5h) starting PCB design

After researching all the parts I started with the core PCB which is kind of a HAT for the Raspberry Pi Zero 2 and will be in the middle of the case. Everything else will be designed arround it. To make it a bit extra I added a bar of neopixels above the display this will later be usefull to show status or be indicator LEDs. Because I quite like habtical buttons I added three on each side of the display. These will later be for navigating on the display of showing specific dashboards. These additions make the whole thing a bit mode interesting so now it is not "just a display" :).

This time I really tried making my schematics a bit better than the last one. I think it is quite organised. Another challenge for me was learing on how to use a ground plane which I have never done befoder but eventually got it working.

<p float="left">
  <img src="./journal%20files/2025-07-06/KiCad_schematics.png" width="500" />
  <img src="./journal%20files/2025-07-06/KiCad_pcb_design.png" width="500" />
</p>
