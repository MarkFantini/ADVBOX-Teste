import re
import pandas as pd
from datetime import date

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

PROFESSIONS_DICT = {
	'APOSENTADO'                                                : 'Aposentadoria',
	'Acabador'                                                  : 'Construção Civil',
	'Administrador'                                             : 'Administração',
	'Administrador de RH'                                       : 'Administração',
	'Administrador de empresas'                                 : 'Administração',
	'Administradora de Empresas'                                : 'Administração',
	'Advogado'                                                  : 'Direito',
	'Agente Penitenciario'                                      : 'Segurança',
	'Agente Penitenciário'                                      : 'Segurança',
	'Agente de Viagens'                                         : 'Turismo',
	'Ajudante'                                                  : 'Serviços Gerais',
	'Ajudante Florestal'                                        : 'Serviços Gerais',
	'Ajudante Geral'                                            : 'Serviços Gerais',
	'Ajudante de Adestrador'                                    : 'Serviços Gerais',
	'Ajudante de Limpeza'                                       : 'Serviços Gerais',
	'Ajudante de Mecânico'                                      : 'Serviços Gerais',
	'Ajudante de Motorista'                                     : 'Serviços Gerais',
	'Ajudante de Pedreiro'                                      : 'Serviços Gerais',
	'Ajudante de motorista'                                     : 'Serviços Gerais',
	'Ajudante de pedreiro'                                      : 'Serviços Gerais',
	'Analista de Gestão'                                        : 'Administração',
	'Analista de Sistema'                                       : 'Tecnologia',
	'Analista de sistemas'                                      : 'Tecnologia',
	'Anotador de Pátio'                                         : 'Logística e Transporte',
	'Aposentada'                                                : 'Aposentadoria',
	'Aposentado'                                                : 'Aposentadoria',
	'Aposentadoria'                                             : 'Aposentadoria',
	'Arquiteto'                                                 : 'Engenharia e Arquitetura',
	'Artesã'                                                    : 'Artesanato e Cultura',
	'Ascensorista'                                              : 'Serviços Gerais',
	'Assistente Admininistrativo'                               : 'Administração',
	'Assistente Administrativo'                                 : 'Administração',
	'Assistente Financeiro'                                     : 'Finanças',
	'Assistente Jurídica'                                       : 'Direito',
	'Assistente Técnico'                                        : 'Técnico',
	'Assistente administrativo'                                 : 'Administração',
	'Assistente técnico'                                        : 'Técnico',
	'Atendente'                                                 : 'Comércio e Atendimento',
	'Autonoma'                                                  : 'Autônomo(a)',
	'Autonomo'                                                  : 'Autônomo(a)',
	'Autonôma'                                                  : 'Autônomo(a)',
	'Autonômo'                                                  : 'Autônomo(a)',
	'Autônoma'                                                  : 'Autônomo(a)',
	'Autônomo'                                                  : 'Autônomo(a)',
	'Aux Serviços'                                              : 'Serviços Gerais',
	'Aux de Serviço'                                            : 'Serviços Gerais',
	'Auxikliar Servicos Gerais'                                 : 'Serviços Gerais',
	'Auxiliar'                                                  : 'Serviços Gerais',
	'Auxiliar Administrativo'                                   : 'Administração',
	'Auxiliar Logística I'                                      : 'Logística',
	'Auxiliar Mecânico'                                         : 'Manutenção e Reparos',
	'Auxiliar administrativo'                                   : 'Administração',
	'Auxiliar de Educação'                                      : 'Educação',
	'Auxiliar de Enfermagem'                                    : 'Ciências da Saúde',
	'Auxiliar de Expedição'                                     : 'Logística',
	'Auxiliar de Leito Quente'                                  : 'Serviços Gerais',
	'Auxiliar de Limpeza'                                       : 'Serviços Gerais',
	'Auxiliar de Manutenção'                                    : 'Serviços Gerais',
	'Auxiliar de Produção'                                      : 'Serviços Gerais',
	'Auxiliar de Saude Bucal'                                   : 'Ciências da Saúde',
	'Auxiliar de Servicos Gerais'                               : 'Serviços Gerais',
	'Auxiliar de Serviços'                                      : 'Serviços Gerais',
	'Auxiliar de Serviços Gerais'                               : 'Serviços Gerais',
	'Auxiliar de Topografia'                                    : 'Engenharia e Projetos',
	'Auxiliar de cozinha'                                       : 'Serviços Gerais',
	'Auxiliar de serviços gerais'                               : 'Serviços Gerais',
	'Auxiliar de sáude bucal'                                   : 'Ciências da Saúde',
	'Auxiliar na Educação'                                      : 'Educação',
	'Auxliar de Serviços Gerais'                                : 'Serviços Gerais',
	'Babá'                                                      : 'Cuidados Pessoais',
	'Balconista'                                                : 'Comércio e Atendimento',
	'Bancária'                                                  : 'Serviços Financeiros',
	'Biomédico'                                                 : 'Ciências da Saúde',
	'Bombeiro Civil'                                            : 'Segurança e Emergência',
	'Cabeleireira'                                              : 'Beleza e Estética',
	'Cabelereira'                                               : 'Beleza e Estética',
	'Carpinteiro'                                               : 'Construção Civil',
	'Carpiteiro'                                                : 'Construção Civil',
	'Cobrador'                                                  : 'Transporte Coletivo',
	'Comerciante'                                               : 'Comércio e Vendas',
	'Comerciente'                                               : 'Comércio e Vendas',
	'Comerciária'                                               : 'Comércio e Vendas',
	'Comprador'                                                 : 'Logística e Compras',
	'Condutor socorrista'                                       : 'Segurança e Emergência',
	'Confeiteira'                                               : 'Alimentos e Gastronomia',
	'Consultor'                                                 : 'Consultoria e Negócios',
	'Contadora'                                                 : 'Finanças e Contabilidade',
	'Coopeira'                                                  : 'Serviços Gerais',
	'Coordenador Operacional'                                   : 'Gestão Operacional',
	'Corretor'                                                  : 'Vendas e Negócios Imobiliários',
	'Corretor de Imóveis'                                       : 'Vendas e Negócios Imobiliários',
	'Costureira'                                                : 'Moda e Vestuári',
	'Cozinheira'                                                : 'Alimentos e Gastronomia',
	'Desempregada'                                              : 'Disponível para o Mercado',
	'Desempregado'                                              : 'Disponível para o Mercado',
	'Desempregado / Agente Penitenciário'                       : 'Disponível para o Mercado',
	'Designer'                                                  : 'Design e Artes Visuais',
	'Do Lar'                                                    : 'Trabalho Doméstico',
	'Do lar'                                                    : 'Trabalho Doméstico',
	'Domestica'                                                 : 'Trabalho Doméstico',
	'Doméstica'                                                 : 'Trabalho Doméstico',
	'Educador Físico'                                           : 'Educação Física',
	'Eletricista'                                               : 'Manutenção e Reparos',
	'Eletricista Manutenção'                                    : 'Manutenção e Reparos',
	'Eletricista de Manutenção'                                 : 'Manutenção e Reparos',
	'Embalador'                                                 : 'Logística e Transporte',
	'Embalador Líder'                                           : 'Logística e Transporte',
	'Empregada Doméstica'                                       : 'Trabalho Doméstico',
	'Empresario'                                                : 'Administração',
	'Empresária'                                                : 'Administração',
	'Empresário'                                                : 'Administração',
	'Encanador'                                                 : 'Construção Civil',
	'Encanador Industrial'                                      : 'Indústria',
	'Encarregado'                                               : 'Serviços Gerais',
	'Encarregado Administrativo'                                : 'Serviços Gerais',
	'Encarregado Operacional'                                   : 'Serviços Gerais',
	'Encarregado de Carpintaria'                                : 'Serviços Gerais',
	'Encarregado de Mecânica'                                   : 'Serviços Gerais',
	'Encarregado de Produção'                                   : 'Serviços Gerais',
	'Encarregado de Transportes'                                : 'Serviços Gerais',
	'Encarregado de Tubulação'                                  : 'Serviços Gerais',
	'Enfermeira'                                                : 'Ciências da Saúde',
	'Engenheira'                                                : 'Engenharia e Projetos',
	'Engenheira Civil'                                          : 'Engenharia e Projetos',
	'Engenheiro'                                                : 'Engenharia e Projetos',
	'Engenheiro Civil'                                          : 'Engenharia e Projetos',
	'Engenheiro Eletricista'                                    : 'Engenharia e Projetos',
	'Engenheiro Elétrico'                                       : 'Engenharia e Projetos',
	'Engenheiro Mecânico'                                       : 'Engenharia e Projetos',
	'Engenheiro de Planejamento'                                : 'Engenharia e Projetos',
	'Entrada e saída de LA'                                     : 'Logística',
	'Entregador'                                                : 'Logística e Transporte',
	'Escarfador'                                                : 'Indústria Metalúrgica',
	'Esmerilhador'                                              : 'Indústria Metalúrgica',
	'Estudante'                                                 : 'Educação',
	'Farmacêutica'                                              : 'Ciências da Saúde',
	'Faxineira'                                                 : 'Serviços Gerais',
	'Feitor'                                                    : 'Agricultura',
	'Ferroviário'                                               : 'Transporte Ferroviário',
	'Fiscal de Obras'                                           : 'Construção Civil',
	'Fotógrafo'                                                 : 'Design e Artes Visuais',
	'Frentista'                                                 : 'Postos de Combustíveis',
	'Funcionária Pública'                                       : 'Servidor Público(a)',
	'Funcionário Púb. Estadual. - Investigador de P C'          : 'Servidor Público(a)',
	'Gerente Admisnitrativo'                                    : 'Administração',
	'Gerente administrativa'                                    : 'Administração',
	'Gerente de Acougue'                                        : 'Serviços Gerais',
	'Historiador'                                               : 'Ciências Humanas',
	'Idustriario'                                               : 'Industriário(a)',
	'Impressor'                                                 : 'Indústria Gráfica',
	'Industariário'                                             : 'Indústria',
	'Industriario'                                              : 'Indústria',
	'Industriária'                                              : 'Indústria',
	'Industriário'                                              : 'Indústria',
	'Industrário'                                               : 'Indústria',
	'Inspetor'                                                  : 'Controle de Qualidade',
	'Instalador e Reparador'                                    : 'Manutenção Técnica',
	'Instrutora'                                                : 'Educação',
	'Juiz'                                                      : 'Direito',
	'Lavrador'                                                  : 'Agricultura',
	'Lavradora'                                                 : 'Agricultura',
	'Leiturista'                                                : 'Serviços Públicos',
	'Líder de grupo'                                            : 'Gestão Operacional',
	'Mandrilhador'                                              : 'Indústria Metalúrgica',
	'Manicure'                                                  : 'Beleza e Estética',
	'Manobrista'                                                : 'Transportes',
	'Manut Mecanica'                                            : 'Manutenção e Reparos',
	'Maquinista'                                                : 'Transportes',
	'Marmorista'                                                : 'Construção Civil',
	'Maçariqueiro'                                              : 'Construção Civil',
	'Mecanico'                                                  : 'Manutenção e Reparos',
	'Mecanico de Manutencao'                                    : 'Manutenção e Reparos',
	'Mecanico de Manutenção'                                    : 'Manutenção e Reparos',
	'Mecanico de refrigeração'                                  : 'Indústria',
	'Mecanico manutenção'                                       : 'Manutenção e Reparos',
	'Mecânico'                                                  : 'Manutenção e Reparos',
	'Mecânico Hidraúlico'                                       : 'Indústria',
	'Mecânico Hidraúlico II'                                    : 'Indústria',
	'Mecânico Hidráulico'                                       : 'Indústria',
	'Mecânico Hidráulico III'                                   : 'Indústria',
	'Mecânico Hidráulico IV'                                    : 'Indústria',
	'Mecânico Industrial'                                       : 'Indústria',
	'Mecânico Manutenção'                                       : 'Manutenção e Reparos',
	'Mecânico de Manutençao'                                    : 'Manutenção e Reparos',
	'Mecânico de Manutenção'                                    : 'Manutenção e Reparos',
	'Mecânico de Refrigeração'                                  : 'Indústria',
	'Mecânico de manutenção'                                    : 'Manutenção e Reparos',
	'Mecânico manutenção I'                                     : 'Manutenção e Reparos',
	'Mecânico montador'                                         : 'Indústria',
	'Menor Impubere'                                            : 'Menor Impúbere',
	'Menor Impúbere'                                            : 'Menor Impúbere',
	'Menor impúbere'                                            : 'Menor Impúbere',
	'Metalurgico'                                               : 'Indústria',
	'Metalúgico'                                                : 'Indústria',
	'Metalúrgico'                                               : 'Indústria',
	'Micro Empresario'                                          : 'Administração',
	'Microempreendedor Individual'                              : 'Administração',
	'Militar'                                                   : 'Segurança',
	'Modelador'                                                 : 'Modelagem e Design',
	'Montador'                                                  : 'Construção Civil',
	'Montador de Andaime'                                       : 'Construção Civil',
	'Moto-Boy'                                                  : 'Transportes',
	'Motorista'                                                 : 'Motorista',
	'Motorista carreteiro'                                      : 'Motorista',
	'Motorista de Aplicativo'                                   : 'Motorista',
	'Motorista de ônibus'                                       : 'Motorista',
	'Mototaxista'                                               : 'Transportes',
	'Médico'                                                    : 'Médico',
	'Médico CRM-MG 29.610'                                      : 'Médico',
	'Operador'                                                  : 'Serviços Gerais',
	'Operador de Guindaste'                                     : 'Engenharia e Projetos',
	'Operador de Máquina'                                       : 'Engenharia e Projetos',
	'Operador de Máquinas'                                      : 'Engenharia e Projetos',
	'Operador de Ponte'                                         : 'Engenharia e Projetos',
	'Operador de Ponte Rolante'                                 : 'Engenharia e Projetos',
	'Operador de Produção'                                      : 'Engenharia e Projetos',
	'Operador de Produção - Aciaria II'                         : 'Engenharia e Projetos',
	'Operador de máquinas'                                      : 'Engenharia e Projetos',
	'Operador de máquinas de cinta'                             : 'Engenharia e Projetos',
	'Operador de ponte'                                         : 'Engenharia e Projetos',
	'Operador de produção'                                      : 'Engenharia e Projetos',
	'Operador de utilidades'                                    : 'Engenharia e Projetos',
	'Operadora'                                                 : 'Serviços Gerais',
	'Operadora de Caixa'                                        : 'Serviços Gerais',
	'Padeiro'                                                   : 'Alimentação',
	'Pedagoga'                                                  : 'Educação',
	'Pedreiro'                                                  : 'Construção Civil',
	'Pedreiro refratário'                                       : 'Construção Civil',
	'Pensionista'                                               : 'Pensionista',
	'Pintor'                                                    : 'Construção Civil',
	'Policial Militar'                                          : 'Segurança',
	'Porteiro'                                                  : 'Administração e Serviços Gerais',
	'Preparador de Máquinas'                                    : 'Manutenção e Reparos',
	'Preservador de coqueria'                                   : 'Indústria',
	'Produtor rural'                                            : 'Agricultura e Pecuária',
	'Professor'                                                 : 'Educação',
	'Professora'                                                : 'Educação',
	'Programador'                                               : 'Tecnologia',
	'Projetista'                                                : 'Engenharia e Projetos',
	'Representante'                                             : 'Comércio e Atendimento',
	'Representante Comercial'                                   : 'Comércio e Atendimento',
	'Representante comercial'                                   : 'Comércio e Atendimento',
	'Representante de Vendas'                                   : 'Comércio e Atendimento',
	'Revestidor'                                                : 'Construção Civil',
	'Salgadeira'                                                : 'Alimentação',
	'Secretaria'                                                : 'Outros',
	'Secretária'                                                : 'Outros',
	'Segurança'                                                 : 'Segurança',
	'Servente'                                                  : 'Construção Civil',
	'Servente de obras'                                         : 'Construção Civil',
	'Servidor Público'                                          : 'Servidor(a) Público(a)',
	'Servidora Publica'                                         : 'Servidor(a) Público(a)',
	'Servidora Pública'                                         : 'Servidor(a) Público(a)',
	'Soldado'                                                   : 'Segurança',
	'Soldador'                                                  : 'Outros',
	'Supervisor'                                                : 'Supervisor(a)',
	'Supervisor Manutenção'                                     : 'Supervisor(a)',
	'Supervisor Mecânico'                                       : 'Manutenção e Reparos',
	'Supervisor de Manutenção'                                  : 'Manutenção e Reparos',
	'Supervisor de Montagem'                                    : 'Supervisor(a)',
	'Supervisor de manutenção'                                  : 'Manutenção e Reparos',
	'Supervisor operacional'                                    : 'Supervisor(a)',
	'Supervisora de Vendas'                                     : 'Comércio e Atendimento',
	'Sócia'                                                     : 'Administração e Serviços Gerais',
	'Taxista'                                                   : 'Transportes',
	'Tecnica de Segurança'                                      : 'Segurança',
	'Tecnico Enfermagem'                                        : 'Ciências da Saúde',
	'Tecnico de Enfermagem'                                     : 'Ciências da Saúde',
	'Tecnico de Manutencao'                                     : 'Manutenção e Reparos',
	'Tecnico de Manutenção'                                     : 'Manutenção e Reparos',
	'Topógrafo'                                                 : 'Engenharia e Projetos',
	'Torneiro Mecânico'                                         : 'Engenharia e Projetos',
	'Torneiro mecânico'                                         : 'Engenharia e Projetos',
	'Trabalhadora Rural'                                        : 'Agricultura e Pecuária',
	'Trocador de óleo'                                          : 'Engenharia e Projetos',
	'Técnica de Enfermagem'                                     : 'Ciências da Saúde',
	'Técnica de Segurança'                                      : 'Segurança',
	'Técnica de efermagem'                                      : 'Ciências da Saúde',
	'Técnica em Enfermagem'                                     : 'Ciências da Saúde',
	'Técnica em Raio X'                                         : 'Ciências da Saúde',
	'Técnica em Saúde Bucal'                                    : 'Ciências da Saúde',
	'Técnica em enfermagem'                                     : 'Ciências da Saúde',
	'Técnico'                                                   : 'Técnico(a)',
	'Técnico Administrativo'                                    : 'Administração',
	'Técnico Eletricista'                                       : 'Indústria',
	'Técnico Esportivo'                                         : 'Educação Física',
	'Técnico Hidráulico II'                                     : 'Indústria',
	'Técnico Inspetor de Qualidade'                             : 'Indústria',
	'Técnico Manutenção'                                        : 'Manutenção e Reparos',
	'Técnico Mecânico'                                          : 'Indústria',
	'Técnico Mecânico de Manutenção'                            : 'Manutenção e Reparos',
	'Técnico de Laboratório'                                    : 'Indústria',
	'Técnico de Manutenção'                                     : 'Manutenção e Reparos',
	'Técnico de Planejamento'                                   : 'Engenharia e Projetos',
	'Técnico de Segurança de Trabalho'                          : 'Segurança',
	'Técnico em Edificações'                                    : 'Engenharia e Projetos',
	'Técnico em Eletrica'                                       : 'Engenharia e Projetos',
	'Técnico em Enfermagem'                                     : 'Ciências da Saúde',
	'Técnico em Instrumentação'                                 : 'Indústria',
	'Técnico em Manutenção'                                     : 'Manutenção e Reparos',
	'Técnico em Mecânica'                                       : 'Indústria',
	'Técnico em Produção'                                       : 'Engenharia e Projetos',
	'Técnico em Raios X'                                        : 'Ciências da Saúde',
	'Técnico em Refratário'                                     : 'Engenharia e Projetos',
	'Técnico em Segurança'                                      : 'Segurança',
	'Técnico em automação'                                      : 'Engenharia e Projetos',
	'Técnico em eletrotécnica'                                  : 'Engenharia e Projetos',
	'Técnico em instrumentação'                                 : 'Engenharia e Projetos',
	'Técnico mecânico hidraúlico'                               : 'Indústria',
	'Vendedor'                                                  : 'Comércio e Atendimento',
	'Vendedora'                                                 : 'Comércio e Atendimento',
	'Vigia'                                                     : 'Outros',
	'Vigilante'                                                 : 'Segurança',
	'Vigilante Armado'                                          : 'Segurança',
	'do Lar'                                                    : 'Serviço Doméstico',
	'do lar'                                                    : 'Serviço Doméstico',
	'industriario'                                              : 'Industriário(a)',
	'menor impúbere'                                            : 'Menor impúbere',
	''                                                          : '',
	'operador de produção II'                                   : 'Indústria',
	'recepcionista'                                             : 'Administração e Serviços Gerais',
	'taxista'                                                   : 'Transportes',
}


