from PIL import Image, ImageDraw

def drawingLogic(image):
    draw = ImageDraw.Draw(image)

    grid_columns = 5
    grid_rows = 10

    top = 0
    bottom = image.height
    left = 0
    right = image.width
    grid_box_width = int(image.width/grid_columns)
    grid_box_height = int(image.height/grid_rows)

    for x in range(0, image.width, grid_box_width):
        line = ((x, top), (x, bottom))
        draw.line(line, fill=128)

    for y in range(0, image.height, grid_box_height):
        line = ((left, y), (right, y))
        draw.line(line, fill=128)

    del draw

def drawBackgroundImage():
    height = 400
    width = 400
    grayscale_mode = 'L' # L (8-bit pixels, grayscale)
    background_color = 255 # WHITE
    image = Image.new(mode=grayscale_mode, size=(height, width), color=background_color)
    drawingLogic(image)

    is_debug = False
    if is_debug:
        image.show()
    else:
        image.save("background.png")

if __name__ == '__main__':
    drawBackgroundImage()
