"""
最小限のnpyカラーマップ表示＋線分選択ツール
実行するとカレントディレクトリのnpyファイル一覧から選択
2Dまたは3D(y,z,x)のz=0スライスをカラーマップ表示
左ドラッグで線分選択、ESCで終了
"""
from __future__ import annotations

import os
import sys
import argparse
from typing import Optional
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


def load_slice(path: str) -> np.ndarray:
    data = np.load(path)
    if data.ndim == 2:
        return data
    elif data.ndim == 3:
        return data[:, 0, :]
    else:
        raise ValueError("2Dまたは3D配列のみ対応")

def plot_colormap(arr2d: np.ndarray):
    fig, ax = plt.subplots()
    ax.imshow(arr2d, cmap="viridis", origin="lower")
    ax.set_xticks([])
    ax.set_yticks([])
    fig.tight_layout()
    return fig, ax


if __name__ == "__main__":
    npy_files = [f for f in os.listdir('.') if f.endswith('.npy')]
    if not npy_files:
        print(".npyファイルが見つかりません")
        sys.exit(1)
    print("利用可能なnpyファイル:")
    for i, f in enumerate(npy_files):
        print(f"  [{i}] {f}")
    idx = input("番号を選択: ").strip()
    if not idx.isdigit() or not (0 <= int(idx) < len(npy_files)):
        print("不正な入力")
        sys.exit(1)
    path = npy_files[int(idx)]
    arr2d = load_slice(path)
    fig, ax = plot_colormap(arr2d)
    line = None
    while True:
        print("2点を順にクリックしてください（始点→終点、Enterで終了）")
        pts = plt.ginput(2, timeout=0)
        if len(pts) == 2:
            (x0, y0), (x1, y1) = pts
            if line is not None:
                line.remove()
            line, = ax.plot([x0, x1], [y0, y1], color='red', linewidth=2)
            print(f"start=({x0:.2f}, {y0:.2f}) -> end=({x1:.2f}, {y1:.2f})")
            plt.draw()
        else:
            print("終了します")
            break
    plt.show()
