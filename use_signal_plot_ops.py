import signal_plot_ops as sp


signal = sp.load_signal_from_txt("ekg_signal.txt")

print("Average:", sp.signal_avg(signal))

sp.plot_signal(signal)