def clients_data_treatment(df, csv_paths):
	df = df.copy()

	# 01. NOME
	df['NOME'] = pick_first_nonempty_row(df, col1='razao_social', col2='razao_social_2', col3='nome_fantasia')
	
	duplicated_names = df.duplicated(subset=['NOME'], keep='first')
	df = df[~duplicated_names]

	# 02. CPF CNPJ
	df['CPF CNPJ'] = df['cpf_cnpj']
	df[['CPF CNPJ']] = df[['CPF CNPJ']].replace({'\.' : '', '-' : '', '/' : ''}, regex=True)

	# 03. RG
	df['RG'] = df['rg']

	# 04. NACIONALIDADE
	df['NACIONALIDADE'] = df['nacionalidade'].str.capitalize()

	# 05. DATA DE NASCIMENTO
	df['DATA DE NASCIMENTO'] = df['nascimento']
	df['DATA DE NASCIMENTO'] = date_formatting(df, col='DATA DE NASCIMENTO')

	# 06. ESTADO CIVIL
	df['ESTADO CIVIL'] = df['estado_civil'].str.upper()
	df['ESTADO CIVIL'] = df['ESTADO CIVIL'].str.replace('0', '')

	# 07. PROFISSÃO
	df['PROFISSÃO'] = df['profissao']
	df['PROFISSÃO'] = fix_encoding(csv_paths, df, col='profissao')
	df['PROFISSÃO'] = df['PROFISSÃO'].map(PROFESSIONS_DICT)

	# 08. SEXO
	df['SEXO'] = df['NACIONALIDADE'].str.lower()
	df['SEXO'] = df['SEXO'].map({
		'brasileiro' : 'M',
        'brasileira' : 'F',
        '' : ''
		})

	# 09. CELULAR
	df['CELULAR'] = df['telefone2']

	# 10. TELEFONE
	df['TELEFONE'] = pick_first_nonempty_row(df, col1='telefone1', col2='telefone3')

	# 11. EMAIL
	df['EMAIL'] = pick_first_nonempty_row(df, col1='email1', col2='email2')

	# 12. PAIS
	df['PAIS'] = df['NACIONALIDADE'].str.lower()
	df['PAIS'] = df['PAIS'].map({
		'brasileiro' : 'BRASIL',
        'brasileira' : 'BRASIL',
        '' : ''
		})
	
	# 13. ESTADO
	df['ESTADO'] = df['uf'].str.upper()

	# 14. CIDADE
	df['CIDADE'] = df['cidade']

	# 15. BAIRRO
	df['BAIRRO'] = df['bairro']
	df['BAIRRO'] = fix_encoding(csv_paths, df, col='bairro')

	# 16. ENDEREÇO
	df['ENDEREÇO'] = df['logradouro']

	# 17. CEP
	df['CEP'] = df['cep']
	df[['CEP']] = df[['CEP']].replace({'\.' : '', '-' : ''}, regex=True)

	# 18. PIS PASEP
	df['PIS PASEP'] = df['pis']
	df['PIS PASEP'] = df['PIS PASEP'].apply(format_pis)

	# 19. CTPS
	df['CTPS'] = ''
	
	# 20. CID
	df['CID'] = ''
	
	# 21. NOME DA MÃE
	df['NOME DA MÃE'] = df['nome_mae']

	# 22. ORIGEM DO CLIENTE
	df['ORIGEM DO CLIENTE'] = 'MIGRAÇÃO'

	# 23. ANOTAÇÕES GERAIS
	df['ANOTAÇÕES GERAIS'] = ''
	df['ANOTAÇÕES GERAIS'] = insert_general_annotation(
        df,
        original_cols=['razao_social', 'razao_social_2', 'nome_fantasia', 'responsavel', 'contato_nome', 'contato_telefone1', 'observacoes', 'cliente', 'ativo', 'inclusao', 'grupo_cliente', 'telefone_comercial', 'nome_pai', 'cod_fase_cliente', 'cod_perfil_cliente', 'campo_livre1', 'campo_livre2', 'numero_pasta', 'cod_escolaridade'],
        descriptions=['Razão Social', 'Razão Social 2', 'Nome Fantasia', 'Responsável', 'Nome do Contato', 'Telefone Contato', 'Observações', 'Tipo do Cliente', 'Ativo', 'Data de Inclusão', 'Grupo do Cliente', 'Telefone Comercial', 'Nome do Pai', 'Fase Cliente', 'Perfil Cliente', 'Campo Livre 1', 'Campo Livre 2', 'Número da Pasta', 'Código Escolaridade'],
	)



	return df

