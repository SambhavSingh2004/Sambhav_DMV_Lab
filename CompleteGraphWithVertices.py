import networkx as nx
import matplotlib.pyplot as plt

def create_complete_graph():
    try:
        n = int(input("Enter the number of vertices (must be > 3): "))
        
        if n <= 3:
            print("Error: Please enter a number greater than 3.")
            return

        G = nx.complete_graph(n)

        plt.figure(figsize=(8, 6))
        pos = nx.spring_layout(G)
        
        nx.draw(G, pos, 
                with_labels=True, 
                node_color='skyblue', 
                node_size=800, 
                edge_color='gray', 
                font_weight='bold')
        
        plt.title(f"Complete Graph ($K_{{{n}}}$) with {n} Vertices")
        plt.show()

    except ValueError:
        print("Invalid input! Please enter a whole number.")

if __name__ == "__main__":
    create_complete_graph()