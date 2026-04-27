## 査読コメントへの対応を求められたとき

- 変更箇所にはタグ付けをしてください。
- `point_by_point_response.tex`の該当部分に変更点アイテムを追加してください

## 差分 TeX の作成を求められたとき

- `main.tex` と `supporting_information.tex` について、指定された base commit から現在の作業ツリーまでの差分 TeX を作る。
- base commitが指定されなかった場合はユーザーに尋ねる。
- 既存の `latexdiff_*.tex` は削除してよい。
- 差分表示は「現在の文章をそのまま表示し、変更箇所だけ色付け」にする。削除テキストや取り消し線は表示しない。
- `latexdiff --type=CFONT --disable-citation-markup` で生成した後、差分 TeX 内のマクロを調整する。
  - `\DIFadd` は `{\protect\color{blue} #1}` のように、色だけを付ける。フォントサイズやフォントファミリは変えない。
  - `\DIFdel` と `\DIFdelFL` は空定義にする。
  - `\DIFdelbegin` / `\DIFdelend` / `\DIFdelbeginFL` / `\DIFdelendFL` も空定義にする。
- `main.tex` と `supporting_information.tex` と同じように、差分 TeX でも `\linenumbers` が有効になっていることを確認する。
- 生成後は `latexmk -pdf <diff-file>.tex` で main 差分と SI 差分をそれぞれビルドして、PDF が作れることを確認する。
- 生成用に一時的に取り出した旧版 TeX は、成果物でなければ最後に削除する。