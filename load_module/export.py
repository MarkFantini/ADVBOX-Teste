import pandas as pd

def write_excel(df, file_name, write_mode="w", sheetname='Página1'):
    with pd.ExcelWriter(file_name + ".xlsx", mode=write_mode) as writer:
        df.to_excel(writer, sheet_name=sheetname, index=False)