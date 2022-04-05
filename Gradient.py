# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 13:30:10 2022

Generates the frames of a gradient animation

@author: Adíaphoros
"""

import cv2 #pip install opencv
import glob
from PIL import Image
import png #pip install pypng
import os

# Gashler M. (2019, April 16) Creating a PNG file in Python
#	Retrieved March 20 2022, from https://stackoverflow.com/a/55715162/15043016
# Generate the png

def generate_frames():
    
    '''
    R = Red value
    G = Green value
    G = Blue value
    '''
    
    for G in range(256):
        img = []
        for R in range(256):
            row = ()
            for B in range(256):
                color = (R, G, B)
                row += color
            
            img.append(row)
        
        with open(f'results/{G:03}.png', 'wb') as f:
            w = png.Writer(256, 256, greyscale=False)
            w.write(f, img)
        print(f'Generated {G:03}.png')


# Driscoll M. (2021, June 23) Creating an Animated GIF with Python
#   Retrieved April 5 2022, from https://www.blog.pythonlibrary.org/2021/06/23/creating-an-animated-gif-with-python/
# Generate GIF from PNG frames

def generate_gif():
    frames = [Image.open(image) for image in glob.glob("results/*.PNG")]
    frame_one = frames[0]
    frame_one.save("gradient.gif", format="GIF", append_images=frames,
               save_all=True, duration=4267, loop=0)

# BoboDraph (2017, July 6) How to make a movie out of images in python
#   Retrieved April 5 2022, from https://stackoverflow.com/a/44948030/15043016
# Generate video from PNG frames

def generate_video():
    image_folder = 'results'
    video_name = 'Gradient.avi'
    
    images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
    frame = cv2.imread(os.path.join(image_folder, images[0]))
    height, width, layers = frame.shape
    
    # VideoWriter(filename, codec, fps, (width, height))
    video = cv2.VideoWriter(video_name, 0, 60, (width, height))
    
    for image in images:
        video.write(cv2.imread(os.path.join(image_folder, image)))
    
    cv2.destroyAllWindows()
    video.release()

def main():
    generate_frames()
    print("Generated the frames")
    
    generate_video()
    print("Generated the video")
    
if __name__ == "__main__":
    main()
