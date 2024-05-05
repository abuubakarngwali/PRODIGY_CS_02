from PIL import Image

def swap_pixels(image_path):
    img = Image.open(image_path)
    img = img.convert("RGB")
    width, height = img.size

    swapped_pixels = []
    for y in range(height):
        for x in range(width // 2):  
            
            pixel1 = img.getpixel((x, y))
            pixel2 = img.getpixel((width - 1 - x, y))
            swapped_pixels.append(pixel2)
            swapped_pixels.append(pixel1)

    swapped_img = Image.new("RGB", (width, height))
    swapped_img.putdata(swapped_pixels)
    swapped_img.save("swapped_image.png")

def main():
    image_path = input("Enter the path to the image: ")
    swap_pixels(image_path)

if __name__ == "__main__":
    main()
