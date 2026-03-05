"""
extract_profile.py

2D numpy配列と線分座標（start, end）を与えると、
その線分上の画素値（断面プロファイル）を抽出して出力する最小モジュール。

使い方例:
  python extract_profile.py data.npy 91.52 87.96 37.33 40.60

出力:
  画素インデックスと値のリストを標準出力
"""
import sys
import numpy as np

from math import hypot

def extract_line_profile(arr, x0, y0, x1, y1, n_points=None, width=1):
    """
    arr: 2D numpy array
    (x0, y0): 始点 (float)
    (x1, y1): 終点 (float)
    n_points: サンプリング点数（Noneならピクセル長さに自動）
    width: 直交方向の平均幅（ピクセル数, 奇数推奨）
    return: (xs, ys, values)
    """
    if n_points is None:
        n_points = int(np.hypot(x1 - x0, y1 - y0)) + 1
    xs = np.linspace(x0, x1, n_points)
    ys = np.linspace(y0, y1, n_points)
    # 直交方向ベクトル
    dx = x1 - x0
    dy = y1 - y0
    length = np.hypot(dx, dy)
    if length == 0:
        raise ValueError("始点と終点が同じです")
    nx = -dy / length  # x方向の法線成分
    ny = dx / length   # y方向の法線成分
    half = width // 2
    values = []
    for x, y in zip(xs, ys):
        vals = []
        for w in range(-half, half + 1):
            px = x + nx * w
            py = y + ny * w
            ix = int(round(px))
            iy = int(round(py))
            if 0 <= ix < arr.shape[1] and 0 <= iy < arr.shape[0]:
                vals.append(arr[iy, ix])
        if vals:
            values.append(np.mean(vals))
        else:
            values.append(np.nan)
    return xs, ys, np.array(values)


# --- 使用例 ---
if __name__ == "__main__":
    import numpy as np
    import matplotlib.pyplot as plt
    # ここでパラメータを直接指定
    npy_path = "FOPA_Pattern_potential.npy"  # 例: slip_20250708-213823_R変更_FOPA_pattern.npy   topo_20250708-213823_R変更_FOPA_pattern.npy
    x0, y0 = 13.44, 97.06  # 始点
    x1, y1 = 87.25, 27.23  # 終点
    width = 10              # 幅（ピクセル, 奇数推奨）
    arr = np.load(npy_path)
    if arr.ndim == 3:
        arr = arr[:, 0, :]
    elif arr.ndim != 2:
        print("2Dまたは3D配列のみ対応")
        exit(1)
    xs, ys, values = extract_line_profile(arr, x0, y0, x1, y1, width=width)
    print("# index\tx\ty\tvalue")
    for i, (x, y, v) in enumerate(zip(xs, ys, values)):
        print(f"{i}\t{x:.2f}\t{y:.2f}\t{v}")
    # 断面形状をnpyファイルで保存
    np.save('profile_output.npy', values)
    print('Profile saved to profile_output.npy')
    # 断面形状をプロット
    plt.figure()
    plt.plot(values)
    plt.title(f"Extracted profile (width={width})")
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.show()
