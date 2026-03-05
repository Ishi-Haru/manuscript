import os
import numpy as np
import matplotlib.pyplot as plt
from colorbar_ranges import get_range

# ===== .npy ファイルをすべて取得 =====
npy_files = [f for f in os.listdir(".") if f.endswith(".npy")]

if not npy_files:
    print("カレントディレクトリに .npy ファイルが見つかりませんでした。")
    exit()

# ===== 処理と保存 =====
for file_name in npy_files:
    print(f"{file_name} を処理中...")

    # データ読み込みと z=0 面の抽出
    data = np.load(file_name)
    if data.ndim < 3 or data.shape[1] <= 0:
        print(f"スキップ: {file_name} は (y, z, x) 形式ではありません。")
        continue

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

    # カラーバー範囲の設定
    filename_without_ext = os.path.splitext(file_name)[0]
    colorbar_range = get_range(filename_without_ext)
    
    # プロットして保存（ラベル・タイトル非表示）
    plt.figure(figsize=(6, 5))
    
    c_map = "magma"  # デフォルトのカラーマップ

    if colorbar_range:
        vmin, vmax = colorbar_range
        img = plt.imshow(data_2d, cmap=c_map, origin="lower", vmin=vmin, vmax=vmax)
        print(f"カラーバー範囲を設定: {vmin} - {vmax} nm")
    else:
        img = plt.imshow(data_2d, cmap=c_map, origin="lower")
        print("デフォルトのカラーバー範囲を使用")
    
    plt.colorbar(img)
    plt.xticks([])
    plt.yticks([])
    plt.tight_layout()

    output_file = os.path.splitext(file_name)[0] + ".jpg"
    plt.savefig(output_file, dpi=300)
    plt.close()
    print(f"保存しました: {output_file}")

# メモ：カラーマップの種類
"""
Sequential（連続）
単調に変化するデータに適用：
viridis（現在使用中）, plasma, inferno, magma
Blues, Greens, Reds, Oranges, Purples
gray, bone, copper, hot, cool
Diverging（発散）

中央値から両方向に変化するデータに適用：
RdBu, RdYlBu, RdYlGn, BrBG, PiYG
coolwarm, seismic, bwr
Qualitative（質的）

カテゴリカルデータに適用：
tab10, tab20, Set1, Set2, Set3
Pastel1, Pastel2, Dark2, Accent

その他の人気カラーマップ
jet（レインボー、科学データでよく使用）
rainbow, hsv
terrain, ocean, gist_earth
"""