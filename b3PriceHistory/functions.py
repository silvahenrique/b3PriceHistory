from zipfile import ZipFile


def unzip_history_file(zip_file, directory):
    with ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(directory)


def read_file(file_path):
    price_history_file = open(file_path, "r")
    return price_history_file.readlines()


def data_strip(string):
    return string.strip() if not None else string


def parse_header(file_line):
    return {
        'tipreg': data_strip(file_line[0:2]),
        'nomarq': data_strip(file_line[2:15]),
        'codori': data_strip(file_line[15:23]),
        'datger': data_strip(file_line[23:31]),
        'reserv': data_strip(file_line[31:245])
    }


def parse_trailer(file_line):
    return {
        'tipreg': data_strip(file_line[0:2]),
        'nomarq': data_strip(file_line[2:15]),
        'codori': data_strip(file_line[15:23]),
        'datger': data_strip(file_line[23:31]),
        'regtot': data_strip(file_line[31:42]),
        'reserv': data_strip(file_line[42:245])
    }


def parse_history(file_line):
    return {
        'tipreg': data_strip(file_line[0:2]),
        'pregao': data_strip(file_line[2:10]),
        'codbdi': data_strip(file_line[10:12]),
        'codneg': data_strip(file_line[12:24]),
        'tpmerc': data_strip(file_line[24:27]),
        'nomres': data_strip(file_line[27:39]),
        'especi': data_strip(file_line[39:49]),
        'prazot': data_strip(file_line[49:52]),
        'modref': data_strip(file_line[52:56]),
        'preabe': data_strip(file_line[56:69]),
        'premax': data_strip(file_line[69:82]),
        'premin': data_strip(file_line[82:95]),
        'premed': data_strip(file_line[95:108]),
        'preult': data_strip(file_line[108:121]),
        'preofc': data_strip(file_line[121:134]),
        'preofv': data_strip(file_line[134:147]),
        'totneg': data_strip(file_line[147:152]),
        'quatot': data_strip(file_line[152:170]),
        'voltot': data_strip(file_line[170:188]),
        'preexe': data_strip(file_line[188:201]),
        'indopc': data_strip(file_line[201:202]),
        'datven': data_strip(file_line[202:210]),
        'fatcon': data_strip(file_line[210:217]),
        'ptoexe': data_strip(file_line[217:230]),
        'codisi': data_strip(file_line[230:242]),
        'dismes': data_strip(file_line[242:245])
    }


def parse_price_history_file(price_history_file_path):
    history = {
        'header': None,
        'price_history': [],
        'trailer': None
    }

    lines = read_file(price_history_file_path)
    for line in lines:
        if line.startswith('00'):
            header = parse_header(line)
            history['header'] = [ header ]
        if line.startswith('99'):
            trailer = parse_trailer(line)
            history['trailer'] = [ trailer ]
        if line.startswith('01'):
            price_history = parse_history(line)
            lst = history['price_history']
            lst.append(price_history)
            history['price_history'] = lst
    return history
