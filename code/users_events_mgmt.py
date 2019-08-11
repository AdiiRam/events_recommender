import csv
from collections import Counter

class UserEventsMgmt():

    def __init__(self,seedfile):

        self.seedfile = seedfile

        # This will store the User to Events Mapping 
        self.user_events_map = {}

        # This will store the Event to Users Mapping 
        self.event_users_map = {}

        # Initialize the maps 
        self.initialize()
    
    def initialize(self):

        '''
        This will initialize all the maps using the given seedfile 
        '''

        with open(self.seedfile,'r') as fin:

            csvreader = csv.reader(fin)
            # Skip the Header 
            next(csvreader)
            
            for row in csvreader:
                eventid = row[0]
                userid = row[1]
                
                # Update the user_events_map 
                self.user_events_map.setdefault(userid,set()).add(eventid)        
                
                # Update the event_users_map 
                self.event_users_map.setdefault(eventid,set()).add(userid)
        
    
    def get_similar_users(self,user):

        '''
        For the given user , it will get similar users based on the events registered 
        @param : user 
        @returns : Set of users 
        '''
        # Get the Events of the current user 
        cur_events = self.user_events_map.get(user)
        
        # For each event get the set of users 
        similar_users = set()
        for event in cur_events:
            similar_users.update(self.event_users_map.get(event))
                
        similar_users.remove(user)
        return similar_users 
    
    def get_event_recommendations(self,user):

        '''
        For the given user , get the event recommendations 
        @param : user 
        @returns : Dict where Key is event_edition_id , Value of similar users who registered 
        '''

        # Get Similar Users 
        similar_users = self.get_similar_users(user)    
        base_set = self.user_events_map.get(user) 
        similar_events_count = Counter()

        if len(similar_users) > 0:
            for u in similar_users:
                events_set = self.user_events_map.get(u)
                events_set -= base_set
                similar_events_count.update(events_set)
        
        else:
            similar_events_count.update(base_set)
        
        return similar_events_count

