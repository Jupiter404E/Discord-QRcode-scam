# Скам QR-код на Discord Nitro

Скрипт на Python, который автоматически генерирует QR-код discord nitro и дает доступ к учетной записи Discord при сканировании QR-кода. **Этот скрипт демонстрирует, как люди могут обманом заставить других отсканировать свой QR-код для входа в Discord и получить доступ к своей учетной записи. Использовать только в образовательных целях!**

![image](https://github.com/Jupiter404E/Discord-qrcode-scam/blob/main/temp/discord_gift.png?raw=true)

## Демонстрация

![image](https://user-images.githubusercontent.com/75003671/117522092-fd79ff80-afe3-11eb-938c-23dd68d5927c.gif)

## Информация

Загрузите последнюю версию [chromedriver](https://chromedriver.chromium.org/downloads "link chromedriver") и замените старый файл `chromedriver.exe` новым. Если вы столкнулись с какими-либо ошибками, прокрутите вниз, чтобы узнать больше об устранении неполадок.

## Применение

1. Если у вас не установлен python, загрузите python 3.7.6 и убедитесь, что вы выбрали опцию 'ADD TO PATH' во время установки.

2. Установите необходимые модули > `pip install -r requirements.txt` или дважды щелкните по `pip_install_requirements.bat`

3. Введите python `QR_Generator.py` в cmd для запуска или дважды щелкните по run_script.bat

4. Подождите, пока будет сгенерирован `discord_gift.png`. Отправьте изображение жертве и заставьте их отсканировать его.

5. QR-код действует всего около 2 минут. Убедитесь, что вы отправляете жертве свежий и он готов к сканированию.

6. Когда QR-код будет отсканирован, вы автоматически войдете в учетную запись жертвы.

## Установка требуемых библиотек

1. `pip install bs4`
2. `pip install selenium`
3. `pip install PIL`

## Устранение неполадок

Убедитесь, что файл `chromedriver.exe` имеет ту же версию, что и текущая версия Chrome. Чтобы проверить текущую версию Chrome, вставьте `chrome://settings/help` в адрессную строку Google Chrome.

если Chrome крашит,

1. Убедитесь, что ваш файл `chromedriver.exe` имеет ту же версию, что и версия Chrome.
2. Загрузите последнюю версию `chromedriver.exe` здесь: https://chromedriver.chromium.org/downloads
3. Затем замените файл `chromedriver.exe` в папке.
