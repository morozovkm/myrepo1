import pymysql


def read_data_file(file_name):
    file_lines = []
    file = open(file_name, 'r')
    for line in file:
        file_lines.append(line)
    return file_lines


def split_line(line):
    splited_line = line.split(';')
    return splited_line


def connect_to_db(host, port, db_name, user, password):
    connection = pymysql.connect(host=host, user=user,
                                 port=port, db=db_name, password=password)
    cursor = connection.cursor()
    return cursor,connection


if __name__ == '__main__':
    cursor, connection = connect_to_db('10.10.101.183',3306,'test','student','123456')
    stroki_iz_faila = read_data_file('data.csv')
    for stroka in stroki_iz_faila:
        razbitaya_stroka = split_line(stroka)
        cursor.execute("insert into sprav values('{}','{}','{}','{}','{}');".format(razbitaya_stroka[0],razbitaya_stroka[1],razbitaya_stroka[2],razbitaya_stroka[3],razbitaya_stroka[4].strip()))

    connection.commit()