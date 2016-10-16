from BaseAssimilator import Assimilator

class ConcreteAssimilator(Assimilator):
    """
        Clase asimilador que implementa el patrón observador, se encarga  de registrar y avisar a unos observadores cada vez que se completa un trabajo
    """

    def __init__(self):
        Assimilator.__init__(self)
        observers = []
    
    def assimilate_handler(self, wu, results, canonical_result):
        if canonical_result is not None:
            path = self.get_file_path(canonical_result)
            self.notify(path, wu.name)
    
    def register_observer(self, observer):
        self.observers.append(observer)

    def notify(self, path, wu_name):
        for observer in self.observers:
            if observer.should_notify():
                observer.notify(path, wu_name)
