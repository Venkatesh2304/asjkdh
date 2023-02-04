from pylab import *
import numpy as np
from scipy.io import wavfile
from ModemUtils import *
import sys 
from oct_conv import * 

class MFSKModulator(object):
    """ Constant Amplitude/Phase MFSK Modulator Class """
    def __init__(self, sample_rate=8000, base_freq=1000, symbol_rate=31.25, tone_spacing=31.25, start_silence=0, amplitude=0.5):
        self.sample_rate = sample_rate
        self.base_freq = base_freq
        self.symbol_rate = symbol_rate
        self.tone_spacing = tone_spacing
        self.symbol_length = int(sample_rate/symbol_rate)
        self.amplitude = amplitude

        self.phase = int(0)
        self.baseband = np.zeros(start_silence*self.symbol_length)

        self.read_ptr = 0
        self.write_lock = 0

    def read(self,block_size):
        self.write_lock = 1

        samples_available = len(self.baseband) - self.read_ptr
        if(block_size > samples_available):
            # Add silence to baseband output, so we can give data to the consumer
            self.baseband = np.append(self.baseband, np.zeros(block_size - samples_available))

        self.write_lock = 0
        chunk = self.baseband[self.read_ptr:(self.read_ptr + block_size)]
        self.read_ptr = self.read_ptr + block_size

        return chunk

    def write(self, data):
        # In case we have concurrency issues
        while (self.write_lock==1):
            pass

        # Append data onto the end of our baseband array.
        self.baseband = np.append(self.baseband,data)

    def emit_all(self):
        return self.baseband

    def write_wave(self,filename):
        scaled = np.int16(self.baseband * 32767)
        wavfile.write(filename,self.sample_rate,scaled)

    def modulate_symbol(self,symbol_list=0):
        for symb in symbol_list:
            tone_freq = float(self.base_freq) + float(self.tone_spacing)*int(symb)
            x = np.arange(self.phase, self.phase + self.symbol_length, 1)
            symbol = self.amplitude * np.cos(2*np.pi*(tone_freq/self.sample_rate)*x)

            self.write(symbol)

    def modulate_bits(self, symbol_bits, bit_array):
        """ Converts a numpy array of bits (0,1) to gray coded symbols, then transmits them. 
        The array length must be a multiple of the symbol bits.
        """

        # Pad array out to a multiple of symbol_bits
        if(len(bit_array)%symbol_bits > 0):
            bit_array = np.append(bit_array,np.zeros(symbol_bits - len(bit_array)%symbol_bits))

        bit_array = np.reshape(bit_array,(-1,symbol_bits)).astype(np.int8)

        symb_array = []

        for symb in bit_array:
            # Convert array bits to an integer.
            symb_int = symb.dot(1 << np.arange(symb.shape[-1] - 1, -1, -1))
            symb_int = gray_encode(symb_int) # Gray Coding.
            symb_array.append(symb_int)

        self.modulate_symbol(symb_array)
        return symb_array

# Test scripts
if __name__ == "__main__":
    
    mod = MFSKModulator(symbol_rate = 15.625, tone_spacing = 15.625, start_silence=0, base_freq=1500)
    file_length = 512 # symbols
    symbols = binary_to_octal( list(sys.argv[1]) ) 
    symbols = (symbols  + [15]) * 8

    # symbols = [ 1 , 2 , 4 , 5 , 6 , 7 , 8 , 15 ] * 42  # Step 3 tones at a time.
    mod.modulate_symbol(symbols)
    mod.write_wave("mfsk16_3stepped_1500.wav")
    import os 
    os.system("play mfsk16_3stepped_1500.wav & python record.py")

