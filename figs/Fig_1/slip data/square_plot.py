import os
import numpy as np
import matplotlib.pyplot as plt
from typing import Optional

# =============================
# square_plot モジュール
# 指定した .npy (形状 (y, z, x) 想定) の z スライスを読み込み
# 外れ値処理後に正方形へパディングして描画 / 保存するユーティリティ
# =============================

__all__ = [
    "load_npy_slice",
    "pad_to_square",
    "select_line_on_array",
    "select_line_on_npy",
    "extract_profile_along_line",
]
import matplotlib
from matplotlib.lines import Line2D
from matplotlib.figure import Figure
from matplotlib.axes import Axes
def extract_profile_along_line(arr: np.ndarray, p0: tuple, p1: tuple, n_points: int = None) -> np.ndarray:
    """
    arr: 2D ndarray
    p0, p1: (y, x) int tuples (start, end)
    n_points: number of samples (default: max(|dx|,|dy|)+1)
    Returns: 1D ndarray of sampled values (with nan if out of bounds)
    """
    y0, x0 = p0
    y1, x1 = p1
    dy = y1 - y0
    dx = x1 - x0
    if n_points is None:
        n_points = int(max(abs(dx), abs(dy))) + 1
    y_vals = np.linspace(y0, y1, n_points)
    x_vals = np.linspace(x0, x1, n_points)
    # Bilinear interpolation (with nan for out-of-bounds)
    from scipy.ndimage import map_coordinates
    coords = np.vstack([y_vals, x_vals])
    profile = map_coordinates(arr, coords, order=1, mode='nearest')
    return profile

def load_npy_slice(file_path: str, z_index: int = 0, unit_scale: float = 1e9,
                   iqr_k: float = 1000.0) -> np.ndarray:
    """指定 .npy から (y, z, x) 配列を読み z_index スライス (y, x) を取得し単位変換と外れ値除去。

    Parameters
    ----------
    file_path : str
        読み込む .npy ファイルパス
    z_index : int, default 0
        抽出する z スライス index
    unit_scale : float, default 1e9
        倍率 (m -> nm など)
    iqr_k : float, default 1000.0
        IQR に対する許容係数 (非常に緩く設定)

    Returns
    -------
    np.ndarray
        外れ値を NaN に置換した (y, x) 2D 配列 (float64)
    """
    data = np.load(file_path)
    if data.ndim < 3:
        raise ValueError(f"想定形式 (y, z, x) ではありません: {data.shape}")
    if not (0 <= z_index < data.shape[1]):
        raise IndexError(f"z_index {z_index} が範囲外 (0..{data.shape[1]-1})")

    arr = data[:, z_index, :].astype(float) * unit_scale  # m→nm
    flat = arr.flatten()
    q1, q3 = np.percentile(flat, [25, 75])
    iqr = q3 - q1
    lower = q1 - iqr_k * iqr
    upper = q3 + iqr_k * iqr
    arr = np.where((arr < lower) | (arr > upper), np.nan, arr)
    return arr

def pad_to_square(arr: np.ndarray, fill_value=np.nan) -> np.ndarray:
    """短い辺をパディングして正方行列にする（中央寄せ）。"""
    if arr.ndim != 2:
        raise ValueError("2次元配列のみ対応")
    y, x = arr.shape
    if y == x:
        return arr
    size = max(y, x)
    out = np.full((size, size), fill_value, dtype=arr.dtype)
    y_off = (size - y) // 2
    x_off = (size - x) // 2
    out[y_off:y_off + y, x_off:x_off + x] = arr
    return out

###############################################################
#  インタラクティブ線分選択機能のみを提供
#  マウス: 押下 -> ドラッグ -> 離す で線分を選択
#  再度ドラッグすると前回選択を上書き
###############################################################

