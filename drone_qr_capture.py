from djitellopy import Tello
import cv2
import pyzbar.pyzbar as pyzbar

tello = Tello()
tello.connect()
#print(tello.get_battery())

tello.streamon()

myData = "null"

while True:
    img = tello.get_frame_read().frame
    img = cv2.resize(img, (360, 240))
    for barcode in pyzbar(img):
        myData = barcode.data.pyzbar('utf-8')
        print(myData)
    cv2.imshow("Image", img)
    cv2.waitKey(1)
