import matplotlib.pyplot as plt
import os

FIGURE_DIR = os.path.join(os.path.dirname(__file__), "figures")
os.makedirs(FIGURE_DIR, exist_ok=True)

formulas = {
    "rms": r"$V_{rms} = \sqrt{\frac{1}{T} \int_0^T v^2(t)\,dt}$",
    "active_power": r"$P = V_{rms} \cdot I_{rms} \cdot \cos\varphi$",
    "reactive_power": r"$Q = V_{rms} \cdot I_{rms} \cdot \sin\varphi$",
    "thd": r"$THD = \frac{\sqrt{V_2^2 + V_3^2 + \dots}}{V_1}$"
}

for name, formula in formulas.items():
    fig, ax = plt.subplots(figsize=(6, 1))
    ax.text(0.5, 0.5, formula, fontsize=20, ha="center", va="center")
    ax.axis("off")
    filepath = os.path.join(FIGURE_DIR, f"{name}_formula.png")
    plt.savefig(filepath, dpi=150, bbox_inches="tight", transparent=True)
    plt.close()
    print(f"[INFO] Kaydedildi: {filepath}")
