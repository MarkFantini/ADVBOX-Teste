from pathlib import Path
import re

def get_csv_files(pattern='**/v_*_CodEmpresa_*.csv'):
    current_dir = Path.cwd()
    csv_files = sorted(Path(current_dir).glob(pattern))
    return csv_files

def get_filenames(csv_files):
    filenames = [re.sub('_CodEmpresa_\d+.csv', '', file.name) for file in csv_files]
    csv_paths = {name : csv for name, csv in zip(filenames, csv_files)}

    return filenames, csv_paths