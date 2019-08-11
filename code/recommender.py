from user_mgmt import UserMgmt
from users_events_mgmt import UserEventsMgmt
from events_mgmt import EventsMgmt
from utils import readable_date_format
import click

class Recommender():

    def __init__(self,user_file,user_registrations_file,event_file):

        self.user_file = user_file
        self.user_registrations_file = user_registrations_file
        self.event_file = event_file

        self.user_mgmt = None 
        self.user_event_mgmt = None 
        self.event_mgmt = None 

        self.initialize()
    
    def initialize(self):

        print('Setting up the Engine --started')
        # Instantiate the respective user and event managers 
        self.user_mgmt = UserMgmt(self.user_file)

        self.user_event_mgmt = UserEventsMgmt(self.user_registrations_file)

        self.event_mgmt = EventsMgmt(self.event_file)

        print('Setting up the Engine --complete')
    
    def recommend(self,user,no_of_recs=3):

        # Check if the given user exists or not 
        userinfo = self.user_mgmt.get_user_info(user)
        if userinfo:

            # Get the Probable Event Recommendations 
            candidate_events = self.user_event_mgmt.get_event_recommendations(user)

            # Get the final Event Recommendations 
            final_events = self.event_mgmt.get_similar_events(set(candidate_events))

            # Rank the Events based on User Profile 
            event_rankings_list = []
            for ev in final_events:
                city = ev.get('city')
                if city.lower() == userinfo['city'].lower():
                    ev['rank'] = 100
                else:
                    ev['rank'] = 50
                event_rankings_list.append(ev)
            
            # Sort the Events based on the ranks 
            event_rankings_list.sort(key=lambda x: x['rank'], reverse=True)

            ct = 1
            print('\n')
            print('Welcome {}'.format(user))
            if len(event_rankings_list) > 0:
                
                print('Here are our top {} recommendations \n'.format(no_of_recs))
                for ev in event_rankings_list[:no_of_recs]:
                    
                    
                    print('Recommendation : {}'.format(ct))
                    print('Event Name : {}'.format(ev['event_name']))
                    print('Event Category : {}'.format(ev['event_category']))
                    print('Registration Type : {}'.format(ev['registration_type']))
                    print('Venue : {}'.format(ev['venue']))
                    print('Event Tags : {}'.format(ev['event_tags']))
                    print('Start Date : {}'.format(readable_date_format(ev['start_date'])))
                    print('End Date : {}'.format(readable_date_format(ev['end_date'])))
                    print('--------')
                    ct +=1
            
                print('\n')
                print('\n')
            else:
                print('Sorry, the Engine could not generate any recommendations due to insufficient data')
        
        else:

            print('Given user : {} does not exist in our registry'.format(user))

    
if __name__ == '__main__':

    user_file = '../resources/user_dataset.csv'
    event_file = '../resources/event_dataset.csv'
    user_registrations_file = '../resources/user_registrations.csv'
    recommender = Recommender(user_file,user_registrations_file,event_file)

    print('Welcome to Events Recommendation System ')   

    no_of_recommendations = click.prompt('Enter the Number of Recommendations to show. Default is 3',default=3,type=int)


    while True:

        user = click.prompt('Please enter the User for whom to recommend. To stop , provide -1')
        if user == '-1':
            print('Shutting the Engine')
            break
        
        user = user.strip()
        recommender.recommend(user,no_of_recs=no_of_recommendations)



        







