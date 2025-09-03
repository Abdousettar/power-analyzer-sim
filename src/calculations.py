import numpy as np

def calculate_rms(signal):
    return np.sqrt(np.mean(signal**2))

def calculate_active_power(v, i):
    return np.mean(v * i)

def calculate_power_factor(v, i):
    P = calculate_active_power(v, i)
    Vrms = calculate_rms(v)
    Irms = calculate_rms(i)
    S = Vrms * Irms
    return P / S if S != 0 else 0.0

def calculate_phase(v, i, fs, f0=50):
 
    N = len(v)
    V = np.fft.fft(v)
    I = np.fft.fft(i)
    freqs = np.fft.fftfreq(N, 1/fs)

    idx = np.argmin(np.abs(freqs - f0))

    phase_v = np.angle(V[idx])
    phase_i = np.angle(I[idx])

    phi_rad = phase_i - phase_v
    phi_deg = np.degrees(phi_rad)

    phi_deg = (phi_deg + 180) % 360 - 180
    phi_rad = np.radians(phi_deg)

    return phi_rad, phi_deg
