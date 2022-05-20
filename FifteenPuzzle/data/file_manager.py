class FileManager:
    DIR_TXT = 'data/files'
    DIR_GRAPHS = 'data/graphs'

    def save(self, filename: str, _list: list):
        with open(f'{self.DIR_TXT}/{filename}', 'w') as file:
            for i, row in enumerate(_list):
                file.write(str(row))
                if (i + 1) != len(_list):
                    file.write('\n')

    def load(self, filename: str):
        with open(f'{self.DIR_TXT}/{filename}') as file:
            return file.readlines()

    def graph(self):
        pass
