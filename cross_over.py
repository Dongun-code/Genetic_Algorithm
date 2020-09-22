import numpy as np
import random

class Cross_over:
    def __init__(self):
        self.next_gen = []

    def cross_over_function(self, next_generation_list):
        gen_len = len(next_generation_list)
        # print('lenght',gen_len)
        # print('cross_over', next_generation_list)
        new_child = []
        # i = 0
        # while (gen_len - 2) >= i:
        #     mode = 1
        #     if mode == 1:
        #         pt = 6
        #         parent1 = list(next_generation_list[i])
        #         parent2 = list(next_generation_list[i+1])
        #         print('parent1', parent1)
        #         print('parent2', parent2)
        #         offspring1 = parent1[:pt] + parent2[pt:]
        #         offspring2 = parent2[:pt] + parent1[pt:]
        #         new_child.append([offspring1, offspring2])
        #     print(new_child)
        #     print(i)
        #     i = i + 1
        # print('new_child',new_child)
        # print('new_child',np.array(new_child).shape)
        for i in range(gen_len-1):
            for j in range(i+1, gen_len):
                pt = random.randrange(4,16)
                parent1 = list(next_generation_list[i])
                parent2 = list(next_generation_list[j])
                # print('parent1', parent1)
                # print('parent2', parent2)
                offspring1 = parent1[:pt] + parent2[pt:]
                offspring2 = parent2[:pt] + parent1[pt:]
                new_child.append([offspring1, offspring2])

        return new_child
        # print('new_child', new_child)
        # print('new_child',np.array(new_child).shape)

