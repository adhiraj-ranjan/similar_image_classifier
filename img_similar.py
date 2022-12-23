from PIL import ImageStat, Image

def are_similar(first_image, second_image):
    pixel1 = ImageStat.Stat(Image.open(first_image)).mean
    pixel2 = ImageStat.Stat(Image.open(second_image)).mean
    if int(pixel2[0]) in range(int(pixel1[0])-10,int(pixel1[0]+10)) and int(pixel2[1]) in range(int(pixel1[1])-10,int(pixel1[1]+10)) and int(pixel2[2]) in range(int(pixel1[2])-10,int(pixel1[2]+10)):
        return True
    else:
        return False
