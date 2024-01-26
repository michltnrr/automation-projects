import os
import time
import speech_recognition as sr
import pyautogui

# to filter out background noise (music from spotify)
ENERGY_THRESHOLD = 4000

while True:
    # Check if Spotify is already open
    if os.system('pgrep -x "Spotify" > /dev/null') == 0:
        r = sr.Recognizer()
        r.energy_threshold = ENERGY_THRESHOLD

        # Obtain audio from the microphone
        with sr.Microphone() as source:
            print("Listening for audio... ")
        # adjust energy threshold based on background noise
            r.adjust_for_ambient_noise(source)
            r.dynamic_energy_threshold = True  
            audio = r.listen(source) 

        try:
            # Recognize speech using sphinx
            speech = r.recognize_sphinx(audio)
            print("Recognized audio: " + speech)

            # Check if the recognized text contains the phrase "quit"
            if "close" in speech.lower() or "clothes" in speech.lower():
                # close Spotify
                os.system('osascript -e \'quit app "Spotify"\'')
                time.sleep(1)

                # reopen Spotify
                os.system('open -a Spotify')
                time.sleep(1)

                # Simulate pressing the space key
                pyautogui.press('space')
            
            elif "pause" in speech.lower() or "paws" in speech.lower() or "paul" in speech.lower() or "ah" in speech.lower():
                os.system('open -a Spotify')
                pyautogui.moveTo(716, 842)
                time.sleep(2)
                pyautogui.click()
            
            elif "skip" in speech.lower() or "it" in speech.lower() or "this" in speech.lower() or "his" in speech.lower() or "if" in speech.lower():
                os.system('open -a Spotify')
                pyautogui.moveTo(766, 846)
                time.sleep(2)
                pyautogui.click()

        except sr.UnknownValueError:
            print("i couldn't understand the audio gang 💀")
        except sr.RequestError as e:
            print("Speech Recognition error: {0}".format(e))