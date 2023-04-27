import oracledb as orcl
import pandas as pd

try:
    dnStr = orcl.makedsn("oracle.fiap.com.br", "1521", "orcl")
    conn = orcl.connect(user="RM96881", password="250998")

    inst_cadastro = conn.cursor()
    inst_consulta = conn.cursor()
    inst_alteracao = conn.cursor()
    insr_exclusao = conn.cursor()