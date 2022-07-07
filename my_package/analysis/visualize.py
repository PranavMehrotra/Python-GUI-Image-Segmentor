#Imports
import numpy as np
from PIL import Image, ImageDraw , ImageFont

def plot_visualization(pred_boxes, pred_masks, pred_class, pred_score, nimg, copied, h,w): # Write the required arguments

    # The function should plot the predicted segmentation maps and the bounding boxes on the images and save them.
    # Tip: keep the dimensions of the output image less than 800 to avoid RAM crashes.
    font = ImageFont.truetype("/usr/share/fonts/opentype/urw-base35/NimbusRoman-Regular.otf",20)
    draw = ImageDraw.Draw(copied)
    if(len(pred_score)<3):
        for ind in range(len(pred_score)):
            for preds in pred_masks:
                nncopy = np.empty((h,w))
                for j in range(h):
                    for k in range(w):
                        nncopy[j][k] = preds[0][j][k]
                temp = Image.fromarray(np.uint8(nncopy*255),'L')
                nimg.paste(temp,mask=temp)
            
            text = pred_class[ind]
            shape = pred_boxes[ind]
            draw.rectangle(shape,outline='white')
            a,b = shape
            x,y = a
            draw.text((x+5,y+5), text, fill = 'white', font = font, align = "left")   
    else:
        for p in range(3):    
            maxi = max(pred_score)
            for j in range(len(pred_score)):
                if(pred_score[j]==maxi):
                    ind = j
                    break

            nncopy = np.empty((h,w))
            for j in range(h):
                for k in range(w):
                    nncopy[j][k] = pred_masks[ind][0][j][k]
            temp = Image.fromarray(np.uint8(nncopy*255),'L')
            nimg.paste(temp,mask=temp)
            
            text = pred_class[ind]
            shape = pred_boxes[ind]
            draw.rectangle(shape,outline='white')
            a,b = shape
            x,y = a
            draw.text((x+5,y+5), text, fill = 'white', font = font, align = "left")
            pred_score[ind] =0
    #copied.show()
    return nimg,copied
