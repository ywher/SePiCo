import json
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
root_folder_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# foler_name = '230707_0255_dlv2_proj_r101v1c_sepico_BankCL-reg-w1.0-start-iter3000-tau100.0-l3-w1.0_rcs0.01_cpl_self_adamw_6e-05_pmT_poly10warm_1x2_40k_gta2cs_seed76_1d7eb'
# exp_name = 'local-exp2'
# file_path = os.path.join(root_folder_path, 'work_dirs/{}/{}/{}.json'.format(exp_name, foler_name, foler_name))

# relative_path = 'work_dirs/local-exp1/230707_0324_dlv2_proj_r101v1c_sepico_DistCL-reg-w1.0-start-iter3000-tau100.0-l3-w1.0_rcs0.01_cpl_self_adamw_6e-05_pmT_poly10warm_1x2_40k_gta2cs_seed76_36629/230707_0324_dlv2_proj_r101v1c_sepico_DistCL-reg-w1.0-start-iter3000-tau100.0-l3-w1.0_rcs0.01_cpl_self_adamw_6e-05_pmT_poly10warm_1x2_40k_gta2cs_seed76_36629.json'
# file_path = os.path.join(root_folder_path, relative_path)
file_path = '/home/ywh/projects/uda/SePiCo/work_dirs/local-exp2/230707_0255_dlv2_proj_r101v1c_sepico_BankCL-reg-w1.0-start-iter3000-tau100.0-l3-w1.0_rcs0.01_cpl_self_adamw_6e-05_pmT_poly10warm_1x2_40k_gta2cs_seed76_1d7eb/230707_0255_dlv2_proj_r101v1c_sepico_BankCL-reg-w1.0-start-iter3000-tau100.0-l3-w1.0_rcs0.01_cpl_self_adamw_6e-05_pmT_poly10warm_1x2_40k_gta2cs_seed76_1d7eb.json'
with open(file_path, 'r') as f:
    json_content = json.load(f)
f.close()

with open(file_path, 'w') as f:
    json.dump(json_content, f, indent=4)
f.close()

'230707_0324_dlv2_proj_r101v1c_sepico_DistCL-reg-w1.0-start-iter3000-tau100.0-l3-w1.0_rcs0.01_cpl_self_adamw_6e-05_pmT_poly10warm_1x2_40k_gta2cs_seed76_36629'