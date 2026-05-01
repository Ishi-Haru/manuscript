# 教員PDFコメント対応 作業内容案

Source: `teacher_pdf_comments.md`

このファイルは、教員が `point_by_point_response.pdf` に後付けしたコメントに対して、Codexがこれから実施する作業を整理したものです。ユーザー確認後、このファイルを参照しながら実際の修正に入ります。

## 作業方針

- 実修正対象は主に `point_by_point_response.tex`, `main.tex`, `supporting_information.tex`。
- 変更箇所には既存方針どおり `\ChangeTagStart{...}` / `\ChangeTagEnd{...}` などのタグ付けを行う。
- `point_by_point_response.tex` には、対応した変更点を `Changes:` または該当回答本文に反映する。
- 教員コメントで英文案が示されている箇所は、原則としてその英文案を優先して反映する。
- 図・データ差し替えが必要そうな箇所は、Codexだけで判断できる範囲を確認し、不足する元データがある場合はユーザーに確認する。

## 1. point_by_point_response.tex の修正

### 冒頭・Reviewer 1 前

- [ ] Reviewer 3 の推薦文・コメント全文を、Reviewer 1 の回答に入る前の謝辞として反映する。
  - 対応コメント: Comment 2
  - 目的: 査読してもらったことへの謝意を述べたうえで Question 1 に進む。

### Reviewer 1

- [ ] Reviewer 1 comment 1 の `Changes` 行番号を確認する。
  - 対応コメント: Comment 3
  - 確認候補: `49-52` が何を指しているか、既存の line 表記と照合する。

- [x] Reviewer 1 comment 2 の回答文を丁寧な表現に置換する。
  - 対応コメント: Comment 4
  - 置換案:
    `Thank you very much for your helpful comment. Our method is also capable of measuring polar surfaces, and we are in fact planning to study such surfaces in the near future. In that context, the paper you pointed out will be very useful. Thank you again for bringing it to our attention.`

### Reviewer 2

- [x] Reviewer 2 冒頭も Reviewer 1 と同様の始め方にする。
  - 対応コメント: Comment 5

- [ ] Reviewer 2 comment 2 の CNT 回答を再考する。
  - 対応コメント: Comment 6, Comment 7
  - 必須観点: “Why there is massive slippage on CNTs” に明示的に答える。
  - 表現修正: `CNT slip length` が不自然なら `slip length in CNTs` などに変更する。

- [x] Reviewer 2 comment 3 の Vinogradova 関連表現を修正する。
  - 対応コメント: Comment 8, Comment 9, Comment 11
  - `Vinogradovaをciteする` に相当する不自然な英語を避ける。
  - 回答案に、Eq. 4 の導出を Supporting Information に入れたことを明記する。
  - 本文側では `as derived in the Supporting Information I` のように章番号つきで参照する。

- [x] Reviewer 2 comment 4 の f* 回答を教員案に置換する。
  - 対応コメント: Comment 12, Comment 13, Comment 14
  - 置換案:
    `~ the correction factor f*, which was used in Eqs. 3 and 5 in the original manuscript. Specifically, f*(h, bt, bs) is now given as Eq. 4, and the auxiliary quantities A, B, and C are defined in Eq. 5 of the revised manuscript.`
  - 関連式の言及を `in Eqs. 3, 7, S7 and S8.` に修正するか確認する。

- [x] Reviewer 2 comment 5 の Fig. 2 caption 対応に `[for the fit]` を明記する。
  - 対応コメント: Comment 15

- [ ] Reviewer 2 comments 6 と 7 をまとめて回答する。
  - 対応コメント: Comment 16
  - `point_by_point_response.tex` 内にも新規図を `Fig. R1` として紹介する。
  - `Changes:` では `Fig. R1(a, b)` を `Fig. S2(a, b)` として SI に追加した、と書く。
  - 注意: 現在の Fig. S2(b) の force curve が `bs = 217.8 nm` のものなら、`345.3 ± 23.7 nm` に近いデータへ差し替え可能か確認する。

