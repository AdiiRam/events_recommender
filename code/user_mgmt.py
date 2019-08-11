import csv 


class UserMgmt():

    def __init__(self,user_file):

        self.user_file = user_file
        
        # To store the User Information 
        self.user_map = {}

        # Initialize the Map 
        self.initialize()
    
    def initialize(self):

        with open(self.user_file,'r') as fin:

            csvreader = csv.DictReader(fin)

            for row in csvreader:

                self.user_map[row['user_id']] = row
    
    def get_user_info(self,userid):

        return self.user_map.get(userid)
    
