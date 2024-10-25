import pickle

class Datos:
    @staticmethod
    def cargar_datos(file_name):
        try:
            with open(file_name, 'rb') as f:
                return pickle.load(f)
        except FileNotFoundError:
            return []

    @staticmethod
    def guardar_datos(data, file_name):
        with open(file_name, 'wb') as f:
            pickle.dump(data, f)
