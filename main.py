import pyautogui
from cfg_creator import get_cfg
import requests
from bs4 import BeautifulSoup
import schedule
import re
import webbrowser
from time import sleep
import pyperclip
from FunPayAPI import Account

done = set()

token, timer, user_agent = get_cfg()

headers = {
    "User-Agent": f"{user_agent}",
    "Cookie": f"golden_key={token}"
}


def get_status_info():
    url = "https://funpay.com/orders/trade?id=&buyer=&state=paid&game=45&section=lot-1009&server="

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        tc_item = soup.find_all("a", class_="tc-item")
        results = []
        for item in tc_item:
            href = item.get('href')
            if href:
                results.append(href)

        return results
    except requests.RequestException as e:
        print(f"HTTP request failed: {e}")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []


def go_to_link():
    print("waiting...")
    plus_rep_massiv = ["+rep красавчик", "+rep соло плеер", "+rep роблоксер", "+rep жоски", "+rep сигма",
                       "+rep krasava", "+rep gg", "+rep gg wp", "+rep clutch king", "ty for game bro +rep!",
                       "+rep best", "+rep frendly"]
    results = get_status_info()
    global done

    for result in results:
        url = result

        match = re.search(r'orders/([^/]+)/?', url)

        if match:
            order_id = match.group(1)

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            chat_msg_text = soup.find_all("div", class_="chat-msg-text")[-1]
            chat_div = soup.find("div", class_="chat")

            if chat_div:
                chat_id = chat_div['data-id']
            else:
                chat_id = None

            # Process messages only once per URL
            message_processed = False

            message = chat_msg_text
            text = message.get_text()
            if "Ссылка:" in text:
                # Extract the Steam URL and custom text
                match = re.search(r"Ссылка: (\S+), Мой текст: (.+)", text)
                if match:
                    steam_url = match.group(1)
                    steam_text = match.group(2)

                    if "RANDOM" in steam_text or "random" in steam_text:
                        import random
                        steam_text = random.choice(plus_rep_massiv)

                    sleep(3)

                    pyperclip.copy(steam_text)

                    sleep(1)
                    # Check if the URL contains the required text
                    if (
                            "https://steamcommunity.com/profiles/" in steam_url or "https://steamcommunity.com/id/" in steam_url) and order_id not in done:
                        webbrowser.open(steam_url)

                        path_to_image = "comment_png.png"

                        sleep(2)

                        for pd in range(15):
                            pyautogui.press('pagedown')

                        sleep(1)

                        for up in range(5):
                            pyautogui.press("up")

                        sleep(2)

                        location = pyautogui.locateCenterOnScreen(path_to_image)

                        if location:
                            pyautogui.moveTo(location)
                            sleep(1)
                            pyautogui.click()

                            sleep(2)

                            pyautogui.hotkey('ctrl', 'v')

                            sleep(5)

                            enter_path = "Enter.png"
                            location_enter = pyautogui.locateCenterOnScreen(enter_path)

                            if enter_path:
                                pyautogui.moveTo(location_enter)
                                sleep(1)
                                pyautogui.click()

                            done.add(order_id)

                            try:
                                acc = Account(golden_key=token,
                                              user_agent=f"{user_agent}").get()
                                acc.send_message(chat_id=chat_id,
                                                 text="@BOT@: Заказ выполнен! [Для проверки: Мой никнейм Axmed, 20 lvl steam], Не забудьте подтвердить заказ!")
                            except Exception as e:
                                pass

                            done.add(order_id)
                            sleep(1)
                            pyautogui.hotkey("ctrl", "w")
                            message_processed = True
                            break
            elif "Link:" in text:
                match = re.search(r"Link: (\S+), My text: (.+)", text)
                if match:
                    steam_url = match.group(1)
                    steam_text = match.group(2)

                    if "RANDOM" in steam_text or "random" in steam_text:
                        import random
                        steam_text = random.choice(plus_rep_massiv)

                    sleep(1)

                    pyperclip.copy(steam_text)

                    sleep(1)
                    # Check if the URL contains the required text
                    if (
                            "https://steamcommunity.com/profiles/" in steam_url or "https://steamcommunity.com/id/" in steam_url) and order_id not in done:
                        webbrowser.open(steam_url)

                        path_to_image = "comment_png.png"

                        sleep(2)

                        for pd in range(15):
                            pyautogui.press('pagedown')

                        sleep(1)

                        for up in range(5):
                            pyautogui.press("up")

                        sleep(2)

                        location = pyautogui.locateCenterOnScreen(path_to_image)

                        if location:
                            pyautogui.moveTo(location)
                            sleep(1)
                            pyautogui.click()
                            sleep(3)

                            pyautogui.hotkey('ctrl', 'v')

                            sleep(5)

                            enter_path = "Enter.png"
                            location_enter = pyautogui.locateCenterOnScreen(enter_path)

                            if enter_path:
                                pyautogui.moveTo(location_enter)
                                pyautogui.click()

                            try:
                                acc = Account(golden_key=token,
                                              user_agent=f"{user_agent}").get()
                                acc.send_message(chat_id=chat_id,
                                                 text="@BOT@: Заказ выполнен! [Для проверки: Мой никнейм Axmed, 20 lvl steam], Не забудьте подтвердить заказ!")
                            except Exception as e:
                                pass

                            done.add(order_id)
                            sleep(1)
                            pyautogui.hotkey("ctrl", "w")
                            message_processed = True
                            break


schedule.every(timer).seconds.do(go_to_link)
print("Бот запущен!")
while True:
    schedule.run_pending()
    sleep(1)
