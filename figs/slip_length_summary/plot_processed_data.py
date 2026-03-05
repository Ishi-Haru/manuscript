import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
from matplotlib.legend_handler import HandlerErrorbar
from matplotlib.lines import Line2D


# カスタムエラーバーハンドラー（エラーバーなし、マーカーのみ）
class HandlerErrorbarNoLines(HandlerErrorbar):
    def create_artists(self, legend, orig_handle,
                       xdescent, ydescent, width, height, fontsize, trans):
        # マーカーのみを作成
        marker_line = Line2D(
            [width / 2.],
            [height / 2.],
            marker=orig_handle[0].get_marker(),
            markersize=orig_handle[0].get_markersize(),
            markerfacecolor=orig_handle[0].get_markerfacecolor(),
            markeredgecolor=orig_handle[0].get_markeredgecolor(),
            markeredgewidth=orig_handle[0].get_markeredgewidth(),
            linestyle='None'
        )
        marker_line.set_transform(trans)
        return [marker_line]

# matplotlib保存ダイアログのデフォルト保存先をカレントディレクトリに設定
plt.rcParams['savefig.directory'] = os.getcwd()

# フォント設定
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.serif'] = ['Times New Roman']
plt.rcParams['mathtext.fontset'] = 'stix'  # 数式もTimes New Roman風に

# ===== 設定パラメータ =====
# フォントサイズ設定
FONT_SIZE_LEGEND = 10
FONT_SIZE_AXES = 16

# 点線の太さ設定
DASHED_LINEWIDTH = 2

# 凡例設定
LEGEND_LOCATION = 'upper left'  # 'upper left', 'upper right', 'lower left', 'lower right', 'center', etc.
LEGEND_BBOX_TO_ANCHOR = (0.0, 1.0)  # (x, y)で凡例位置を座標指定（0-1の範囲でグラフ内、1.0以上でグラフ外）。例: (0.02, 0.98)は左上内側、Noneの場合はlocのみ使用

# マーカー設定
MARKER_SIZE = 8  # マーカーのサイズ（全基板共通）

# グラフ範囲設定（データに基づいて自動調整するが、ここで上書き可能）
X_MIN = None  # Noneの場合は自動
X_MAX = 130
Y_MIN = -12
Y_MAX = 105


# マーカー・色リスト（十分な数を用意、必要に応じて追加）
MARKERS = ['o', 's', '^', 'D', 'v', 'p', '*', 'h', 'X', 'P', '<', '>', 'd', '+', 'x', 'H', '|', '8', '1', '2', '3', '4', '.', ',', 'H', 'v', '^', '<', '>', '1', '2', '3', '4']
COLORS = [
    '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#bcbd22', '#17becf', '#e7298a',
    '#7f7f7f', '#c7519c', '#ba43b4', '#f07cab', '#00b5d8', '#bc5090', '#ffa600', '#003f5c', '#58508d', '#ff6361',
    '#a05195', '#665191', '#2f4b7c', '#f95d6a', '#ff7c43', '#ffa600', '#b56576', '#6d597a', '#355070', '#eaac8b', '#b56576', '#6d597a', '#355070', '#eaac8b'
]


# CSVファイルを読み込む
csv_path = r"c:\Users\haruy\Desktop\paper\Nano letters\manuscript\figs\slip_length_summary\proccesed_data_for_plot.csv"
df = pd.read_csv(csv_path)

# 数値型に変換
df['contact_angle [degree]'] = pd.to_numeric(df['contact_angle [degree]'], errors='coerce')
df['slip_length [nm]'] = pd.to_numeric(df['slip_length [nm]'], errors='coerce')
df['slip_length_error [nm]'] = pd.to_numeric(df['slip_length_error [nm]'], errors='coerce')
df['contact_angle_error [degree]'] = pd.to_numeric(df['contact_angle_error [degree]'], errors='coerce')

