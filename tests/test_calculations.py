import numpy as np
import pytest
from src.calculations import (
    calculate_rms,
    calculate_active_power,
    calculate_power_factor,
    calculate_phase
)

def test_rms_of_sine():
    fs = 1000
    t = np.arange(0, 1, 1/fs)
    v = np.sin(2 * np.pi * 50 * t)
    Vrms = calculate_rms(v)
    assert np.isclose(Vrms, 1/np.sqrt(2), atol=0.01)

def test_active_power_pure_resistive():
    fs = 1000
    t = np.arange(0, 1, 1/fs)
    v = np.sin(2 * np.pi * 50 * t)
    i = np.sin(2 * np.pi * 50 * t)  
    P = calculate_active_power(v, i)
    assert np.isclose(P, 0.5, atol=0.01)

def test_power_factor_cos_phi():
    fs = 1000
    t = np.arange(0, 1, 1/fs)
    v = np.sin(2 * np.pi * 50 * t)
    i = np.sin(2 * np.pi * 50 * t + np.pi/6)  
    PF = calculate_power_factor(v, i)
    assert np.isclose(PF, np.cos(np.pi/6), atol=0.05)

def test_phase_detection():
    fs = 1000
    t = np.arange(0, 1, 1/fs)
    v = np.sin(2 * np.pi * 50 * t)
    i = np.sin(2 * np.pi * 50 * t + np.pi/4) 
    phi_rad, phi_deg = calculate_phase(v, i, fs)
    assert np.isclose(phi_deg, 45, atol=5)  
