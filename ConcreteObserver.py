from BaseObserver import BaseObserver

import subprocess

import sys



class ConcreteObserver(BaseObserver):
    """
        Observador concreto, sirve de referencia para crear otros observadores en el futuro, cuando se corran multiples aplicaciones
        tambien es necesario sobreescribir el metodo should_notify()
    """

    def __init__(self, count_stop = 99999):
        """
            se inicializa el hijo y se llama al constructor del padre para inicializr la variable count
        """
        BaseObserver.__init__(self)
        self.count_stop = count_stop

    def notify(self, result_path, wu_name):
        self.count = self.count + 1
        print "Llega un resultado de %s" % result_path
        # se copia el resultado a la carpeta de resultados
        subprocess.call(["cp", result_path, "/home/boincadm/results/"+wu.name ])
        if self.count == count_stop:
            print "se finaliza la aplicacion"
            sys.exit()
            #aca se puede llamar al que recopila los resultados antes de terminar