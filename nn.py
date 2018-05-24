import matplotlib.pyplot as plt
import numpy as np

def get_edge_color(x):
    x = 0 if x<-20 else 40 if x>20 else x+20
    return "#{:02x}{:02x}{:02x}".format(int(255*(1-(x/40.))),int(255*(x/40.)),0)

# Modified from https://gist.github.com/craffel/2d727968c3aaebd10359
def draw_neural_net(ax, nodes, edges):
    n_layers = len(nodes)
    n_lengths = [len(n) for n in nodes]
    v_spacing = .8/float(max(n_lengths))
    h_spacing = .8/float(len(nodes) - 1)

    # Nodes
    for n, layer_size in enumerate(n_lengths):
        #layer_size = len(layer_size)
        layer_top = v_spacing*(layer_size - 1)/2. + .5
        for m in range(layer_size):
            circle = plt.Circle((n*h_spacing + .1, layer_top - m*v_spacing), v_spacing/4.,
                                color='w', ec='k', zorder=4)
            ax.add_artist(circle)
    # Edges
    for n, (layer_size_a, layer_size_b) in enumerate(zip(n_lengths[:-1], n_lengths[1:])):
        layer_top_a = v_spacing*(layer_size_a - 1)/2. + .5
        layer_top_b = v_spacing*(layer_size_b - 1)/2. + .5
        for m in range(layer_size_a):
            for o in range(layer_size_b):
                line = plt.Line2D([n*h_spacing + .1, (n + 1)*h_spacing + .1],
                                  [layer_top_a - m*v_spacing, layer_top_b - o*v_spacing], c=get_edge_color(edges[n][m][o]))
                ax.add_artist(line)
