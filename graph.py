import matplotlib.pyplot as plt

traffic = []

def update_graph(count):

    traffic.append(count)

    plt.clf()
    plt.plot(traffic)
    plt.title("MyShark Live Traffic")
    plt.xlabel("Packets")
    plt.ylabel("Traffic")

    plt.pause(0.01)
