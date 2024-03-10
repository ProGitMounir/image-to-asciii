from PIL import Image
import os

def asciiConvert(image, type, saveas, scale):
    scale = int(scale)

    # open and get image size
    img = Image.open(image)
    w,h = img.size

    # resize image (downscale)
    img.resize((w//scale, h//scale)).save("resized.%s" % type)

    # open new image
    img = Image.open("resized.%s" % type)
    w, h = img.size # get new width and height


    # list with correct length and height (same as resized image")
    grid = []
    for i in range(h):
        grid.append(["X"] * w)

    pix = img.load()


    for y in range(h):
        for x in range(w):
            if sum(pix[x,y]) == 0:
                grid[y][x] = "#" 
            elif sum(pix[x,y]) in range(1, 100):
                grid[y][x] = "X" 
            elif sum(pix[x,y]) in range(100, 200):
                grid[y][x] = "%" 
            elif sum(pix[x,y]) in range(200, 300):
                grid[y][x] = "&" 
            elif sum(pix[x,y]) in range(300, 400):
                grid[y][x] = "*" 
            elif sum(pix[x,y]) in range(400, 500):
                grid[y][x] = "+" 
            elif sum(pix[x,y]) in range(500, 600):
                grid[y][x] = "/" 
            elif sum(pix[x,y]) in range(600, 700):
                grid[y][x] = "(" 
            elif sum(pix[x,y]) in range(700, 750):
                grid[y][x] = "'" 
            else:
                grid[y][x] = " "

    art = open(saveas, "w")

    for row in grid:
        art.write("".join(row)+"\n")
    
    art.close()

#if __name__ == '__main__' : 
#   asciiconvert("mona_lisa.jpg", "jpg", "mona_lisa.txt","3")

def process_images_in_directory(directory, scale):
    for filename in os.listdir(directory):
        if filename.endswith(".jpg"):
            image_path = os.path.join(directory, filename)
            file_name, _ = os.path.splitext(filename)
            output_file = f"{file_name}_ascii.txt"
            asciiConvert(image_path, "jpg", output_file, scale)

if __name__ == '__main__':
    scale_factor = "3"  # Set your desired scaling factor here
    process_images_in_directory("D:\Programmes\GitHub\image-to-asciii\images", scale_factor)