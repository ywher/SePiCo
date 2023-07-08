import json
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
root_folder_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
foler_name = '230608_0916_gta2cs_dacs_a999_fdthings_rcs001_cpl_daformer_sepaspp_mitb5_poly10warm_s0_bf49f'
exp_name = 'local-exp7'
file_path = os.path.join(root_folder_path, 'work_dirs/{}/{}/{}.json'.format(exp_name, foler_name, foler_name))
with open(file_path, 'r') as f:
    json_content = json.load(f)
f.close()

with open(file_path, 'w') as f:
    json.dump(json_content, f, indent=4)