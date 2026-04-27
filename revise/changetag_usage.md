# ChangeTag usage

This note summarizes how the manuscript line-range tagging system works.

## Purpose

`ChangeTag` markers are used to record where each revision appears in the final line-numbered manuscript or Supporting Information. The recorded line numbers are then referenced from `point_by_point_response.tex`.

## Marking a changed range

In `main.tex` or `supporting_information.tex`, wrap each changed range with:

```tex
\ChangeTagStart{tag_name}
Changed manuscript text...
\ChangeTagEnd{tag_name}
```

Use one unique `tag_name` per changed range. Current tags follow this format:

```text
r{reviewer}_{comment}_{short_description}
```

Examples:

```tex
\ChangeTagStart{r2_15_hopg_contact_angle}
Because the HOPG surface was freshly cleaved immediately before measurement...
\ChangeTagEnd{r2_15_hopg_contact_angle}
```

```tex
\ChangeTagStart{r2_6_tip_calibration_fit_si}
...
\ChangeTagEnd{r2_6_tip_calibration_fit_si}
```

Use the `_si` suffix for tags that appear in `supporting_information.tex` when it helps distinguish them from main-text tags.

## Referencing a tag in the response document

In `point_by_point_response.tex`, use:

```tex
\ChangeText{main}{tag_name}{Description of the change.}
```

for tags in `main.tex`, and:

```tex
\ChangeText{si}{tag_name}{Description of the change.}
```

for tags in `supporting_information.tex`.

Examples:

```tex
\item \ChangeText{main}{r2_15_hopg_contact_angle}{Clarified that the measured HOPG contact angle is close to the reported value for freshly cleaved HOPG.}
```

```tex
\item \ChangeText{si}{r2_6_tip_calibration_fit_si}{Added the representative DLC calibration fitting plot and reported its mean absolute error.}
```

The output becomes, for example:

```text
Clarified ... (main lines 206--212)
```

## Required setup

`main.tex` and `supporting_information.tex` must load `lineno` and define:

```tex
\newcommand{\ChangeTagStart}[1]{\linelabel{changetag:start:#1}}
\newcommand{\ChangeTagEnd}[1]{\linelabel{changetag:end:#1}}
```

`point_by_point_response.tex` must import the compiled aux files:

```tex
\usepackage{xr}
\externaldocument[main-]{build/main}
\externaldocument[si-]{build/supporting_information}
```

and define:

```tex
\newcommand{\ChangeLineRange}[2]{#1 lines~\ref{#1-changetag:start:#2}--\ref{#1-changetag:end:#2}}
\newcommand{\ChangeText}[3]{#3 (\ChangeLineRange{#1}{#2})}
```

## Build order

Compile in this order so that the line labels exist before the response document is built:

```powershell
latexmk -pdf main.tex
latexmk -pdf supporting_information.tex
latexmk -pdf point_by_point_response.tex
```

If a line range appears as `??`, rebuild the source file containing the tag first, then rebuild `point_by_point_response.tex`.

## Checking tags

To confirm that tags are written to the aux files:

```powershell
rg "changetag" build/main.aux build/supporting_information.aux
```

To check whether the response PDF still contains unresolved references:

```powershell
pdftotext build/point_by_point_response.pdf - | Select-String "\?\?"
```

## Practical notes

- Put tags around the smallest text range that reasonably represents the change.
- For figure/table caption changes, put an empty tag immediately before or after the float if `\linelabel` behaves poorly inside the caption.
- For a reviewer comment with both main-text and SI changes, include multiple `\ChangeText` items under the same response.
- Avoid reusing a tag name; duplicate labels can make line references unreliable.
- If the line number changes after editing, just rebuild the source `.tex` and then rebuild `point_by_point_response.tex`.
