from pathlib import Path
import re
import zipfile
from io import BytesIO

def get_csv_files(pattern='**/v_*_CodEmpresa_*.csv'):
    current_dir = Path.cwd()
    csv_files = sorted(Path(current_dir).glob(pattern))
    return csv_files

def get_filenames(csv_files):
    filenames = [re.sub('_CodEmpresa_\d+.csv', '', file.name) for file in csv_files]
    name_csv_dict = {name : csv for name, csv in zip(filenames, csv_files)}

    return filenames, name_csv_dict

def streamlit_get_csv_files(zip_file_buffer, pattern='**/v_*_CodEmpresa_*.csv'):

    with zipfile.ZipFile(zip_file_buffer, 'r') as zip_file:
        csv_filenames = [name for name in zip_file.namelist() if re.match(pattern)]
        
        return csv_filenames