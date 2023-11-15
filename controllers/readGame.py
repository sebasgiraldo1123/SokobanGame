class ReadData:
    def __init__(self, file_name):
        self.file_name = file_name

    def read_data(self):
        try:
            with open("assets/data/"+self.file_name, 'r') as file:
                dataTemp = [line.strip().split(', ') for line in file]
                data = [[element.rstrip(',') for element in row]
                        for row in dataTemp]
                invertedData = list(reversed(data))
            return invertedData
        except FileNotFoundError:
            raise FileNotFoundError("File not found")
        except Exception as e:
            raise Exception("Error: " + str(e))
