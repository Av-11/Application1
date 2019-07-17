class Migrator:
    def __init__(self, reader, writer):
        self.reader = reader
        self.writer = writer

    def migrate(self):
        # 1. get the column names
        columns = self.reader.get_columns()

        # 2. create the table with columns
        self.writer.create_table(columns)

        # 3. 