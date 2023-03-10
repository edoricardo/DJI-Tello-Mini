from djitellopy import Tello
import cv2
import pyzbar.pyzbar as pyzbar

tello = Tello()
tello.connect
print(tello.get_battery())

tello.streamon()

myData = "null"

def get_qr():
    img = tello.get_frame_read().frame
    for barcode in pyzbar(img):
        myData = barcode.data.pyzbar('utf-8')
        print(myData)
    
    return

while True:
    get_qr()
    image = tello.get_frame_read().frame
    image = cv2.resize(image, (360, 240))
    cv2.imshow("Image", image)
    cv2.waitKey(1)
