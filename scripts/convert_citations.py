"""
Docstring for scripts.convert_citations
[数字]形式の参考文献を\cite{}形式に変換するスクリプト
"""

import json
import re
import argparse

def load_key_mapping(json_path):
    """JSONファイルからcitation keyのマッピングを読み込む"""
    with open(json_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def convert_citations(tex_path, key_mapping, preview=False, keep_original=False):
    """TEXファイル内の[数字]を\cite{}形式に変換"""
    with open(tex_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    conversions = []  # 変換内容を記録
    
    # [数字]または[数字-数字]または[数字,数字]のパターンを検索
    def replace_citation(match):
        citation_str = match.group(1)
        original = match.group(0)
        
        # [44]はそのまま残す
        if citation_str == "44":
            return original
        
        # 範囲指定（例：1-7）
        if '-' in citation_str and ',' not in citation_str:
            parts = citation_str.split('-')
            if len(parts) == 2 and parts[0].isdigit() and parts[1].isdigit():
                start = int(parts[0])
                end = int(parts[1])
                keys = []
                for i in range(start, end + 1):
                    key = key_mapping.get(str(i))
                    if key:
                        keys.append(key)
                if keys:
                    cite_part = r'\cite{' + ', '.join(keys) + '}'
                    if keep_original:
                        replacement = original + ' ' + cite_part
                    else:
                        replacement = cite_part
                    conversions.append((original, replacement))
                    return replacement
        
        # カンマ区切り（例：12,13）
        elif ',' in citation_str:
            nums = [n.strip() for n in citation_str.split(',')]
            keys = []
            for num in nums:
                key = key_mapping.get(num)
                if key:
                    keys.append(key)
            if keys:
                cite_part = r'\cite{' + ', '.join(keys) + '}'
                if keep_original:
                    replacement = original + ' ' + cite_part
                else:
                    replacement = cite_part
                conversions.append((original, replacement))
                return replacement
        
        # 単一の数字
        else:
            key = key_mapping.get(citation_str)
            if key:
                cite_part = r'\cite{' + key + '}'
                if keep_original:
                    replacement = original + cite_part
                else:
                    replacement = cite_part
                conversions.append((original, replacement))
                return replacement
        
        # マッピングが見つからない場合は元のまま
        return original
    
    # [数字]のパターンをすべて置換
    # [で始まり、数字、カンマ、ハイフンを含み、]で終わるパターン
    pattern = r'\[([0-9,\-]+)\]'
    converted_content = re.sub(pattern, replace_citation, content)
    
    # プレビューモードの場合は変換内容を表示
    if preview:
        print("\n=== 変換プレビュー ===\n")
        if conversions:
            for i, (before, after) in enumerate(conversions, 1):
                print(f"{i}. {before}  →  {after}")
            print(f"\n合計 {len(conversions)} 箇所の変換があります。")
        else:
            print("変換される箇所はありません。")
        print("\n" + "="*50 + "\n")
    
    return converted_content, conversions

def save_converted_file(tex_path, converted_content, output_path=None):
    """変換したコンテンツをファイルに保存"""
    if output_path is None:
        output_path = tex_path
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(converted_content)

if __name__ == "__main__":
    # コマンドライン引数のパース
    parser = argparse.ArgumentParser(
        description='[数字]形式の参考文献を\\cite{}形式に変換'
    )
    parser.add_argument(
        '-p', '--preview',
        action='store_true',
        help='変換内容をプレビューするのみでファイルは更新しない'
    )
    parser.add_argument(
        '-k', '--keep-original',
        action='store_true',
        help='元の[数字]表記を残しつつ\\cite{}を追加する（例: [1]\\cite{key}）'
    )
    parser.add_argument(
        '--json',
        default='scripts/key_mapping_PRL.json',
        help='citation keyマッピングのJSONファイルパス（デフォルト: scripts/key_mapping_PRL.json）'
    )
    parser.add_argument(
        '--tex',
        default='main.tex',
        help='変換対象のTEXファイルパス（デフォルト: main.tex）'
    )
    
    args = parser.parse_args()
    
    # パスの設定
    json_path = args.json
    tex_path = args.tex
    
    # マッピングの読み込み
    key_mapping = load_key_mapping(json_path)
    
    # 変換実行
    converted_content, conversions = convert_citations(
        tex_path, key_mapping, 
        preview=args.preview, 
        keep_original=args.keep_original
    )
    
    # プレビューモードでなければファイルに保存
    if not args.preview:
        save_converted_file(tex_path, converted_content)
        print("Citation conversion completed successfully!")
        print(f"Updated file: {tex_path}")
        if conversions:
            print(f"Total conversions: {len(conversions)}")
        if args.keep_original:
            print("Mode: 元の表記を残しつつ\\cite{}を追加")
    else:
        print("プレビューモードで実行しました。ファイルは更新されていません。")
        print("実際に変換を実行する場合は、-p オプションなしで実行してください。")
