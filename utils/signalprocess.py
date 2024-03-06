'''
info: --> Auto create header by koroFileHeader <--
Author: Northern NOOB
Mail: northsnoob@gmail.com
Date: 2024-03-01 13:50:44
LastEditors: Northern NOOB
LastEditTime: 2024-03-01 13:53:47
Version: default
'''
import numpy as np
class fftbuffer:
    def __init__(self, maxsize=480, fft_n=2048,datatype=np.float64):
        self.input_max_size = maxsize
        self.input_count = 0
        self.fft_n_size = fft_n
        # self.signal_input = np.zeros(maxsize)
        self.fft_input = np.zeros(fft_n,dtype=datatype)
        self.fft_output = ''

    def append_data(self, _data):
        self.fft_input[1:self.input_max_size] = self.fft_input[0:self.input_max_size-1]
        self.fft_input[0] = _data
        self.input_count += 1

    @property
    def get_fftinput(self):
        return self.fft_input
    
    @property
    def get_fftoutput(self):
        return self.fft_output
    
    def clear(self):
        self.fft_input = np.fill(0)
        self.fft_output = ''
        self.input_count = 0



def index2bpm(index, SAMPLE_RATE=30, FFT_N=1024):
    return index * (SAMPLE_RATE / FFT_N) * 60


def bpm2index(bpm, SAMPLE_RATE=30, FFT_N=1024):
    return int(bpm / ((SAMPLE_RATE / FFT_N) * 60))


def pushSig(sig, new):
    sig[:-1] = sig[1:]
    sig[-1] = new
    return sig