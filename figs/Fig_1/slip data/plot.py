import os
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog

# ===== カラーバー範囲設定定数 =====
COLORBAR_MIN = None  # None の場合は自動設定
COLORBAR_MAX = 200  # None の場合は自動設定
# 例: 固定範囲を使用したい場合
# COLORBAR_MIN = -10.0
# COLORBAR_MAX = 10.0

# ===== ファイル選択ダイアログ =====
root = tk.Tk()
root.withdraw()  # メインウィンドウを非表示

file_path = filedialog.askopenfilename(
    title="プロットする .npy ファイルを選択してください",
    filetypes=[("NumPy files", "*.npy"), ("All files", "*.*")],
    initialdir="."
)

if not file_path:
    print("ファイルが選択されませんでした。")
    exit()

print(f"{os.path.basename(file_path)} を処理中...")

# データ読み込みと z=0 面の抽出
data = np.load(file_path)
if data.ndim < 3 or data.shape[1] <= 0:
    print(f"スキップ: {os.path.basename(file_path)} は (y, z, x) 形式ではありません。")
    exit()

data_2d_raw = data[:, 0, :] * 1e9  # 単位 m → nm
y_size, x_size = data_2d_raw.shape

# IQRによる外れ値除去
flattened = data_2d_raw.flatten()
Q1 = np.percentile(flattened, 25)
Q3 = np.percentile(flattened, 75)
IQR = Q3 - Q1
lower_bound = Q1 - 1000.0 * IQR
upper_bound = Q3 + 1000.0 * IQR
data_2d = np.where((data_2d_raw < lower_bound) | (data_2d_raw > upper_bound), np.nan, data_2d_raw)

# プロットして保存（ラベル・タイトル非表示）
plt.figure(figsize=(6, 5))
img = plt.imshow(data_2d, cmap="viridis", origin="lower", vmin=COLORBAR_MIN, vmax=COLORBAR_MAX)
plt.colorbar(img)
plt.xticks([])
plt.yticks([])
plt.tight_layout()

output_file = os.path.splitext(file_path)[0] + ".jpg"
plt.savefig(output_file, dpi=300)
plt.show()  # 画面に表示
plt.close()
print(f"保存しました: {output_file}")
