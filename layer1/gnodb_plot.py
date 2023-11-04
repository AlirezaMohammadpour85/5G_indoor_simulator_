import matplotlib.pyplot as plt


def gnodb_plot(gnodb_postion_lst, tile_postion_list, ue=[1, 1], machine_tile=None, machine_3d=True, scenario_16=False):
    x_list = []
    y_list = []
    machine_height = 5  ### Fixme: Given as input make it dynamic
    machine_size = 3  ### Fixme: Given as input make it dynamic
    x_gnob_lst = []
    y_gnob_lst = []
    z_gnob_lst = []
    if scenario_16:
        gnodb_postion_lst = [[i, j] for i in [1, 50, 75, 100] for j in [1, 50, 75, 100]]

    for i in tile_postion_list:
        x = i[0]
        y = i[1]
        x_list.append(x)
        y_list.append(y)
    for i in gnodb_postion_lst:
        x_gnodb = i[0]
        y_gnodb = i[1]
        x_gnob_lst.append(x_gnodb)
        y_gnob_lst.append(y_gnodb)
    plt.figure(1)
    plt.scatter(x_list, y_list)

    z_gnob_lst = [10] * len(y_gnob_lst)  # height 0f gnob are 10

    plt.scatter(x_gnob_lst, y_gnob_lst, s=40, label="gNodeB")
    plt.scatter(ue[0], ue[1], s=70, marker="^", label=f"UE[{ue[0]},{ue[1]}]")
    # if machine_tile is not None:
    #     plt.scatter(tile_postion_list[machine_tile][0], tile_postion_list[machine_tile][1], marker='X', s=150,
    #                 label=f"Machine[{int(tile_postion_list[machine_tile][0])}, {int(tile_postion_list[machine_tile][1])}]")

    plt.xlabel("x (m)")
    plt.ylabel("y (m)")
    # plt.colorbar()title(f'Postion of gNodeBs ')
    plt.legend()

    # plt.legend(bbox_to_anchor=(1.004, 1), loc="upper left")
    plt.show()

    if machine_3d:
        plt.figure(2)
        ax2 = plt.axes(projection='3d')
        ax2.scatter(x_gnob_lst, y_gnob_lst, z_gnob_lst, s=40, label="gNodeB")
        ax2.scatter(ue[0], ue[1], s=70, marker='^', label=f"UE[{ue[0]},{ue[1]}]")

        # add small path for machine with length of 10
        length = len(range(20, int(tile_postion_list[machine_tile][1])))
        ax2.scatter([(1 if length == 0 else length) * [tile_postion_list[machine_tile][0]]],
                    # [i+tile_postion_list[machine_tile][1] for i in range(0,20)],
                    [i + 21 for i in range(0, length)],
                    s=10, marker='s', label=f"Machine path" if length > 1 else "")

        # connected lines from UE to gNBs
        if scenario_16:
            for i in range(0, len(y_gnob_lst)):
                ax2.plot([ue[0], x_gnob_lst[i]], [ue[1], y_gnob_lst[i]], [0, 10], 'b', linewidth=1,
                         label="LOS" if i == 0 else "")
        else:
            for i in range(0, len(y_gnob_lst)):  # -3 0r -2
                if i == 0:
                    ax2.plot([ue[0], x_gnob_lst[i]], [ue[1], y_gnob_lst[i]], [0, 10], 'b',
                             label="LOS" if i == 0 else "")
                elif i == 1 and machine_tile < 615:
                    ax2.plot([ue[0], x_gnob_lst[i]], [ue[1], y_gnob_lst[i]], [0, 10], 'r--',
                             label='NLOS' if i == 1 else "")
                elif i == 2 and machine_tile < 620:
                    ax2.plot([ue[0], x_gnob_lst[i]], [ue[1], y_gnob_lst[i]], [0, 10], 'r--')
                else:
                    ax2.plot([ue[0], x_gnob_lst[i]], [ue[1], y_gnob_lst[i]], [0, 10], 'b',
                             label="LOS" if i == 0 else "")

        # ax2.scatter(x_list, y_list, color = 'blue' )
        ax2.plot(
            [tile_postion_list[machine_tile][0] - machine_size / 2,
             tile_postion_list[machine_tile][0] - machine_size / 2],
            [tile_postion_list[machine_tile][1] - machine_size / 2,
             tile_postion_list[machine_tile][1] + machine_size / 2],
            [machine_height, machine_height], color='red', label=f"Machine[{int(tile_postion_list[machine_tile][0])},"
                                                                 f" {int(tile_postion_list[machine_tile][1])}]")
        ax2.plot(
            [tile_postion_list[machine_tile][0] - machine_size / 2,
             tile_postion_list[machine_tile][0] + machine_size / 2],
            [tile_postion_list[machine_tile][1] - machine_size / 2,
             tile_postion_list[machine_tile][1] - machine_size / 2],
            [machine_height, machine_height], color='red')
        ax2.plot(
            [tile_postion_list[machine_tile][0] + machine_size / 2,
             tile_postion_list[machine_tile][0] + machine_size / 2],
            [tile_postion_list[machine_tile][1] - machine_size / 2,
             tile_postion_list[machine_tile][1] + machine_size / 2],
            [machine_height, machine_height], color='red')
        ax2.plot(
            [tile_postion_list[machine_tile][0] - machine_size / 2,
             tile_postion_list[machine_tile][0] + machine_size / 2],
            [tile_postion_list[machine_tile][1] + machine_size / 2,
             tile_postion_list[machine_tile][1] + machine_size / 2],
            [machine_height, machine_height], color='red')
        # bottom
        ax2.plot(
            [tile_postion_list[machine_tile][0] - machine_size / 2,
             tile_postion_list[machine_tile][0] - machine_size / 2],
            [tile_postion_list[machine_tile][1] - machine_size / 2,
             tile_postion_list[machine_tile][1] + machine_size / 2],
            [0, 0], color='red')
        ax2.plot(
            [tile_postion_list[machine_tile][0] - machine_size / 2,
             tile_postion_list[machine_tile][0] + machine_size / 2],
            [tile_postion_list[machine_tile][1] - machine_size / 2,
             tile_postion_list[machine_tile][1] - machine_size / 2],
            [0, 0], color='red')
        ax2.plot(
            [tile_postion_list[machine_tile][0] + machine_size / 2,
             tile_postion_list[machine_tile][0] + machine_size / 2],
            [tile_postion_list[machine_tile][1] - machine_size / 2,
             tile_postion_list[machine_tile][1] + machine_size / 2],
            [0, 0], color='red')
        ax2.plot(
            [tile_postion_list[machine_tile][0] - machine_size / 2,
             tile_postion_list[machine_tile][0] + machine_size / 2],
            [tile_postion_list[machine_tile][1] + machine_size / 2,
             tile_postion_list[machine_tile][1] + machine_size / 2],
            [0, 0], color='red')
        # # connect squares to shape cube
        ax2.plot(
            [tile_postion_list[machine_tile][0] - machine_size / 2,
             tile_postion_list[machine_tile][0] - machine_size / 2],
            [tile_postion_list[machine_tile][1] - machine_size / 2,
             tile_postion_list[machine_tile][1] - machine_size / 2],
            [0, 5], color='red')
        ax2.plot(
            [tile_postion_list[machine_tile][0] - machine_size / 2,
             tile_postion_list[machine_tile][0] - machine_size / 2],
            [tile_postion_list[machine_tile][1] + machine_size / 2,
             tile_postion_list[machine_tile][1] + machine_size / 2],
            [0, 5], color='red')
        ax2.plot(
            [tile_postion_list[machine_tile][0] + machine_size / 2,
             tile_postion_list[machine_tile][0] + machine_size / 2],
            [tile_postion_list[machine_tile][1] - machine_size / 2,
             tile_postion_list[machine_tile][1] - machine_size / 2],
            [0, 5], color='red')
        ax2.plot(
            [tile_postion_list[machine_tile][0] + machine_size / 2,
             tile_postion_list[machine_tile][0] + machine_size / 2],
            [tile_postion_list[machine_tile][1] + machine_size / 2,
             tile_postion_list[machine_tile][1] + machine_size / 2],
            [0, 5], color='red')
        plt.title("Factory size=[100,100,10]")
        ax2.set_xlabel('X (m)')
        ax2.set_ylabel("Y (m)")
        ax2.set_zlabel("Z (m)")
        ax2.set_ylim([0, 100])
        ax2.set_xlim([0, 100])
        # handle doublicated labels in legend
        # handles, labels = plt.gca().get_legend_handles_labels()
        # by_label = dict(zip(labels, handles))
        # plt.legend(by_label.values(), by_label.keys(),fontsize=9)
        plt.legend(fontsize=13)
        plt.show()
        # Fixme: Sample of plotting machines like cubes follow this sample to plot machines
        # x_ls = range(0, 100, 2)
        # y_ls = range(0, 100, 2)
        # X, Y = np.meshgrid(x_ls, y_ls)
        # ax2 = plt.axes(projection='3d')
        # ax2.scatter(X, Y)
        # # plot point at top
        # ax2.plot([0, 0], [0, 3], [5, 5], color='red')
        # ax2.plot([0, 3], [0, 0], [5, 5], color='red')
        # ax2.plot([3, 3], [0, 3], [5, 5], color='red')
        # ax2.plot([0, 3], [3, 3], [5, 5], color='red')
        # # plot point at low height
        # ax2.plot([0, 0], [0, 3], [0, 0], color='red')
        # ax2.plot([0, 3], [0, 0], [0, 0], color='red')
        # ax2.plot([3, 3], [0, 3], [0, 0], color='red')
        # ax2.plot([0, 3], [3, 3], [0, 0], color='red')
        # # connect squares to shape cube
        # ax2.plot([0, 0], [0, 0], [0, 5], color='red')
        # ax2.plot([0, 0], [3, 3], [0, 5], color='red')
        # ax2.plot([3, 3], [0, 0], [0, 5], color='red')
        # ax2.plot([3, 3], [3, 3], [0, 5], color='red')
