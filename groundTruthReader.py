from matplotlib import pyplot as plt

class GroundTruthReader:
    def __init__(self)
        

    
    def get_boundary_groundtruth(self,img, show=False, all=False):
        groundTruth = img.get('groundTruth')
        no_groundtruths = groundTruth.size
        trueBoundary = groundTruth[0][0]['Boundaries'][0][0]
        for i in range(1, no_groundtruths):
            boundary = groundTruth[0][i]['Boundaries'][0][0]
            trueBoundary += boundary

        h = trueBoundary.shape[0]
        w = trueBoundary.shape[1]
        trueBoundary = trueBoundary.reshape(h, w)
        ## For adding colors
        trueBoundary = 255 * np.ones([height, width], dtype="uint8") - (trueBoundary > 0) * 255
        f1 = plt.figure()
        if show == True:
                if all == True:
                    for i in range(no_groundtruths):
                        f1.add_subplot(2, 3, i+1)
                        plt.imshow(groundTruth[0][i]['Boundaries'][0][0])
                    plt.show()

                plt.imshow(trueBoundary)

        return trueBoundary


    def get_segmentation_groundtruth(self,img, show=False, all=False):
        groundTruth = img.get('groundTruth')
        no_groundtruths = groundTruth.size
        finalsegmentation = groundTruth[0][0]['Segmentation'][0][0]
        for i in range(1, no_groundtruths):
            segmentation = groundTruth[0][i]['Segmentation'][0][0]
            finalsegmentation += boundary

        height = trueBoundary.shape[0]
        width = trueBoundary.shape[1]
        finalsegmentation = finalsegmentation.reshape(height, width)
        ## For adding colors
        #finalsegmentation = 255 * np.ones([height, width, 1], dtype="uint8") - (finalsegmentation > 0) * 255

        f1 = plt.figure()
        if show == True:
                if all == True:
                    for i in range(no_groundtruths):
                        f1.add_subplot(2, 3, i+1)
                        plt.imshow(groundTruth[0][i]['Segmentation'][0][0])
                    plt.show()

                plt.imshow(finalsegmentation)

        return finalsegmentation
