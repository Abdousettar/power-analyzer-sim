import numpy as np
import pytest
from src.fft_analysis import compute_thd

def test_thd_of_pure_sine():
    fs = 1000
    t = np.arange(0, 1, 1/fs)
    v = np.sin(2 * np.pi * 50 * t)  # saf sinüs
    THD = compute_thd(v, fs)
    assert np.isclose(THD, 0, atol=0.01)  # saf sinüsün THD ≈ 0 olmalı

def test_thd_with_harmonic():
    fs = 1000
    t = np.arange(0, 1, 1/fs)
    # %10 3. harmonik ekle
    v = np.sin(2 * np.pi * 50 * t) + 0.1 * np.sin(2 * np.pi * 150 * t)
    THD = compute_thd(v, fs)
    # %10 harmonik için THD ≈ 0.1 beklenir
    assert 0.08 < THD < 0.12