def lawsuits_data_treatment(df, csv_paths):
    df = df.copy()
    
    # 01. NOME DO CLIENTE
    clients_names = create_subset_df(csv_paths, cols=['codigo', 'razao_social', 'razao_social_2', 'nome_fantasia'], file='v_clientes')
    
    clients_names['NOME'] = pick_first_nonempty_row(clients_names, col1='razao_social', col2='razao_social_2', col3='nome_fantasia')
    
    clients_dict = create_code_description_dict(clients_names, code='codigo', descrip='NOME')
    
    df['NOME DO CLIENTE'] = df['cod_cliente']
    df['NOME DO CLIENTE'] = df['NOME DO CLIENTE'].map(clients_dict)
    duplicated_names = df.duplicated(subset=['NOME DO CLIENTE'], keep='first')
    df = df[~duplicated_names]
    

    # 02. PARTE CONTRÁRIA
    

    # 03. TIPO DE AÇÃO - v_assunto | 'codassunto'
    df['TIPO DE AÇÃO'] = column_mapped_by_dict(df, csv_paths, cols=['codigo', 'descricao'], file='v_objeto_acao', code='codigo', descrip='descricao', df_col='objeto_acao')

    # 04. GRUPO DE AÇÃO - v_area_atuacao | 'codarea_acao'
    df['GRUPO DE AÇÃO'] = column_mapped_by_dict(df, csv_paths, cols=['codigo', 'descricao'], file='v_area_atuacao', code='codigo', descrip='descricao', df_col='codarea_acao')

    # 05. FASE PROCESSUAL
    fase_subset = create_subset_df(csv_paths, cols=['codigo', 'fase'], file='v_fase')
    fase_dict = create_code_description_dict(fase_subset, code='codigo', descrip='fase')
    
    df['FASE PROCESSUAL'] = df['codigo_fase']
    df['FASE PROCESSUAL'] = df['FASE PROCESSUAL'].map(fase_dict)
    
    # 06. ETAPA
    

    # 07. NÚMERO DO PROCESSO
    df['NÚMERO DO PROCESSO'] = df['numero_processo']
    df['NÚMERO DO PROCESSO'], df['PROTOCOLO'] = process_number_validation(df)
    
    # 08. PROCESSO ORIGINÁRIO
    

    # 09. TRIBUNAL


    # 10. VARA - v_local_tramite | 'codlocaltramite'
    df['VARA'] = column_mapped_by_dict(df, csv_paths, cols=['codigo', 'descricao'], file='v_local_tramite', code='codigo', descrip='descricao', df_col='codlocaltramite')
    

    # 11. COMARCA
    df['COMARCA'] = column_mapped_by_dict(df, csv_paths, cols=['codigo', 'descricao'], file='v_comarca', code='codigo', descrip='descricao', df_col='codcomarca')

    # 12. PROTOCOLO
    

    # 13. EXPECTATIVA/VALOR
    df['EXPECTATIVA/VALOR'] = df['valor_causa'].astype(float)
    df['EXPECTATIVA/VALOR'] = df['EXPECTATIVA/VALOR'].apply(lambda x: f"{x:.2f}")
    df['EXPECTATIVA/VALOR'] = df['EXPECTATIVA/VALOR'].astype(str)
    df['EXPECTATIVA/VALOR'] = df['EXPECTATIVA/VALOR'].str.replace('.', ',')

    # 14. VALOR HONORÁRIOS
    df['VALOR HONORÁRIOS'] = df['valor_causa2'].astype(float)
    df['VALOR HONORÁRIOS'] = df['VALOR HONORÁRIOS'].apply(lambda x: f"{x:.2f}")
    df['VALOR HONORÁRIOS'] = df['VALOR HONORÁRIOS'].astype(str)
    df['VALOR HONORÁRIOS'] = df['VALOR HONORÁRIOS'].str.replace('.', ',')

    # 15. PASTA
    pasta_df = create_subset_df(csv_paths, cols=['numero_pasta'], file='v_clientes')
    df['PASTA'] = pasta_df['numero_pasta']
    
    # 16. DATA CADASTRO
    df['DATA CADASTRO'] = df['data_entrada']
    df['DATA CADASTRO'] = date_formatting(df, col='DATA CADASTRO')
    df['DATA CADASTRO'] = df['DATA CADASTRO'].apply(lambda row: row if row else date.today().strftime("%d/%m/%Y"))
    

    # 17. DATA FECHAMENTO
    df['DATA FECHAMENTO'] = df['data_contratacao']
    df['DATA FECHAMENTO'] = date_formatting(df, col='DATA FECHAMENTO')
    df['DATA FECHAMENTO'] = df['DATA FECHAMENTO'].apply(lambda row: row if row else date.today().strftime("%d/%m/%Y"))

    # 18. DATA TRANSITO
    df['DATA TRANSITO'] = df['data_transitojulgado']
    df['DATA TRANSITO'] = date_formatting(df, col='DATA TRANSITO')

    # 19. DATA ARQUIVAMENTO
    df['DATA ARQUIVAMENTO'] = df['data_encerramento']
    df['DATA ARQUIVAMENTO'] = date_formatting(df, col='DATA ARQUIVAMENTO')

    # 20. DATA REQUERIMENTO
    df['DATA REQUERIMENTO'] = df['data_distribuicao']
    df['DATA REQUERIMENTO'] = date_formatting(df, col='DATA REQUERIMENTO')

    # 21. RESPONSÁVEL
    df['RESPONSÁVEL'] = column_mapped_by_dict(df, csv_paths, cols=['id', 'nome'], code='id', descrip='nome', file='v_usuario', df_col='cod_usuario')

    # 22. ANOTAÇÕES GERAIS
    df['grupo_processo'] 	= column_mapped_by_dict(df, csv_paths, file='v_grupo_processo', df_col='grupo_processo')
    
    df['destino'] 			= column_mapped_by_dict(df, csv_paths, file='v_localizador', df_col='destino')
    
    df['codassunto'] 		= column_mapped_by_dict(df, csv_paths, file='v_assunto', df_col='codassunto')
    
    df['codprognostico'] 	= column_mapped_by_dict(df, csv_paths, file='v_prognosticos', df_col='codprognostico')
    
    df['statusprocessual'] 	= column_mapped_by_dict(df, csv_paths, file='v_statusprocessual', df_col='statusprocessual')
    
    
    df['ANOTAÇÕES GERAIS'] = insert_general_annotation(
        df,
        original_cols=['grupo_processo', 'destino', 'codassunto', 'codprognostico', 'statusprocessual', 'observacoes', 'data_atendimento', 'data_sentenca', 'data_execucao', 'data_ultima_visualizacao'],
        descriptions=['Grupo Processo', 'Destino', 'Assunto', 'Prognóstico', 'Status Processual', 'Observações', 'Atendimento', 'Sentença', 'Execução', 'Última Visualização'],
	)


    
    return df

