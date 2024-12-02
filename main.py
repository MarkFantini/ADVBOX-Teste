#!/usr/bin/env python3

import logging
from pathlib import Path
import re
from pprint import pprint

import pandas as pd

from extract_module.extract import get_csv_files, get_filenames
from transform_module.transform import generate_df_dict, filter_df_dict
from transform_module.transform import generate_base_clients, generate_base_lawsuits
from load_module.load import write_excel



COLS_CLIENTES_FINAL = [
	'NOME',							# OBRIGATÓRIO # CHECK
	'CPF CNPJ', # CHECK
	'RG', # CHECK
	'NACIONALIDADE', # CHECK
	'DATA DE NASCIMENTO', # CHECK
	'ESTADO CIVIL', # CHECK
	'PROFISSÃO',
    'SEXO',
	'CELULAR', # CHECK
	'TELEFONE', # CHECK
	'EMAIL', # CHECK
	'PAIS',
	'ESTADO', # CHECK
	'CIDADE', # CHECK
	'BAIRRO', # CHECK
	'ENDEREÇO', # CHECK
	'CEP', # CHECK
	'PIS PASEP', # CHECK
	'CTPS',
	'CID',
	'NOME DA MÃE', # CHECK
	'ORIGEM DO CLIENTE',			# OBRIGATÓRIO
	'ANOTAÇÕES GERAIS' # CHECK
]
COLS_PROCESSOS_FINAL = [
	'NOME DO CLIENTE', 				# OBRIGATÓRIO
	'PARTE CONTRÁRIA',
	'TIPO DE AÇÃO', 				# OBRIGATÓRIO
	'GRUPO DE AÇÃO', 				# OBRIGATÓRIO
	'FASE PROCESSUAL', 				# OBRIGATÓRIO
	'ETAPA',
	'NÚMERO DO PROCESSO',
	'PROCESSO ORIGINÁRIO',
	'TRIBUNAL',
	'VARA',
	'COMARCA',
	'PROTOCOLO',
	'EXPECTATIVA/VALOR',
	'VALOR HONORÁRIOS',
	'PASTA',
	'DATA CADASTRO',
	'DATA FECHAMENTO',
	'DATA TRANSITO',
	'DATA ARQUIVAMENTO',
	'DATA REQUERIMENTO',
	'RESPONSÁVEL',
	'ANOTAÇÕES GERAIS'
]
DROP_COLS_PROCESSOS = [
                                'cod_empresa',
                                'tipo_acao',
                                'local_tramite',
                                'data_atendimento',
                                'vinculo_tipo',
                                'etiqueta',
                                'data_entrada',
                                'prazo',
                                'previsao_saida',
                                'origem',
                                'prognostico',
                                'data_execucao',
                                'migracao',
                                'cod_fase_processo',
                                'processo_traduzido',
                                'campo_livre2',
                                'campo_livre4',
                                'migra_parceiro',
                                'unificador_cliente',
                                'cod_cliente_removido',
                                'migracao2',
                                'migracao3',
                                'cod_empresa',
                                'cod_advogado_usuario',
                                'cod_parte_adversa',
                                'cod_adv_parte_adversa',
                                'tipo',
                                'codorigem',
                                'coddetalhesadm',
                                'contingencia',
                                'acao_ajuizada',
                                'unificador_processo',
                                'cod_processo_removido'
                              ]

