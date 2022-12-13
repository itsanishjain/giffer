from PIL import Image
 
# Giving The Original image Directory
# Specified
Original_Image = Image.open("lil.png")
 
# Rotate Image By 180 Degree
rotated_image1 = Original_Image.rotate(10)

for i in range(50):
    img = Original_Image.rotate(i)
    img.save(f'lilOutput/{i}.png')

print("DONE")


 
# This is Alternative Syntax To Rotate
# The Image
# rotated_image2 = Original_Image.transpose(Image.ROTATE_90)
 
# This Will Rotate Image By 60 Degree
# rotated_image3 = Original_Image.rotate(60)
 
# rotated_image1.show()
# rotated_image1.save('lil1.png')
# rotated_image2.show()
# rotated_image3.show()