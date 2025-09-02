# main.py
from src.generate_signals import generate_signals
from src.calculations import (
    calculate_rms,
    calculate_active_power,
    calculate_power_factor,
    calculate_phase
)
from src.visualize import plot_signals, plot_power
from src.fft_analysis import plot_fft, compute_thd

def main():
    # Sinyal üret (harmonik ve gürültü ekleyebilirsin)
    t, v, i = generate_signals(add_harmonics=True, add_noise=True)

    fs = 1000  # örnekleme frekansı

    # Hesaplamalar
    Vrms = calculate_rms(v)
    Irms = calculate_rms(i)
    P = calculate_active_power(v, i)
    PF = calculate_power_factor(v, i)
    phi_rad, phi_deg = calculate_phase(v, i, fs, f0=50)
    THD_v = compute_thd(v, fs)
    THD_i = compute_thd(i, fs)

    # Sonuçları yazdır
    print("=== Güç Analizörü Sonuçları ===")
    print(f"Vrms: {Vrms:.2f} V")
    print(f"Irms: {Irms:.2f} A")
    print(f"Aktif Güç (P): {P:.2f} W")
    print(f"Güç Faktörü (PF): {PF:.3f}")
    print(f"Faz Farkı: {phi_deg:.2f}°")
    print(f"Gerilim THD: {THD_v*100:.2f}%")
    print(f"Akım THD: {THD_i*100:.2f}%")

    # Grafikler
    plot_signals(t, v, i, save_fig=True)
    plot_power(t, v, i, save_fig=True)
    plot_fft(v, fs, title="Gerilim FFT", save_fig=True, filename="fft_voltage.png")
    plot_fft(i, fs, title="Akım FFT", save_fig=True, filename="fft_current.png")

if __name__ == "__main__":
    main()
