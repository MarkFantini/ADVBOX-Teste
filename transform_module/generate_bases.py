import pandas as pd

FILTER_COLS = {
	'v_advogado_adverso'			: ['codigo', 'nome', 'telefone1', 'telefone2', 'email1', 'data_cadastro', 'cod_escritorio', 'oab', 'ativo'],

	'v_area_atuacao'		        : ['codigo', 'descricao', 'ativo'],

	'v_assunto' 			        : ['codigo', 'descricao', 'ativo'],

	'v_atendimentos_processo'	    : ['codigo', 'descricao', 'codcliente', 'inclusao', 'codusuario', 'codprocesso', 'data_atendimento', 'cod_tipo_movimento', 'ativo'],

	'v_campo_livre2'			    : ['codigo', 'descricao', 'data_cadastro', 'ativo', 'tipo'],

	'v_clientes'				    : ['codigo', 'razao_social', 'razao_social_2', 'nome_fantasia', 'cpf_cnpj', 'rg', 'responsavel', 'telefone1', 'telefone2',
									   'telefone3', 'email1', 'email2', 'contato_nome', 'contato_ddd1', 'contato_telefone1', 'contato_telefone2', 'estado_civil', 'nacionalidade', 'uf', 'cidade', 'cep', 'logradouro', 'bairro', 'grupo_cliente', 'pis', 'nascimento', 'nome_mae', 'nome_pai', 'inscricao_estadual', 'inscricao_municipal', 'ramo_atividade', 'profissao', 'site', 'observacoes', 'cliente', 'inclusao', 'telefone_comercial', 'cod_fase_cliente', 'cod_perfil_cliente', 'campo_livre1', 'campo_livre2', 'cod_campo_livre2', 'cod_terceiro_categoria', 'numero_pasta', 'cod_escolaridade','ativo','tipocliente',],

	'v_cliente_estado_civil'	    : ['codigo', 'descricao', 'data_cadastro', 'ativo'],

	'v_comarca'					    : ['codigo', 'descricao', 'ativo'],

	'v_estado_brasil'			    : ['codigo', 'estado', 'uf', 'ativo'],

	'v_fase'					    : ['codigo', 'fase', 'ativo'],

	'v_grupo_cliente'			    : ['codigo', 'descricao', 'ativo'],

	'v_grupo_processo'			    : ['codigo', 'descricao', 'ativo'],

	'v_litis_adverso'		        : ['cod_parte', 'cod_processo', 'cod_advparte', 'cod_usuario', 'parte_principal', 'ativo'],

	'v_litis_cliente'			    : ['cod_parte', 'cod_processo', 'cod_usuario', 'parte_principal', 'ativo', 'listar_como_cliente'],

	'v_litis_terceiro'			    : ['cod_parte', 'cod_processo', 'cod_usuario', 'parte_principal', 'ativo'],

	'v_localizador'				    : ['codigo', 'descricao', 'ativo'],

	'v_local_tramite'			    : ['codigo', 'descricao', 'ativo'],

	'v_objeto_acao'				    : ['codigo', 'descricao', 'ativo', 'cod_processo_tipo'],

	'v_pastas'					    : ['codigo', 'descricao', 'ativo'],

	'v_perfil_cliente'			    : ['codigo', 'descricao', 'data_cadastro', 'ativo'],

	'v_processos'				    : ['ativo', 'campo_livre1', 'campo_livre3', 'capturar_andamentos', 'cnj_ok', 'cod_cliente', 'cod_processo_apensar', 'cod_usuario', 

						 			   'codarea_acao', 'codassunto', 'codcomarca', 'codigo', 'codigo_fase', 'codlocaltramite', 'codobjetoadm', 'codparceiros', 'codprognostico', 'data_contratacao', 'data_distribuicao', 'data_encerramento', 'data_sentenca', 'data_transitojulgado', 'data_ultima_visualizacao', 'destino', 'exibir_apenso_raiz', 'favorito', 'grupo_processo', 'inclusao', 'numero_cnj', 'numero_interno', 'numero_pasta', 'numero_processo', 'numero_vara', 'objeto_acao', 'observacoes', 'pasta', 'pedido', 'segredo_justica', 'statusprocessual', 'tipoprocesso', 'uf', 'valor_causa', 'valor_causa2'],

	'v_prognosticos'			    : ['codigo', 'descricao', 'ativo'],

	'v_protocolo_status'		    : ['codigo', 'descricao', 'data_cadastro', 'ativo'],

	'v_recurso'					    : ['codigo', 'codusuario', 'codprocesso', 'codtipo', 'codtribunal', 'orgao_julgador', 'relator', 'data_distribuicao', 'data_julgamento', 

									   'inclusao', 'codprognostico', 'numero_recurso', 'cod_orgao_julgado', 'cod_tribunal_uf', 'numero_orgao_julgado'],

	'v_recurso_prognostico'		    : ['codigo', 'descricao', 'ativo'],

	'v_statusprocessual'		    : ['codigo', 'descricao', 'ativo'],

	'v_tipo_recurso'			    : ['codigo', 'descricao', 'ativo'],

	'v_tribunal'				    : ['codigo', 'descricao', 'ativo'],

	'v_usuario_advogado'	        : ['cod_usuario', 'cod_advogado'],

	'v_usuario'					    : ['id', 'usuario', 'senha', 'nome', 'apelido', 'data_cadastro', 'dia_nascimento', 'mes_nascimento', 'ativo', 'cod_usuario_nivel', 

									   'cod_cor_sistema', 'cod_modulo_principal', 'cod_controle_acesso_grupo', 'cod_tema_sistema', 'codigo', 'modelo_agenda', 'agrupamento_imail', 'email', 'flag_alteracao_cor_integra', 'horario_personalizado'],

	'v_valor_causa2'		        : ['codigo', 'valor_causa', 'codprocesso', 'data_inclusao', 'codusuario'],

	'v_valor_causa'				    : ['codigo', 'valor_causa', 'codprocesso', 'data_inclusao', 'codusuario'],

}

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

