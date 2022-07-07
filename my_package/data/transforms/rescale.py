#Imports
import numpy as np
from PIL import Image

class RescaleImage(object):
    '''
        Rescales the image to a given size.
    '''

    def __init__(self, output_size):
        '''
            Arguments:
            output_size (tuple or int): Desired output size. If tuple, output is
            matched to output_size. If int, smaller of image edges is matched
            to output_size keeping aspect ratio the same.
        '''

        # Write your code here
        self.out = output_size
        if(type(output_size)==type(1) or len(output_size)==1):
            self.typ = 'i'
        else:
            self.typ = 't'

    def __call__(self, image):
        '''
            Arguments:
            image (numpy array or PIL image)

            Returns:
            image (numpy array or PIL image)

            Note: You do not need to resize the bounding boxes. ONLY RESIZE THE IMAGE.
        '''

        # Write your code here
        img = Image.fromarray(image)
        width, height = img.size   # Get dimensions
        if(self.typ=='i'):
            if(width<=height):
                n_width = self.out
                n_height = int(n_width * (height/width))
            else:
                n_height = self.out
                n_width = int(n_height * (width/height))
        else:
            n_height , n_width = self.out
        img = img.resize((n_width,n_height))
        return np.array(img)