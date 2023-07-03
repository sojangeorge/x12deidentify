from datetime import datetime

class x12transaction():

    def __init__(self, parameters, TCN_Sequence, claiminput: dict, dataHandle=None) -> None:        
        self.x12segments = []
        self.TransactionSetControlNumber = str(TCN_Sequence).zfill(5)
        self.parameters = parameters
        self.processtime = datetime.now()
        self.ReferenceIdentification = 'SG' + self.processtime.strftime("%m%d%H%M%S")
        self.claimAttributes = claiminput
        self.dataHandle = dataHandle


    def add_Transactionset(self):

        self.add_STsegment()
        self.add_BHTsegment()
        self.add_1000A()
        self.add_1000B()
        self.add_2000A()
        self.add_2000B()
        self.add_2000C()
        self.add_SEsegment()
    
    def add_STsegment(self):
        segment =[]
        #segment name
        segment.append('ST')
        #Transaction Set Identifier Code
        segment.append('837')
        #Transaction Set Control Number
        segment.append(self.TransactionSetControlNumber)
        #Implementation Convention Reference
        segment.append(self.parameters['TransactionAttributes']['x12version'] )

        self.x12segments.append(segment)
        return

    def add_BHTsegment(self):
        segment =[]
        #segment name
        segment.append('BHT')
        #Hierarchical Structure Code
        segment.append('0019')
        #Transaction Set Purpose Code
        segment.append('00')
        #Reference Identification
        segment.append(self.ReferenceIdentification)
        #Date                
        segment.append(self.processtime.strftime("%Y%m%d"))        
        #Time
        segment.append(self.processtime.strftime("%H%M%S"))  
        #Transaction Type Code
        segment.append('CH')

        self.x12segments.append(segment)
        return

    def add_1000A(self):
        
        #Submitter details

        segment =[]
        #segment name
        segment.append('NM1')
        #Entity Identifier Code
        segment.append('41')
        #Entity Type Qualifier
        segment.append('2')
        #Name Last or Organization Name
        segment.append(self.parameters['1000Aattributes']['SubmitterOrganizationName'])
        #Name First                
        segment.append('')
        #Name Middle
        segment.append('')
        #Name Prefix
        segment.append('')
        #Name Suffix
        segment.append('')
        #Identification Code Qualifier
        segment.append('46')
        #Identification Code
        segment.append(self.parameters['1000Aattributes']['SubmitterETIN'])
        self.x12segments.append(segment)

        segment.clear()
        #segment name
        segment.append('PER')
        #Contact Function Code
        segment.append('IC')
        #Name
        segment.append(self.parameters['1000Aattributes']['SubmitterContactName'])
        #Communication Number Qualifier
        segment.append('TE')
        #Communication Number
        segment.append(self.parameters['1000Aattributes']['SubmitterContactTelephone'])
        #Communication Number Qualifier
        segment.append('EM')
        #Communication Number
        segment.append(self.parameters['1000Aattributes']['SubmitterContactEmail'])
        self.x12segments.append(segment)

        return        

    def add_1000B(self):

        segment = []
        #segment name
        segment.append('NM1')
        #Entity Identifier Code
        segment.append('40')
        #Entity Type Qualifier
        segment.append('2')
        #Name Last or Organization Name
        segment.append(self.parameters['1000Battributes']['ReceiverName'])
        #Name First                
        segment.append('')
        #Name Middle
        segment.append('')
        #Name Prefix
        segment.append('')
        #Name Suffix
        segment.append('')
        #Identification Code Qualifier
        segment.append('46')
        #Identification Code
        segment.append(self.parameters['1000Battributes']['ReceiverETIN'])
        self.x12segments.append(segment)  

    def add_2000A(self):

        self.identify_billingprovider()        
        self.add_2000A_HL1()
        self.add_2000A_HL1()

    def add_2000B(self):
        pass

    def add_2000C(self):
        pass

    def add_SEsegment(self):
        
        segment =[]
        #segment name
        segment.append('SE')
        

        self.x12segments.append(segment)
        pass
