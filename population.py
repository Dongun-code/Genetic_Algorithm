import numpy as np
# np.random.seed(9)

class population:
    def __init__(self):
        self.input_feature = ['knuckle_fl_acc_x','knuckle_fl_acc_y','knuckle_fl_acc_z'
            ,'knuckle_fr_acc_x','knuckle_fr_acc_y','knuckle_fr_acc_z','knuckle_rl_acc_x', 'knuckle_rl_acc_y'
                        ,'knuckle_rl_acc_z','knuckle_rr_acc_x','knuckle_rr_acc_y','knuckle_rr_acc_z'
                                        , 'pt_eng_src_acc_x', 'pt_eng_src_acc_y','pt_eng_src_acc_z',
                                        'topmount_fl_acc_x','topmount_fl_acc_y','topmount_fl_acc_z','topmount_rr_acc_x','topmount_rr_acc_y','topmount_rr_acc_z',
                                        'frt_subframe_src_acc_x','frt_subframe_src_acc_y','frt_subframe_src_acc_z','rear_xmbr_src_acc_x','rear_xmbr_src_acc_y','rear_xmbr_src_acc_z',
                                        'rear_xmbr_body_acc_x','rear_xmbr_body_acc_y','rear_xmbr_body_acc_z']




    def make_chromosome(self, M, N, P):
        self.parent_list = np.random.choice([0, 1], size=(M, N), p=[P, 1 - P])
        return self.parent_list

    def select_feature(self, list):
            True_feature = []
            # print('select feature',list)
            for i in list:
                True_feature.append(self.input_feature[i])

            return True_feature

    def generate_choromosome(self):
        chromosome = self.make_chromosome(10,30,0.5)
        # print(type(chromosome))
        return chromosome

    def classify_choromosome(self, chromosome):
        filtered_list = []
        True_feature_list = []
        for unit in chromosome:
            True_list = [i for i, value in enumerate(unit) if value == 1]
            filtered_list.append(True_list)

        for i in filtered_list:
            feature_name = self.select_feature(i)
            True_feature_list.append(feature_name)

        return True_feature_list

    def parent_index_catcher(self,parent_data, parent_index):
        parent_data = np.array(parent_data)
        print('parent data ', parent_data.shape, 'parent index', parent_index)
        next_generation = parent_data[parent_index]
        # print(next_generation)
        return next_generation

