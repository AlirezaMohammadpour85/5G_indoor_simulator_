import pickle
import matplotlib.pyplot as plt

def load_figures():
# # load figure from file
    figz,_ = pickle.load(open(f"blers_time_serie_ue_11.pickle", "rb"))
    figx,_ = pickle.load(open(f"blers_time_serie_ue_610.pickle", "rb"))
    data = {
        "data1" : figx.axes[0].lines[0].get_data(),
        "data2" : figx.axes[1].lines[0].get_data(),
        "data3" : figx.axes[2].lines[0].get_data(),
        "data4" : figx.axes[3].lines[0].get_data(),
        "data5" : figx.axes[4].lines[0].get_data(),
        "data6" : figx.axes[5].lines[0].get_data(),
        "dataf1" : figz.axes[0].lines[0].get_data(),
        "dataf2" : figz.axes[1].lines[0].get_data(),
        "dataf3" : figz.axes[2].lines[0].get_data(),
        "dataf4" : figz.axes[3].lines[0].get_data(),
        "dataf5" : figz.axes[4].lines[0].get_data(),
        "dataf6" : figz.axes[5].lines[0].get_data(),
    }

    return data

data = load_figures()
print(data["data1"])
fig, ax = plt.subplots(2,3)
fig.suptitle(f"BLER time series for UE [25, 1, 0]")

ax[0,0].plot(data["data1"][0],data["data1"][1], label="Machine at tile 610")
ax[0,0].plot(data["dataf1"][0],data["dataf1"][1], label = "Avg. LOS BLER")
ax[0,0].legend(loc='upper right', fontsize=6)

ax[0,1].plot(data["data2"][0],data["data2"][1], label="Machine at tile 610")
ax[0,1].plot(data["dataf2"][0],data["dataf2"][1], label = "Avg. LOS BLER")
ax[0,1].legend(loc='upper right', fontsize=6)

ax[0,2].plot(data["data3"][0],data["data3"][1], label="Machine at tile 610")
ax[0,2].plot(data["dataf3"][0],data["dataf3"][1], label = "Avg. LOS BLER")
ax[0,2].legend(loc='upper right', fontsize=6)

ax[1,0].plot(data["data4"][0],data["data4"][1], label="Machine at tile 610")
ax[1,0].plot(data["dataf4"][0],data["dataf4"][1], label = "Avg. LOS BLER")
ax[1,0].legend(loc='upper right', fontsize=6)

ax[1,1].plot(data["data5"][0],data["data5"][1], label="Machine at tile 610")
ax[1,1].plot(data["dataf5"][0],data["dataf5"][1], label = "Avg. LOS BLER")
ax[1,1].legend(loc='upper right', fontsize=6)

ax[1,2].plot(data["data6"][0],data["data6"][1], label="Machine at tile 610")
ax[1,2].plot(data["dataf6"][0],data["dataf6"][1], label = "Avg. LOS BLER")
ax[1,2].legend(loc='upper right', fontsize=6)

gnb_ls = {
    1: "[25,25]",
    2: "[25,50]",
    3: "[25,75]",
    4: "[75,25]",
    5: "[75,50]",
    6: "[75,75]",
    
}
sel=1
for i in [0,1]:
    for j in [0,1,2]:
        ax[i, j].set_title(f"gNodeB {gnb_ls[sel]}")
        ax[i, j].set(xlabel=f"Each step = 100 $\Delta t$", ylabel="BLER")
        ax[i, j].set_ylim([0, 1])
        sel+=1

fig.tight_layout(h_pad=2)
plt.show()



