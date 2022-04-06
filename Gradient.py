# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 13:30:10 2022
Generates a seamlessly looping animation of a gradient
@author: Adíaphoros
"""

import cv2 #pip install opencv
import glob
from PIL import Image
import numpy
import os
import shutil

"""
Gashler M. (2019, April 16) Creating a PNG file in Python
    Retrieved March 20 2022, from https://stackoverflow.com/a/55715162/15043016
Aggarwal N. (2020, December 29) Create a directory in Python
    Retrieved April 5 2022, from https://www.geeksforgeeks.org/create-a-directory-in-python/
Generate the PNG frames and the folder to store them in
"""

def generate_frames():
    try: 
        os.mkdir('results') 
    except OSError as error: 
        print(error)
    
    for G in range(256):
        image = []
        for R in range(256):
            row = []
            for B in range(256):
                color = [R, G, B]
                row.append(color)
            image.append(row) # this needs to be n * n * 3 array
        image = numpy.array(image)
        cv2.imwrite(f'results/{G:03}.png', image)
        
"""
Driscoll M. (2021, June 23) Creating an Animated GIF with Python
    Retrieved April 5 2022, from https://www.blog.pythonlibrary.org/2021/06/23/creating-an-animated-gif-with-python/
Generate GIF from PNG frames
"""

def generate_gif():
    frames = [Image.open(image) 
              for image 
              in glob.glob("results/*.PNG")]
    frames = frames + list(reversed(frames))
    frame_one = frames[0]
    frame_one.save("gradient.gif", format="GIF", append_images=frames,
               save_all=True, duration=8533, loop=0)

"""
BoboDraph (2017, July 6) How to make a movie out of images in python
    Retrieved April 5 2022, from https://stackoverflow.com/a/44948030/15043016
Generate video from PNG frames
"""

def generate_video():
    video_name = 'Gradient.avi'
    
    frames = [cv2.imread(os.path.join('results', image)) 
              for image in os.listdir('results') 
              if image.endswith(".png")]
    frames += list(reversed(frames))
    frames = numpy.array(frames)
    frame_one = frames[0]
    height, width, layers = frame_one.shape
    
    # VideoWriter(filename, codec, fps, (width, height))
    video = cv2.VideoWriter(video_name, 0, 60, (width, height))
    
    for frame in frames:
        video.write(frame)
    
    cv2.destroyAllWindows()
    video.release()
    
"""
Tripathi A. (2017, March 7) How do I delete a file or folder in Python?
    Retrieved April 5 2022, from https://stackoverflow.com/a/42641792/15043016
Delete the PNG frames and the folder
"""

def delete_frames():
    
    # Try to remove tree; 
    # if the removal failed, 
    # show an error using try...except on screen
    try:
        shutil.rmtree('results')
    except OSError as e:
        print ("Error: %s - %s." % (e.filename, e.strerror))
    

def main():
    generate_frames()
    print("Generated the frames")
    
    generate_video()
    print("Generated the video")
    
    delete_frames()
    print("Deleted the frames")
    
    
if __name__ == "__main__":
    main()
