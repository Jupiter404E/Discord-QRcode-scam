# Scam QR code on Discord Nitro v1.2

A Python script that automatically generates a discord nitro QR code and gives you access to your Discord account when you scan the QR code. **This scenario demonstrates how people can trick others into scanning their Discord login QR code and gaining access to their account. Use for educational purposes only!**

![image](https://github.com/Jupiter404E/Discord-qrcode-scam/blob/main/temp/discord_gift.png?raw=true)

## Information

Download the latest version of [chromedriver](https://chromedriver.chromium.org/downloads "link chromedriver") and replace the old `chromedriver.exe` with the new one. If you run into any errors, scroll down to learn more about troubleshooting.

## Usage

1. If you haven't installed python, download python 3.7.6 and make sure you select "ADD TO PATH" during installation.

2. Install required modules > `pip install -r requirements.txt` or double click on `pip_install_requirements.bat`

3. Type `python QR_Generator.py` in cmd to run or double click on `QR_Generator.bat`

4. Wait for `discord_gift.png` to be generated. Send the image to the victim and have them scan it.

5. The QR code is only valid for about 2 minutes. Make sure you send a fresh picture to your victim.

6. When the QR code is scanned, you will be automatically logged into the victim's account.

## Troubleshooting

Make sure the `chromedriver.exe` file is the same version as the current version of Chrome. To check the current version of Chrome, paste `chrome://settings/help` into the Google Chrome address bar.

if Chrome crashes:

1. Make sure your `chromedriver.exe` file is the same version as Chrome version.
2. Download the latest version of `chromedriver.exe` here: https://chromedriver.chromium.org/downloads
3. Then replace the `chromedriver.exe` file in the folder.