# contact_angleとslip_lengthの両方が存在するデータをフィルタリング
df_plot = df.dropna(subset=['contact_angle [degree]', 'slip_length [nm]']).copy()

# 著者リスト（csv出現順、重複除去）とマーカー・色割当
author_order = []
author_marker_style = {}
marker_count = len(MARKERS)
color_count = len(COLORS)
for idx, a in enumerate(df_plot["author"]):
    a_stripped = a.strip() if isinstance(a, str) else a
    if a_stripped not in author_order:
        author_order.append(a_stripped)
        marker = MARKERS[(len(author_order)-1) % marker_count]
        color = COLORS[(len(author_order)-1) % color_count]
        author_marker_style[a_stripped] = {'marker': marker, 'color': color}

# 理論曲線パラメータ
C_VALUE_MD = 0.41
C_VALUE_EXPERIMENT = 6.0
THEORY_COLOR_MD = 'red'
THEORY_COLOR_EXPERIMENT = 'blue'
# =========================

# CSVファイルを読み込む
csv_path = r"c:\Users\haruy\Desktop\paper\Nano letters\manuscript\figs\slip_length_summary\proccesed_data_for_plot.csv"
df = pd.read_csv(csv_path)

# 数値型に変換
df['contact_angle [degree]'] = pd.to_numeric(df['contact_angle [degree]'], errors='coerce')
df['slip_length [nm]'] = pd.to_numeric(df['slip_length [nm]'], errors='coerce')
df['slip_length_error [nm]'] = pd.to_numeric(df['slip_length_error [nm]'], errors='coerce')
df['contact_angle_error [degree]'] = pd.to_numeric(df['contact_angle_error [degree]'], errors='coerce')

# contact_angleとslip_lengthの両方が存在するデータをフィルタリング
df_plot = df.dropna(subset=['contact_angle [degree]', 'slip_length [nm]']).copy()


def plot_data_points(ax):
    """データ点をプロットする関数(author列の出現順でマーカー・色を割当）"""
    for author in author_order:
        group = df_plot[df_plot["author"].str.strip() == author]
        x = group["contact_angle [degree]"].values
        y = group["slip_length [nm]"].values
        yerr = group["slip_length_error [nm]"].values
        xerr = group["contact_angle_error [degree]"].values
        style = author_marker_style[author]
        color = style['color']
        ax.errorbar(
            x, y,
            xerr=xerr,
            yerr=yerr,
            fmt=style['marker'],
            markersize=MARKER_SIZE,
            markerfacecolor=color,
            markeredgecolor='black',
            markeredgewidth=1,
            ecolor=color,
            elinewidth=1.5,
            capsize=4,
            capthick=1.5,
            label=author,
            alpha=1.0
        )


# グラフ範囲の決定
if X_MIN is None:
    X_MIN = df_plot['contact_angle [degree]'].min() - 5
if X_MAX is None:
    X_MAX = df_plot['contact_angle [degree]'].max() + 5
if Y_MIN is None:
    y_min_data = df_plot['slip_length [nm]'].min()
    y_max_data = df_plot['slip_length [nm]'].max()
    y_margin = (y_max_data - y_min_data) * 0.1
    Y_MIN = y_min_data - y_margin
if Y_MAX is None:
    y_min_data = df_plot['slip_length [nm]'].min()
    y_max_data = df_plot['slip_length [nm]'].max()
    y_margin = (y_max_data - y_min_data) * 0.1
    Y_MAX = y_max_data + y_margin

# 理論曲線の計算
theta_theory = np.linspace(max(1, X_MIN), min(178, X_MAX), 1000)
theta_rad = np.deg2rad(theta_theory)  # ラジアンに変換

# 理論曲線の値を計算
slip_theory_md = C_VALUE_MD / (1 + np.cos(theta_rad))**2
slip_theory_experiment = C_VALUE_EXPERIMENT / (1 + np.cos(theta_rad))**2



