# src/visualize.py
import matplotlib.pyplot as plt
import numpy as np
import os

FIGURE_DIR = os.path.join(os.path.dirname(__file__), "..", "figures")
os.makedirs(FIGURE_DIR, exist_ok=True)

def plot_signals(t, v, i, save_fig=False):
    """
    Gerilim ve akım sinyallerini zaman domeninde çizer.
    save_fig=True olursa figures klasörüne PNG kaydeder.
    """
    plt.figure(figsize=(10, 5))
    plt.plot(t, v, label="Voltage (V)")
    plt.plot(t, i, label="Current (A)")
    plt.title("Voltage and Current")
    plt.xlabel("Time (t)")
    plt.ylabel("Amplitude")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    if save_fig:
        filepath = os.path.join(FIGURE_DIR, "signals.png")
        plt.savefig(filepath, dpi=150)
        print(f"[INFO] Graph saved: {filepath}")
    else:
        plt.show()

def plot_power(t, v, i, save_fig=False):
    """
    Anlık gücü hesaplayıp sinyalle birlikte çizer.
    save_fig=True olursa figures klasörüne PNG kaydeder.
    """
    p = v * i
    plt.figure(figsize=(10, 5))
    plt.plot(t, p, label="Instantenous Power (W)", color="red")
    plt.title("Instantenous Power")
    plt.xlabel("Time (t)")
    plt.ylabel("Power (W)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    if save_fig:
        filepath = os.path.join(FIGURE_DIR, "power.png")
        plt.savefig(filepath, dpi=150)
        print(f"[INFO] Graph saved: {filepath}")
    else:
        plt.show()
