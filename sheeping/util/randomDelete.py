# -*- coding: utf-8 -*-

import math
import random
import os

if __name__ == "__main__":
    #
    src=r'D:\Faceswap\11-18\Julisha\faces'
    threshold=0.5
    for i in os.listdir(src):
        poss=random.random()
        if poss < threshold:
            os.remove(src+'\\'+i)
    
    print