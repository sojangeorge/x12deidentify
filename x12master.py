from datetime import datetime
from x12testbed import testbed

class x12():

    def __init__(self, delimiter='*', terminator='~', parameters=None) -> None:
        
        self.x12dataset = []
        self.delimiter = delimiter
        self.terminator = terminator
        self.parameters = parameters
        self.processtime = datetime.now()

        self.InterchangeControlNumber = self.processtime.strftime("%d%H%M%S")
        self.GroupControlNumber = self.processtime.strftime("%d%H%M%S")

        self.STSEcounts = 0        

    def add_ISAsegment(self):
        segment = []
        #segment name
        segment.append('ISA')
        #Authorization Information Qualifier
        segment.append('00')
        #Authorization Information
        segment.append('          ')
        #Security Information Qualifier
        segment.append('00')
        #Security Information
        segment.append('          ')       
        #Interchange ID Qualifier
        segment.append('ZZ')
        #Interchange Sender ID
        segment.append(self.parameters['x12attributes']['InterchangeSenderID'].ljust(15))
        #Interchange ID Qualifier
        segment.append('ZZ')
        #Interchange Receiver ID
        segment.append(self.parameters['x12attributes']['InterchangeReceiverID'].ljust(15))
        #Interchange Date                
        segment.append(self.processtime.strftime("%y%m%d"))
        #Interchange Time
        segment.append(self.processtime.strftime("%H%M"))
        #Repetition Separator
        segment.append(self.parameters['x12attributes']['RepetitionSeparator'])
        #Interchange Control Version Number
        segment.append('00501')
        #Interchange Control Number
        segment.append(self.InterchangeControlNumber)
        #Acknowledgment Requested
        segment.append('1')
        #Interchange Usage Indicator
        segment.append(self.parameters['x12attributes']['InterchangeUsageIndicator'])
        #Component Element Separator
        segment.append(self.parameters['x12attributes']['ComponentElementSeparator'])

        self.x12dataset.append(segment)
        return

    def add_IEAsegment(self):
        segment = []
        #segment name
        segment.append('IEA')
        #Authorization Information Qualifier
        segment.append('1')  # this process will only create one GS-GE loop
        #Interchange Control Number
        segment.append(self.InterchangeControlNumber)

        self.x12dataset.append(segment)
        return

    def add_GSsegment(self):

        segment = []
        #segment name
        segment.append('GS')
        #Functional Identifier Code
        segment.append(self.parameters['x12attributes']['GSFunctionalIdentifierCode'])
        #Application Sender’s Code
        segment.append(self.parameters['x12attributes']['InterchangeSenderID'])
        #Application Receiver’s Code
        segment.append(self.parameters['x12attributes']['InterchangeReceiverID'])
        #Date                
        segment.append(self.processtime.strftime("%Y%m%d"))        
        #Time
        segment.append(self.processtime.strftime("%H%M%S"))        
        #Group Control Number
        segment.append(self.GroupControlNumber)
        #Responsible Agency Code
        segment.append('X')
        #Version / Release / Industry Identifier Code
        segment.append(self.parameters['x12attributes']['x12version'])

        self.x12dataset.append(segment)
        return

    def add_GEsegment(self):

        segment = []
        #segment name
        segment.append('GE')
        #Number of Transaction Sets Included
        segment.append(self.STSEcounts)
        #Group Control Number
        segment.append(self.GroupControlNumber)

        self.x12dataset.append(segment)
        return





        
