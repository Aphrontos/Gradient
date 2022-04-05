# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 13:30:10 2022

Generates the frames of a gradient animation

@author: Adíaphoros
"""

import png #pip install pypng

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
        
        with open(f'results/{G}.png', 'wb') as f:
            w = png.Writer(256, 256, greyscale=False)
            w.write(f, img)
        print(f'Generated {G:X}.png')
        
def main():
    generate_frames()
    print("Generated the frames")
    
if __name__ == "__main__":
    main()
