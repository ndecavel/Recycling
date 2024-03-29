import cv2 as cv
import os

#don't forget to change the path
path = os.path.join('AMLI-trashnet','Paper')#HERE!!!!!!!!!
files = os.listdir(path+"Video")

save_path = path+"V_Photos/" 
#os.mkdir(save_path) #Uncomment if material folder does not already have V_Photos



for name in files:
    print(name)
### capture the video
    video = cv.VideoCapture(path+"Video/"+name)
    fps = video.get(cv.CAP_PROP_FPS)

### Setting up parameters
    f_s = 3            #wanted frames per second! change based on how fast the video is recorded
    x = round(fps/f_s)

    count = 0 
    success = 1 

    while success:
        frameId = int(round(video.get(1)))
        success, image = video.read()
        if frameId % x == 0:
            cv.imwrite(save_path+name+"frame%d.jpg" % frameId, image) 
              #added file name here so images won't be replaced

    video.release()
    print("100%")

print("Complete")

#select 
