"""
monitor display resolution

1150 * 864

made by taishan 20200910
"""
from pymouse import PyMouse
import time
import datetime

m= PyMouse()
time.sleep(10)

while True:
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    m.move(153,111)
    m.click(153, 111,1)
    time.sleep(10)
    m.move(352,595)
    m.click(352,595,1)
    print(m.position())
    print(now)
    print("Success!")
    time.sleep(3600)
