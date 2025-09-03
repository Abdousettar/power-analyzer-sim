import numpy as np
import os

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")
os.makedirs(DATA_DIR, exist_ok=True)

def generate_signals(
    Vm=325, Im=10, f=50, phi=np.pi/6, fs=1000, duration=1,
    add_harmonics=False, add_noise=False, save_csv=False
):
  
    t = np.arange(0, duration, 1/fs)

    v = Vm * np.sin(2 * np.pi * f * t)
    i = Im * np.sin(2 * np.pi * f * t + phi)

    if add_harmonics:
        v += 0.1 * Vm * np.sin(2 * np.pi * 3*f * t)
        i += 0.1 * Im * np.sin(2 * np.pi * 3*f * t + phi)

    if add_noise:
        v += 0.02 * Vm * np.random.randn(len(t))
        i += 0.02 * Im * np.random.randn(len(t))

    if save_csv:
        filepath = os.path.join(DATA_DIR, "sample_signals.csv")
        arr = np.column_stack((t, v, i))
        np.savetxt(filepath, arr, delimiter=",", header="time,voltage,current", comments="")
        print(f"[INFO] Sample Signals saved: {filepath}")

    return t, v, i

if __name__ == "__main__":
  
    t, v, i = generate_signals(add_harmonics=True, add_noise=True, save_csv=True)
    print("Time Samples:", t[:5])
    print("Voltage Samples:", v[:5])
    print("Current Samples:", i[:5])
