class BaseObserver(object):

    def __init__(self):
        self.count = 0
    
    def should_notify(self, canonical_result):
        """
            metodo que determina si un observador debe notificarse
            este es el caso cuando hay multiples aplicaciones que 
            necesitan observadores diferentes para cumplir con su trabajo
        """
        return True
    
    def notify(self, result_path, wu_name):
        """
            metodo que se ejecuta cada vez que un workunit termina 
        """
        pass
