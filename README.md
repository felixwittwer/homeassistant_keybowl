<div align="center">

![Home Assistant](https://img.shields.io/badge/home%20assistant-%2341BDF5.svg?style=for-the-badge&logo=home-assistant&logoColor=white) &nbsp; &nbsp; ![Static Badge](https://img.shields.io/badge/Hack_Club_HIGHWAY_TO_UNDERCITY-Hack_Club?style=flat&logo=hackclub&color=white)

</div>

# homeassistant_keybowl
a smart bowl for your keys with Homeassistant integration and a display to show simple dashoards.

## About the project

This project is smart keyboawl where you can toss all your keys into and it will show you some interestign stuff from your Homeassistant instance. It simply hits you with the information you need when leaving home or comming back. The shown dashboards a custom for each user and are recognised by the RFID tag on each keychain.

## BOM

**total:** 91.60 USD

| part name | amount | price | link | note |
| --------- | ------ | ----- | ---- | ---- |
| UHF RFID Module 1dbi 35x35mm | 1 | 39.27 USD | https://de.aliexpress.com/item/1005008307223636.html?spm=a2g0o.productlist.main.2.3a2056acCbDovs&algo_pvid=561ac428-5895-4565-92d7-d20539900a0c&pdp_ext_f=%7B%22order%22%3A%228%22%2C%22eval%22%3A%221%22%7D&utparam-url=scene%3Asearch%7Cquery_from%3A | |
| 4.2inch e-paper | 1 | 29.38 USD | https://de.aliexpress.com/item/1005005825856739.html?spm=a2g0o.productlist.main.11.398af4a457pUEA&algo_pvid=a1b8dab7-90ac-46bd-aca0-fde6fcd30138&pdp_ext_f=%7B%22order%22%3A%2213%22%2C%22eval%22%3A%221%22%7D&utparam-url=scene%3Asearch%7Cquery_from%3A | would have liked to choose another one but waveshare has the best documentation and if you decide to upgrade the displays have the same footprint (upgrading from 4 grayscale to black/white/red possible)|
| Raspberry Pi Zero 2 W | 1 | 20.57 USD | https://de.aliexpress.com/item/1005008147614202.html?spm=a2g0o.productlist.main.9.1e3f432ciKsp9W&algo_pvid=32a8750d-1fe9-43b5-99b0-1ed1efdb7aec&pdp_ext_f=%7B%22order%22%3A%22141%22%2C%22eval%22%3A%221%22%7D&utparam-url=scene%3Asearch%7Cquery_from%3A | Pi Zero needed because of Homeassistant integration and connectivity (ESP32-S3 can't quite manage all this stuff together) |
| keyswitches | 6 | 1.19 USD | https://de.aliexpress.com/item/1005005371211477.html?spm=a2g0o.productlist.main.6.79e64294kL6s5H&algo_pvid=e22f25ac-00f0-4e9f-a177-d081d068b5ac&pdp_ext_f=%7B%22order%22%3A%2213%22%2C%22eval%22%3A%221%22%7D&utparam-url=scene%3Asearch%7Cquery_from%3A | come as 10 pcs set |
| basic DSA Keycaps | 6 | 1.19 USD | https://de.aliexpress.com/item/1005006005905021.html?spm=a2g0o.productlist.main.11.3fe97aeaDABDMY&algo_pvid=8be567c0-1498-4e45-9ebd-240fe64a8e61&pdp_ext_f=%7B%22order%22%3A%22525%22%2C%22eval%22%3A%221%22%7D&utparam-url=scene%3Asearch%7Cquery_from%3A | come as 20 pcs set |

**total:** 91.60 USD

## Credits

Raspberry Pi Zero Symbol, Footprint and 3D-Model for KiCad: https://www.snapeda.com/parts/RASPBERRY%20PI%20ZERO%202%20W/Raspberry%20Pi/view-part/?welcome=home

Waveshare 4.2inch e-Paper Module CAD: https://grabcad.com/library/waveshare-4-2-e-paper-module-1