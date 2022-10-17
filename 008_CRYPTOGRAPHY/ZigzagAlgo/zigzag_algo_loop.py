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


def mse(imageA, imageB):
    # the 'Mean Squared Error' between the two images is the
    # sum of the squared difference between the two images;
    # NOTE: the two images must have the same dimension
    err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    err /= float(imageA.shape[0] * imageA.shape[1])

    # return the MSE, the lower the error, the more "similar"
    # the two images are
    return err

def uaci(image1,image2):
    pixel1=image1.copy()
    pixel2=image2.copy()
    width,height=image1.shape
    value=0.0
    for y in range(0,height):
        for x in range(0,width):
            value=(abs(int(pixel1[x][y])-int(pixel2[x][y]))/255)+value

    value=(value/(width*height))*100
    return value





def sumofpixel(height,width,img1,img2):
    ematrix = np.empty([width, height])
    for y in range(0,height):
        for x in range(0,width):
            if img1[x][y] == img2[x][x]:
                ematrix[x][y] = 0
            else:
                ematrix[x][y] = 1
    psum = 0
    for y in range(0,height):
        for x in range(0,width):
            psum = ematrix[x][y] + psum
    return psum


def npcr(c1,c2):
    width, height = c1.shape
    pixel1 = c1.copy()
    pixel2 = c2.copy()

    per = ((sumofpixel(height,width,c1,c2)/(height*width))*100)
    # per=(((sumofpixel(height,width,pixel1,pixel2,ematrix,0)/(height*width))*100)+((sumofpixel(height,width,pixel1,pixel2,ematrix,1)/(height*width))*100)+((sumofpixel(height,width,pixel1,pixel2,ematrix,2)/(height*width))*100))/3
    return per


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
var1 = ('image')
var3 = ('.png')
var4 = ('encrypted')
var5 = ('decrypted')
var6 = ('Histogram')
n1= 2
MSE_VAL = np.zeros(n1)
PSNR_VAL = np.zeros(n1)
UACI_VAL = np.zeros(n1)
# CC_VAL_Org = np.zeros(n)
# CC_VAL_Enc = np.zeros(n)
NPCR_VAL = np.zeros(n1)
Entropy_VAL = np.zeros(n1)

h = 5
IS = 256
ph = pow(2, h)
sr = (IS * IS) / (ph * ph)
sr = int(sr)
r = np.zeros(sr)
for i in range(sr):
    r[i] = random.randint(4, h)
# print(r)

with open('Key_file.csv', newline='') as file:
    reader = csv.reader(file,
                        quoting=csv.QUOTE_ALL,
                        delimiter=' ')

    # storing all the rows in an output list
    output = []
    for row in reader:
        output.append(row[:])

key = []

for i in range(IS * IS):
    ky = substring_after(output[i][0], ",")
    key.append(int(ky))


for lp in range(n1):
    var2 = str(lp)
    f_name = f'{var1}{var2}{var3}'
    x = cv.imread(f_name)
    # x = cv.imread('lena.jpg')
    im = cv.cvtColor(x,cv.COLOR_BGR2GRAY)

    img = cv.resize(im,(IS,IS))
    img_si = img.shape
    mi = img_si[0]
    ni = img_si[1]

    # cv.imshow('Lena',img)
    # cv.waitKey(0)


    imgg = confusion(img,h,r)
    # cv.imshow('split Rotate',imgg)
    # cv.waitKey(0)



    Encrypted = img
    # k = 0
    for i in range(mi):
        for j in range(ni):
            Encrypted[i,j] = imgg[i,j] ^ key[k]
            # k = k + 1
            k = i * mi + j
    # cv.imshow('Encrypted Image',Encrypted)
    # cv.waitKey(0)

    # k=0
    Decrypted_rot = Encrypted.copy()
    for i in range(mi):
        for j in range(ni):
            Decrypted_rot[i,j] = Encrypted[i,j] ^ key[k]
            # k = k + 1
            k = i * mi + j





    Decrypted = rev_confusion(imgg,h,r)

    # cv.imshow('Decrypted Image',Decrypted)
    # cv.waitKey(0)
    fname = f'{var4}{var2}{var3}'
    cv.imwrite(fname, Encrypted)
    fname1 = f'{var5}{var2}{var3}'
    cv.imwrite(fname1, Decrypted)
    # MSE_VAL_withoutPCA[j] = np.square(np.subtract(img,Decrypted)).mean()
    # PSNR_VAL_withoutPCA[j] = cv.PSNR(img, Decrypted)
    MSE_VAL[lp] = np.square(np.subtract(imgg, Decrypted)).mean()
    PSNR_VAL[lp] = cv.PSNR(imgg, Decrypted)
    UACI_VAL[lp] = uaci(imgg, Decrypted)
    # CC_VAL_Org =
    NPCR_VAL[lp] = npcr(imgg, Decrypted)
    # Entropy
    marg = np.histogramdd(np.ravel(Encrypted), bins=256)[0] / Encrypted.size
    marg = list(filter(lambda p: p > 0, np.ravel(marg)))
    Entropy_VAL[lp] = -np.sum(np.multiply(marg, np.log2(marg)))

    histr = cv.calcHist([Encrypted], [0], None, [256], [0, 256])
    fname2 = f'{var6}{var2}{var3}'
    plt.plot(histr)
    plt.savefig(fname2)
    plt.clf()
    print(lp)
    # cv.imshow('Lena',img)
    # cv.waitKey(0)


print('MSE_VAL')
print(MSE_VAL)
print('PSNR_VAL')
print(PSNR_VAL)
print('UACI_VAL')
print(UACI_VAL)
# print('CC_VAL_Org')
# print(CC_VAL_Org)
# print('CC_VAL_Enc')
# print(CC_VAL_Enc)
print('NPCR_VAL')
print(NPCR_VAL)
print('Entropy_VAL')
print(Entropy_VAL)
