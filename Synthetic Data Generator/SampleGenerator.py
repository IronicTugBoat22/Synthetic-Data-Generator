import random

class SampleGenerator(object):
    """description of class"""

    # Generates a list of random values with a gaussian distribution
    def GenerateGaussianList(sampleSize, iterationCount, seed = None):

        # If a seed is provided, use it.
        # Otherwise Python uses system time as default seed.
        if seed is not None:
            random.seed(seed)

        # Generate each point in the dataset.
        gaussianSamples = list()
        for i in range(sampleSize):
            # Initialize the uniform sum to zero.
            uniformSum = 0

            # Sum up the set amount of uniform samples.
            for j in range(iterationCount):
                uniformSum += random.random()

            # The summed samples are now a single gaussian data point.
            gaussianSamples.append(uniformSum)

        # The gaussian samples new need to be rescaled, to return them
        #       to a standard normal.
        gaussianMean = iterationCount / 2.0
        gaussianStdDev = (iterationCount / 12.0)

        # The rescale transformation involves the mean and std dev.
        rescale = lambda a : (a - gaussianMean) / gaussianStdDev

        # Rescale each point in the list of samples.
        scaledList = [rescale(x) for x in gaussianSamples]

        # Return the scaled list.
        return scaledList
