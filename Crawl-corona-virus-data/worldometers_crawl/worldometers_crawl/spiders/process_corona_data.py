class process_data:
    def __init__(self,string_data):
        self.string_data = string_data

    def getTitle(self):
        return self.string_data[4:len(self.string_data)-5] 
        
    def getDate(self):
        Date_index_start = self.string_data.find('["')+2
        Date_index_end = self.string_data.find('"]')
        Date = self.string_data[Date_index_start:Date_index_end].split('","')
        return Date#self.string_data[Date_start:Date_end]
    
    def getNumberData(self):
        NumberData_index_start = self.string_data.find('data: [')
        NumberData_index_end = self.string_data.find('responsive')
        
        String = self.string_data[NumberData_index_start:NumberData_index_end]
        NumberData_index_start = String.find('[')+1
        NumberData_index_end = String.find(']')
        
        NumberData =  String[NumberData_index_start:NumberData_index_end].split(',')
        return NumberData
