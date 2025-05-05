from collections import defaultdict
import numpy as np
import networkx as nx
from networkx.drawing.nx_agraph import graphviz_layout
import matplotlib.pyplot as plt
from instructions import *

class PCFGBuilder:
    def __init__(self, instructions, labels):
        self.instructions = instructions
        self.label_map = {label: idx for idx, label in enumerate(labels)}
        self.graph = defaultdict(dict)  # source_label → {target_label: probability}
        self.instruction_regions = self._compute_instruction_regions()

    def build(self):
        for i, instr in enumerate(self.instructions):
            src_label = self.instruction_regions.get(i)
            if not src_label:
                continue  # ignore unlabeled or unreachable regions
    
            if isinstance(instr, Goto):
                self._add_edge(src_label, instr.target_label, 1.0)
    
            elif isinstance(instr, IfGoto) or isinstance(instr, IfFalseGoto):
                true_target = instr.target_label
                false_target = self._next_label(i)
                if false_target:
                    self._add_edge(src_label, true_target, 1.0)
                    self._add_edge(src_label, false_target, 1.0)
    
            elif isinstance(instr, Flip):
                total = sum(instr.weights)
                for weight, tgt in zip(instr.weights, instr.target_labels):
                    self._add_edge(src_label, tgt, weight / total)
    
            else:
                next_label = self._next_label(i)
                if next_label:
                    self._add_edge(src_label, next_label, 1.0)
    
        return self._to_matrix()

    def _compute_instruction_regions(self):
        regions = {}
        current_label = None
        
        for idx, instr in enumerate(self.instructions):
            if instr.labels:
                current_label = instr.labels[-1]  # take the last label if multiple
            regions[idx] = current_label
        
        return regions


    def _add_edge(self, src, tgt, prob, is_stop=False):
        if is_stop or tgt != src:
            self.graph[src][tgt] = prob

    def _instruction_to_label_map(self):
        """Map instruction indices to their associated label."""
        index_to_label = {}
        for i, instr in enumerate(self.instructions):
            for label in instr.labels:
                index_to_label[i] = label
        return index_to_label

    def _to_matrix(self):
        n = len(self.label_map)
        T = np.zeros((n, n))
        for src_label, edges in self.graph.items():
            i = self.label_map[src_label]
            for tgt_label, prob in edges.items():
                j = self.label_map[tgt_label]
                T[i][j] = prob
        return T
    
    def _next_label(self, index):
        return self.instruction_regions.get(index + 1)

    

    def visualize(self, filename='pcfg.png'):
        G = nx.DiGraph()

        # Add nodes
        for label in self.label_map:
            G.add_node(label)

        # Add edges with weights
        for src_label, targets in self.graph.items():
            for tgt_label, prob in targets.items():
                G.add_edge(src_label, tgt_label, weight=prob, label=f"{prob:.2f}")

        # Use dot with LR direction and increased spacing
        pos = graphviz_layout(
            G,
            prog='dot',
            args='-Grankdir=LR -Gnodesep=1.0 -Granksep=0.75 -Gpackmode=clust -Gpack=true'
        )

        edge_labels = nx.get_edge_attributes(G, 'label')

        NODE_SIZE = 1200
        plt.figure(figsize=(14, 6))  # Wider aspect ratio to help node spread

        # Nodes
        nx.draw_networkx_nodes(G, pos, node_size=NODE_SIZE, node_color='lightgray')

        # Edges with curved connectionstyle to avoid overlap
        nx.draw_networkx_edges(
            G, pos,
            arrowstyle='-|>',
            arrowsize=25,
            edge_color='black',
            connectionstyle='arc3,rad=0.25',
            node_size=NODE_SIZE
        )

        # Labels
        nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red', font_size=9, rotate=False)

        plt.title("Probabilistic Control Flow Graph")
        plt.axis('off')
        plt.tight_layout()
        plt.savefig(filename)
        plt.close()

        print(f"✅ PCFG saved to {filename}")
    
