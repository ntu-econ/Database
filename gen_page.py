import pandas as pd
csv_read = pd.read_csv('link_of_ECONDB_4.csv')
csv_read = csv_read.fillna('')
for index in csv_read.index:
    path = csv_read['Full Path'][index].split('/')
    filename = ""
    filepath = ""
    if len(path) >= 3:
        for i in range(2, len(path)):
            if i == len(path) - 1:
                filename += path[i]
            else:
                filename += path[i] + "_"
        for i in range(1, len(path)):
            filepath += f'- {path[i]}\n'
    else:
        filename = path[1]
        filepath = f'- {path[1]}\n'

    print(f'Generating page:{filename} at {filepath}...')
    f = open(f'source/_posts/{filename}.md', 'w')
    if csv_read['Description'][index] != '':
        f.write(
            f'---\ntitle: {filename}\ndate: 2023-10-17\ntags: \ncategories:\n{filepath}\n---\n{csv_read["Description"][index]}\n{csv_read["URL"][index]}\n')
    else:
        f.write(
            f'---\ntitle: {filename}\ndate: 2023-10-17\ntags: \ncategories:\n{filepath}\n---\n{csv_read["URL"][index]}\n')
    f.close()
