import tkinter as tk
from tkinter import filedialog
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import RectangleSelector

# --- 設定 ---
REMOVE_OUTLIERS = False  # 外れ値処理のオン/オフ（True: 処理する, False: 処理しない）
LOWER_BOUND = -100      # 外れ値の下限（nm）
UPPER_BOUND = 100       # 外れ値の上限（nm）

# --- ファイル選択 ---
def select_npy_file():
    root = tk.Tk()
    root.withdraw()
    return filedialog.askopenfilename(
        title="npyファイルを選択してください",
        filetypes=[("NumPy files", "*.npy")],
        initialdir="."
    )

# --- メイン処理 ---
file_path = select_npy_file()
if not file_path:
    print("ファイルが選択されませんでした。")
    exit()

data = np.load(file_path)
if data.ndim == 3 and data.shape[1] == 1:
    data_2d_raw = data[:, 0, :]
elif data.ndim == 2:
    data_2d_raw = data
else:
    raise ValueError("2D または (y, 1, x) の3D配列のみ対応しています。")

# nmにスケーリング
data_2d_raw *= 1e9

# 外れ値処理
if REMOVE_OUTLIERS:
    data_2d = np.where((data_2d_raw < LOWER_BOUND) | (data_2d_raw > UPPER_BOUND), np.nan, data_2d_raw)
else:
    data_2d = data_2d_raw

# --- 選択コールバック ---
def onselect(eclick, erelease):
    x1, x2 = int(eclick.xdata), int(erelease.xdata)
    y1, y2 = int(eclick.ydata), int(erelease.ydata)
    xmin, xmax = sorted([x1, x2])
    ymin, ymax = sorted([y1, y2])
    xmin = max(0, xmin)
    xmax = min(data_2d.shape[1], xmax)
    ymin = max(0, ymin)
    ymax = min(data_2d.shape[0], ymax)
    selected = data_2d[ymin:ymax, xmin:xmax]
    mean_val = np.nanmean(selected)
    print(f"選択範囲の平均値: {mean_val:.5f}")

# --- 表示 ---
fig, ax = plt.subplots()
cax = ax.imshow(data_2d, cmap='viridis', origin='upper')
fig.colorbar(cax)
ax.set_title("任意の領域をドラッグして選択")

selector = RectangleSelector(
    ax,
    onselect,
    useblit=True,
    button=[1],
    minspanx=1,
    minspany=1,
    spancoords='pixels',
    interactive=True
)

plt.show()
