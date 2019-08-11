### Simple Event Recommendation Engine

#### Introduction 
The Simple Event Recommendation Engine will recommend events for the given User . 

#### Approach 
The Engine provides the recommendations based on the information available to it. 
More specifically for a given user, it takes the below points into consideration

1. Finds similar users based on the events registered 
2. Finds unregistered events based on the similar users determined in Step 1 
3. Finds similar events determined in Step 2 
4. Ranks the resultant events based on the given user's profile and also if its a future event. 

#### Assumptions 

1. Removed the non-essential fields/columns from the Events Sample Dataset. 
2. Removed the non-essential fields/columns from the Transaction Sample Dataset. 
3. Removed the non-essential fields/columns from the User Sample Dataset. 

#### Usage 

The codebase is organized as follows : 

```

├── code
│   ├── events_mgmt.py
│   ├── recommender.py
│   ├── user_mgmt.py
│   ├── users_events_mgmt.py
│   └── utils.py
├── docs
├── README.md
├── requirements.txt
└── resources
    ├── event_dataset.csv
    ├── user_dataset.csv
    └── user_registrations.csv

```

1. The code directory contains all the source python files. 
2. The resources contains all the datasets required by the recommendation engine.
3. requirements.txt lists the dependences to be installed.
4. The docs directory contains documentation if any. 


#### Setting up 

1. First , create virtual environment if needed and activate it. 
2. Install all the dependencies using below command.
```
 pip install -r requirements.txt
```

#### Execution 

From the **code** directory , run the below command 

```python
python3 recommender.py 
```

The engine will prompt for inputs to be provided. 