# === 出力フォルダ設定 ===
output_dir = os.path.join(os.getcwd(), 'output')
os.makedirs(output_dir, exist_ok=True)

# === プロット本体（凡例なし） ===
fig, ax = plt.subplots()
plot_data_points(ax)
ax.plot(theta_theory, slip_theory_md, '--', linewidth=DASHED_LINEWIDTH, color=THEORY_COLOR_MD, zorder=1, label='C=0.41')
ax.plot(theta_theory, slip_theory_experiment, '--', linewidth=DASHED_LINEWIDTH, color=THEORY_COLOR_EXPERIMENT, zorder=1, label='C=6.0')
ax.set_xlim(X_MIN, X_MAX)
ax.set_ylim(Y_MIN, Y_MAX)
ax.axhline(0, linestyle='--', color='black', linewidth=1, zorder=0, label='_nolegend_')
ax.set_xlabel('Contact angle (degree)', fontsize=FONT_SIZE_AXES)
ax.set_ylabel('Slip length (nm)', fontsize=FONT_SIZE_AXES)
ax.tick_params(axis='both', which='major', labelsize=FONT_SIZE_AXES)

# 凡例を一時的に非表示にして本体のみ保存

# 背景透過・余白最小化で保存
output_path_main = os.path.join(output_dir, 'slip_length_plot_main.svg')
ax.get_legend().remove() if ax.get_legend() else None
plt.savefig(output_path_main, format='svg', dpi=300, bbox_inches='tight', transparent=True, pad_inches=0.01)
print(f"プロット本体を保存しました: {output_path_main}")

# === 凡例のみSVG ===
# 新しいFigureでダミー軸を作り、全著者分のハンドルを生成


# --- データに含まれる著者のみ凡例に出力（author_marker_styleを利用） ---
handles = []
labels = []

for author in author_order:
    style = author_marker_style[author]
    handles.append(Line2D([0], [0], marker=style['marker'], color='w', markerfacecolor=style['color'], markeredgecolor='black', markeredgewidth=1, markersize=MARKER_SIZE, linestyle='None'))
    labels.append(author)

# 理論曲線の凡例ラベル（最後に追加）
handles.append(Line2D([0], [0], linestyle='--', color=THEORY_COLOR_EXPERIMENT, linewidth=DASHED_LINEWIDTH))
labels.append('Eq.2 with C=6.0')
handles.append(Line2D([0], [0], linestyle='--', color=THEORY_COLOR_MD, linewidth=DASHED_LINEWIDTH))
labels.append('Eq.2 with C=0.41')


# 1列で凡例を出力し、枠線を黒にする

# 凡例のみ: 余白最小化・背景透過
fig_legend = plt.figure(figsize=(3.2, 0.5 + 0.32 * len(labels)))
legend_obj = fig_legend.legend(handles, labels, loc='center', ncol=1, fontsize=FONT_SIZE_LEGEND, frameon=True)
legend_obj.get_frame().set_edgecolor('black')
plt.axis('off')
output_path_legend = os.path.join(output_dir, 'slip_length_plot_legend.svg')
fig_legend.savefig(output_path_legend, format='svg', dpi=300, bbox_inches='tight', transparent=True, pad_inches=0.01)
print(f"凡例のみを保存しました: {output_path_legend}")


# データ情報の出力
print(f"\nプロット対象データ数: {len(df_plot)}")
print("\nデータ一覧:")
print(df_plot[['contact_angle [degree]', 'contact_angle_error [degree]', 'slip_length [nm]', 'slip_length_error [nm]', 'author']])

# --- プロットに使われた著者リストとスタイル情報をCSVで保存 ---
import csv
author_style_csv = os.path.join(output_dir, 'slip_length_plot_legend_data.csv')
with open(author_style_csv, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['author', 'marker', 'color'])
    for author in author_order:
        style = author_marker_style[author]
        writer.writerow([author, style['marker'], style['color']])
print(f"凡例著者リストを保存しました: {author_style_csv}")

plt.show()
