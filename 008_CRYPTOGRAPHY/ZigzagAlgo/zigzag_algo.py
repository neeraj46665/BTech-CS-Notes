import random

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mg
import csv

def rotate(image):
    img_s = image.shape
    m = img_s[0]
    n = img_s[1]
    # cv.imshow('Lena', image)
    # cv.waitKey(0)
    # print(m,n)
    image1 = image.copy()
    for a in range(m):
        for b in range(n):
            image1[m-b-1][a] = image[a][b]
    return image1
    #
    # cv.imshow('Rotated', image1)
    # cv.waitKey(0)

def inv_rotate(image):
    img_s = image.shape
    m = img_s[0]
    n = img_s[1]
    # cv.imshow('Lena', image)
    # cv.waitKey(0)
    # print(m,n)
    image1 = image.copy()
    for a in range(m):
        for b in range(n):
            image1[b][m-a-1] = image[a][b]
    return image1
    #
    # cv.imshow('Rotated', image1)
    # cv.waitKey(0)

def zigzag(image):
    img_s = image.shape
    rows = img_s[0]
    columns = img_s[1]
    # rows = len(image)
    # columns = len(image[0])
    image1 = image.copy()
    solution = [[] for i in range(rows + columns - 1)]

    for i in range(rows):
        for j in range(columns):
            sum = i + j
            if (sum % 2 == 0):

                # add at beginning
                solution[sum].insert(0, image[i][j])
            else:

                # add at end of the list
                solution[sum].append(image[i][j])

    t = 0

    for i in solution:
        for j in i:
            r = t // rows
            c = t % rows
            image1[r,c] = j
            t = t + 1
    return image1

def inv_zifzag(image):
    img_s = image.shape
    rows = img_s[0]
    columns = img_s[1]
    image1 = image.copy()
    res = [[] for i in range(rows)]
    solution = [[] for i in range(rows + columns - 1)]
    temp = []
    for i in range(rows):
        for j in range(columns):
            temp.append(image[i][j])
    k = 0
    for i in range(rows + columns - 1):
        if i < rows:
            for j in range(i + 1):
                solution[i].append(temp[k])
                k = k + 1
        else:
            for j in range(rows + columns - 1 - i):
                solution[i].append(temp[k])
                k = k + 1

    for i in range(rows):
        for j in range(columns):
            sum = i + j
            if (sum % 2 == 0):
                res[i].append(solution[sum].pop(-1))
            else:
                res[i].append(solution[sum].pop(0))
    t = 0
    for i in res:
        for j in i:
            r = t // rows
            c = t % rows
            image1[r,c] = j
            t = t + 1
    return image1

def confusion(img,h,r):

    ph = pow(2, h)
    sr = (mi * ni) / (ph * ph)
    sr = int(sr)


    k = 0
    imgg = img.copy()
    for i in range(int(mi / ph)):
        for j in range(int(ni / ph)):
            ia = ph * i
            ja = ph * j
            split_im = img[ia:ia + ph, ja:ja + ph]
            if r[k] != h:
                sub_img = split_im.copy()
                pr = int(pow(2, r[k]))
                for spi in range(int(ph / pr)):
                    for spj in range(int(ph / pr)):
                        spia = int(pr * spi)
                        spja = int(pr * spj)
                        sub_split_im = split_im[spia:spia + pr, spja:spja + pr]
                        sub_im_zigzag = zigzag(sub_split_im)
                        sub_split_rot = rotate(sub_im_zigzag)
                        sub_img[spia:spia + pr, spja:spja + pr] = sub_split_rot.copy()
                split_im_rot = sub_img.copy()
            else:
                im_zigzag = zigzag(split_im)
                split_im_rot = rotate(im_zigzag)
            imgg[ia:ia + ph, ja:ja + ph] = split_im_rot.copy()
            k = k + 1
    return imgg

def rev_confusion(img,h,r):

    ph = pow(2, h)
    sr = (mi * ni) / (ph * ph)
    sr = int(sr)


    k = 0
    imgg = img.copy()
    for i in range(int(mi / ph)):
        for j in range(int(ni / ph)):
            ia = ph * i
            ja = ph * j
            split_im = img[ia:ia + ph, ja:ja + ph]
            if r[k] != h:
                sub_img = split_im.copy()
                pr = int(pow(2, r[k]))
                for spi in range(int(ph / pr)):
                    for spj in range(int(ph / pr)):
                        spia = int(pr * spi)
                        spja = int(pr * spj)
                        sub_split_im = split_im[spia:spia + pr, spja:spja + pr]

                        rev_sub_split_rot = inv_rotate(sub_split_im)
                        rev_sub_im_zigzag = inv_zifzag(rev_sub_split_rot)
                        sub_img[spia:spia + pr, spja:spja + pr] = rev_sub_im_zigzag.copy()
                rev_im_zigzag = sub_img.copy()
            else:
                rev_split_im_rot = inv_rotate(split_im)
                rev_im_zigzag = inv_zifzag(rev_split_im_rot)
            imgg[ia:ia + ph, ja:ja + ph] = rev_im_zigzag.copy()
            k = k + 1
    return imgg

def substring_after(s, delim):
    return s.partition(delim)[2]

# k = 1
# temp = [[0] * 16] *16
# for i in range(16):
#     for j in range(16):
#         temp[i][j] = k
#         k = k + 1
# zig = zigzag(temp)
# print(temp)
# print(zig)

x = cv.imread('lena.jpg')
im = cv.cvtColor(x,cv.COLOR_BGR2GRAY)
IS = 256
img = cv.resize(im,(IS,IS))
img_si = img.shape
mi = img_si[0]
ni = img_si[1]

cv.imshow('Lena',img)
cv.waitKey(0)
# rot = rotate(img)
# cv.imshow('rotation',rot)
# cv.waitKey(0)
# invrot = inv_rotate(rot)
# cv.imshow('Inversr rotate',invrot)
# cv.waitKey(0)
h = 5
ph = pow(2, h)
sr = (mi * ni) / (ph * ph)
sr = int(sr)
r = np.zeros(sr)
for i in range(sr):
    r[i] = random.randint(4, h)
print(r)

imgg = confusion(img,h,r)
# cv.imshow('split Rotate',imgg)
# cv.waitKey(0)


with open('Key_file.csv', newline='') as file:
    reader = csv.reader(file,
                        quoting=csv.QUOTE_ALL,
                        delimiter=' ')

    # storing all the rows in an output list
    output = []
    for row in reader:
        output.append(row[:])


key = []

for i in range(IS*IS):
    ky = substring_after(output[i][0],",")
    key.append(int(ky))
Encrypted = img
k = 0
for i in range(mi):
    for j in range(ni):
        Encrypted[i,j] = imgg[i,j] ^ key[k]
        k = k + 1
cv.imshow('Encrypted Image',Encrypted)
cv.waitKey(0)

k=0

Decrypted_rot = Encrypted.copy()
for i in range(mi):
    for j in range(ni):
        Decrypted_rot[i,j] = Encrypted[i,j] ^ key[k]
        k = k + 1





Decrypted = rev_confusion(imgg,h,r)

cv.imshow('Decrypted Image',Decrypted)
cv.waitKey(0)
