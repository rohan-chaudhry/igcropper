import PIL,  resizeimage, glob, os
from PIL import Image as IMG
from resizeimage import resizeimage
pics = sorted(glob.glob('DSC_*.JPG'))  # input picture files are .JPG


def createFolder(directory):  # create folder to hold resized images within current folder
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error: Creating directory. ' + directory)


def resize_all():  # resize JPG images in the same folder as image_sizer.py
    for pic in pics:
        print('working on ' + pic)
        with open(pic, 'r+b') as f:
            with IMG.open(f) as picture:
                new_name = 'resized_' + str(pic) + ".jpg" # saving as .jpg
                dpi_val = picture.info['dpi']
                # Instagram square dim is 640x640px
               #cover = resizeimage.resize_contain(picture, [1000, 1000])
                cover = resizeimage.resize_contain(picture, [640,640])  # only resizing, no cropping
                cover = cover.convert("RGB")
                cover.save(new_name, picture.format, quality = 100, dpi = dpi_val)
                picture.close()


def move_files():  # move resized files to their own folder within main folder
    resized = sorted(glob.glob('resized_*.JPG'))
    for pic in resized:
        src = pic
        dst = './ig_size/'+pic
        os.rename(src, dst)


def main():
    createFolder('./ig_size/')
    resize_all()
    move_files()


main()

