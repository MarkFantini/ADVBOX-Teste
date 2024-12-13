from io import BytesIO
import re

import streamlit as st
import pandas as pd

from transform_module.generate_bases import generate_base_clients, generate_base_lawsuits
from transform_module.data_wrangling import clients_data_treatment, lawsuits_data_treatment

# from load_module.export import write_excel

st.title("Migração ADVBOX")

st.header("Envie aqui seus arquivos")

csv_files_buffer = st.file_uploader(
    "Enviar arquivos",
    type=['csv'],
    accept_multiple_files=True,
    help="Clique aqui para escolher os arquivos",
    label_visibility="visible",
    )

@st.cache_data
def fetch_files(csv_files_buffer):
    if csv_files_buffer:
        cod_empresa = re.findall('\d+', csv_files_buffer[0].name)[0]
        "Código da empresa: " + str(cod_empresa)
        filenames = [re.sub('_CodEmpresa_\d+.csv', '', csv.name) for csv in csv_files_buffer]

    return csv_files_buffer, filenames, cod_empresa

if csv_files_buffer:
    csv_files, filenames, cod_empresa = fetch_files(csv_files_buffer)

@st.cache_data
def generate_df_dict(csv_files, filenames):
    df_dict = dict()
    latin_encoding = {'v_advogado_adverso', 'v_atendimentos_processo', 'v_clientes'}
    for csv, name in zip(csv_files, filenames):
        if name in latin_encoding:
            df_dict[name] = pd.read_csv(csv, sep=';', encoding='latin1', dtype=str)
            df_dict[name] = df_dict[name].fillna('')
        else:
            df_dict[name] = pd.read_csv(csv, sep=';', encoding='utf-8', dtype=str)
            df_dict[name] = df_dict[name].fillna('')

    return df_dict

df_dict = generate_df_dict(csv_files, filenames)

base_clients         = generate_base_clients(df_dict)
cleaned_base_clients = clients_data_treatment(base_clients, csv_files)