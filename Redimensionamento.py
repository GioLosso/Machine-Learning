
Image = 'paisagem-g.png'


def grayscale(colored):
    w, h = colored.size
    img = Image.new("RGB", (w, h))
    for x in range(w):
        for y in range(h):
            pxl = colored.getpixel((x, y))
            
            lum = (pxl[0] + pxl[1] + pxl[2])//3
            img.putpixel((x, y), (lum, lum, lum))


if __name__ == "__main__":
    img = Image.open("paisagem-g.png")
    print(img.getpixel((100, 100)))
    print(img.getpixel((500, 300)))
    print(img.getpixel((300, 180)))

