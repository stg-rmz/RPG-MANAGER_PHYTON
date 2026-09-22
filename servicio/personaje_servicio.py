from models.personaje import Personaje

class PersonajeServicio:
    def validarPersonaje(self, nombre, nivel, clase):
        if nivel < 1 or nivel > 100:
            return False
        if nombre is None or nombre.strip() == "":
            return False
        if clase.lower() in ["mago", "arquero", "guerrero"]:
            return True
        return False