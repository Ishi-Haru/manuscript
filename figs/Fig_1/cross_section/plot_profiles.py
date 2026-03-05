"""
plot_profiles.py

- 複数のnpyファイル（例: slip_1.npy, topo_1.npy など）から断面形状を選択してプロット
- 実行時にプロットするファイルを選択可能
"""

import os
import csv
import numpy as np
import matplotlib.pyplot as plt

# ====== 設定ここから ======
# プロットするnpyファイル名リスト（カレントディレクトリ相対パス）
PLOT_FILES = [
    # 例: 'slip_1.npy', 'topo_1.npy'
    'topo_1.npy',
    'slip_1.npy',
    'charge_1.npy',
]
# 縦軸範囲（Noneなら自動）
YLIMS_LEFT = (-1e-9, 11e-9)  # 例: (0, 1)
YLIMS_RIGHT = (-2e-9, 2e-9)
# 横軸の範囲指定（Noneなら自動、タプルで指定: (0, 10)など）
X_RANGE = (0, 4)  # 例: (0, 10)
# 文字サイズ
TITLE_FONTSIZE = 16
LABEL_FONTSIZE = 14
TICK_FONTSIZE = 18
LEGEND_FONTSIZE = 12
# 凡例を表示するか
SHOW_LEGEND = False
# 凡例の位置
LEGEND_LOC = 'upper right'
# 図サイズ（幅、高さ）
FIGWIDTH = 8
FIGHEIGHT = 3
# フォント設定
FONT_FAMILY = 'Times New Roman'
# 縦軸をnmでスケーリング（1e9倍）
SCALE_TO_NM = True
# データのオフセット設定（ファイル名ごとに指定、nmスケール後に適用）
DATA_OFFSETS = {
    'topo_1.npy': 2,   # topographyのオフセット
    'slip_1.npy': 0,   # slipのオフセット
    'charge_1.npy': 0, # chargeのオフセット
}
# 描画の色設定
Colors = ['#ff7f0e', '#1f77b4', '#2ca02c']
# 線の太さ設定（ファイル名ごとに指定）
LINE_WIDTHS = {
    'topo_1.npy': 2.0,
    'slip_1.npy': 2.0,
    'charge_1.npy': 2.0,
}
# 線の種類設定（ファイル名ごとに指定）
# '-': 実線, '--': 破線, ':': 点線, '-.': 一点鎖線
LINE_STYLES = {
    'topo_1.npy': '--',
    'slip_1.npy': '-',
    'charge_1.npy': '-',
}
# CSV出力設定（Noneなら出力しない）
CSV_EXPORT_PATH = "plot_profiles_export.csv"
# ====== 設定ここまで ======