def select_line_on_array(arr: np.ndarray, cmap: str = "viridis", title: Optional[str] = None):
    """2D 配列上で線分（始点, 終点）を選択し、最新の 1 本を返す。再ドラッグで上書き。
    選択線分上の断面形状を別ウィンドウにプロットする。
    Returns
    -------
    ((int,int),(int,int)) | None
        ( (y0, x0), (y1, x1) )  元の arr 座標（パディング除去後）/ 未選択 None
    """
    if arr.ndim != 2:
        raise ValueError("2D 配列のみ対応")

    y, x = arr.shape
    size = max(y, x)
    y_off = (size - y) // 2
    x_off = (size - x) // 2
    sq = pad_to_square(arr)

    # メイン画像ウィンドウ
    fig, ax = plt.subplots(figsize=(5, 5))
    cmap_obj = plt.get_cmap(cmap).copy()
    cmap_obj.set_bad(color="black")
    im = ax.imshow(sq, origin="lower", cmap=cmap_obj)
    ax.set_xticks([])
    ax.set_yticks([])
    if title:
        ax.set_title(title)
    plt.colorbar(im, fraction=0.046, pad=0.04)
    plt.tight_layout()

    # プロファイル用ウィンドウ
    prof_fig, prof_ax = plt.subplots(figsize=(6, 3))
    prof_ax.set_title("選択線分上の断面形状")
    prof_ax.set_xlabel("Pixel index (along line)")
    prof_ax.set_ylabel("Value")
    prof_line, = prof_ax.plot([], [], 'b-')
    prof_ax.grid(True)
    prof_fig.tight_layout()

    # --- エクスポートボタン追加 ---
    from matplotlib.widgets import Button
    import tkinter as tk
    from tkinter import filedialog
    profile_data = {"arr": np.array([])}

    def export_profile(event=None):
        # 現在の profile_data["arr"] を npy で保存
        if profile_data["arr"].size == 0:
            print("エクスポートするデータがありません")
            return
        # Tkinter でファイルダイアログ
        root = tk.Tk()
        root.withdraw()
        fname = filedialog.asksaveasfilename(
            defaultextension=".npy",
            filetypes=[("NumPy array", ".npy")],
            title="断面形状データの保存先を選択",
            initialfile="profile_export.npy"
        )
        root.destroy()
        if fname:
            np.save(fname, profile_data["arr"])
            print(f"エクスポートしました: {fname}")
        else:
            print("保存をキャンセルしました")

    # matplotlib 3.5以降は layout='constrained' でボタン位置が崩れにくい
    btn_ax = prof_fig.add_axes([0.8, 0.82, 0.15, 0.12])  # [left, bottom, width, height]
    export_btn = Button(btn_ax, 'エクスポート', color='#e0e0e0', hovercolor='#ffcccb')
    export_btn.on_clicked(export_profile)

    line = Line2D([], [], color='red', linewidth=1.5)
    ax.add_line(line)

    state = {"press_raw": None, "last": None}

    def _inside_original(py: float, px: float):
        yi = int(round(py))
        xi = int(round(px))
        if yi < 0 or xi < 0 or yi >= size or xi >= size:
            return None
        oy = yi - y_off
        ox = xi - x_off
        if 0 <= oy < y and 0 <= ox < x:
            return oy, ox
        return None

    def on_press(event):
        if event.button != 1 or event.inaxes != ax:
            return
        if event.ydata is None or event.xdata is None:
            return
        orig = _inside_original(event.ydata, event.xdata)
        if orig is None:
            return
        state["press_raw"] = (event.ydata, event.xdata, orig)
        # 初期化
        line.set_data([event.xdata, event.xdata], [event.ydata, event.ydata])
        fig.canvas.draw_idle()

    def on_move(event):
        if state["press_raw"] is None:
            return
        if event.inaxes != ax or event.ydata is None or event.xdata is None:
            return
        y0d, x0d, _ = state["press_raw"]
        line.set_data([x0d, event.xdata], [y0d, event.ydata])
        fig.canvas.draw_idle()

    def on_release(event):
        if event.button != 1 or state["press_raw"] is None:
            return
        if event.ydata is None or event.xdata is None:
            state["press_raw"] = None
            return
        orig_end = _inside_original(event.ydata, event.xdata)
        if orig_end is None:
            state["press_raw"] = None
            return
        y0d, x0d, orig0 = state["press_raw"]
        y1d, x1d = event.ydata, event.xdata
        y0, x0 = orig0
        y1, x1 = orig_end
        # orig_end is only defined in this scope, so use it here
        state["last"] = ((y0, x0), (y1, x1))
        print("--- 線分選択 ---")
        print(f"表示座標: start=({y0d:.2f},{x0d:.2f}) -> end=({y1d:.2f},{x1d:.2f})")
        print(f"配列インデックス: start=(y={y0}, x={x0}) end=(y={y1}, x={x1})")
        v0 = arr[y0, x0]
        v1 = arr[y1, x1]
        print(f"値: start={v0}, end={v1}")
        # プロファイル抽出・表示
        profile = extract_profile_along_line(arr, (y0, x0), (y1, x1))
        profile_data["arr"] = profile
        prof_line.set_data(np.arange(len(profile)), profile)
        prof_ax.relim()
        prof_ax.autoscale_view()
        prof_fig.canvas.draw_idle()
        state["press_raw"] = None

    print("左クリック->ドラッグ->離す で線分。再度ドラッグで上書き。ウィンドウを閉じると終了。\n断面形状は別ウィンドウに表示されます。")
    fig.canvas.mpl_connect('button_press_event', on_press)
    fig.canvas.mpl_connect('motion_notify_event', on_move)
    fig.canvas.mpl_connect('button_release_event', on_release)
    plt.show()
    plt.close(prof_fig)

    return state["last"]

def select_line_on_npy(file_path: str, z_index: int = 0, cmap: str = "viridis"):
    """指定 .npy の z スライス上で線分を選択し最終結果を返す。"""
    arr = load_npy_slice(file_path, z_index=z_index)
    return select_line_on_array(arr, cmap=cmap, title=f"{os.path.basename(file_path)}  z={z_index}")

def interactive_select_and_plot(directory: str = ".", z_index: int = 0):
    """ディレクトリ内の .npy を列挙し番号選択して表示。"""
    files = [f for f in os.listdir(directory) if f.endswith('.npy')]
    if not files:
        print("npy が見つかりません。")
        return
    print("=== ファイル一覧 ===")
    for i, f in enumerate(files):
        print(f"[{i}] {f}")
    sel = input(f"表示する番号 (0 - {len(files)-1}): ")
    try:
        idx = int(sel)
    except ValueError:
        print("数値を入力してください。")
        return
    if not (0 <= idx < len(files)):
        print("範囲外です。")
        return
    target = os.path.join(directory, files[idx])
    print(f"表示: {target}")
    # 以前は表示のみ機能があったが削除したため、ここでは線分選択に直接誘導
    print("線分選択モードに入ります (閉じると終了)")
    select_line_on_npy(target, z_index=z_index)

if __name__ == "__main__":  # 簡単デモ: 最初の npy に対して線分選択
    files = [f for f in os.listdir('.') if f.endswith('.npy')]
    if not files:
        print("npy がありません")
    else:
        select_line_on_npy(files[0], z_index=0)
