from pathlib import Path
import re

def get_csv_files(pattern='**/v_*_CodEmpresa_*.csv'):
    current_dir = Path.cwd()
    csv_files = sorted(Path(current_dir).glob(pattern))
    return csv_files

def get_filenames(csv_files):
    cod_empresa = re.findall('\d+', csv_files[0].name)[0]
    filenames = [re.sub('_CodEmpresa_\d+.csv', '', file.name) for file in csv_files]
    name_csv_dict = {name : csv for name, csv in zip(filenames, csv_files)}

    return filenames, name_csv_dict, cod_empresa
