import pandas as pd
import pandasql
import sqlite3
from datetime import datetime

date_today = datetime.today()

df = pd.read_excel('media/CLIENTES_SEGUROS.xlsx')

pd.to_datetime(df['DATA']).apply(lambda x: x.date())
#date_object = datetime.strptime(str(a), '%Y-%m-%d')

print(df['DATA'])

def read_all(): #DB Tables Read

	return df

def read_sql(task): #DB Tables Read
	conn = sqlite3.connect('db.sqlite3')
   
	sql_datas = f"""
				SELECT * FROM {task};
	"""
	read_db = pd.read_sql_query(sql_datas, conn)
	conn.close()
	return read_db


def read_sql_all(): #DB Tables Read
	conn = sqlite3.connect('db.sqlite3')
   
	sql_datas = f"""
				SELECT * FROM task_cliente;
	"""
	read_db = pd.read_sql_query(sql_datas, conn)
	conn.close()
	return read_db


def creat_sub_item():
    read = []
    ag = df.groupby('AG').count().index
    prod = df.groupby('PRODUTO').count().index
    seg_type = df.groupby('TIPO_SEGURO').count().index
    renew = df.groupby('REN').count().index

    read.append([ag,prod,seg_type,renew])

    return read


def insert_ag(name_ag, commit, date_today):
    conn = sqlite3.connect('db.sqlite3')
    c = conn.cursor()

    qsl_datas = f"""
                INSERT INTO task_agency(name_agency, comments, update_at, create_at)
                VALUES ('{name_ag}', '{commit}','{date_today}','{date_today}');
                """
    c.execute(qsl_datas)
    conn.commit()
    conn.close()


def insert_prod(name_prod, commit, date_today):
    conn = sqlite3.connect('db.sqlite3')
    c = conn.cursor()

    qsl_datas = f"""
                INSERT INTO task_product(name_product, comments, update_at, create_at)
                VALUES ('{name_prod}', '{commit}','{date_today}','{date_today}');
                """
    c.execute(qsl_datas)
    conn.commit()
    conn.close()


def insert_seg_type(name_seg, commit, date_today):
    conn = sqlite3.connect('db.sqlite3')
    c = conn.cursor()

    qsl_datas = f"""
                INSERT INTO task_secure(name_secure, comments, update_at, create_at)
                VALUES ('{name_seg}', '{commit}','{date_today}','{date_today}');
                """
    c.execute(qsl_datas)
    conn.commit()
    conn.close()


def insert_renew(name_ren, commit, date_today):
    conn = sqlite3.connect('db.sqlite3')
    c = conn.cursor()

    qsl_datas = f"""
                INSERT INTO task_renew(name_renew, comments, update_at, create_at)
                VALUES ('{name_ren}', '{commit}','{date_today}','{date_today}');
                """
    c.execute(qsl_datas)
    conn.commit()
    conn.close()


def insert_clientes(name_,renew_,cpf_,cnpj_,prod_,agency_,secure_,gerency_,conta_,policy_,
                amount_paid_,tel1_,tel2_,cel1_,cel2_,email_,comments_,date_contract_,date_today):
    conn = sqlite3.connect('db.sqlite3')
    c = conn.cursor()

    qsl_datas = f"""
                INSERT INTO task_cliente(name,renew_id,cpf,cnpj,prod_id,agency_id,secure_id,gerency,conta,policy,
                amount_paid,tel1,tel2,cel1,cel2,email,comments,date_contract,update_at,create_at)
                VALUES ('{name_}',{renew_},'{cpf_}','{cnpj_}',{prod_},{agency_},{secure_},
                '{gerency_}','{conta_}','{policy_}',{amount_paid_},'{tel1_}','{tel2_}','{cel1_}',
                '{cel2_}','{email_}','{comments_}','{date_contract_}','{date_today}','{date_today}');
                """
    c.execute(qsl_datas)
    conn.commit()
    conn.close()