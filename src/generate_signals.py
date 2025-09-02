# src/generate_signals.py
import numpy as np
import os

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")
os.makedirs(DATA_DIR, exist_ok=True)

def generate_signals(
    Vm=325, Im=10, f=50, phi=np.pi/6, fs=1000, duration=1,
    add_harmonics=False, add_noise=False, save_csv=False
):
    """
    Sentetik gerilim ve akım sinyali üretir.
    Opsiyonel olarak harmonik ve gürültü eklenebilir.

    Parametreler:
    Vm : float -> Gerilimin tepe değeri (ör: 325 V ≈ 230 Vrms)
    Im : float -> Akımın tepe değeri
    f  : float -> Temel frekans (Hz)
    phi: float -> Faz farkı (radyan)
    fs : int   -> Örnekleme frekansı (Hz)
    duration : float -> Süre (saniye)
    add_harmonics : bool -> True ise 3. harmonik eklenir
    add_noise : bool -> True ise küçük rastgele gürültü eklenir
    save_csv : bool  -> True ise data/ klasörüne CSV kaydeder

    Dönen:
    t : numpy array -> Zaman dizisi
    v : numpy array -> Gerilim sinyali
    i : numpy array -> Akım sinyali
    """
    t = np.arange(0, duration, 1/fs)

    # Temel sinyaller
    v = Vm * np.sin(2 * np.pi * f * t)
    i = Im * np.sin(2 * np.pi * f * t + phi)

    # 3. harmonik ekle (örneğin %10 genlik)
    if add_harmonics:
        v += 0.1 * Vm * np.sin(2 * np.pi * 3*f * t)
        i += 0.1 * Im * np.sin(2 * np.pi * 3*f * t + phi)

    # Gürültü ekle (örneğin sinyalin %2’si kadar)
    if add_noise:
        v += 0.02 * Vm * np.random.randn(len(t))
        i += 0.02 * Im * np.random.randn(len(t))

    if save_csv:
        filepath = os.path.join(DATA_DIR, "sample_signals.csv")
        arr = np.column_stack((t, v, i))
        np.savetxt(filepath, arr, delimiter=",", header="time,voltage,current", comments="")
        print(f"[INFO] Örnek sinyaller kaydedildi: {filepath}")

    return t, v, i

if __name__ == "__main__":
    # Hem harmonik hem gürültü eklenmiş test
    t, v, i = generate_signals(add_harmonics=True, add_noise=True, save_csv=True)
    print("Zaman örnekleri:", t[:5])
    print("Gerilim örnekleri:", v[:5])
    print("Akım örnekleri:", i[:5])
