#########################
# @short: The following code detects and removes the sky in a picture
#
# The goal is to detect the sky and remove it from the image to make
# the task easier for a DL algorithm. It is assumed that the image
# is always taken with the sky in the upper side of the picture.
#########################

import cv2 as cv
import numpy as np
import os

### [Picture_Filter]
#
# Class to handle an image

class Picture_Filter:

    def __init__(self, file):
        self.original = cv.imread(file)
        if self.original is None:
            print ("Error while opening file " + file)
        else:
            self.height     = self.original.shape[0]
            self.width      = self.original.shape[1]
            self.image      = self.original
            self.thresh_img = self.original
            self.border     = 0
            self.filterd_img= self.original
            self.cutted     = False
            self.name       = file[file.rfind('/')+1:]


    def get_info(self):
        print("Name:   " + str(self.name))
        print("Height: " + str(self.height))
        print("Width:  " + str(self.width))

    def show_original(self, seks = 0):
        if self.image is None:
            print("No image loaded in memory")
        else:
            cv.imshow(self.name,self.image)
            k = cv.waitKey(seks*1000)

    def show_filter(self, seks = 0):
        if self.thresh_img is None:
            print("No image loaded in memory")
        else:
            cv.imshow(self.name,self.thresh_img)
            cv.imwrite(os.getcwd() + "/filtered_cutted/" +  self.name,self.thresh_img)
            k = cv.waitKey(seks*1000)

    def show_filtered(self, seks = 0):
        if self.thresh_img is None:
            print("No image loaded in memory")
        else:
            cv.imshow(self.name,self.filterd_img)
            k = cv.waitKey(seks*1000)

    def save_at(self,path):
        if self.image is None:
            print("File is empty and cannot be saved")
        else:
            #print("Saving image at: " + path + "/" +  self.name)
            cv.imwrite(path + "/" +  self.name,self.filterd_img)
        return

    def apply_filter_black(self):
        # Applies filter over the image setting it in black
        for jdx in range(0,self.width):
            for idx in range(0,self.border):
                self.filterd_img[idx,jdx,0] = 0
                self.filterd_img[idx,jdx,1] = 0
                self.filterd_img[idx,jdx,2] = 0
    
    def apply_filter_cut(self):
        # Applies filter over the image cutting it
        if (not self.cutted):
            self.cutted = True
            self.filterd_img = np.delete(self.filterd_img,range(0,self.border),0)

    def dynamic_detection(self, threshold, percentage = True):
        # Applying adaptatove threshold gaussian
        if threshold <=255 and threshold >=0:
            ret,self.thresh_img = cv.threshold(self.image,threshold,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C)
            
        # Pure red should be considered black (some clouds)
        for idx in range(0,self.height):
            for jdx in range(0,self.width):
                self.thresh_img[idx,jdx,2] = 0

        self.find_sky_horizont()

    def find_sky_horizont(self):
        # Finds the horizont of between sky and ground

        # Finds 20 borders
        border_found   = np.zeros(20, dtype=int)
        segment_size = self.width/len(border_found)

        # Finding the borders
        for border_idx in range(0,len(border_found)):
            jdx = round((border_idx + 0.5)*segment_size)
            for idx in range(1,self.height):
                if self.thresh_img[idx,jdx,0] == 0 and self.thresh_img[idx,jdx,1] == 0:
                    border_found[border_idx] = idx
                else:
                    break

        # If border takes more than 65% of the image, discard it
        for border_idx in range(0,len(border_found)):
            if border_found[border_idx] > round(0.65*self.height):
                border_found[border_idx] = 0

        # Printing in red areas analyzed
        # Only for debugging reasons!
        for border_idx in range(0,len(border_found)):
            jdx = round((border_idx + 0.5)*segment_size)
            for idx in range(1,int(border_found[border_idx])):
                for j in range(-2,+2):
                    self.thresh_img[idx,jdx+j,0] = 0
                    self.thresh_img[idx,jdx+j,1] = 0
                    self.thresh_img[idx,jdx+j,2] = 255

        self.border = max(border_found)
        for jdx in range(0,self.width):
            for i in range(-2,2):
                self.thresh_img[self.border+i,jdx,0] = 0
                self.thresh_img[self.border+i,jdx,1] = 0
                self.thresh_img[self.border+i,jdx,2] = 255
        
            


        








    



