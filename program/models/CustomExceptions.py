class PlayerMovedTwiceInARowException(Exception):
    def message(self):
        return "El jugador no puede mover dos veces consecutivas"

class PositionAlreadyTakenException(Exception):
    def message(self):
        return "No se puede agregar un elemento en la posicion dada puesto a que hay anteriormente otro"