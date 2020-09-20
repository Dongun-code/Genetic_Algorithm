from xgboost import XGBRFRegressor, plot_importance, plot_tree, XGBRegressor
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, mean_squared_error
import pandas as pd
import random
import matplotlib.pyplot as plt
import numpy as np
from population import population
from find_index import find_index
from cross_over import Cross_over
from mutation import mutation
import copy

pd.set_option('display.max_row',100)
pd.set_option('display.max_columns', 100)

class evaluate:
    def __init__(self):
        self.population = population()


    def evalue_function(self, data, pop_list):
        regressor_result_list = []

        Xgrf = XGBRegressor(objective ='reg:squarederror')
        y = pd.DataFrame(data, columns=['steering_top_acc_x'])
        y = np.squeeze(y,axis=1)

        # print('pop_list',pop_list)
        for i, feature_list in enumerate(pop_list):
            # print('pop',feature_list)
            X = pd.DataFrame(data, columns=feature_list)
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)
            Xgrf.fit(X_train, y_train, verbose=1)
            regressor_result = Xgrf.score(X_test, y_test)
            regressor_result_list.append(regressor_result)

        regressor_result_original = copy.deepcopy(regressor_result_list)
        regressor_result_list.sort()
        # print('regressor_result_original', np.array(regressor_result_original).shape)
        # print(regressor_result_list)
        # print(regressor_result_list[-5:])

        parent_index = []
        for i in regressor_result_list[-5:]:
            # print(i)
            x = regressor_result_original.index(i)
            parent_index.append(x)

        return parent_index

        # next_generation = population.parent_index_catcher(parent_index)
        #
        # print('next_generation',list(next_generation))
        # cross_over_ = Cross_over()
        # child_list = cross_over_.cross_over_function(next_generation)
        # child_list = np.reshape(child_list,(-1,30))
        # child_original = copy.deepcopy(child_list)
        # child_original = list(child_original)
        # mutation_function = mutation()
        # mutant_child = mutation_function.mutation_operation(child_list)
        # mutant_child = list(mutant_child)







