import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

# matplotlib保存ダイアログのデフォルト保存先をカレントディレクトリに設定
plt.rcParams['savefig.directory'] = os.getcwd()

# フォント設定
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.serif'] = ['Times New Roman']
plt.rcParams['mathtext.fontset'] = 'stix'  # 数式もTimes New Roman風に

# ===== 設定パラメータ =====
# フォントサイズ設定
FONT_SIZE_LEGEND = 12
FONT_SIZE_AXES = 16

# 点線の太さ設定
DASHED_LINEWIDTH = 2

# 凡例設定
LEGEND_LOCATION = 'upper left'  # 'upper left', 'upper right', 'lower left', 'lower right', 'center', etc.
LEGEND_BBOX_TO_ANCHOR = (0.03, 0.85)  # (x, y)で凡例位置を座標指定（0-1の範囲でグラフ内、1.0以上でグラフ外）。例: (0.02, 0.98)は左上内側、Noneの場合はlocのみ使用

# マーカー設定
MARKER_SIZE = 8  # マーカーのサイズ（全基板共通）

# 基板名ラベル設定
SHOW_SUBSTRATE_LABELS = True  # 基板名を点の横に表示するか
LABEL_FONT_SIZE = 9  # 基板名のフォントサイズ
LABEL_OFFSET_X = 3  # X方向のオフセット（度）
LABEL_OFFSET_Y = 2  # Y方向のオフセット（nm）

# グラフ範囲設定（データに基づいて自動調整するが、ここで上書き可能）
X_MIN = -10  # Noneの場合は自動
X_MAX = 160
Y_MIN = -5
Y_MAX = None

# マーカー設定（著者ごと）
MARKER_STYLES = {
    'Zhang et al. 2021': {'marker': 'o', 'color': '#1f77b4'},
    'Bhushan et al. 2009': {'marker': 's', 'color': '#ff7f0e'},
    'Maali et al. 2008': {'marker': '^', 'color': '#2ca02c'},
    'Li et al. 2022': {'marker': 'D', 'color': '#d62728'},
    'Vinogradova & Yakubov 2003': {'marker': 'v', 'color': '#9467bd'},
    'Bonaccurso et al. 2002': {'marker': 'p', 'color': '#8c564b'}
}

# 理論曲線パラメータ
C_VALUE = 0.41
THEORY_COLOR = 'red'
# =========================

# CSVファイルを読み込む
csv_path = r"c:\Users\haruy\Desktop\paper\Nano letters\manuscript\figs\slip_length_summary\slipe_length.csv"
df = pd.read_csv(csv_path, skipinitialspace=True)

# contact_angleとslip_lengthが数値で、どちらも存在するデータをフィルタリング
df_clean = df.copy()
df_clean['contact_angle [degree]'] = pd.to_numeric(df_clean['contact_angle [degree]'], errors='coerce')
df_clean['slip_length [nm]'] = pd.to_numeric(df_clean['slip_length [nm]'], errors='coerce')
df_clean['slip_length_error [nm]'] = pd.to_numeric(df_clean['slip_length_error [nm]'], errors='coerce')

# NaNを除去
df_plot = df_clean.dropna(subset=['contact_angle [degree]', 'slip_length [nm]']).copy()


def plot_data_points(ax):
    """データ点をプロットする関数"""
    # CSVの出現順でauthorリストを作成
    author_order = []
    for a in df_plot["author"]:
        if a not in author_order:
            author_order.append(a)

    for author in author_order:
        group = df_plot[df_plot["author"] == author]
        x = group["contact_angle [degree]"].values
        y = group["slip_length [nm]"].values
        yerr = group["slip_length_error [nm]"].values
        substrates = group["substrate"].values

        style = MARKER_STYLES.get(author, {'marker': 'o', 'color': 'black'})
        color = style['color']

        ax.errorbar(
            x, y,
            yerr=yerr,
            fmt=style['marker'],
            markersize=MARKER_SIZE,
            markerfacecolor=color,
            markeredgecolor='black',
            markeredgewidth=1.5,
            ecolor=color,
            elinewidth=1.5,
            capsize=4,
            capthick=1.5,
            label=author,
            alpha=0.7
        )
        
        # 基板名をラベル表示
        if SHOW_SUBSTRATE_LABELS:
            for xi, yi, substrate in zip(x, y, substrates):
                ax.text(xi + LABEL_OFFSET_X, yi + LABEL_OFFSET_Y, substrate,
                       fontsize=LABEL_FONT_SIZE, color='black',
                       verticalalignment='bottom', horizontalalignment='left')


# 理論曲線の計算
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

theta_theory = np.linspace(max(1, X_MIN), min(178, X_MAX), 1000)
theta_rad = np.deg2rad(theta_theory)  # ラジアンに変換

# 理論曲線の値を計算
slip_theory = C_VALUE / (1 + np.cos(theta_rad))**2

# === プロット: データ点 + 理論曲線 ===
fig, ax = plt.subplots()
plot_data_points(ax)

# 理論曲線
ax.plot(theta_theory, slip_theory, '--', linewidth=DASHED_LINEWIDTH, 
         color=THEORY_COLOR, label=f'C={C_VALUE}', zorder=1)

# 軸の範囲を設定
ax.set_xlim(X_MIN, X_MAX)
ax.set_ylim(Y_MIN, Y_MAX)
# y=0 の黒い破線（凡例に入れない）
ax.axhline(0, linestyle='--', color='black', linewidth=1, zorder=0, label='_nolegend_')

# 軸の目盛りラベルのフォントサイズを設定
ax.tick_params(axis='both', which='major', labelsize=FONT_SIZE_AXES)

# 凡例のみ表示
if LEGEND_BBOX_TO_ANCHOR is not None:
    legend = ax.legend(fontsize=FONT_SIZE_LEGEND, loc=LEGEND_LOCATION, bbox_to_anchor=LEGEND_BBOX_TO_ANCHOR)
else:
    legend = ax.legend(fontsize=FONT_SIZE_LEGEND, loc=LEGEND_LOCATION)
legend.get_frame().set_edgecolor('black')

plt.tight_layout()

# SVG形式で保存
output_path = 'slip_length_plot.svg'
plt.savefig(output_path, format='svg', dpi=300, bbox_inches='tight')
print(f"プロットを保存しました: {output_path}")

print(f"プロット対象データ数: {len(df_plot)}")
print("\nデータ一覧:")
print(df_plot[['substrate', 'contact_angle [degree]', 'slip_length [nm]', 'slip_length_error [nm]', 'author']])
