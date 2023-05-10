# NetworkAnalysis
Network Analysis for EEPS 1720 final project involving US migration due to natural hazards. For the sake of clarity, each file will be briefly described below:

centrality.ipynb: This jupyter notebook includes all the code to conduct our centrality analysis (calculating various centralities and graphing them).
check_disasters.ipynb: This jupyter notebook takes the raw disaster data and converts it to the aggregated data for the median/mean and 2006 (used for the network analysis).
clustering.ipynb: This jupyter noteboook includes the code to conduct the clustering analysis.
gravity_mod.ipynb: This notebook includes the code to conduct the gravity analysis (OLS).
n_analysis.ipynb: This notebook has the code to create the graph and dataframe for the rest of the network analysis. 
disasters.pickle: The raw disaster data, separated by year. 
disasters_2006.pkl: The disaster data aggregated by state for 2006 --> from the check_disasters notebook.
disasters_mean_median.pkl: The disaster data aggregated for 1990-2011, the median and mean are shown for each state --> from the check_disasters notebook.
graph_2006.p: The 2006 migration graph --> created from the n_analysis notebook.
median_graph.p: The median graph --> created from the n_analysis notebook. 
in_migv2: The raw migration data.
state_distances.csv: The distances between each state.
state_mig_2006.pkl: The migration dataframe for 2006 --> created from the n_analysis notebook.
state_mig_median.pkl: The median migration dataframe --> created from the n_analysis notebook.
