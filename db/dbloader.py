import csv
import logging
import os

class loader ():

    def __init__(self, db, db_commit_interval, table, sourcefile) -> None:

        logging.info ('{} loader'.format(table))

        self.dbObj = db        
        self.commit_Threshold = db_commit_interval
        
        self.tablename = table
        self.create_table()        
        self.tablecolumns = self.dbObj.get_table_columnnames(self.tablename)

        self.data = []
        self.read_loader_file(sourcefile)
        return
        
    def create_table(self):
        table = self.dbObj.checkif_table_exists(self.tablename)
        if len(table) > 0:  return

        filename = 'create_' +  self.tablename + '.sql'
        filepath = os.path.dirname(os.path.realpath(__file__))
        with open(os.path.join(filepath, filename), 'r') as f:
            sql = f.read().strip()
        sql = sql.replace('\n','')
        self.dbObj.execute_DDL(sql)
        return

    def read_loader_file(self, filename):
        with open(filename,'r') as fin:
            dr = csv.DictReader(fin, delimiter=';')                        
            for row in dr: self.data.append(row)
        return

    def delete_rows(self):        
        self.dbObj.delete_all_rows(self.tablename)
        return

    def load_rows(self):        
        values=[]
        logging.info('loading rows... table {}'.format(self.tablename))
        for row in self.data:
            values.append(tuple([row[col] if row[col]!='' else None for col in self.tablecolumns]))
            if len(values) >= self.commit_Threshold:
                self.dbObj.insert_many(self.tablename, self.tablecolumns, values)
                values.clear()                
        else:
            if len(values) > 0:
                self.dbObj.insert_many(self.tablename, self.tablecolumns, values)
        return