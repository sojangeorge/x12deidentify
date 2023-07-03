import logging
from db.dbloader import loader
from db.dbio import dbio

class members():
    def __init__(self) -> None:
        pass
    
    def load_data(self, db, commit_interval, file,renew_flag):
        ldr = loader(db=db,db_commit_interval=commit_interval, table='Member',sourcefile=file)
        if renew_flag: ldr.delete_rows()
        ldr.load_rows()

    def get_all_members(self, db):
        sql = 'Select * from Member'
        return db.execute_sql(sql)        

class suppliers():
    def __init__(self) -> None:
        pass

    def load_data(self, db, commit_interval, file,renew_flag):
        ldr = loader(db=db,db_commit_interval=commit_interval, table='Supplier',sourcefile=file)
        if renew_flag: ldr.delete_rows()
        ldr.load_rows()

    def get_all_suppliers(self,db):
        sql = 'Select * from Supplier'
        return db.execute_sql(sql)

class providers():
    def __init__(self) -> None:
        pass

    def load_data(self, db, commit_interval, file,renew_flag):
        ldr = loader(db=db,db_commit_interval=commit_interval, table='Provider',sourcefile=file)
        if renew_flag: ldr.delete_rows()
        ldr.load_rows()

    def get_all_providers(self, db):
        sql = 'Select * from Provider'
        return db.execute_sql(sql)

class testbed():
    def __init__(self, parameters) -> None:               
        self.dbObj= dbio(parameters['testbed']['dbfile'])
        self.commit_interval = int(parameters['testbed']['db_commitinterval'])
        
        self.m = members()
        self.s = suppliers()        
        self.p = providers()
        return
    
    def load_data(self,parameters):
        if parameters['testbed']['loadMember']: 
            self.m.load_data (db=self.dbObj, commit_interval=self.commit_interval,
                        file=parameters['testbed']['member_file'], 
                        renew_flag=parameters['testbed']['DELETE_EXISTING'])
        if parameters['testbed']['loadBillingSupplier']: 
            self.s.load_data (db=self.dbObj, commit_interval=self.commit_interval,
                        file=parameters['testbed']['supplier_file'], 
                        renew_flag=parameters['testbed']['DELETE_EXISTING'])
        if parameters['testbed']['loadProviders']: 
            self.p.load_data (db=self.dbObj,  commit_interval=self.commit_interval,
                        file=parameters['testbed']['provider_file'], 
                        renew_flag=parameters['testbed']['DELETE_EXISTING'])
        return
       
    def fetch_all_suppliers(self):
        return self.s.get_all_suppliers(db=self.dbObj)
    
    def fetch_all_providers(self):
        return self.p.get_all_providers(db=self.dbObj)
    
    def fetch_all_members(self):
        return self.m.get_all_members(db=self.dbObj)
    