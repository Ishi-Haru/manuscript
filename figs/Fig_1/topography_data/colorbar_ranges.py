import json
import os

def get_range(filename_without_ext):
    """
    JSONファイルからファイル名（拡張子なし）に対応する範囲を取得
    
    Args:
        filename_without_ext (str): 拡張子を除いたファイル名
    
    Returns:
        tuple: (vmin, vmax) または None（設定がない場合）
    """
    config_file = "colorbar_ranges.json"
    
    # JSONファイルが存在しない場合
    if not os.path.exists(config_file):
        return None
    
    try:
        with open(config_file, 'r', encoding='utf-8') as f:
            colorbar_ranges = json.load(f)
        
        if filename_without_ext in colorbar_ranges:
            vmin, vmax = colorbar_ranges[filename_without_ext]
            return vmin, vmax
        
    except (json.JSONDecodeError, FileNotFoundError, KeyError):
        # JSON読み込みエラーの場合はNoneを返す
        pass
    
    return None
