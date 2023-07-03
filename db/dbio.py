import sqlite3
import logging

class dbio():

    def __init__(self, dbfile):
        # variables
        self.connection = None
        self.__create_connection(dbfile)
        
        
    #create database connection
    def __create_connection(self, dbfile):

        try:
            self.connection = sqlite3.connect(dbfile)        
        except Exception as error:
            logging.error(str(error))
            raise Exception ('DB {} connection filed'.format(dbfile))
        return

    def execute_DDL(self, sql):           
        try:
            cur = self.connection.cursor()
            cur.execute(sql)                        
        except Exception as error:
            logging.error(str(error))
            raise Exception ('db execute DDL error {}'.format(error))
        return 

    def checkif_table_exists(self, tablename):
        list =[]
        try:
            cur = self.connection.cursor()
            sql = 'Select name FROM sqlite_master WHERE type=? AND name=?'
            values = ('table',tablename)
            cur.execute(sql, values)
            list = [row[0] for row in cur]
        except Exception as error:
            logging.error(str(error))
            raise Exception ('db get table column names sql error {}'.format(error))
        return list  

    def get_table_columnnames(self, tablename):
        list =[]
        try:
            cur = self.connection.cursor()
            sql = 'Select name from PRAGMA_TABLE_INFO(?)'
            values = (tablename,)
            cur.execute(sql, values)
            list = [row[0] for row in cur]
        except Exception as error:
            logging.error(str(error))
            raise Exception ('db get table column names sql error {}'.format(error))
        return list   

    #execute sql
    def execute_sql(self,sql):
        list =[]
        try:
            cur = self.connection.cursor()
            cur.execute(sql)             
            list = [row for row in cur]
        except Exception as error:
            logging.error(str(error))
            raise Exception ('db execute sql error {}'.format(error))
        return list

    #execute sql with values
    def execute_sql_with_values(self,sql,values):
        list =[]
        try:
            cur = self.connection.cursor()
            cur.execute(sql, values)             
            list = [row for row in cur]
        except Exception as error:
            logging.error(str(error))
            raise Exception ('db execute sql error {}'.format(error))
        return list
    
    #insert records into table
    def insert_many(self, tablename, cols, values):

        if self.connection == None:
            raise Exception ("DB connection is not established")
        
        if len(cols) != len(values[0]):
            raise Exception ("table columns {} and values {} must have same length".format(len(cols),len(values)))

        if len(cols) <= 0 :
            raise Exception ("there must be atleast one column in the input")

        sql = "INSERT INTO " + tablename +   " (" + ', '.join(cols) + ") VALUES (" + ('?,' * len(cols))[:-1] + ");"

        try:
            cur = self.connection.cursor()    
            cur.executemany(sql, values)
            cur.close()
            self.connection.commit()
            logging.info ('data inserted into DB, count {}'.format(len(values)))
        except sqlite3.Error as error:
            logging.error('error during insert details {}'.format(error))
            logging.error('error during insert query {}'.format(sql))
            logging.error('error during insert values {}'.format(values))
            raise Exception ('db execute sql error {}'.format(error))

        return 

    #delete all records in the table
    def delete_all_rows(self, tablename):

        try:
            sql = sql = 'DELETE FROM ' + tablename
            cur = self.connection.cursor()
            cur.execute(sql)
            self.connection.commit() 
        except sqlite3.Error as error:
            logging.error('error during delete query{}'.format(sql))  
            logging.error('error during delete query{}'.format(error))  
            raise Exception ('db delete sql error {}'.format(error))          
        return

    # close and release resources
    def close(self):
        self.connection.commit()
        self.connection.close()