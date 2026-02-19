import pandas as pd
import numpy as np

# CSVファイルを読み込み
df = pd.read_csv('slipe_length.csv')

# 列名のスペースを削除
df.columns = df.columns.str.strip()

# デバッグ用：列名を表示
print("列名一覧:")
print(df.columns.tolist())
print()

# use列をブール型に変換（TRUE/FALSEの文字列をboolに変換）
df['use'] = df['use'].astype(str).str.upper().isin(['TRUE', '1', 'YES'])

# 新しいデータフレームを作成
processed_df = pd.DataFrame()

# adv.とrec.のcontact angleから平均値とエラーを計算
for idx, row in df.iterrows():
    adv_angle = row['adv._contact_angle [degree]']
    rec_angle = row['rec._contact_angle [degree]']
    contact_angle = row['contact_angle [degree]']
    contact_angle_error = row['contact_angle_error [degree]']
    
    # adv.とrec.の両方が存在する場合
    if pd.notna(adv_angle) and pd.notna(rec_angle):
        # 平均値を計算
        avg_angle = (adv_angle + rec_angle) / 2
        # エラーを計算（adv. - 平均値）
        angle_error = adv_angle - avg_angle
        
        df.at[idx, 'contact_angle [degree]'] = avg_angle
        df.at[idx, 'contact_angle_error [degree]'] = angle_error

# use列がTRUEのデータのみをフィルタリング
df_filtered = df[df['use'] == True].copy()

print(f"元データ数: {len(df)}")
print(f"use=TRUEのデータ数: {len(df_filtered)}")
print()

# 必要な列のみを選択
output_df = df_filtered[[
    'contact_angle [degree]',
    'contact_angle_error [degree]',
    'slip_length [nm]',
    'slip_length_error [nm]',
    'author'
]].copy()

# 出力
output_df.to_csv('proccesed_data_for_plot.csv', index=False)
print("変換完了: proccesed_data_for_plot.csv を作成しました")
print(f"データ数: {len(output_df)}")
print("\n最初の数行:")
print(output_df.head(10))
