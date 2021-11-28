import pandas as pd
import pandasql
import sqlite3
from datetime import datetime

date_today = datetime.today()

df = pd.read_excel('media/CLIENTES_SEGUROS.xlsx')

pd.to_datetime(df['DATA']).apply(lambda x: x.date())
#date_object = datetime.strptime(str(a), '%Y-%m-%d')

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


def insert_clientes(name_,renew_,cpf_,cnpj_,prod_,agency_,secure_,gerency_,conta_,policy_,amount_paid_,tel1_,tel2_,cel1_,cel2_,email_,comments_,date_contract_,date_today):
    print(name_,renew_,cpf_,cnpj_,prod_,agency_,secure_,gerency_,conta_,policy_,amount_paid_,tel1_,tel2_,cel1_,cel2_,email_,comments_,date_contract_,date_today)

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


def create_table():
    df = pd.read_excel('media/RENOVACAO.xlsx')

    df = df[['RENOVA', 'PRODUTO', 'NOME_CLIENTE', 'TIPO_SEGURO', 'CPF', 'AG', 'APOLICE', 'VALOR','DATA', '_11', 'TEL1', 'CEL1', 'TEL2', 'CEL2', 'OBS']]
    new_column = ['REN', 'PRODUTO', 'NOME_CLIENTE', 'TIPO_SEGURO', 'CPF', 'AG', 'APOLICE', 'VALOR', 'DATA', 'CORRETOR',  'TEL1', 'CEL1', 'TEL2', 'CEL2', 'OBS']

    for a in range(0, len(df.columns)):
        print(df.columns[a])
        df.rename(columns={df.columns[a]:new_column[a]}, inplace=True)
        
    df.fillna('',inplace=True)

    for a in range(0, len(df['CEL1'])):
        df['TEL1'].loc[a] = str(df['TEL1'].loc[a])[:-2]
        df['CEL1'].loc[a] = str(df['CEL1'].loc[a])[:-2]
        df['TEL2'].loc[a] = str(df['TEL2'].loc[a])[:-2]
        df['CEL2'].loc[a] = str(df['CEL2'].loc[a])[:-2]
        
    df.to_excel('media/CLIENTES_SEGUROS.xlsx')



def compare_tables():

    conn = sqlite3.connect('db.sqlite3')
    sql_datas = f"""
				SELECT * FROM task_cliente;
	"""
    read_db = pd.read_sql_query(sql_datas, conn)
    conn.close()

    df = read_db
    df2 = pd.read_excel('media/CLIENTES_SEGUROS.xlsx')

    #df.drop(columns=['Unnamed: 0'], inplace=True)
    df2.drop(columns=['Unnamed: 0'], inplace=True)

    df['ID'] = ''
    df2['ID'] = ''

    for a in df.index:
        df['ID'].loc[a] = '{}{}'.format(df['CPF'].loc[a], df['APOLICE'].loc[a])

    for b in df2.index:
        df2['ID'].loc[b] = '{}{}'.format(df2['CPF'].loc[b], df2['APOLICE'].loc[b])

    df.index = pd.Index(np.arange(0,len(df)))
    df.index2 = pd.Index(np.arange(0,len(df_new)))

    df['ST_REN'] = False
    df['ST_PRODUTO'] = False
    df['ST_NOME_CLIENTE'] = False
    df['ST_TIPO_SEGURO'] = False
    df['ST_AG'] = False
    df['ST_VALOR'] = False
    df['ST_DATA'] = False
    df['ST_CORRETOR'] = False
    df['ST_OBS'] = False
    df['ST_TEL1'] = False
    df['ST_CEL1'] = False
    df['ST_TEL2'] = False
    df['ST_CEL2'] = False

    df2['ST_REN'] = False
    df2['ST_PRODUTO'] = False
    df2['ST_NOME_CLIENTE'] = False
    df2['ST_TIPO_SEGURO'] = False
    df2['ST_AG'] = False
    df2['ST_VALOR'] = False
    df2['ST_DATA'] = False
    df2['ST_CORRETOR'] = False
    df2['ST_OBS'] = False
    df2['ST_TEL1'] = False
    df2['ST_CEL1'] = False
    df2['ST_TEL2'] = False
    df2['ST_CEL2'] = False

    for a in df.index:
        for b in df2.index:
            if df['ID'].loc[a] == df2['ID'].loc[b]:
                if df['REN'].loc[a] != df2['REN'].loc[b]:
                    df2['ST_REN'].loc[a] = True

                if df['PRODUTO'].loc[a] != df2['PRODUTO'].loc[b]:
                    df2['ST_PRODUTO'].loc[a] = True

                if df['PRODUTO'].loc[a] != df2['PRODUTO'].loc[b]:
                    df2['ST_PRODUTO'].loc[a] = True
                    
                if df['NOME_CLIENTE'].loc[a] != df2['NOME_CLIENTE'].loc[b]:
                    df2['ST_NOME_CLIENTE'].loc[a] = True
                    
                if df['TIPO_SEGURO'].loc[a] != df2['TIPO_SEGURO'].loc[b]:
                    df2['ST_TIPO_SEGURO'].loc[a] = True
                    
                if df['AG'].loc[a] != df2['AG'].loc[b]:
                    df2['ST_AG'].loc[a] = True
                    
                if df['VALOR'].loc[a] != df2['VALOR'].loc[b]:
                    df2['ST_VALOR'].loc[a] = True
                    
                if df['DATA'].loc[a] != df2['DATA'].loc[b]:
                    df2['ST_DATA'].loc[a] = True
                    
                if df['CORRETOR'].loc[a] != df2['CORRETOR'].loc[b]:
                    df2['ST_CORRETOR'].loc[a] = True
                    
                if df['OBS'].loc[a] != df2['OBS'].loc[b]:
                    df2['ST_OBS'].loc[a] = True
                    
                if df['TEL1'].loc[a] != df2['TEL1'].loc[b]:
                    df2['ST_TEL1'].loc[a] = True
                    
                if df['TEL2'].loc[a] != df2['TEL2'].loc[b]:
                    df2['ST_TEL2'].loc[a] = True
                    
                if df['CEL1'].loc[a] != df2['CEL1'].loc[b]:
                    df2['ST_CEL1'].loc[a] = True
                    
                if df['CEL2'].loc[a] != df2['CEL2'].loc[b]:
                    df2['ST_CEL2'].loc[a] = True
                    
    df2['SEG_IGUAL'] = ''
    for a in df.index:
        for b in df2.index:
            if df['ID'].loc[a] == df2['ID'].loc[b]:
                df2['SEG_IGUAL'].loc[b] = 'x'

    index_df = df2[df2['SEG_IGUAL'] == 'x'].index
    df2.drop(index_df, inplace=True)
    df2.reset_index()
    df2['NEW'] = True

    df_new = pd.concat([df, df2])
    df_new .drop('SEG_IGUAL', axis=1, inplace=True)
    
    df_new.to_excel('media/CLIENTES_SEGUROS_Analyzed.xlsx')
