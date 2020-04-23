from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import sys
from subprocess import call
import time
from twilio.rest import Client

if __name__ == "__main__":
    CHROMEDRIVER_PATH = "/usr/local/bin/chromedriver"
    WINDOW_SIZE = "1920,1080"
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)

    with webdriver.Chrome(
        executable_path=CHROMEDRIVER_PATH, options=chrome_options
    ) as browser:  # Add chrome driver to classpath - e.g. /usr/local/bin on Mac
        browser.get("https://www.waangoo.com/deliveryslotdetails")
        time.sleep(1)
        try:
            print("\tTrying to find open slot...\n")
            slots = browser.find_element_by_xpath("//td[@style='text-align: center;']")
            if slots is not None:
                print("\tFound open slot!\n")
                client = Client()
                from_whatsapp_number = "whatsapp:+14155238886"

                # Send to Akshay
                to_whatsapp_number = "whatsapp:+"
                client.messages.create(
                    body="WAANGOO slot available! Hurry up!",
                    from_=from_whatsapp_number,
                    to=to_whatsapp_number,
                )

                # Send to Sumit
                to_whatsapp_number = "whatsapp:+"
                client.messages.create(
                    body="WAANGOO slot available! Hurry up!",
                    from_=from_whatsapp_number,
                    to=to_whatsapp_number,
                )

                # Increase Mac volume to 100%
                call(["osascript -e 'set volume output volume 100'"], shell=True)
                audio_file = "/System/Library/Sounds/Glass.aiff"
                for i in range(50):
                    return_code = call(["afplay", audio_file])  # Works on Mac
                    # print('\a\a\a\a\a\a\a\a\a') # For windows may be
        except:
            print("\tNo open slot!\n")
