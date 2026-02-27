import csv
import re

INPUT_FILE = 'table_ready_slip_length.csv'
OUTPUT_FILE = 'table_ready_slip_length.tex'

LATEX_TEMPLATE = r"""
% Requires \usepackage{{multirow}}
\begin{{table}}
    \caption{{Contact angle and slip length for various substrates}}
    \label{{tbl:Previous_contact_angle_slip}}
    \begin{{tabular}}{{llccc}}
        \hline
        Author & Method & Substrate & Contact Angle $\\theta$ (\si{{\\degree}}) & Slip length (\si{{\\nano\\metre}}) \\
        \hline
{rows}
        \hline
    \end{{tabular}}
\end{{table}}
"""

def latex_escape(text):
    # Escape LaTeX special chars
    if not text:
        return ''
    return text.replace('&', '\\&').replace('%', '\\%').replace('#', '\\#').replace('_', '\\_').replace('^', '\\^{}').replace('~', '\\textasciitilde{}').replace('$', '\\$').replace('{', '\\{').replace('}', '\\}')

def format_angle(val):
    if not val or val.strip() == '':
        return '---'
    # e.g. 91 \pm 2 → \SI{91 \pm 2}{\degree}
    pm_match = re.match(r"([\d.]+) \\pm ([\d.]+)", val)
    range_match = re.match(r"([\d.]+)\s*-\s*([\d.]+)", val)
    if pm_match:
        return r"$%s \\pm %s$" % (pm_match.group(1), pm_match.group(2))
    elif range_match:
        return r"$%s$--$%s$" % (range_match.group(1), range_match.group(2))
    else:
        return r"$%s$" % val

def format_slip(val):
    if not val or val.strip() == '':
        return '---'
    pm_match = re.match(r"([\-\d.]+) \\pm ([\d.]+)", val)
    range_match = re.match(r"([\-\d.]+)\s*-\s*([\-\d.]+)", val)
    if pm_match:
        return r"$%s \\pm %s$" % (pm_match.group(1), pm_match.group(2))
    elif range_match:
        return r"$%s$--$%s$" % (range_match.group(1), range_match.group(2))
    else:
        return r"$%s$" % val

def main():
    with open(INPUT_FILE, encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        # グループ化: 著者ごと
        grouped = {}
        for row in reader:
            author = latex_escape(row.get('Autor') or row.get('author') or '---')
            if author not in grouped:
                grouped[author] = []
            grouped[author].append(row)

    rows = []
    for author, items in grouped.items():
        n = len(items)
        method = latex_escape(items[0].get('Method') or '---')
        for i, row in enumerate(items):
            substrate = latex_escape(row['Substrate']) or '---'
            angle = format_angle(row['Contact Angle'])
            slip = format_slip(row['Slip Length'])
            if i == 0:
                author_cell = f"\\multirow{{{n}}}{{*}}{{{author}}}"
                method_cell = f"\\multirow{{{n}}}{{*}}{{{method}}}"
            else:
                author_cell = ''
                method_cell = ''
            rows.append("    {} & {} & {} & {} & {} {}".format(author_cell, method_cell, substrate, angle, slip, '\\'*2))
        # Add a thin line (\cline) after each author group except the last
        rows.append("    \\cline{{1-5}}")
    latex_rows = '\n'.join(rows)
    latex_table = LATEX_TEMPLATE.format(rows=latex_rows)
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(latex_table)

if __name__ == '__main__':
    main()
