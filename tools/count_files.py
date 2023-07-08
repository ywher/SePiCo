import os

if __name__ == '__main__':
    folder_path = '/home/cyber-fx/ywh/projects/SePiCo/work_dirs/local-exp3/230707_1739_dlv2_proj_r101v1c_sepico_ProtoCL-reg-w1.0-start-iter3000-tau100.0-l3-w1.0_rcs0.01_cpl_self_adamw_6e-05_pmT_poly10warm_1x2_40k_gta2cs_seed76_bedc9/pred_train'
    # folder_path = '/home/cyber-fx/ywh/projects/DAFormer_new/work_dirs/local-exp7/230526_1633_syn2cs_dacs_a999_fdthings_rcs001_cpl_daformer_sepaspp_mitb5_poly10warm_s0_103e3/pred_train_new'
    # folder_path = '/home/cyber-fx/ywh/projects/DAFormer_new/data/cityscapes/leftImg8bit/train'
    file_list = os.listdir(folder_path)
    file_list.sort()
    if 'exp1' in folder_path or 'exp3' in folder_path:
        for file in file_list:
            print(file, '\t', len(os.listdir(os.path.join(folder_path, file)))//4)
    # elif 'exp8' in folder_path:
    #     total = 0
    #     for file in file_list:
    #         print(file, '\t', len(os.listdir(os.path.join(folder_path, file)))//4)
    #         total += len(os.listdir(os.path.join(folder_path, file)))//4
    #     print('total: ', total)
        # print(len(file_list)//4)
    elif 'cityscapes' in folder_path:
        for file in file_list:
            print(file, '\t', len(os.listdir(os.path.join(folder_path, file))))
        # if file.endswith('.png'):
            # print(file)