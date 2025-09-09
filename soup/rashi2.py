import requests
from bs4 import BeautifulSoup
from gtts import gTTS
from playsound import playsound
import os

def extract_text_between(url, start_marker, end_marker):
    try:
        resp = requests.get(url)
        resp.raise_for_status()
        html = resp.text
    except Exception:
        html = None

    for source in ('raw', 'selenium'):
        if source == 'selenium' or html is None:
            from selenium import webdriver
            from selenium.webdriver.chrome.options import Options
            options = Options()
            options.add_argument("--headless")
            driver = webdriver.Chrome(options=options)
            driver.get(url)
            html = driver.page_source
            driver.quit()

        soup = BeautifulSoup(html, "html.parser")  # Use "lxml" if installed
        text = soup.get_text(separator=" ").strip()
        if start_marker in text and end_marker in text:
            start = text.find(start_marker) + len(start_marker)
            end = text.find(end_marker)
            return text[start:end].strip(" ·:-–")
    return None

def get_rashi_kathan(rashi_number):
    url = f"https://www.divyabhaskar.co.in/rashifal/{rashi_number}/today?ref=inbound_RHS"
    print(f"Fetching Rashi #{rashi_number} from: {url}")
    result = extract_text_between(url, "ચંદ્રરાશિ પ્રમાણે", "લકી નંબર")
    if result:
        with open("kathan.txt", "w", encoding="utf-8") as f:
            f.write(result)
        print("File saved as kathan.txt")
        return result
    else:
        print("Could not extract content from the page.")
        return None

def text_to_speech_gujarati(text, output_file="output.mp3"):
    try:
        tts = gTTS(text=text, lang='gu', slow=False)
        tts.save(output_file)
        print(f"Audio saved to {output_file}")
        playsound(output_file)
        os.remove(output_file)
    except Exception as e:
        print(f"Error during text-to-speech: {str(e)}")

# Mapping of Rashi numbers to names (optional, for user-friendly display)
rashi_names = {
    1: "મેષ",
    2: "વૃષભ",
    3: "મિથુન",
    4: "કર્ક",
    5: "સિંહ",
    6: "કન્યા",
    7: "તુલા",
    8: "વૃશ્ચિક",
    9: "ધન",
    10: "મકર",
    11: "કુંભ",
    12: "મીન"
}

# MAIN PROGRAM
try:
    print("રાશિફળ માટે નંબર પસંદ કરો:")
    for num, name in rashi_names.items():
        print(f"{num}: {name}")

    choice = int(input("\nતમારી રાશિ માટે નંબર દાખલ કરો (1 થી 12): ").strip())

    if 1 <= choice <= 12:
        print("મહેરબાની કરીને રાહ જુઓ... માહિતી મેળવી રહ્યા છીએ...")
        result = get_rashi_kathan(choice)
        if result:
            print("\nમાહિતી મેળવાઈ ગઈ છે. હવે અવાજ ઉત્પન્ન કરી રહ્યા છીએ...")
            text_to_speech_gujarati(result)
    else:
        print("માફ કરશો, કૃપા કરીને 1 થી 12 વચ્ચેનો નંબર દાખલ કરો.")

except ValueError:
    print("અમાન્ય દાખલ. કૃપા કરીને નંબર દાખલ કરો.")
