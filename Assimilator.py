from BaseAssimilator import Assimilator

class DivideAndConquerAssimilator(Assimilator):

    def __init__(self):
        super(Assimilator, self).__init__()
    
    def assimilate_handler(self, wu, results, canonical_result):
        print "Workunit"
        dir(wu)
        print "results"
        dir(results)
        print "canonical_result"
        dir(canonical_result)