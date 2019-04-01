# wsjAuto

Important details


`pyautogui.locateOnScreen('trustZoneStartButton.png', grayscale=True, confidence=.5)`

Was struggling to find image. Installed OpenCV `pip install opencv_python`, which allowed me to adjust confidence level. Also used `grayscale = True`. Image needs to be exact pixel match so it's easier to find with grayscale, and confidence allows you to adjust exactness of pixel match. Image need be in same monitor as the script. I suggest testing the script with an easy image before using specific one.

`subprocess.Popen(r"C:\Program Files\Trust.Zone VPN Client\trustzone.exe", close_fds=True)` was hanging when trying open exe. It appears subprocess.Popen and subprocess.call wait for the applicaiton to fully load. Adding `close_fds=true` made it so the script no longer waits for the exe to fully load.