DICIO_CONVERSAO_DF_CLIENTES = {
    'codigo'                        : 'ANOTAÇÕES GERAIS',
	'razao_social' 					: 'NOME', # CHECK
	'razao_social_2' 				: 'NOME',
	'nome_fantasia' 				: 'NOME',
	'cpf_cnpj' 						: 'CPF CNPJ', # CHECK
	'rg'							: 'RG', # CHECK
	'responsavel'					: 'ANOTAÇÕES GERAIS', # CHECK
	'telefone1'						: 'TELEFONE', # CHECK
	'telefone2'						: 'CELULAR', # CHECK
	'telefone3'						: 'TELEFONE',
	'email1'						: 'EMAIL', # CHECK
	'email2'						: 'EMAIL',
	'contato_nome'					: 'ANOTAÇÕES GERAIS',
	'contato_ddd1'					: 'ANOTAÇÕES GERAIS',
	'contato_telefone1'				: 'ANOTAÇÕES GERAIS',
	'contato_telefone2'				: 'ANOTAÇÕES GERAIS',
	'estado_civil'				 	: 'ESTADO CIVIL', # CHECK
	'nacionalidade'				 	: 'NACIONALIDADE', # CHECK
	'uf'				 			: 'ESTADO', # CHECK
	'cidade'				 		: 'CIDADE', # CHECK
	'cep'				 			: 'CEP', # CHECK
	'logradouro'				 	: 'ENDEREÇO', # CHECK
	'bairro'				 		: 'BAIRRO', # CHECK
	'grupo_cliente'				 	: 'ANOTAÇÕES GERAIS',
	'pis'				 			: 'PIS PASEP', # CHECK
	'nascimento'				 	: 'DATA DE NASCIMENTO', # CHECK
	'nome_mae'				 		: 'NOME DA MÃE', # CHECK
	'nome_pai'				 		: 'ANOTAÇÕES GERAIS',
	'inscricao_estadual'			: 'ANOTAÇÕES GERAIS',
	'inscricao_municipal'			: 'ANOTAÇÕES GERAIS',
	'ramo_atividade'				: 'ANOTAÇÕES GERAIS',
	'profissao'				 		: 'PROFISSÃO', # CHECK
	'site'				 			: 'ANOTAÇÕES GERAIS',
	'observacoes'				 	: 'ANOTAÇÕES GERAIS',
	'cliente'				 		: 'ANOTAÇÕES GERAIS',
	'inclusao'				 		: 'ANOTAÇÕES GERAIS',
	'telefone_comercial'			: 'ANOTAÇÕES GERAIS',
	'cod_fase_cliente'				: 'ANOTAÇÕES GERAIS',
	'cod_perfil_cliente'			: 'ANOTAÇÕES GERAIS',
	'campo_livre1'				 	: 'ANOTAÇÕES GERAIS',
	'campo_livre2'				 	: 'ANOTAÇÕES GERAIS',
	'cod_campo_livre2'				: 'ANOTAÇÕES GERAIS',
	'cod_terceiro_categoria'		: 'ANOTAÇÕES GERAIS',
	'numero_pasta'				 	: 'ANOTAÇÕES GERAIS',
	'cod_escolaridade'				: 'ANOTAÇÕES GERAIS',
}
DICIO_CONVERSAO_DF_PROCESSOS = {
    'ativo'							: 'ANOTAÇÕES GERAIS',
    'campo_livre1'					: 'ANOTAÇÕES GERAIS',
    'campo_livre3'					: 'ANOTAÇÕES GERAIS',
    'capturar_andamentos'			: 'ANOTAÇÕES GERAIS',
    'cnj_ok'						: 'ANOTAÇÕES GERAIS',
    'cod_cliente'					: 'NOME DO CLIENTE',
    'cod_processo_apensar'			: 'PROCESSO ORIGINÁRIO',
    'cod_usuario'					: 'RESPONSÁVEL',
    'codarea_acao'					: 'GRUPO DE AÇÃO',
    'codassunto'					: 'TIPO DE AÇÃO',
    'codcomarca'					: 'COMARCA',
    'codigo'						: 'PROTOCOLO',
    'codigo_fase'					: 'FASE PROCESSUAL',
    'codlocaltramite'				: 'ETAPA',
    'codobjetoadm'					: 'ANOTAÇÕES GERAIS',
    'codparceiros'					: 'PARTE CONTRÁRIA',
    'codprognostico'				: 'EXPECTATIVA/VALOR',
    'data_contratacao'				: 'DATA REQUERIMENTO',
    'data_distribuicao'				: 'DATA CADASTRO',
    'data_encerramento'				: 'DATA FECHAMENTO',
    'data_sentenca'					: 'DATA ARQUIVAMENTO',
    'data_transitojulgado'			: 'DATA TRANSITO',
    'data_ultima_visualizacao'		: 'ANOTAÇÕES GERAIS',
    'destino'						: 'ANOTAÇÕES GERAIS',
    'exibir_apenso_raiz'			: 'ANOTAÇÕES GERAIS',
    'favorito'						: 'ANOTAÇÕES GERAIS',
    'grupo_processo'				: 'GRUPO DE AÇÃO',
    'inclusao'						: 'DATA CADASTRO',
    'numero_cnj'					: 'NÚMERO DO PROCESSO',
    'numero_interno'				: 'PROTOCOLO',
    'numero_pasta'					: 'PASTA',
    'numero_processo'				: 'NÚMERO DO PROCESSO',
    'numero_vara'					: 'VARA',
    'objeto_acao'					: 'TIPO DE AÇÃO',
    'observacoes'					: 'ANOTAÇÕES GERAIS',
    'pasta'							: 'PASTA',
    'pedido'						: 'ANOTAÇÕES GERAIS',
    'segredo_justica'				: 'ANOTAÇÕES GERAIS',
    'statusprocessual'				: 'FASE PROCESSUAL',
    'tipoprocesso'					: 'TIPO DE AÇÃO',
    'uf'							: 'TRIBUNAL',
    'valor_causa'					: 'EXPECTATIVA/VALOR',
    'valor_causa2'					: 'VALOR HONORÁRIOS'
}




