import csv
from utils import is_future


class EventsMgmt():

    def __init__(self,events_file):

        self.events_file = events_file        

        # Map to store Event related Information 
        self.event_master_map = {}
        
        # Map to store Events grouped by Cluster 
        self.event_cluster_map = {}

        # Initialize the Maps 
        self.initialize()
    
    def initialize(self):


        with open(self.events_file,'r') as fin:

            csvreader = csv.DictReader(fin)

            # Skip the Header 
            next(csvreader)

            for row in csvreader:

                # Add to the Master Map 
                self.event_master_map[row['event_edition_id']] = row

                # Add to Cluster Map 
                self.event_cluster_map.setdefault(row['cluster'],set()).add(row['event_edition_id'])
                

    def get_similar_events(self,events_set):

        '''
        This will get similar_events for the given events_set based on the clusters they belong to 
        @param : Set of events 
        @returns : List of Event Information 
        '''

        cluster_sets = set()

        for ev in events_set:
            cluster_sets.add(self.event_master_map.get(ev).get('cluster'))
        
        similar_events = set()

        for cluster in cluster_sets:
            similar_events.update(self.event_cluster_map.get(cluster))
        
        # Remove the events_set from similar_events 
        similar_events -= events_set

        # Get Event Details and also ones which are yet to happen in future 
        similar_events_list = []
        for ev in similar_events:
            evinfo = self.event_master_map.get(ev)
            if is_future(evinfo.get('start_date')):                
                similar_events_list.append(evinfo)

        return similar_events_list
    
