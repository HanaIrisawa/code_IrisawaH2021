import cv2
import glob
import os
import shutil
import time


#parameta
frame_size = -1  #FHD=0, 4K=1
frame_rate = 30.0  #FPS


#size set
width = 1450
height = 800


def timelaps(images):
    fourcc = cv2.VideoWriter_fourcc('m','p','4','v')
    video = cv2.VideoWriter('wave_animation.mp4', fourcc, frame_rate, (width, height))
    
    for i in range(len(images)):
        img = cv2.imread(images[i])
        img = cv2.resize(img,(width,height))
        video.write(img)       

    print("complete")


if __name__ == '__main__':
    start = time.time()
    images = sorted(glob.glob('./*.png'))
    print("Total of images:{0}".format(len(images)))
    timelaps(images)

    #elapsed_time = time.time() - start
    #print ("complete Time:{0}".format(elapsed_time) + "[sec]")
