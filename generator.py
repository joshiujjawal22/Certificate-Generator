# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 22:44:58 2020

@author: Ujjawal

Certificate has been taken from geeks for geeks
"""
from PIL import Image, ImageDraw, ImageFont 
  
   
def coupons(names: list, certificate: str, font_path: str): 
   
    for name in names: 
          
        # Position of text
        text_vert_position = 900 
   
        # opens the image 
        img = Image.open(certificate, mode ='r') 
          
        # gets the image width 
        image_width = img.width  
   
        draw = ImageDraw.Draw(img) 

        font = ImageFont.truetype( 
            font_path, 
            200 
        ) 

        # To get the text Width or Height
        text_width, _ = draw.textsize(name, font = font)
   
        draw.text( 
            (   
                # To center the image
                (image_width - text_width) / 2 , 
                text_vert_position 
            ), 
            name, 
            fill=150,
            font = font,
              ) 
   
        # Saves the image in png format 
        img.save("GeneratedStuff/{}.png".format(name))  
  


if __name__ == "__main__": 
    
    NAMES = ['Ankur', 
             'Akshit', 
             'Chetan', 
             'Nikunj', 
             'Utkarsh'] 
      
    
    FONT = "C:/Windows/Fonts/AdobeArabic-Bold.otf"
       
    CERTIFICATE = "certificate/Certificate.png"

    coupons(NAMES, CERTIFICATE, FONT) 