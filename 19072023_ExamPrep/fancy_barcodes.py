import re


def parse_barcode(barcode_data):
    pattern = r"@#+[A-Z][A-Za-z0-9]{4,}[A-Z]@#+"

    for barcode in barcode_data:
        if re.fullmatch(pattern, barcode):
            product_group = re.findall(r"\d", barcode)
            product_group = ''.join(product_group) if product_group else "00"
            print(f"Product group: {product_group}")
        else:
            print(f"Invalid barcode")


n = int(input())
barcode_data = [input() for i in range(n)]
parse_barcode(barcode_data)