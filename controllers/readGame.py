class ReadData:
    def __init__(self, file_name):
        self.file_name = file_name

    def read_data(self):
        try:
            with open("assets/data/" + self.file_name, 'r') as file:
                contenido = file.read()
            lineas = contenido.split('\n')
            filas = []
            for linea in lineas:
                print(linea)
                elementos = [item.strip() for item in linea.split(',')]
                filas.append(elementos[:-1])
            return list(reversed(filas))
        except FileNotFoundError:
            raise FileNotFoundError("File not found")
        except Exception as e:
            raise Exception("Error: " + str(e))
