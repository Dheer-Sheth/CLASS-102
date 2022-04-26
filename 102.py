import cv2
import time
import random
import dropbox

start_time= time.time()

def take_snapshot():
    number = random.randint(0,100)

    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frame=videoCaptureObject.read()
        img_name = "pic"+str(number)+".png"
        cv2.imwrite(img_name,frame)
        start_time = time.time
        result= False

    return img_name
    print("snapshot taken")

    videoCaptureObject.release()
    cv2.destroyAllWindows()

def upload_file(img_name):
    access_token = "sl.BGc6ywqYQKaddVYBSNZJ7SD5FxfnCLL4VR0gPie-cjgQR8Ucjf26gFAQlkvh18EoHfX4gBF_xSKiJvBipVnISmxnqbJVrtNit9TJQd53xWXE2fnsGgPpUS-y7ZxDrX-alRdxv6Q"
    file = img_name
    file_from = file
    file_to= "/newFolder/"+(img_name)
    dbx = dropbox.Dropbox(access_token)

    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(), file_to, mode= dropbox.files.WriteMode.overwrite)
        print("file uploaded")

def main():
    while(True):
        if((time.time() - start_time)>=300):
            name = take_snapshot()
            #upload_file(name)#
main()


