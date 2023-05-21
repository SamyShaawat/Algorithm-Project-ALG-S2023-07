# Build the Network
## Explanation of the Code

This code performs the following tasks:

1. Imports necessary libraries: `pandas`, `networkx`, and `matplotlib.pyplot`.
2. Reads data from a CSV file called "dataset.csv" using the `pd.read_csv()` function and stores it in a DataFrame called `df`.
3. Creates an empty graph using the `nx.Graph()` function and assigns it to the variable `graph`.
4. Extracts unique usernames from the 'usernames' column of the DataFrame and stores them in the `users` variable.
5. Adds nodes to the graph for each unique username using the `graph.add_nodes_from()` function.
6. Optimizes the creation of edges by performing the following steps:
   - Creates a dictionary called `user_subs` where each username is mapped to a set of subreddits they participated in.
   - Converts the sets of subreddits to lists within the `user_subs` dictionary.
7. Adds edges to the graph for each combination of users who participated in the same subreddit. It iterates over each user, compares their subreddit lists with other users, finds the common subreddits, and adds an edge between the users with the common subreddits as an attribute.
8. Sets the data type for the 'subreddits' attribute of each edge to a string by using the `nx.set_edge_attributes()` function.
9. Prints the number of nodes and edges in the graph using the `graph.number_of_nodes()` and `graph.number_of_edges()` functions.
10. Saves the graph in GraphML format using the `nx.write_graphml()` function.
11. Draws the graph using NetworkX and saves it as a PNG image:
    - Creates a figure and an axis using `plt.subplots()`.
    - Computes the layout of the graph using the spring layout algorithm with a random seed and a distance parameter.
    - Draws nodes as blue circles with transparency using `nx.draw_networkx_nodes()`.
    - Draws edges as gray lines with transparency using `nx.draw_networkx_edges()`.
    - Draws labels for nodes with a small font size and a sans-serif font using `nx.draw_networkx_labels()`.
    - Turns off the axis using `plt.axis('off')`.
    - Saves the graph as a PNG image using `plt.savefig()`.
12. Displays the graph using `plt.show()`.
13. The code execution ends.
