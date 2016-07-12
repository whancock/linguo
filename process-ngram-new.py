import csv
from graph_tool.all import *
from collections import defaultdict


g = Graph(directed=False)
eprop_freq_dict = g.new_edge_property("int")
vprop_name = g.new_vertex_property("string")

word_idx = 0
word_map = {}
pos = set(["nn1", "nn2"])


with open('./coca-ngrams/w2c.txt', newline='') as csvfile:
	spamreader = csv.reader(csvfile, delimiter='\t')
	for row in spamreader:
		if row[3] in pos and row[4] in pos:
			

			if not row[1] in word_map.keys():
				word_map[row[1]] = word_idx
				word_idx += 1

			if not row[2] in word_map.keys():
				word_map[row[2]] = word_idx
				word_idx += 1


			edge = g.add_edge(word_map[row[1]], word_map[row[2]], add_missing=True)
			eprop_freq_dict[edge] = row[0]

			vprop_name[edge.source()] = row[1]
			vprop_name[edge.target()] = row[2]



subgraph_idx = 0
subgraph_map = {}

target_vertex_label = "bank"
subgraph = Graph(directed=False)

vprop_name_subgraph = subgraph.new_vertex_property("string")


target_vertex = g.vertex(word_map[target_vertex_label])

for edge in target_vertex.out_edges():
	#print(edge.source(), edge.target())
	#subgraph.add_edge(edge.source(), edge.target(), add_missing=True)

	if not edge.source() in subgraph_map.keys():
		subgraph_map[edge.source()] = subgraph_idx
		subgraph_idx += 1

	if not edge.target() in subgraph_map.keys():
		subgraph_map[edge.target()] = subgraph_idx
		subgraph_idx += 1

	sub_edge = subgraph.add_edge(subgraph_map[edge.source()], subgraph_map[edge.target()])

	vprop_name_subgraph[sub_edge.source()] = vprop_name[edge.source()]
	vprop_name_subgraph[sub_edge.target()] = vprop_name[edge.target()]






graph_draw(
	subgraph, 
	vertex_text=vprop_name_subgraph, 
	vertex_text_position=0,
	vertex_font_size=10, 
	output_size=(1000, 1000), 
	output="graph.png")