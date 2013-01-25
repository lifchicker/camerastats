#!/usr/bin/env python2

#Thanks to http://gnuplot-surprising.blogspot.ru/2011/09/statistic-analysis-and-histogram.html for histrogram in gnuplot

from collections import Counter

from os.path import join
import pyexiv2
import os

__author__ = 'lh'

def getFocalLength(file):
    metadata = pyexiv2.ImageMetadata(file)
    metadata.read()

    tag = metadata['Exif.Photo.FocalLength']
    return tag.value

def walkDir(dir):
    for root, dirs, files in os.walk(dir):
        for name in files:
            if name.endswith(".PEF"):
                focal = getFocalLength(join(root, name))
                if focal == 0 : focal = 50  # trick for Zenitar
                f.write(str(focal) + "\n")
                #focalLengthes.append(int(getFocalLength(join(root, name))))


if __name__ == "__main__":
    focalLengthes = list()
    f = open("focaldata.dat", 'w')
    walkDir('/home/lh/pictures')
    walkDir('/media/TRASH/raw/')
    f.close()

    #focalCounter = Counter(focalLengthes)
    #print focalCounter.items()
    os.system('gnuplot plot.script')
    os.unlink('focaldata.dat')
    os.system('gwenview histogram.png')