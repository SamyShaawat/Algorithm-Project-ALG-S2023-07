# Community Discovery
## Explanation of the Code

The provided code performs the following tasks:

1. The code imports the necessary libraries: networkx for graph operations, community for community detection, and matplotlib.pyplot for visualization.

2. The graph is loaded from a GraphML file using nx.read_graphml() and assigned to the graph variable.

3. The Louvain algorithm is applied to detect communities in the graph using community.best_partition(graph). The result is stored in the partition dictionary, where each node is mapped to its corresponding community ID.

4. The number of communities is calculated by finding the maximum community ID in the partition dictionary and adding 1.

5. The number of communities is printed to the console using print(f"Number of communities: {num_communities}").

6. The community assignment is saved to a text file named Community_Discovery_result.txt. The file is opened in write mode using open('Community_Discovery_result.txt', 'w') and assigned to the file handle f. The partition dictionary is iterated using for node, community_id in partition.items(), and each node's ID and its corresponding community ID are written to the file using f.write(f"Node {node}: Community {community_id}\n").

7. The layout for visualization is computed using nx.spring_layout(graph), and assigned to the pos variable.

8. The colormap for communities is defined using plt.cm.get_cmap('viridis', num_communities), and assigned to the cmap variable.

9. The nodes of the graph are drawn with colors corresponding to their community assignments using nx.draw_networkx_nodes(graph, pos, node_color=list(partition.values()), cmap=cmap).

10. The edges of the graph are drawn using nx.draw_networkx_edges(graph, pos).

11. The plot is displayed using plt.show().