def pick_first_nonempty_row(df, col1, col2, col3=None):
    df = df.copy()

    if col3 is None:
        return df.apply(lambda row: row[col1] if row[col1] else (row[col2] if row[col2] else ''), axis=1)
	
    return df.apply(lambda row: row[col1] if row[col1] else (row[col2] if row[col2] else row[col3]), axis=1)

def format_pis(string):
    formatted = ''
    
    if string:
        formatted = f'{string[0:3]}.{string[3:7]}.{string[7:10]}-{string[10:]}'
    
    return formatted

def date_formatting(df, col=None):
	new_col = df.apply(lambda row: re.sub(' \d{1,2}:\d{1,2}', '', row[col]), axis=1)
     
	return new_col

def fix_encoding(csv_paths, df, col, file='v_clientes'):
    csv = csv_paths[file]
    correct_col = pd.read_csv(csv, sep=';', encoding='utf-8', usecols=[col], dtype=str)
    df[col] = correct_col

    return df[col]

def insert_general_annotation(df, original_cols=None, descriptions=None, base_col='ANOTAÇÕES GERAIS'):
    if original_cols is None or descriptions is None:
        return df[base_col]
    
    col_mapping = {original : description for original, description in zip(original_cols, descriptions)}

    def row_processing(row):
        values = [f'{col_mapping[col]}: {row[col]}' for col in col_mapping if row[col]]
        joined_str = '\n'.join(values)

        return joined_str
    
    df[base_col] = df.apply(row_processing, axis=1)
    
    return df[base_col]

