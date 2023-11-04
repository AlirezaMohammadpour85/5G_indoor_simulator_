import pickle
import matplotlib.pyplot as plt

# # load figure from file
fig = pickle.load(open(f"blers_time_serie_machine610.pickle", "rb"))
fig2 = pickle.load(open(f"blers_time_serie_ue_{ue_dir}.pickle", "rb"))
fig, axs = plt.subplots(2, len_input // 2)

plt.show()
