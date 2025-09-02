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
    plt.plot(t, v, label="Gerilim (V)")
    plt.plot(t, i, label="Akım (A)")
    plt.title("Gerilim ve Akım")
    plt.xlabel("Zaman (s)")
    plt.ylabel("Genlik")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    if save_fig:
        filepath = os.path.join(FIGURE_DIR, "signals.png")
        plt.savefig(filepath, dpi=150)
        print(f"[INFO] Grafik kaydedildi: {filepath}")
    else:
        plt.show()

def plot_power(t, v, i, save_fig=False):
    """
    Anlık gücü hesaplayıp sinyalle birlikte çizer.
    save_fig=True olursa figures klasörüne PNG kaydeder.
    """
    p = v * i
    plt.figure(figsize=(10, 5))
    plt.plot(t, p, label="Anlık Güç (W)", color="red")
    plt.title("Anlık Güç")
    plt.xlabel("Zaman (s)")
    plt.ylabel("Güç (W)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    if save_fig:
        filepath = os.path.join(FIGURE_DIR, "power.png")
        plt.savefig(filepath, dpi=150)
        print(f"[INFO] Grafik kaydedildi: {filepath}")
    else:
        plt.show()
