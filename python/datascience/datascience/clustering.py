#! coding: utf-8
"""
clustering
==========

where we such clusters had
as made us nobly wild, not mad. -- robert herrick

"""
from datascience.algebra import vector_mean, squared_distance
import random


class KMeans:
    """performs k-means clustering"""

    def __init__(self, k):
        self.k = k
        self.means = None

    def classify(self, input):
        """return the index of the cluster closest to the input"""
        return min(range(self.k),
                   key=lambda i: squared_distance(input, self.means[i]))

    def train(self, inputs):
        """choose k random points as the intial means"""
        self.means = random.sample(inputs, self.k)
        assignments = None
        while True:
            # find new assignments
            new_assignments = map(self.classify, inputs)

            # if no assignments have changed, we're done
            if assignments == new_assignments:
                return

            # otherwise keep the new assignments
            assignments = new_assignments

            # compute new means based on the new assignments
            for i in range(self.k):
                # find all the points assigned to cluster i
                i_points = [p for p, a in zip(inputs, assignments) if a == i]

                # make sure i_points is not empty avoid divide by 0
                if i_points:
                    self.means[i] = vector_mean(i_points)


def squared_clustering_errors(inputs, k):
    """find the total squared error from k-means clustering the inputs"""
    clusterer = KMeans(k)
    clusterer.train(inputs)
    means = clusterer.means
    assignments = map(clusterer.classify, inputs)

    return sum(squared_distance(input, means[cluster])
               for input, cluster in zip(inputs, assignments))


def choosing_k(inputs):
    # plot from 1 up to len(inputs) clusters
    ks = range(1, len(inputs) + 1)
    errors = [squared_clustering_errors(inputs, k) for k in ks]

    plt.plot(ks, errors)
    plt.xticks(ks)
    plt.xlabel('k')
    plt.ylabel('total squared error')
    plt.title('total error vs. # of clusters')
    plt.show()


def clustering_colors():
    from datascience import clustering
    import matplotlib.image as mping
    import matplotlib.pyplot as plt
    # create a five-color version of an image
    # 1. choose five color
    # 2. assigning one of those colors to each pixel

    # k-means clustering
    # partition the pixels into five clusters in rgb space
    # recolor the pixels in each cluster to the mean color

    # 1. read image into python
    file_png = r'C:\images\compass.jpg'
    # behind the scenes `img` is a numpy array
    img = mping.imread(file_png)

    # 2. flatten list of all the pixels
    # top_row = img[0]
    # top_left_pixel = top_row[0]
    # red, green, blue = top_left_pixel
    pixels = [pixel for row in img for pixel in row]

    # 3. feed them to our cluster
    clusterer = clustering.KMeans(5)
    clusterer.train(pixels)

    print clusterer.means

    # 4. construct a new image with the same format
    def recolor(pixel):
        cluster = clusterer.classify(pixel)
        return clusterer.means[cluster]

    new_img = [[recolor(pixel) for pixel in row]
               for row in img]
    # 5. display it
    plt.imshow(new_img)
    plt.axis('off')
    plt.show()

if __name__ == '__main__':

    # # get the same result
    # random.seed(0)
    # clusterer = KMeans(3)
    # clusterer.train(inputs)
    # print clusterer.means

    # # two meetups
    # ...
    # clusterer = KMeans(2)
    # ...

    clustering_colors()