if __name__ == "__main__":
    # フォント設定
    plt.rcParams['font.family'] = FONT_FAMILY
    
    selected = PLOT_FILES
    if not selected:
        print("PLOT_FILESが空です")
        exit(1)
    for f in selected:
        if not os.path.exists(f):
            print(f"ファイルが見つかりません: {f}")
            exit(1)
    
    # 2つのグラフを重ねて表示
    fig, ax1 = plt.subplots(figsize=(FIGWIDTH, FIGHEIGHT))
    colors = Colors
    data_series = []  # CSV出力用にプロットに使うデータを保持
    
    # 1つ目のデータは左軸
    arr1 = np.load(selected[0])
    if SCALE_TO_NM:
        arr1 = arr1 * 1e9
    # オフセット適用
    offset1 = DATA_OFFSETS.get(selected[0], 0)
    arr1 = arr1 + offset1
    x_values = np.arange(len(arr1))
    if X_RANGE:
        x_values = np.linspace(X_RANGE[0], X_RANGE[1], len(arr1))
    
    # 線の太さと種類を取得
    linewidth1 = LINE_WIDTHS.get(selected[0], 1.0)
    linestyle1 = LINE_STYLES.get(selected[0], '-')
    ax1.plot(x_values, arr1, color=colors[0], linewidth=linewidth1, linestyle=linestyle1, label=selected[0])
    data_series.append((selected[0], x_values, arr1))
    ax1.tick_params(axis='both', labelsize=TICK_FONTSIZE)
    if YLIMS_LEFT:
        ylims = YLIMS_LEFT
        if SCALE_TO_NM:
            ylims = (ylims[0] * 1e9, ylims[1] * 1e9)
        ax1.set_ylim(*ylims)
    
    # 2つ目のデータは右軸（データが複数ある場合）
    if len(selected) > 1:
        ax2 = ax1.twinx()
        arr2 = np.load(selected[1])
        if SCALE_TO_NM:
            arr2 = arr2 * 1e9
        # オフセット適用
        offset2 = DATA_OFFSETS.get(selected[1], 0)
        arr2 = arr2 + offset2
        x_values2 = np.arange(len(arr2))
        if X_RANGE:
            x_values2 = np.linspace(X_RANGE[0], X_RANGE[1], len(arr2))
        
        # 線の太さと種類を取得
        linewidth2 = LINE_WIDTHS.get(selected[1], 1.0)
        linestyle2 = LINE_STYLES.get(selected[1], '-')
        ax2.plot(x_values2, arr2, color=colors[1], linewidth=linewidth2, linestyle=linestyle2, label=selected[1])
        data_series.append((selected[1], x_values2, arr2))
        ax2.tick_params(axis='both', labelsize=TICK_FONTSIZE)
        # 右軸のデータ範囲（最小/最大）を初期化
        right_min = float(np.min(arr2))
        right_max = float(np.max(arr2))
        
        # 3つ目以降も右軸に追加
        for i, fname in enumerate(selected[2:], start=2):
            arr = np.load(fname)
            if SCALE_TO_NM:
                arr = arr * 1e3
            # オフセット適用
            offset = DATA_OFFSETS.get(fname, 0)
            arr = arr + offset
            x_vals = np.arange(len(arr))
            if X_RANGE:
                x_vals = np.linspace(X_RANGE[0], X_RANGE[1], len(arr))
            # 線の太さと種類を取得
            linewidth = LINE_WIDTHS.get(fname, 1.0)
            linestyle = LINE_STYLES.get(fname, '-')
            ax2.plot(x_vals, arr, color=colors[i % len(colors)], linewidth=linewidth, linestyle=linestyle, label=fname)
            data_series.append((fname, x_vals, arr))
            # 右軸のデータ範囲を更新
            right_min = min(right_min, float(np.min(arr)))
            right_max = max(right_max, float(np.max(arr)))

        # 右軸のy範囲を自動的に包含するように設定（固定範囲が与えられている場合は統合）
        if 'right_min' in locals():
            if YLIMS_RIGHT is None:
                ymin, ymax = right_min, right_max
            else:
                base_min, base_max = YLIMS_RIGHT
                if SCALE_TO_NM:
                    base_min, base_max = base_min * 1e9, base_max * 1e9
                ymin = min(base_min, right_min)
                ymax = max(base_max, right_max)
            # 小さなマージンを追加
            if ymax > ymin:
                pad = 0.05 * (ymax - ymin)
            else:
                pad = 1.0
            ax2.set_ylim(ymin - pad, ymax + pad)

    # CSV出力
    if CSV_EXPORT_PATH:
        max_len = max(len(x_vals) for _, x_vals, _ in data_series)
        headers = []
        for name, _, _ in data_series:
            headers.extend([f"{name}_x", f"{name}_y"])
        with open(CSV_EXPORT_PATH, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(headers)
            for i in range(max_len):
                row = []
                for _, x_vals, y_vals in data_series:
                    if i < len(x_vals):
                        row.extend([x_vals[i], y_vals[i]])
                    else:
                        row.extend(["", ""])
                writer.writerow(row)
    
    # 凡例の表示
    if SHOW_LEGEND:
        lines1, labels1 = ax1.get_legend_handles_labels()
        if len(selected) > 1:
            lines2, labels2 = ax2.get_legend_handles_labels()
            fig.legend(lines1 + lines2, labels1 + labels2, loc=LEGEND_LOC, fontsize=LEGEND_FONTSIZE)
        else:
            ax1.legend(loc=LEGEND_LOC, fontsize=LEGEND_FONTSIZE)
    
    plt.tight_layout()
    plt.show()
