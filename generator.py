# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 22:44:58 2020

@author: Ujjawal
"""
from PIL import Image, ImageDraw, ImageFont 
  
   
def coupons(names: list, certificate: str, font_path: str): 
   
    for name in names: 
          
        # adjust the position according to  
        # your sample 
        text_y_position = 900 
   
        # opens the image 
        img = Image.open(certificate, mode ='r') 
          
        # gets the image width 
        image_width = img.width 
          
        # gets the image height 
        image_height = img.height  
   
        # creates a drawing canvas overlay  
        # on top of the image 
        draw = ImageDraw.Draw(img) 
   
   
        draw.text( 
            ( 
                # this calculation is done  
                # to centre the image 
                (image_width - 200) / 2, 
                text_y_position 
            ), 
            name, 
                   ) 
   
        # saves the image in png format 
        img.save("{}.png".format(name))  
  

# Driver Code 
if __name__ == "__main__": 
   
    # some example of names 
    NAMES = ['Frank Muller', 
             'Mathew Frankfurt', 
             'Cristopher Greman', 
             'Natelie Wemberg', 
             'John Ken'] 
      
    # path to font 
    FONT = "C:/WINDOWS/FONTS?ADOBEARABIC-ITALIC.OTF"
      
    # path to sample certificate 
    CERTIFICATE = "certificate/Certificate.png"
   
    coupons(NAMES, CERTIFICATE, FONT) 