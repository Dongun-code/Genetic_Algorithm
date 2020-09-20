import random
import numpy as np

class mutation:

    def mutation_operation(self, child_list):
        child_list_result = []
        for i, child in enumerate(child_list):
            child = list(child)
            random_value = random.randrange(20,31)
            if random_value == 30:
                # print(i)
                # print('mutation function opertaion!!')
                element_position1 = random.randrange(0, len(child) - 1)
                element_position2 = random.randrange(0, len(child) - 1)
                insert_position1 = random.randrange(0, len(child) - 2)
                insert_position2 = random.randrange(0, len(child) - 2)
                random_element = random.randrange(1, 2)
                del child[element_position1]
                del child[element_position2]
                child.insert(insert_position1, random_element)
                child.insert(insert_position2, random_element)

            child_list_result.append(child)
        # print('attention!!!!!!!!!!',np.array(child_list_result).shape)
        # self.overlap_check(child_list_result)
        # print('attention!!!!!!!!!!',np.array(child_list_result).shape)
        return child_list_result


            #     for i in range(random_option):
            #         random_location = random.randrange(1, 30)
            #         random_location_list.append(random_location)
            # print(random_location_list)
    def overlap_check(self, data):

        for i, value in enumerate(data):
            for j, com in enumerate(data):

                if i != j and value == com:
                    # print(i)
                    # print(j)
                    del data[j]
                    # print('yes')


