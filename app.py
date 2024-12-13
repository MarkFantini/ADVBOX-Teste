from io import BytesIO

import streamlit as st
import pandas as pd

from extract_module.extract import streamlit_get_csv_files, get_filenames

from transform_module.generate_bases import generate_df_dict
from transform_module.generate_bases import generate_base_clients, generate_base_lawsuits
from transform_module.data_wrangling import clients_data_treatment, lawsuits_data_treatment

from load_module.export import write_excel

st.title("Migração ADVBOX")

st.header("Envie aqui seus arquivos")

escolha = st.selectbox("Escolha o tipo de upload", ["Zip", "CSVs"])

match escolha:
    case 'Zip':
        zip_file_buffer = st.file_uploader(
            "Enviar arquivo",
            type=['rar', 'zip'],
            accept_multiple_files=False,
            help="Clique aqui para escolher o arquivo",
            label_visibility="visible",
            )
    case "CSVs":
        csv_files_buffer = st.file_uploader(
            "Enviar arquivos",
            type=['csv'],
            accept_multiple_files=True,
            help="Clique aqui para escolher os arquivos",
            label_visibility="visible",
            )
        
if zip_file_buffer:
    ########## EXTRACTION PHASE
    bytes_data = zip_file_buffer.getvalue()
    zip_bytes = BytesIO(bytes_data)
    csv_filenames = streamlit_get_csv_files(zip_bytes)
    # filenames, name_csv_dict = get_filenames(csv_files)
    for filename in csv_filenames:
        print(filename)