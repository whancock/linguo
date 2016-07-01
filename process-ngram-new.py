import csv
from graph_tool.all import *
from collections import defaultdict


g = Graph(directed=False)
eprop_dict = g.new_edge_property("int")

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
			eprop_dict[edge] = row[0]






graph_draw(g, vprops=word_map, vertex_font_size=18, output_size=(1000, 1000), output="graph.png")