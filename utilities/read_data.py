import pandas

def get_sheet_into_list(file,sheetname):
    df = pandas.read_excel(file, sheet_name=sheetname)
    return df.values.tolist()