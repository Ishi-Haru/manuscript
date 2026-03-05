"""square_plot モジュールの使用例.

使い方:
1) 対話選択:
    python example_usage.py
2) 直接指定して保存:
    python example_usage.py path/to/file.npy 0  # z=0 を表示 & 保存
"""
import sys
from square_plot import (
    interactive_select_and_plot,
    select_line_on_npy,
)

def main():
    if len(sys.argv) == 1:
        interactive_select_and_plot(".", z_index=0)
    else:
        file_path = sys.argv[1]
        z_index = int(sys.argv[2]) if len(sys.argv) > 2 else 0
        pts = select_line_on_npy(file_path, z_index=z_index)
        print(f"選択結果: {pts}")

if __name__ == "__main__":
    main()
