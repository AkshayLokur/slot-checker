from selenium import webdriver
import sys
from subprocess import call

if __name__ == "__main__":
    with webdriver.Chrome() as browser:  # Add chrome driver to classpath - e.g. /usr/local/bin on Mac
        browser.get("https://www.waangoo.com/deliveryslotdetails")
        try:
            print('\tTrying to find open slot...\n')
            slots = browser.find_element_by_xpath("//td[@style='text-align: center;']")
            if slots is not None:
                print('\tFound open slot!\n')
                # Increase Mac volume to 100%
                call(["osascript -e 'set volume output volume 100'"], shell=True)
                audio_file = "/System/Library/Sounds/Funk.aiff"
                for i in range(50):
                    return_code = call(["afplay", audio_file])  # Works on Mac
                    # print('\a\a\a\a\a\a\a\a\a') # For windows may be
        except:
            print("\tNo open slot!\n")