def main():
    ##############################
    ##########
    #          EXTRACTION PHASE
    ##########
    ##############################
    csv_files = get_csv_files()
    filenames = get_filenames(csv_files)
    
    
    
    ##############################
    ##########
    #          TRANSFORMATION PHASE
    ##########
    ##############################

    dataframes_dict = generate_df_dict(csv_files, filenames)
    filtered_dfs = filter_df_dict(dataframes_dict)

    base_clients = generate_base_clients(filtered_dfs)
    base_clients['PAIS'] = base_clients['PAIS'].map({'Brasileiro' : 'BRASIL', 'Brasileira' : 'BRASIL', '' : ''})
    # print(base_clients)
    # base_df_lawsuits = filtered_dfs['v_processos']
    # base_df_clients  = filtered_dfs['v_clientes']

    # base_df_clients['NOME']                 = base_df_clients['razao_social']
    # base_df_clients['CPF CNPJ']             = base_df_clients['cpf_cnpj']
    # base_df_clients['RG']                   = base_df_clients['rg']
    # base_df_clients['TELEFONE']             = base_df_clients['telefone1']
    # base_df_clients['CELULAR']              = base_df_clients['telefone2']
    # base_df_clients['EMAIL']                = base_df_clients['email1']
    # base_df_clients['ESTADO CIVIL']         = base_df_clients['estado_civil']
    # base_df_clients['NACIONALIDADE']        = base_df_clients['nacionalidade']
    # base_df_clients['ESTADO']               = base_df_clients['uf']
    # base_df_clients['CIDADE']               = base_df_clients['cidade']
    # base_df_clients['CEP']                  = base_df_clients['cep']
    # base_df_clients['ENDEREÇO']             = base_df_clients['logradouro']
    # base_df_clients['BAIRRO']               = base_df_clients['bairro']
    # base_df_clients['PIS PASEP']            = base_df_clients['pis']
    # base_df_clients['DATA DE NASCIMENTO']   = base_df_clients['nascimento']
    
    

    
    ##############################
    ##########
    #          LOAD PHASE
    ##########
    ##############################

    print(base_clients[COLS_CLIENTES_FINAL])
    final_df_clients    = base_clients[COLS_CLIENTES_FINAL]
    # final_df_clients    = base_clients
    write_excel(final_df_clients, 'FINAL - CLIENTES')

    # final_df_lawsuits   = base_df_lawsuits[COLS_PROCESSOS_FINAL]
    # write_excel(final_df_lawsuits, 'FINAL - PROCESSOS')






##################################################
####################
#                    INITIALIZATION OF SCRIPT
####################
##################################################

if __name__ == '__main__':
    main()