- [x] Reviewer 2 comment 8 付近の本文・回答表現を `on the slippery surface` に合わせる。
  - 対応コメント: Comment 17

- [x] Reviewer 2 comment 9 の回答を教員案に置換する。
  - 対応コメント: Comment 18, Comment 19
  - 置換案では、Teflon と HOPG の違いを contact angle ではなく interfacial friction / graphite-water interface で説明する。
  - `Changes:` は削除し、最後を `This point is discussed in lines 197-217 of the revised manuscript.` で締める。

- [x] Reviewer 2 comment 10 の回答冒頭を `We apologize for the confusion.` に変更し、参照図を `Fig. S3` に合わせる。
  - 対応コメント: Comment 20, Comment 21

- [x] Reviewer 2 comment 11 の表現を修正する。
  - 対応コメント: Comment 22, Comment 23
  - `line 196` 付近で `calculated from` を `predicted by` に変更する。
  - Table S2 caption と表中見出しを `b predicted by C = xx nm (nm)` に変更する。

- [x] Reviewer 2 comment 12 の回答を教員案に置換する。
  - 対応コメント: Comment 24
  - ただし `common` の意味が特に不要なら削る、または明確な語に置換する。
  - 対応コメント: Comment 25

- [x] Reviewer 2 comment 13 の回答を教員案に置換する。
  - 対応コメント: Comment 28
  - `unpatterned reference substrates` を response と SI の両方で使う。
  - 関連する短い注釈 `unpatterned` も反映する。
  - 対応コメント: Comment 29

- [x] Reviewer 2 comment 14 または関連箇所に、`leaving the intrinsic slip length on hydrophobic surfaces unresolved` を必要に応じて反映する。
  - 対応コメント: Comment 30

- [x] Reviewer 2 comment 15 または関連箇所の末尾に、`. as discussed in our response to question 9.` の趣旨を反映する。
  - 対応コメント: Comment 31

### Reviewer 3 と Non-scientific changes

- [x] Reviewer 3 への回答の後に `Non-scientific changes` の章を追加する。
  - 対応コメント: Comment 1
  - 非科学的・事務的な修正項目への回答をここにまとめる。

- [ ] Non-scientific changes の項目 4 に対する回答を教員案に沿って作る。
  - 対応コメント: Comment 1
  - 注意: 図の改変は Wu et al. 由来部分のみで、他はデータをまとめたものなら、追加データ源の許可が必要かどうかを慎重に表現する。

## 2. main.tex の修正

- [x] Abstract 見出しの文字サイズを Keywords と同じ大きさにそろえる。
  - 対応コメント: Comment 1
  - 既存の `\renewcommand*\acs@keywords@print` と abstract 出力の体裁を確認して調整する。

- [x] `Keywords` に修正色が付いていない問題を直す。
  - 対応コメント: Comment 1
  - `\keywords{...}` または出力マクロ側に変更タグ・色指定を入れる。

- [ ] 式番号が変更された箇所にも修正色が付くようにする。※対応しない
  - 対応コメント: Comment 1
  - ユーザー指示により、この項目は今回の Codex 作業対象から外す。

- [ ] Fig. 1 caption に credit line を追加する。
  - 対応コメント: Comment 1
  - 追加案:
    `Adapted with permission from ref XX. Copyright XXXX [Publisher]. Additional experimental data were taken from refs YY-ZZ.`
  - `XX`, `YYYY`, `[Publisher]`, `YY-ZZ` は実際の文献番号・出版社名に置換が必要。

- [x] CNT 関連本文を確認し、`CNT slip length` など不自然な表現を `slip length in CNTs` 等へ修正する。
  - 対応コメント: Comment 7

- [x] Eq. 4 導出の本文説明を、Supporting Information I への参照つきで修正する。
  - 対応コメント: Comment 9, Comment 11