CLIENTS_FINAL_COLS = [
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
	'PAIS',  # CHECK
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

LAWSUITS_FINAL_COLS = [
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

def generate_df_dict(csv_files, filenames):
	df_dict = dict()

	for csv, name in zip(csv_files, filenames):
		try:
			df_dict[name] = pd.read_csv(csv, delimiter=';', encoding='utf-8', dtype=str)
			df_dict[name] = df_dict[name].fillna('')
		except UnicodeDecodeError:
			df_dict[name] = pd.read_csv(csv, delimiter=';', encoding='latin1', dtype=str)
			df_dict[name] = df_dict[name].fillna('')
	
	return df_dict


def filter_df_dict(dataframes_dict):
	filtered_dfs = {}

	for name, df in dataframes_dict.items():
		filtered_dfs[name] = df[FILTER_COLS[name]]

	return filtered_dfs


def generate_base_clients(dataframes_dict, name='v_clientes'):
	base_clients = dataframes_dict[name].copy()

	base_clients[CLIENTS_FINAL_COLS] = ''
	
	for result_col, base_col in BASE_CLIENTS_DICT.items():
		try:
			base_clients[result_col] = base_clients[base_col]
		except:
			continue
		
	return base_clients


def generate_base_lawsuits(dataframes_dict, name='v_processos'):
	base_lawsuits = dataframes_dict[name].copy()

	base_lawsuits[LAWSUITS_FINAL_COLS] = ''
	
	# for result_col, base_col in BASE_LAWSUITS_DICT.items():
	# 	try:
	# 		base_lawsuits[result_col] = base_lawsuits[base_col]
	# 	except:
	# 		continue
	
	return base_lawsuits

