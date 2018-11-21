#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
Given a of single-field features and single-field outcomes,
break them down column by column to get a dataset of columns.

E.g. (field_1_type, field_1_mean, ..., field_N_type, field_N_mean) =>
(mean, type)

Just a hack to avoid recomputing features
'''
import os
from pprint import pprint
from collections import OrderedDict
import numpy as np
import pandas as pd

single_field_features_df = pd.DataFrame()

features_dir = 'features'
outcomes_dir = 'features'
features_file = 'features_all.pkl'
outcomes_file = 'outcomes.pkl'

features_df = pd.read_pickle(os.path.join(features_dir, features_file)).iloc[:10000, :]
outcomes_df = pd.read_pickle(os.path.join(outcomes_dir, outcomes_file)).iloc[:10000, :]

joined_df = pd.merge(features_df, outcomes_df, on='fid')

single_field_feature_names = [ n[:-2] for n in features_df.columns[:features_df.columns.get_loc('length_2')] ]
all_single_field_features = []

print(single_field_feature_names)
for row_num, row in joined_df.iterrows():
	try:
		if (row_num % 1000 == 0):
			print(row_num)
		for i in range(1, 21):
			field_features = OrderedDict([ (n, None) for n in ( single_field_feature_names + [ 'has_single_src', 'has_single_x_src', 'has_single_y_src', 'is_single_x_src', 'is_single_y_src' ])])

			field_features['has_single_src'] = row.get('has_single_src')
			field_features['has_single_x_src'] = row.get('has_single_x_src')
			field_features['has_single_y_src'] = row.get('has_single_y_src')				

			if np.isnan(row.get('length_{}'.format(i))): break

			for single_field_feature_name in single_field_feature_names:
				v = row.get('{}_{}'.format(single_field_feature_name, i))
				field_features[single_field_feature_name] = v

			if i == row.get('single_x_src_order'):
				field_features['is_single_x_src'] = True
			if i == row.get('single_y_src_order'):
				field_features['is_single_y_src'] = True

			all_single_field_features.append(field_features)
	except Exception as e:
		print(e)
		continue

single_field_features_df = pd.DataFrame(all_single_field_features)
print(single_field_features_df)
pd.to_pickle(single_field_features_df, os.path.join(outcomes_dir, 'bag_of_columns_features_and_outcomes.pkl'))