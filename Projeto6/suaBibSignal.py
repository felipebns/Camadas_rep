import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt
from scipy.fftpack import fft
from scipy import signal as window

class signalMeu:
    def __init__(self):
        self.init = 0

    def __init__(self):
        self.init = 0

 
    def calcFFT(self, sinal, fs):
        # https://docs.scipy.org/doc/scipy/reference/tutorial/fftpack.html
        N  = len(sinal)
        W = window.hamming(N)
        T  = 1/fs
        xf = np.linspace(0.0, 1.0/(2.0*T), N//2)
        yf = fft(sinal*W)
        return(xf, np.abs(yf[0:N//2]))

    def plotFFT(self, sinal, fs):
        x,y = self.calcFFT(sinal, fs)
        plt.figure()
        plt.plot(x, np.abs(y))
        plt.title('Fourier')
