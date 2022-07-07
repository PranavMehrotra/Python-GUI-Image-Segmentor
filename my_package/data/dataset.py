#Imports
import numpy as np
from PIL import Image
import json
import matplotlib.pyplot as plt

from my_package.data.transforms import CropImage, BlurImage, FlipImage, RotateImage, RescaleImage




class Dataset(object):
    '''
        A class for the dataset that will return data items as per the given index
    '''

    def __init__(self, annotation_file, transforms = None):
        '''
            Arguments:
            annotation_file: path to the annotation file
            transforms: list of transforms (class instances)
                        For instance, [<class 'RandomCrop'>, <class 'Rotate'>]
        '''
        self.annot = annotation_file
        self.trans = transforms
        # with open(self.annot, 'r') as reader:
        #     self.dic = [json.loads(line) for line in reader]
        

    def __len__(self):
        '''
            return the number of data points in the dataset
        '''
        return 1

    def __getitem__(self, idx):
        '''
            return the dataset element for the index: "idx"
            Arguments:
                idx: index of the data element.

            Returns: A dictionary with:
                image: image (in the form of a numpy array) (shape: (3, H, W))
                gt_png_ann: the segmentation annotation image (in the form of a numpy array) (shape: (1, H, W))
                gt_bboxes: N X 5 array where N is the number of bounding boxes, each 
                            consisting of [class, x1, y1, x2, y2]
                            x1 and x2 lie between 0 and width of the image,
                            y1 and y2 lie between 0 and height of the image.

            You need to do the following, 
            1. Extract the correct annotation using the idx provided.
            2. Read the image, png segmentation and convert it into a numpy array (wont be necessary
                with some libraries). The shape of the arrays would be (3, H, W) and (1, H, W), respectively.
            3. Scale the values in the arrays to be with [0, 1].
            4. Perform the desired transformations on the image.
            5. Return the dictionary of the transformed image and annotations as specified.
        '''
        # img_path = self.dic[idx]["img_fn"]
        # png_path = self.dic[idx]["png_ann_fn"]
        img = Image.open(self.annot)
        # png = Image.open(png_path)
        # img_id = self.dic[idx]["img_id"]
        # img_bboxes = self.dic[idx]["bboxes"]
        img = np.array(img)
        # png = np.array(png)
        if(self.trans !=None and len(self.trans)>0):
            # plt.subplot((len(self.trans)//2+1),2,1)
            # plt.imshow(img)
            # ind=2
            for func in self.trans:
                fun = func
                img = fun.__call__(img)
                # plt.subplot((len(self.trans)//2+1),2,ind)
                # plt.imshow(copied)
                # ind+=1
            # plt.show()
        img = np.array(img)/255
        # png = np.array(png)/255
        diction = {}
        diction["image"] = img
        # diction["gt_png_ann"] = png
        # diction["gt_bboxes"] = []
        # listi = []
        # for box in img_bboxes:
        #     listi.append(box["category"])
        #     listi.extend(box["bbox"])
        #     diction["gt_bboxes"].append(listi.copy())
        #     listi.clear()
        return diction        
        
        
# def main():
#     data = Dataset('D:/KGP Semesters/SEM 4/Software Engg Lab/Assignments/Codes/Assignment3/CS29006_SW_Lab_Spr2022-master/Python_DS_Assignment/data/annot.jsonl')
#     dic = data.__getitem__(4)
#     #Image.fromarray(np.uint8(dic["image"]*255)).show()
#     Image.fromarray(np.uint8(dic["gt_png_ann"]*255)).show()
# if __name__ == '__main__':
#     main()