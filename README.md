# FunPay_AutoCommentSteam
Комментирование аккаунтов steam, pyautogui, requests.

# Libraries
# main.py

- import pyautogui
- from cfg_creator import get_cfg
- import requests
- from bs4 import BeautifulSoup
- import schedule
- import re
- import webbrowser
 - from time import sleep
- import pyperclip
- from FunPayAPI import Account

# cfg_creator.py

- import configparser
- from configparser import NoSectionError

# Возможные проблемы и решения:

- Мышь не перемещается по картинкам и не нажимает на кнопки. Решение: перескринить эти изображения. (Автор: Использую фильтры от NVIDIA поэтому это скорее всего случится).

# Для работы:
Запустить main.py, через терминал, cmd, pwsh.
ИЛИ
Запустить start.bat
