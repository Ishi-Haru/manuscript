"""
Docstring for scripts.extract_bib_entry
.bibファイルから参考文献のcitation keyの文字列だけを抽出する。
"""

bib_path = "ihtc18bib.bib"

def extract_bib_entry(bib_path):
    with open(bib_path, "r", encoding="utf-8") as f:
        bib_content = f.read()

    entries = bib_content.split("\n@")
    citation_keys = []

    for entry in entries:
        if entry.strip():  # 空でないエントリーのみ処理
            if not entry.startswith("@"):
                entry = "@" + entry  # 最初のエントリーには@がないため追加
            # citation keyを抽出（@の後から最初の{までの部分、またはカンマまでの部分）
            entry_stripped = entry.strip()
            # @type{key, の形式からkeyを抽出
            start = entry_stripped.find("{") + 1
            end = entry_stripped.find(",")
            if start > 0 and end > start:
                citation_key = entry_stripped[start:end].strip()
                citation_keys.append(citation_key)

    return citation_keys

if __name__ == "__main__":
    keys = extract_bib_entry(bib_path)
    for key in keys:
        print(key)