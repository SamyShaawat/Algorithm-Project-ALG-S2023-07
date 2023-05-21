# Network Analysis of Reddit for Egyptians

This repo contains a network/graph analysis of Reddit users who follow Egyptian subreddits. The goal is to understand the structure and dynamics of the Egyptian Reddit community and to identify the most influential and active users and subreddits.

## Dataset

The dataset consists of 23185 rows and 16 columns. The first column contains the usernames of 23185 Reddit users who follow at least one Egyptian subreddit. The other 15 columns contain the names of the subreddits that each user follows. There are 105 Egyptian subreddits in total.

The dataset was collected by scraping Reddit using the PRAW library.

## Network

The network was constructed from the dataset as follows:

- Nodes: Usernames
- Edges: common Subreddit(s) between two usernames

The network was visualized and analyzed using NetworkX and Graphml.

## The Analysis

The following analyses were performed on the network:

- Degree analysis: to measure the number of edges connected to each node and the average degree of the graph.
- Degree distribution analysis: to examine the frequency distribution of the number of edges per node and compare it with theoretical models such as Poisson, power-law, and exponential.
- Path analysis: to measure the average shortest path length and diameter of the network and compare them with random graphs.
- Centrality analysis: to rank the nodes according to their importance or influence in the network using metrics such as degree centrality, betweenness centrality, closeness centrality, and eigenvector centrality.
- Connected components analysis: to identify the largest connected component and the number of isolated nodes in the network and calculate their fractions of the total nodes.
- Clustering coefficients: to measure the tendency of nodes to form clusters or triangles in the network and compare them with random graphs.
- Density analysis: to measure the ratio of actual edges to possible edges in the network and compare it with random graphs.
- Network type: to classify the network as scale-free, small-world, random, or regular based on its properties such as degree distribution, clustering coefficient, average path length, and diameter.
- Community discovery: to detect groups of nodes that are more densely connected to each other than to the rest of the network using algorithms such as Louvain method, Girvan-Newman method, and Label Propagation method and evaluate their quality using modularity and silhouette scores.
- Dynamic community discovery: to track how communities evolve over time using dynamic network analysis techniques such as temporal snapshots, sliding windows, and event detection.

I hope this helps. 😊

## Folders

The repo contains the following folders:

01. Prepare and Collect the Dataset: contains the code and data for scraping Reddit and creating the dataset.    
    - This folder also contains a subfolder called Subreddits Contains their Usernames, which contains separate files for each subreddit with the usernames that follow them.
02. Build the Network: contains the code and data for constructing the network from the dataset.
03. Degree Distribution Analysis: contains the code and data for analyzing and plotting the degree distribution of the network.
04. Degree analysis: contains the code and data for calculating and displaying the degree of each node in the network.
05. Clustering Coefficients: contains the code and data for computing and visualizing the clustering coefficients of the network.
06. Network Type: contains the code and data for determining and comparing the network type with other types of networks.
07. Centrality Analysis: contains the code and data for computing and ranking the centrality measures of each node in the network.
08. Community Discovery: contains the code and data for applying and evaluating different community detection algorithms on the network.
09. Dynamic Community Discovery: contains the code and data for analyzing how communities change over time in the network.
10. Connected Component Analysis: contains the code and data for identifying and analyzing the connected components of the network.
11. Density Analysis: contains the code and data for calculating and interpreting the density of the network. 
12. Shortest Path Analysis: contains the code and data for finding and displaying the shortest paths between any pair of nodes in the network.

## .gitignore

- This repo contains a .gitignore file that specifies the files and folders that Git should ignore. The main file that is ignored is Network.graphml, which is a large XML file that contains the network structure. This file represents the network as a graph with nodes and edges, where each node corresponds to a username and each edge corresponds to a common subreddit between two usernames. The edge data also contains the list of subreddits that the two usernames follow.
- This file exist in every folder in the repo because it Network.graphml used in every analysis and can not upload it with the repo because it is very big file 
