#!/usr/local/bin/python
from simple_graph import *;

f = open("graph_in");
lines = f.readlines();
g = weighted_graph(lines);
g.draw();