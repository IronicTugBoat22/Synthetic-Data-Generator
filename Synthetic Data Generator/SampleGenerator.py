import random

class SampleGenerator(object):
    """
    Contains methods related to generating synthetic datasets

    Methods:
        GenerateGaussianList(sampleSize, iterationCount, seed = None)
            Generates a list of random values with a gaussian distribution.
        IntroduceLinearTrend(points, direction, scalar)
            Introduces a linear trend of the given strength and direction into the given set of points as a new dimension on those points.
    """

    def GenerateGaussianList(sampleSize, iterationCount, seed = None):
        """
        Generates a list of random values with a gaussian distribution
        
        Arguments:
            sampleSize : int
                The number of samples to generate
            iterationCount : int
                The number of iterations to use in generating the samples. More iterations more closely approximates a gaussian distribution, but takes longer to generate.
            seed : float, optional
                The seed to use for the random number generator (defaults to the current system time)
        Returns:
            A list of random values with a gaussian distribution
        """

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

    def IntroduceLinearTrend(points, direction, scalar):
        """
        Introduces a linear trend of the given strength and direction into the given set of points as a new dimension on those points.

        Arguments:
            points : list
                List of tuples representing points
            direction : tuple
                A tuple representing the direction vector of the trend to introduce. Length must match the length of the tuples in the points list.
            scalar : float
                The strength (magnitude) of the trend to introduce.
        Returns:
            The list of input points, where each point has an added dimension and the values in that added dimension form a linear trend of the input strength and direction.
        Raises:
            AssertionError
                If there is not at least one point in the points iterable
                If the dimensionality of the points in the points iterable does not match the direction vector
        """

        # Validate the length
        assert (len(points) >= 1, "There must be at least one point.")
        assert(len(points[0]) == len(direction), "The direction vector must have the same length as each point in the point list.")
        
        # Version 1
        # Sum the dimensional values within the point, weighted by the direction in that dimesion, and then multiply by the scalar.
        weighDimension = lambda p, n : direction[n] * p[n]
        calculateTrend = lambda p : p + tuple(scalar * (sum([weighDimension(p, n) for n in range(len(p))])))
        points = [calculateTrend(point) for point in points]

        # Version 2
        #for point in points:
        #    weightedSum = 0
        #    for n in range(len(point)):
        #        weightedSum += direction[n] * point[n]
        #    trendingValue = weightedSum * scalar
        #    point = point + tuple(trendingValue)

        return points