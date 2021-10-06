import datetime
import pymysql
import pandas as pd

con = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='Aa213456',
    db='WOW',
    charset='utf8'
)
cur = con.cursor(cursor=pymysql.cursors.DictCursor)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', None)

'''
    @Description:
        Insert a record into the targeted database
    @Params:
        db_name: the name of database
        record: has all the information to insert into DB
    @Return:
        None
'''


def insert_record(db_name: str, record: dict):
    record['TableLastDate'] = str(get_cur_time())
    columns = '('
    values = '('
    for k, v in record.items():
        columns += str(k) + ','
        if isinstance(v, str):
            values += "'" + str(v) + "',"
        else:
            values += str(v) + ','
    columns = columns[:-1]
    values = values[:-1]
    columns += ')'
    values += ')'
    sql = "insert into " + db_name + columns + "values" + values
    cur.execute(sql)
    con.commit()
    print(sql + 'executed')


'''
    @Description:
        Update a record in the targeted database whose id is specified
    @Params:
        db_name: the name of database
        id: the id of the modified record
        changes: all the information which is needed to be updated
    @Return:
        None
'''


def update_record(db_name: str, id: int, changes: dict):
    changes['TableLastDate'] = str(get_cur_time())
    entities = ''
    for k, v in changes.items():
        if isinstance(v, str):
            entities += k + " = '" + v + "', "
        else:
            entities += k + " = " + str(v) + ", "
    entities = entities[:-2]
    sql = "UPDATE " + db_name + " SET " + entities + " WHERE id=" + str(id)
    cur.execute(sql)
    con.commit()
    print(sql + 'executed')


def show_columns(db_name: str):
    get_sql = 'show columns from ' + db_name
    cur.execute(get_sql)
    get_df = pd.DataFrame(cur.fetchall())
    print(get_df)
    return get_df


def show_data(db_name: str):
    get_sql = 'select * from ' + db_name
    cur.execute(get_sql)
    get_df = pd.DataFrame(cur.fetchall())
    print(get_df)
    return get_df

# 'age > 17'
def search_data(db_name: str, condition: str):
    get_sql = 'select * from ' + db_name + ' where ' + condition
    cur.execute(get_sql)
    get_df = pd.DataFrame(cur.fetchall())
    return get_df


def get_cur_time():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


if __name__ == '__main__':
    try:
        # READ TABLE
        get_sql = 'select * from patient'
        cur.execute(get_sql)
        get_df = pd.DataFrame(cur.fetchall())
        print(get_df)

        # WRITE TABLE
        date_time = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))
        record = {'Name': 'test', 'Address': '235 grand ST.', 'PhoneNumber': '3322349999',
                  'RelationshipWithEmergencyContact': 'Parent',
                  'EmergencyContact': 'Zhang', 'IsInPatient': True, 'FollowUpDate': date_time, 'BedNumber': 3,
                  'Floor': 2,
                  'DischargeDate': date_time, 'TableLastDate': date_time}
        insert_record('patient', record)

        # UPDATE RECORD
        changes = {'Name': 'King', 'PhoneNumber': '123456789'}
        update_record('patient', 4, changes)

        print('Done')
    except Exception as e:
        raise e
    finally:
        con.close()
