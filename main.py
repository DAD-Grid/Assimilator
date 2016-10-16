#!/usr/bin/env python

from ConcreteAssimilator import ConcreteAssimilator
from ConcreteObserver import ConcreteObserver

if __name__ == "__main__":
    # se crea un observador y un asimilador
    concrete_observer = ConcreteObserver(count_stop = 100)
    assimilator = ConcreteAssimilator()
    # se le registra el observador al asimilador y se corre el asimilador
    assimilator.register_observer(concrete_observer)
    assimilator.run()
