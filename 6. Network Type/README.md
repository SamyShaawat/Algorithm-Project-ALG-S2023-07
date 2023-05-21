# Network Type

This Python code determines the type of network based on the average degree and average clustering coefficient of the graph. It performs the following steps:

1. Read the average degree and average clustering coefficient from a text file called "Network_Properties.txt" this file content come from Degree of the graph and Clustering Coefficients txt files.
2. Determine the type of network based on the properties.
3. Write the network type to a text file called "Network_Type_results.txt".

The average degree of a graph is the sum of the degrees of all nodes divided by the total number of nodes in the graph. The average clustering coefficient of a node in a graph is the fraction of triangles around that node that are closed. These properties can be used to determine the type of network.

The code reads the average degree and average clustering coefficient from a text file called "Network_Properties.txt". The file contains two lines: one for the average degree and one for the average clustering coefficient. The code reads these lines, extracts the values, and converts them to float values.

Based on the average degree and average clustering coefficient, the code determines the type of network. If the average degree is less than 2, the network is an isolated node. If the average clustering coefficient is less than 0.1, the network is a random network. If the average degree is greater than 10 and the average clustering coefficient is greater than 0.5, the network is a small-world network.Otherwise, the network is a complex network.

After determining the network type, the code writes it to a text file called "Network_Type_results.txt". This file will contain one line with the network type.

Writing the results to a file is important for documenting the analysis and for later reference. Finally, the code prints a message to the console indicating that the network type has been saved to the text file.