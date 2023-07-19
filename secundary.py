import sqlite3


class DbCreator:
    def __init__(self, db_file) -> None:
        self.db_file = db_file
        self.table_name = ''
        self.connection = self.connect()
        self.cursor = self.setCursor()
    
    def connect(self):
        return sqlite3.connect(self.db_file)
    
    def setCursor(self):
        return self.connection.cursor()
    
    def createATable(self, table_name, columns):
        columns_str = ', '.join(f'{name} {datatype}' for name, datatype in columns)
        self.cursor.execute(f'CREATE TABLE IF NOT EXISTS {table_name} ({columns_str})')
        self.connection.commit()
    
    def insertInTable(self, table_name, values):
        placeholders = ', '.join('?' for _ in values)
        self.cursor.execute(f'INSERT INTO {table_name} VALUES ({placeholders})', values)
        self.connection.commit()
        
    
if __name__ == '__main__':
    '''
    columns = [
    ('id', 'INTEGER PRIMARY KEY'),
    ('name', 'TEXT NOT NULL'),
    ('begin_date', 'TEXT'),
    ('end_date', 'TEXT')
    ]
    '''   
