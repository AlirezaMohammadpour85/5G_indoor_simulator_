import matplotlib.pyplot as plt
from create_bler_list import create_bler_list


def histo_blers_per_gnodb(gnodbs_list:list, bler_values: dict(), ue_dir=None):
    # number of gNodeBs
    # len_input = len(serie)
    # if len(gnodb_postion_lst) % 2 > 0:
    #     len_input -= 1
    # fig, axs = plt.subplots(2, len_input // 2)
    # fig.suptitle(f"BLER time series for UE {ue_dir}")
    max_blers_per_ue_gnb = dict()
    average_blers_per_ue_gnb = dict()
    fig1 = plt.figure()
    fig2 = plt.figure()
    ax1 = fig1.add_subplot(111)
    ax2 = fig2.add_subplot(111)
    gnb_number = 0
    for gnb_name, gnb_bler in bler_values.items():
        if gnb_name in gnodbs_list:
            max_blers_per_ue_gnb[f"UE{ue_dir}"] = {gnb_name: max(gnb_bler)}
            average_blers_per_ue_gnb[f"UE{ue_dir}"] = {gnb_name: sum(gnb_bler) / len(gnb_bler)}
            ax1.bar(f"[{gnb_name.split('_')[1]},{gnb_name.split('_')[2]}]",
                    max_blers_per_ue_gnb[f"UE{ue_dir}"].values())
            ax2.bar(f"[{gnb_name.split('_')[1]},{gnb_name.split('_')[2]}]",
                    average_blers_per_ue_gnb[f"UE{ue_dir}"].values())
            # ax1.bar(gnb_number, max_blers_per_ue_gnb[f"UE{ue_dir}"].values())
            # ax2.bar(gnb_number, average_blers_per_ue_gnb[f"UE{ue_dir}"].values())
            # gnb_number+=1

    ax1.set_xlabel("gNodeBs")
    ax1.set_ylabel("Max BLER")
    ax1.set_title(f"UE{ue_dir}")
    ax1.set_ylim([0,1])

    ax2.set_xlabel("gNodeBs")
    ax2.set_title(f"UE{ue_dir}")
    ax2.set_ylabel("AVG BLER")
    ax2.set_ylim([0,1])





    plt.show()
    # for i in range(len_input):
    #     x_axis = range(len(repeated_serie[i]))
