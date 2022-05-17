class canvas:
    def __init__(self, width, heigth, pixels):

        self.height = heigth
        self.width = width
        self.pixels = pixels
        

    def draw(self):
        for i in range(len(self.pixels)):
            for x in range(len(self.pixels[i])):
                print(self.pixels[i][x], end="")
            print("")