- [x] f* の式番号参照・本文説明を response と整合させる。
  - 対応コメント: Comment 12, Comment 14

- [x] `on the slippery surface` に合わせるべき本文表現を修正する。
  - 対応コメント: Comment 17

- [x] Teflon/HOPG の議論を教員案と整合させる。
  - 対応コメント: Comment 18, Comment 19
  - 既存の議論が更新済みか、response の line 197-217 と整合するか確認する。

- [x] 120° / CF3 に関する本文修正を教員案に合わせる。
  - 対応コメント: Comment 26, Comment 27
  - 置換案:
    `A contact angle of approximately 120° is achieved on a surface where –CF3 groups, which have the lowest surface free energy among surface-terminating groups, are arranged in a hexagonal close-packed structure, and is known as the near-maximum water contact angle achievable on a chemically homogeneous flat surface[23].`
  - `chemically homogeneous smooth flat surfaces` の重複表現を避け、`chemically homogeneous flat surfaces` などに統一する。

- [x] Contact angle 測定説明を `unpatterned reference substrates` を用いる表現に変更する。
  - 対応コメント: Comment 28, Comment 29

- [x] Hydrophobic surfaces の consensus に関する記述に、`leaving the intrinsic slip length on hydrophobic surfaces unresolved` の趣旨を必要に応じて反映する。
  - 対応コメント: Comment 30

- [ ] HOPG / graphite 関連の議論で、question 9 への回答参照に相当する表現を整える。
  - 対応コメント: Comment 31

## 3. supporting_information.tex の修正

- [ ] Fig. S2 を確認し、DLC と nanobubble の representative fitting plots が `(a, b)` として正しく入っているか確認する。
  - 対応コメント: Comment 16
  - Fig. S2(b) が `bs = 217.8 nm` のデータなら、`345.3 ± 23.7 nm` に近いデータ・図へ差し替え可能か確認する。
  - データや図ファイルが見つからない場合はユーザーに確認する。

- [x] Fig. S3 caption 内のアルファベットの組み合わせを修正する。
  - 対応コメント: Comment 1

- [x] Table S2 caption の `calculated from` を `predicted by` に変更する。
  - 対応コメント: Comment 23

- [x] Table S2 の列見出しを `b predicted by C = xx nm (nm)` 形式に変更する。
  - 対応コメント: Comment 23

- [x] Contact angle 測定説明を `unpatterned reference substrates` に変更する。
  - 対応コメント: Comment 28, Comment 29

## 4. 確認・ビルド

- [x] 修正後、`latexmk -pdf main.tex` を実行して main PDF がビルドできるか確認する。
- [x] 修正後、`latexmk -pdf supporting_information.tex` を実行して SI PDF がビルドできるか確認する。
- [x] 修正後、`latexmk -pdf point_by_point_response.tex` を実行して response PDF がビルドできるか確認する。
- [x] `rg` で以下を確認する。
  - `calculated from` が Table S2 周辺に残っていないこと。
  - `chemically homogeneous smooth flat surfaces` の重複表現が残っていないこと。
  - `keep it in mind` が response に残っていないこと。
  - `CNT slip length` が不自然な形で残っていないこと。
  - `unpatterned reference substrates` が main/SI/response で整合していること。

## 5. ユーザー確認が必要そうな点

- [ ] Fig. S2(b) の差し替えに使う、`345.3 ± 23.7 nm` に近い nanobubble fitting curve の元データまたは図ファイルがあるか。
- [ ] Fig. 1 caption の `ref XX`, `Copyright XXXX [Publisher]`, `refs YY-ZZ` に入れる正確な文献番号・出版社・年。
- [ ] Non-scientific changes の章に含める項目の範囲。
- [ ] `Abstract` 見出しの文字サイズ変更を、TeXマクロで対応するか、差分PDF上の見た目だけを調整するか。
