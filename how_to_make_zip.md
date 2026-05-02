# ZIP 作成手順

提出用 zip には、TeX ソースとそれらが直接参照している図だけを入れる。
作業用ファイル、`revise/`、`build/`、`tex_diff_tmp/`、スクリプト、元データは入れない。

## 入れるファイル

- `main.tex`
- `supporting_information.tex`
- `point_by_point_response.tex`
- `main.bib`
- `latexmkrc`
- `figs/TOC.png`
- `figs/slip_length_summary/previous_slip_length.png`
- `figs/schematics_of_measurement.png`
- `figs/mapping_results.png`
- `figs/scaling_result.png`
- `figs/DLC_bubble.png`
- `figs/HOPG_strong_force.png`
- `figs/mapping_colormaps.png`

## PowerShell

```powershell
$zip = "submission_source.zip"
Remove-Item $zip -ErrorAction SilentlyContinue
Compress-Archive -Path `
  main.tex, `
  supporting_information.tex, `
  point_by_point_response.tex, `
  main.bib, `
  latexmkrc, `
  figs/TOC.png, `
  figs/slip_length_summary/previous_slip_length.png, `
  figs/schematics_of_measurement.png, `
  figs/mapping_results.png, `
  figs/scaling_result.png, `
  figs/DLC_bubble.png, `
  figs/HOPG_strong_force.png, `
  figs/mapping_colormaps.png `
  -DestinationPath $zip
```

PDF も求められる場合は、`build/main.pdf`、`build/supporting_information.pdf`、`build/point_by_point_response.pdf` を別途アップロードする。
