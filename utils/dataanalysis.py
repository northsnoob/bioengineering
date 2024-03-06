'''
info: --> Auto create header by koroFileHeader <--
Author: Northern NOOB
Mail: northsnoob@gmail.com
Date: 2024-03-06 07:08:02
LastEditors: Northern NOOB
LastEditTime: 2024-03-06 07:09:49
Version: default
'''
import numpy as np
def getResult(_gt,_predic,rnd=2,datatype=np.float32):
    # gt = np.array(_gt,dtype='uint8').astype(np.float32)
    gt = np.array(_gt,dtype=datatype)
    predic = np.array(_predic,dtype=datatype)
    # indices_to_keep = np.where(gt != 255)
    # gt = gt[indices_to_keep]
    # predic = predic[indices_to_keep]
    # print(gt)
    # print(predic)
    e = gt - predic
    ae = np.abs(e)
    mae = np.mean(ae)
    se = np.power(e,2)
    mse = np.mean(se)
    rmse = pow(mse,0.5)
    num_of_ae = len(ae)
    sr5  = len(ae[ae<=5]) / num_of_ae  *100
    sr10 = len(ae[ae<=10]) / num_of_ae *100
    sr25 = len(ae[ae<=25]) / num_of_ae *100
    srs = [np.where(ae <= t, 1, 0).mean() for t in range(0, 11)]
    out_dic = {
        'MAE':round(mae,rnd),
        'RMSE':round(rmse,rnd),
        'SR-5':round(sr5,rnd),
        'SR-10':round(sr10,rnd),
        'SR-25':round(sr25,rnd),
        'SRs':srs
    }
    return out_dic

def getAvg(_arr,rnd=3,datatype=np.float32):
    arr = np.array(_arr,dtype=datatype)
    # print(arr)
    arr = arr[~np.isnan(arr)]
    avg = np.mean(arr)
    return round(avg,rnd)
    