def create_subset_df(csv_paths, cols=None, file=None):
	csv = csv_paths[file]
	subset_df = pd.read_csv(csv, usecols=cols, sep=';', encoding='utf-8', dtype=str)
    
	return subset_df

def create_code_description_dict(df, code=None, descrip=None):
    mapping_dict = {code_num : description for code_num, description in zip(df[code], df[descrip])}
    
    mapping_dict[''] = ''
    mapping_dict['0'] = ''
    
    return mapping_dict

def column_mapped_by_dict(df, csv_paths, cols=['codigo', 'descricao'], file=None, code='codigo', descrip='descricao', df_col=None):
    subset_df = create_subset_df(csv_paths, cols=cols, file=file)
    map_dict = create_code_description_dict(subset_df, code=code, descrip=descrip)

    df[df_col] = df[df_col].map(map_dict)
    
    return df[df_col]

def process_number_validation(df, keep='NÚMERO DO PROCESSO', move_to='PROTOCOLO'):
    pattern = '\d+-\d+\.\d+\.\d+\.\d+\.\d+'
    
    matches = df[keep].str.contains(pattern, regex=True)
    df.loc[~matches, move_to] = df.loc[~matches, keep]
    df.loc[~matches, keep] = ''
    
    return df[keep], df[move_to]