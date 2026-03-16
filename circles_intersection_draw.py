import matplotlib.pyplot as plt

def draw_data(circle_1, circle_2):

    fig, ax = plt.subplots()

    c1 = plt.Circle((circle_1["x"], circle_1["y"]), circle_1["r"],
                    fill=False, color="blue")

    c2 = plt.Circle((circle_2["x"], circle_2["y"]), circle_2["r"],
                    fill=False, color="red")

    ax.add_patch(c1)
    ax.add_patch(c2)

    # nastavíme rozsah grafu
    min_x = min(circle_1["x"] - circle_1["r"], circle_2["x"] - circle_2["r"])
    max_x = max(circle_1["x"] + circle_1["r"], circle_2["x"] + circle_2["r"])

    min_y = min(circle_1["y"] - circle_1["r"], circle_2["y"] - circle_2["r"])
    max_y = max(circle_1["y"] + circle_1["r"], circle_2["y"] + circle_2["r"])

    ax.set_xlim(min_x - 1, max_x + 1)
    ax.set_ylim(min_y - 1, max_y + 1)

    ax.set_aspect("equal")
    ax.set_title("Intersection of Circles")

    plt.show()