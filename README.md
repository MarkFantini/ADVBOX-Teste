# Introdução

Este repositório é sobre o projeto de teste prático para vaga de Analista Python Júnior da empresa ADVBOX.

O teste consiste em:
- Elaborar um processamento que trará os dados dos arquivos CSV para tabelas;
- Realizar a seleção e tratamento dos dados das tabelas para duas planilhas resultado (CLIENTES e PROCESSOS), garantindo as condições de validação;
- Criar uma interface simples de usuário para que o operador possa subir a base de backup e obter as planilhas correspondentes.

# Em progresso

1. [x] ~~Validação das colunas da planilha CLIENTES e ajustes finais.~~
2. [x] ~~Geração da planilha PROCESSOS.~~
3. Validação das colunas da planilha PROCESSOS e ajustes finais.
4. Criação de um log para monitoramento do processo de criação, garantindo observabilidade para o processo.
5. Criação de testes para as etapas, garantindo uma pipeline segura.
6. Criação da interface usando Streamlit.

# Changelog

- **2024-12-12**
    - Validação da coluna NÚMERO DO PROCESSO e transferência de valores que não se encaixam na coluna PROTOCOLO
    - Arquivo final renomeado para CLIENTES - 92577 e PROCESSOS - 92577, correspondente ao número da empresa
    - Ajuste do preenchimento da coluna ANOTAÇÕES GERAIS da planilha CLIENTES
    - Início do tratamento da planilha PROCESSOS. Colunas preenchidas:
        - NOME DO CLIENTE
        - TIPO DE AÇÃO
        - GRUPO DE AÇÃO
        - FASE PROCESSUAL
        - NÚMERO DO PROCESSO (Falta validação)
        - VARA
        - COMARCA
        - EXPECTATIVA/VALOR
        - VALOR HONORÁRIOS
        - PASTA
        - DATA CADASTRO
        - DATA FECHAMENTO
        - DATA TRANSITO
        - DATA ARQUIVAMENTO
        - DATA REQUERIMENTO
        - RESPONSÁVEL
        - ANOTAÇÕES GERAIS (parcialmente)
- **2024-12-11**
    - Finalização da coluna CLIENTES, incluindo tratamento dos dados das colunas:
        - NOME
        - CPF CNPJ
        - PROFISSÃO
        - CEP
        - PIS PASEP
        - NACIONALIDADE
        - PAIS
        - SEXO
        - DATA DE NASCIMENTO
        - ANOTAÇÕES GERAIS
- **2024-12-03**
    - Atualização do README, início da validação das colunas de CLIENTES.
    - Criação do arquivo `data_wrangling` para limpeza e transformação das colunas dos dataframes.
- **2024-12-02**
    - Base do projeto pronta.
    - Capaz de gerar uma planilha de CLIENTES porém sem validação.




