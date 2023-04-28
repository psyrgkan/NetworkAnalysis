import pandas as pd
import scipy.spatial
import us

# load csv with states' data. 
# this csv is included in this gist. 
# Data taken from https://en.wikipedia.org/wiki/List_of_geographic_centers_of_the_United_States#Updated_list_of_geographic_centers
# Coordinates correspond to Updated geographic centers of the states of the United States and Washington, DC
statesDF = pd.read_csv('states.csv');

# create distances dataframe
distancesDF = pd.DataFrame(columns=["state1", "state2", "distance"])

# Line 22 can be modified to calculate whichever distance is preferred. 
# See available options at 
# https://docs.scipy.org/doc/scipy/reference/spatial.distance.html#module-scipy.spatial.distance


# Define a function to get the abbreviation of a state name
def get_state_abbreviation(state_name):
    state = us.states.lookup(state_name)
    return state.abbr if state else state_name

# get the abbreviation of each state
statesDF['state'] = statesDF['state'].apply(get_state_abbreviation)

for state1, lat1, lon1 in zip(statesDF.state, statesDF.latitude, statesDF.longitude):
    for state2, lat2, lon2 in zip(statesDF.state, statesDF.latitude, statesDF.longitude):
        distancesDF = distancesDF.append({
            "state1": state1,
            "state2": state2,
            "distance": scipy.spatial.distance.euclidean([float(lat1), float(lon1)], [float(lat2), float(lon2)])
            }, ignore_index=True);

distancesDF.to_csv('state_distances.csv', index=False);
