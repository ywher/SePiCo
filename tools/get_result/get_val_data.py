import pandas as pd


data_list = []
begin = end = 0

with open('val_result.txt', 'r') as f:
    contents = f.readlines()

for i in range(len(contents)):
    content = contents[i]
    if '.' not in content:
        continue
    if 'Summary' in content:
        break
    dot_first_pos = content.find('.')
    begin = dot_first_pos - 1
    end = dot_first_pos + 1
    while (content[begin] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']):
        begin -= 1
    while (end < len(content) and content[end] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']):
        end += 1
    if end >= len(content):
        number = content[begin+1:]
    else:
        number = content[begin+1:end]
    data_list.append(number)

#for synthia, remove the zero items
if eval(data_list[9]) + eval(data_list[14]) + eval(data_list[16]) < 1e-4:
    data_list = data_list[:9] + data_list[10:14] + data_list[15:16] + data_list[17:]

file_name = 'data_val.csv'
data_dict = {}

if (eval(data_list[10]) == 0 and eval(data_list[15]) == 0 and eval(data_list[17]) == 0):
    data_list = data_list[:10] + data_list[11:15] + data_list[16:17] + data_list[18:]

expand_100_flag = eval(data_list[0]) < 10  # 是否扩大100倍
for i in range(len(data_list)):
    if expand_100_flag:
        data_dict[i] = [eval(data_list[i]) * 100]
    else:
        data_dict[i] = [eval(data_list[i])]

data_dict = pd.DataFrame(data_dict)
data_dict.to_csv(file_name, index=False)

puls = False
if eval(data_list[0]) < 10:
    puls = True
for data in data_list:
    num = eval(data)
    if puls:
        num *= 100
    print('& %.1f'%num, ' ', end='')