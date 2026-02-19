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
LEGEND_BBOX_TO_ANCHOR = (0.0, 1.0)  # (x, y)で凡例位置を座標指定（0-1の範囲でグラフ内、1.0以上でグラフ外）。例: (0.02, 0.98)は左上内側、Noneの場合はlocのみ使用

# マーカー設定
MARKER_SIZE = 8  # マーカーのサイズ（全基板共通）

# グラフ範囲設定（データに基づいて自動調整するが、ここで上書き可能）
X_MIN = None  # Noneの場合は自動
X_MAX = None
Y_MIN = None
Y_MAX = None

# マーカー設定（著者ごと）
MARKER_STYLES = {
    'Zhang et al. 2021': {'marker': 'o', 'color': '#1f77b4'},
    'Bhushan et al. 2009': {'marker': 's', 'color': '#ff7f0e'},
    'Maali et al. 2008': {'marker': '^', 'color': '#2ca02c'},
    'Li et al. 2022': {'marker': 'D', 'color': '#d62728'},
    'Vinogradova & Yakubov 2003': {'marker': 'v', 'color': '#9467bd'},
    'Bonaccurso et al. 2002': {'marker': 'p', 'color': '#8c564b'},
    'Cottin-Bizonne et al. 2005': {'marker': '*', 'color': '#e377c2'},
    'Honig & Ducker 2007': {'marker': 'h', 'color': '#bcbd22'},
    'Chen et al. 2019': {'marker': 'X', 'color': '#17becf'},
    'Jing & Bhushan 2013': {'marker': 'P', 'color': '#e7298a'},
    'Young et al. 2013': {'marker': '<', 'color': '#7f7f7f'},
    'Han et al. 2025': {'marker': '>', 'color': '#c7519c'},
    'Zhu et al. 2011': {'marker': 'd', 'color': '#ba43b4'},
    'Scarratt et al. 2019': {'marker': '+', 'color': '#f07cab'},
    'Ahmad et al. 2015': {'marker': 'x', 'color': '#00b5d8'}
}

# 理論曲線パラメータ
C_VALUE = 0.41
THEORY_COLOR = 'red'
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
    """データ点をプロットする関数"""
    # CSVの出現順でauthorリストを作成
    author_order = []
    for a in df_plot["author"]:
        a_stripped = a.strip() if isinstance(a, str) else a
        if a_stripped not in author_order:
            author_order.append(a_stripped)

    for author in author_order:
        group = df_plot[df_plot["author"].str.strip() == author]
        x = group["contact_angle [degree]"].values
        y = group["slip_length [nm]"].values
        
        # エラーバーの設定（xerrとyerrを追加）
        yerr = group["slip_length_error [nm]"].values
        xerr = group["contact_angle_error [degree]"].values

        style = MARKER_STYLES.get(author, {'marker': 'o', 'color': 'black'})
        color = style['color']

        ax.errorbar(
            x, y,
            xerr=xerr,  # contact_angleのエラーバーを追加
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
slip_theory = C_VALUE / (1 + np.cos(theta_rad))**2

# === プロット: データ点 + 理論曲線 ===
fig, ax = plt.subplots()
plot_data_points(ax)

# 理論曲線
ax.plot(theta_theory, slip_theory, '--', linewidth=DASHED_LINEWIDTH, 
         color=THEORY_COLOR, zorder=1)

# 軸の範囲を設定
ax.set_xlim(X_MIN, X_MAX)
ax.set_ylim(Y_MIN, Y_MAX)

# y=0 の黒い破線（凡例に入れない）
ax.axhline(0, linestyle='--', color='black', linewidth=1, zorder=0, label='_nolegend_')

# 軸ラベル
ax.set_xlabel('Contact angle (degree)', fontsize=FONT_SIZE_AXES)
ax.set_ylabel('Slip length (nm)', fontsize=FONT_SIZE_AXES)

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
output_path = 'slip_length_plot_processed.svg'
plt.savefig(output_path, format='svg', dpi=300, bbox_inches='tight')
print(f"プロットを保存しました: {output_path}")

print(f"\nプロット対象データ数: {len(df_plot)}")
print("\nデータ一覧:")
print(df_plot[['contact_angle [degree]', 'contact_angle_error [degree]', 'slip_length [nm]', 'slip_length_error [nm]', 'author']])

plt.show()
