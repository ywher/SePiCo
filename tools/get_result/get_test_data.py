import pandas as pd

class_data_dict = {}
begin = end = 0
class_name_order = ['Mean',
                    'road', 'sidewalk', 'building', 'wall', 'fence',
                    'pole', 'traffic light', 'traffic sign', 'vegetation',
                    'terrain', 'sky', 'person', 'rider', 'car', 'truck',
                    'bus', 'train', 'motorcycle', 'bicycle']


with open('test_result.txt', 'r') as f:
    contents = f.readlines()

for i in range(len(contents)):
    content = contents[i]
    # if '.' not in content:
    #     continue
    if 'Summary' in content:
        break
    t_pos = content.find('\t')
    # dot_first_pos = content.find('.')
    begin = t_pos + 1
    end = begin + 2 
    while(end < len(content) and content[end] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']):
        end += 1
    if end >= len(content):
        number = content[begin:]
    else:
        number = content[begin:end]
    
    class_name_end = content.find('\t')
    class_name = content[:class_name_end]
    class_data_dict[class_name] = number
    # data_list.append(number)

data_list = []
for class_name in class_name_order:
    data_list.append(class_data_dict[class_name])

file_name = 'data_test.csv'
data_dict = {}

for i in range(len(data_list)):
    if eval(data_list[i]) < 1:
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
    print('& %.1f'%num, ' ',end='')