import csv
import re

INPUT_FILE = 'slipe_length.csv'
OUTPUT_FILE = 'table_ready_slip_length.csv'

# Helper to clean and get value

def clean(val):
    if val is None:
        return ''
    return str(val).strip()

def format_contact_angle(row):
    ca = clean(row.get('contact_angle [degree]'))
    ca_err = clean(row.get('contact_angle_error [degree]'))
    adv = clean(row.get('adv._contact_angle [degree]'))
    rec = clean(row.get('rec._contact_angle [degree]'))
    if ca and ca_err:
        # Use LaTeX style \pm for CSV output
        return f"{ca} \\pm {ca_err}"
    elif rec and adv:
        return f"{rec} - {adv}"
    elif ca:
        return ca
    elif rec or adv:
        return f"{rec or ''} {('- ' + adv) if adv else ''}".strip()
    else:
        return ''

def format_slip_length(row):
    sl = clean(row.get('slip_length [nm]'))
    sl_err = clean(row.get('slip_length_error [nm]'))
    sl_from = clean(row.get('slip_length_from [nm]'))
    sl_to = clean(row.get('slip_length_to [nm]'))
    if sl and sl_err:
        # Use LaTeX style \pm for CSV output
        return f"{sl} \\pm {sl_err}"
    elif sl_from and sl_to:
        return f"{sl_from} - {sl_to}"
    elif sl:
        return sl
    elif sl_from or sl_to:
        return f"{sl_from or ''} {('- ' + sl_to) if sl_to else ''}".strip()
    else:
        return ''

def main():
    with open(INPUT_FILE, encoding='utf-8') as f:
        reader = csv.DictReader(f, skipinitialspace=True)
        # Remove leading/trailing spaces from fieldnames
        reader.fieldnames = [fn.strip() for fn in reader.fieldnames]
        rows = []
        for row in reader:
            # Remove leading/trailing spaces from all keys in each row
            clean_row = {k.strip(): v for k, v in row.items()}
            rows.append(clean_row)

    output_rows = []
    for row in rows:
        use_val = clean(row.get('use')).lower()
        if use_val == 'true':
            author = clean(row.get('author'))
            method = clean(row.get('Method'))
            substrate = clean(row.get('substrate'))
            contact_angle = format_contact_angle(row)
            slip_length = format_slip_length(row)
            output_rows.append({
                'Autor': author,
                'Method': method,
                'Substrate': substrate,
                'Contact Angle': contact_angle,
                'Slip Length': slip_length
            })

    with open(OUTPUT_FILE, 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['Autor', 'Method', 'Substrate', 'Contact Angle', 'Slip Length'])
        writer.writeheader()
        for row in output_rows:
            writer.writerow(row)

if __name__ == '__main__':
    main()
