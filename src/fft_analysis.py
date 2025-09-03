import numpy as np
import matplotlib.pyplot as plt
import os

FIGURE_DIR = os.path.join(os.path.dirname(__file__), "..", "figures")
os.makedirs(FIGURE_DIR, exist_ok=True)

def compute_fft(signal, fs):

    N = len(signal)
    fft_vals = np.fft.fft(signal)
    fft_vals = np.abs(fft_vals[:N // 2]) * (2 / N)  
    freqs = np.fft.fftfreq(N, d=1/fs)[:N // 2]
    return freqs, fft_vals

def compute_thd(signal, fs, f0=50, nharmonics=5):
   
    freqs, spectrum = compute_fft(signal, fs)

    f1_idx = np.argmin(np.abs(freqs - f0))
    V1 = spectrum[f1_idx]

    harmonic_powers = 0
    for n in range(2, nharmonics+1):
        idx = np.argmin(np.abs(freqs - n*f0))
        harmonic_powers += spectrum[idx]**2

    THD = np.sqrt(harmonic_powers) / V1 if V1 != 0 else 0
    return THD

def plot_fft(signal, fs, title="FFT Spectrum", save_fig=False, filename="fft.png"):
    freqs, spectrum = compute_fft(signal, fs)

    plt.figure(figsize=(10,5))
    plt.stem(freqs, spectrum, basefmt=" ")
    plt.title(title)
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Amplitude")
    plt.xlim(0, 500)  
    plt.grid(True)
    plt.tight_layout()

    if save_fig:
        filepath = os.path.join(FIGURE_DIR, filename)
        plt.savefig(filepath, dpi=150)
        print(f"[INFO] FFT graph saved: {filepath}")
    else:
        plt.show()
