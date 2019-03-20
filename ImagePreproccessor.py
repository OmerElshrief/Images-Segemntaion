class preprocessing:

    def image_to_pixels(self, img , RGB = True ,axis = 0 ):
        pixels = []
        red = img[:, :, 0]
        green = img[:, :, 1]
        blue = img[:, :, 2]
        green.shape
        size = img.shape
        h = size[0]
        w = size[1]
        ch = size[2]

        for j in range(w):
            for i in range(h):
                pixels.append((red[i][j], green[i][j], blue[i][j], i, j))

        return np.array(pixels)
