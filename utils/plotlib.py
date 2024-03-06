'''
info: --> Auto create header by koroFileHeader <--
Author: Northern NOOB
Mail: northsnoob@gmail.com
Date: 2024-03-01 12:24:11
LastEditors: Northern NOOB
LastEditTime: 2024-03-01 12:55:09
Version: default
'''
import matplotlib.pyplot as plt
import numpy as np

def nor(sig):
    min = sig.min()
    sig = sig - min
    max = sig.max()
    sig = sig / (max+1e-10)
    return sig

def plotfft(fft_records, gt, processHR, VIDEO_FPS, test_name, folder):

    plt.close()

    fft_record = fft_records.copy()
    print(fft_record.shape)
    print('id: fft_record',id(fft_record))

    fft_record = np.transpose(fft_record)
    print(fft_record.shape)
    
    # fft_record = fft_record_t.copy()
    print('id: fft_record',id(fft_record))
    
    # print(f"fft_n = {fft_n}")
    fft_n = 1024
    low_index = int(40 / ((30) * 60 / fft_n))
    high_index = int(200 / ((30) * 60 / fft_n))
    # fft_record = fft_record[low_index:high_index, :]
    # fft_record = fft_record[low_index:high_index, :]
    
    # print(low_index, high_index)
    for i in range(fft_record.shape[1]):
        # for i in range(VIDEO_FPS*60*12):
        fft_record[:, i] = nor(fft_record[:, i])
    # print(len(fft_record[:,0]))
    fig, ax1 = plt.subplots()
    fig.set_size_inches(18, 9)
    # fig.set_size_inches(10, 6)
    plt.xlabel("Second", fontsize="10")
    ax2 = ax1.twinx()
    fig.suptitle(test_name, fontsize=16)

    
    im = ax1.pcolormesh(fft_record[:, :], norm=colors.PowerNorm(vmin=0, vmax=1, gamma=1.4/1.),
                        cmap="inferno")
    plt.colorbar(im, ax=ax1)
    ax1.axes.get_yaxis().set_visible(False)
    # values = ['0', '120', '240', '360', '480', '600', '720']

    ax2.axis(xmin=VIDEO_FPS*0, xmax=VIDEO_FPS*300)

    lim = VIDEO_FPS*8*1
    ananp = np.arange(0, lim+1, lim/8)
    xnp = np.arange(0, 8+1, 1)
    plt.xticks(ananp, xnp, label='second')
    # 這裡這裡這裡這裡這裡這裡這裡這裡這裡這裡這裡這裡這裡這裡這裡這裡這裡這裡這裡這裡
    srang1 = [0, 8]  # <--------------------

    ax2.axis(xmin=VIDEO_FPS*srang1[0], xmax=VIDEO_FPS*srang1[1])

    # ananp = np.arange(0, 15600-13800+1, (15600-13800)/6)
    # xnp = np.arange(460, 520+1, 10)

    # plt.xticks(ananp, xnp, /label='second')
    # plt.xticks(values)
    # sec2frame = np.arange(0, VIDEO_FPS * (len(gt)), VIDEO_FPS)
    ax2.axis(ymin=40, ymax=200)
    plt.xlabel("Second", fontsize="10")
    plt.ylabel("BPM", fontsize="10")
    # print(sec2frame)
    # path.check_dir(f"{folder}/ori")
    # plt.savefig(f"{folder}/ori/{test_name}_{srang1[0]}-{srang1[1]}s_ori.png")
    # print(x_peaks)
    # ax2.plot(sec2frame, np.array(x_peaks)*60*30/1024, color=(0.95, 0, 0, 1),label='x_peaks')
    # ax2.plot(sec2frame, np.array(y_peaks)*60*30/1024, color=(1.0, 1.0, 1.0, 1),label='y_peaks')
    plt.axhline(y=40, color='r', linestyle='--', label='BPM=40')
    # ax2.plot(range(len(x_peaks)), np.array(x_peaks)*60*30/1024, color=(0.95, 0, 0, 1),label='xpeaks')
    # ax2.plot(range(len(y_peaks)), np.array(y_peaks)*60*30/1024, color=(1.0, 1.0, 1.0, 1),label='ypeaks')
    # ax2.plot(range(len(z_peaks)), np.array(z_peaks)*60*30/1024, color=(0.5, 1.0, 1.0, 1),label='zpeaks')
    # x_m = np.array(x_peaks)*60*30/1024
    # y_m = np.array(y_peaks)*60*30/1024
    # z_m = np.array(z_peaks)*60*30/1024

    
    
    
    # print(y_peaks)
    
    # ax2.plot(sec2frame, processHR, color=(1, 0.8, 1, 1))
    # ax2.scatter(sec2frame, gt, color=(
    #     0, 0.9, 1, 1), s=2**2, label='GroundTruth')
    
    
    # sec2frame = np.arange(0+30*8, 30 * (len(processHR))+30*8, 30)
    # ax2.scatter(sec2frame, processHR, color=(
    #     0, 1, 0.1, 1), s=2**2, label='processHR')

    ax2.legend()

    plt.show()

    plt.clf()