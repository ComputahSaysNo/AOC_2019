from processInputs import get_formatted_input

WIDTH = 25
HEIGHT = 6


def part1(data):
    imageData = str(data)
    pointer = 0
    minZeroes = 999999
    output = 0
    while pointer < len(imageData):
        digitCount = [0, 0, 0]
        for i in range(WIDTH * HEIGHT):
            currentPixel = imageData[pointer + i]
            digitCount[int(currentPixel)] += 1
        if digitCount[0] < minZeroes:
            minZeroes = digitCount[0]
            output = digitCount[1] * digitCount[2]
        pointer += WIDTH * HEIGHT
    return output


def part2(data):
    imageData = str(data)
    image = []
    for y in range(HEIGHT):
        row = ""
        for x in range(WIDTH):
            positionOffset = y * WIDTH + x
            topPixel = -1
            layerOffset = 0
            for z in range(len(imageData) // (WIDTH * HEIGHT)):
                pixel = imageData[positionOffset + layerOffset]
                if pixel != '2':
                    topPixel = pixel
                    break
                layerOffset += WIDTH * HEIGHT
            row += topPixel
        image.append(row)
    formattedImage = "\n"
    for i in image:
        formattedImage += i.replace("1", "███").replace("0", "   ") + "\n"
    return formattedImage


INPUT = get_formatted_input(8)
print(part1(INPUT), part2(INPUT))
