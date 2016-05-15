from geometry import *;

class weighted_edge:
    def __init__(self, fields):
        # head ---cost--> tail
        self.head = fields[0];
        self.cost = fields[1];
        self.tail = fields[2]; 
         
class weighted_graph:
    def __init__(self, edge_list):
        # edge_list has strings of the form: <node> <node> <weight>
        self.nodes = {};
        for i in edge_list:
            fields = i.split();
            if len(fields) == 3:
                edge = weighted_edge(fields);
                if fields[0] not in self.nodes:
                    self.nodes[fields[0]] = [];
                self.nodes[fields[0]].append(edge);
                if fields[2] not in self.nodes:
                    self.nodes[fields[2]] = [];
                self.nodes[fields[2]].append(edge);

    def draw(self, precision = None):
        template_circle = make_circle(10);
        print (template_circle);
        #Silly stuff that could be done better, but that doesn't matter.
        for node, adj in self.nodes.iteritems():
            print node, '{',
            n = len(adj);
            i = 0;
            while i < (n-1):
                print '(', adj[i].tail, ',', adj[i].cost, '), ',
                i += 1;
            if i<n:
                print '(', adj[i].tail, ',', adj[i].cost, ')',
            print '}';



