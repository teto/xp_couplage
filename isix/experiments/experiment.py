


class XPDataSet:

    def __init__()


class Experiment:

    def __init__(self):
        # abstract class
        if self.__class__ is 'Experiment':
            raise NotImplementedError()

    def prestart():
        raise NotImplementedError()

    def start(self):
        raise NotImplementedError()

    def resume(self):
        raise NotImplementedError()

    def stop(self):
        raise NotImplementedError()

    def saveResults(self):
        raise NotImplementedError()


    def poststop():
        raise NotImplementedError()


# class NumpyExperiment
#     def saveResults(self,resultFilename,results):
#         np.savetxt( resultFilename, results, fmt="%.3f",delimiter="," )


#         # creates a 2-dimensional array 
#         results = np.empty( (max_repeat +1, len(fileSizes) ) );
#         results.fill( np.NAN )
#         results[0,] = fileSizes
#         # print("results", results )

#                         logger.info("Attempt %d out of %d..."%( attempt, MAX_ATTEMPT) )
#                     elapsedTime = self.run_unit_test(fileToDownload)
#                     # results[iteration, no] = elapsedTime
#                     results[ index[0],index[1] ] = elapsedTime
#                     # value = elapsedTime
#                     # save intermediate results
#                     self.saveResults( resultFilename, results )
                    

class ResultProcessor:
    # takes result in and transforms them
    def __init__(self):
        pass
