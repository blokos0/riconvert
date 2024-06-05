import glob
import cv2

def rgb_to_hex(r, g, b):
    return "#{:02x}{:02x}{:02x}".format(r, g, b)

images = [cv2.imread(file) for file in glob.glob("img/*.png")] # load images
imgf = images[0] # load the first image to get the sizes (assuming all of the images are the same size)
rows, cols, _ = imgf.shape
str = "-m=1 " # define the string and flags
for i in range(rows):
    for j in range(cols):
        imgindex = 0
        countofstacks = 0
        for img in images: # loop through images
            imgindex += 1
            k = img[i, j] # get the pixel
            colhex = rgb_to_hex(k[2], k[1], k[0]) # convert the pixel to hex
            animstr = ">"
            if imgindex == 1:
                animstr = "" # dont put > if its the first frame
            if colhex in str[len(str) - 7 - countofstacks : len(str) - countofstacks] and imgindex != 1: # stacked > check
                str += f"{animstr}"
                countofstacks += 1
            else:
                if imgindex == 1:
                    str += f"pixel:{colhex}" # the first frame should have the tile name
                else:
                    str += f"{animstr}:{colhex}"
                    countofstacks -= 2
        if j != cols - 1:
            str += " "
    str += "\n"
with open("out.txt", "w") as f:
    print(str, file = f)
print("done! output is in out.txt")