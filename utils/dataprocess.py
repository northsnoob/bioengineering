'''
info: --> Auto create header by koroFileHeader <--
Author: Northern NOOB
Mail: northsnoob@gmail.com
Date: 2024-03-01 12:26:19
LastEditors: Northern NOOB
LastEditTime: 2024-03-04 14:27:55
Version: default
'''
import pandas as pd

def printl(**kws):
    for kw in kws:
        print(f'{kw}:{kws[kw]},')
def dic2df(**output_dic):

    newlist = list(output_dic.keys())
    output_df = pd.DataFrame(output_dic,
                             #  index = output_dic_index,
                             columns=newlist)

    # _file_path = f'./test.csv'
    # output_pd.to_csv(_file_path)
    return output_df
class dbg_record:
    def __init__(self,
                 save_path='./log.txt'):
        self.dbg_str = ''
        self.save_path = save_path
    def add(self,_str):
        self.dbg_str += _str + '\n'
    def show(self):
        return self.dbg_str
    def save(self):
        with open(f'{self.save_path}',mode='w') as logtxt:
            logtxt.write(self.dbg_str)
        return True