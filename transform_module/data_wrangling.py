import pandas as pd

BASE_CLIENTS_DICT = {
	'NOME'                 	: 'razao_social',
	'CPF CNPJ'             	: 'cpf_cnpj',
	'RG'                   	: 'rg',
	'TELEFONE'             	: 'telefone1',
	'CELULAR'              	: 'telefone2',
	'EMAIL'                	: 'email1',
	'ESTADO CIVIL'         	: 'estado_civil',
	'NACIONALIDADE'        	: 'nacionalidade',
	'ESTADO'               	: 'uf',
	'CIDADE'               	: 'cidade',
	'CEP'                  	: 'cep',
	'ENDEREÇO'             	: 'logradouro',
	'BAIRRO'               	: 'bairro',
	'PIS PASEP'            	: 'pis',
	'DATA DE NASCIMENTO'   	: 'nascimento',
	'NOME DA MÃE'			: 'nome_mae',
	'PROFISSÃO'				: 'profissao',
	'ANOTAÇÕES GERAIS'		: 'responsavel',
	'PAIS'					: 'nacionalidade',
}

BASE_LAWSUITS_DICT = {
	
}


def fix_professions_encoding(csv_paths, df, file='v_clientes', col='profissao'):
    csv = csv_paths[file]
    correct_col = pd.read_csv(csv, sep=';', encoding='utf-8', usecols=[col], dtype=str)
    df[col] = correct_col

    return df[col]


def complete_free_fields():
    pass