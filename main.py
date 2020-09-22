import numpy as np
import pandas as pd
import copy
from population import population
from find_index import find_index
from cross_over import Cross_over
from evaluate import evaluate
from mutation import mutation
from tqdm import tqdm

pd.set_option('display.max_row',100)
pd.set_option('display.max_columns', 100)

class GA_alg:
    def __init__(self):
        self.epoch = 50
        self.data = pd.read_csv('./A-car/A-car_Seoul_40 1.txt', sep="\t", engine='python')

    def main(self):

        evaluate_function = evaluate()
        cross_over_ = Cross_over()
        population_function = population()

        for i in tqdm(range(self.epoch)):
            if i == 0:
                self.pop_data = population_function.generate_choromosome()
            print('pop data ',self.pop_data)
            pop_data = self.pop_data
            # print(type(pop_data))
            pop_list = population_function.classify_choromosome(pop_data)

            parent_data = evaluate_function.evalue_function(self.data, pop_list)
            # print('parent_shape',np.array(parent_data).shape)
            self.next_generation = population_function.parent_index_catcher(self.pop_data,parent_data)
            # print("next_generation",next_generation)
            child_list = cross_over_.cross_over_function(self.next_generation)
            child_list = np.reshape(child_list, (-1, 30))
            mutation_function = mutation()
            mutant_child = mutation_function.mutation_operation(child_list)
            self.pop_data = mutant_child
            # print('next pop data',self.pop_data)
            # print('next pop data',np.array(self.pop_data).shape)
        return self.next_generation

    def show_result(self, data):
        population_function = population()
        print('show',data)

        feature = population_function.classify_choromosome(data)
        for i in feature:
            print(i)




if __name__ == "__main__":
    ga_alg = GA_alg()
    result = ga_alg.main()
    ga_alg.show_result(result)