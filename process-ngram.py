import pandas
from graph_tool.all import *

from math import sqrt

columns = ['count', 'pre', 'post', 'pre-pos', 'post-pos']
index = ['pre', 'post']
df = pandas.read_csv("./coca-ngrams/w2c.txt", delim_whitespace=True, names=columns)


print(df.loc[df['pre'] == "ring"])
print(df.loc[df['post'] == "ring"])



# pre_list = df[['pre']]['pre']
# pre_set = set(pre_list)





# data_ab = df[['pre', 'post']]
# data_bc = df[['post', 'pre']]


# g = Graph(directed=True)
# props_ab = g.add_edge_list(data_ab.values, hashed=True)
# props_bc = g.add_edge_list(data_bc.values, hashed=True)

# name_to_idx_ab = {name: idx for idx,name in enumerate(props_ab)}
# name_to_idx_bc = {name: idx for idx,name in enumerate(props_bc)}


# print(name_to_idx_ab["wedding"])
# print(name_to_idx_bc["wedding"])


# # print(name_to_idx["B-plus"])
# # print(props[g.vertex(10)])


# vertex = g.vertex(name_to_idx["vows"])

# for neighbor in vertex.out_neighbours():
#  	print(props[neighbor])



# graph_draw(ug, vertex_text=ug.vertex_index, vertex_font_size=18, output_size=(1000, 1000), output="graph.png")