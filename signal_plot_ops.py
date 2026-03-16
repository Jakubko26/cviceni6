import matplotlib.pyplot as plt

def load_signal_from_txt(path):
    values = []

    with open(path, "r") as f:
        for line in f:
            values.append(float(line.strip()))

    return values

def signal_min(values):
    return min(values)

def signal_max(values):
    return max(values)

def signal_avg(values):
    return sum(values) / len(values)

def plot_signal(values):
    plt.plot(values)
    plt.title("Signal")
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.show()


if __name__ == "__main__":

    signal = load_signal_from_txt("ekg_signal.txt")

    print("Minimum:", signal_min(signal))
    print("Maximum:", signal_max(signal))
    print("Average:", signal_avg(signal))

    plot_signal(signal)