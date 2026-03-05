import os
import numpy as np
import matplotlib.pyplot as plt

def plot_cross_section_npy(file_path: str):
    """
    指定した .npy (1D array) をプロット
    """
    arr = np.load(file_path)
    if arr.ndim != 1:
        raise ValueError(f"1次元配列ではありません: {file_path}")
    plt.figure(figsize=(8, 4))
    plt.plot(np.arange(len(arr)), arr, '-o', markersize=3)
    plt.title(os.path.basename(file_path))
    plt.xlabel("Pixel index (along line)")
    plt.ylabel("Value")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # cross_section ディレクトリ内の npy を列挙
    dir_path = os.path.join(os.path.dirname(__file__), "cross_section")
    npy_files = [f for f in os.listdir(dir_path) if f.endswith('.npy')]
    if not npy_files:
        print("cross_section に .npy ファイルがありません")
    else:
        for i, f in enumerate(npy_files):
            print(f"[{i}] {f}")
        idx = input(f"番号を選択 (0-{len(npy_files)-1}): ")
        try:
            idx = int(idx)
            if 0 <= idx < len(npy_files):
                plot_cross_section_npy(os.path.join(dir_path, npy_files[idx]))
            else:
                print("範囲外です")
        except Exception as e:
            print(f"エラー: {e}")
