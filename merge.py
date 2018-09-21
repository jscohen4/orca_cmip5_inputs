import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('swe-sorted.csv', index_col = 0, parse_dates = True)
df = df.reindex(index = pd.date_range("1950-01-01", "2099-12-31"))
df = df.asfreq('D')
df = df.fillna(method = 'backfill')
with open('scenario_names_all.txt') as f:
	scenarios = f.read().splitlines()
for sc in scenarios:
	df2 = pd.read_csv('input_climate_files/%s_input_data.csv'%sc,index_col = 0, parse_dates = True)
	# for res in ['SHA_swe','ORO_swe','YUB_swe','FOL_swe']:
	df2['YRS_swe'] = df['YUB_swe_%s'%sc]
	# df2.to_csv('input_climate_files_2/%s_input_data.csv'%sc)
	df2.to_csv('input_climate_files/%s_input_data.csv'%sc)

#change names...
# df = pd.read_csv('swe-sorted.csv', index_col = 0, parse_dates = True)
# df = df.asfreq('D')
# df = df.fillna(method = 'backfill')
# df = df.index = pd.DatetimeIndex(df.index)
# # df = df.reindex(index = pd.date_range("1950-01-01", "2099-12-31"))
# with open('scenario_names_all.txt') as f:
# 	scenarios = f.read().splitlines()
# for sc in scenarios:
# 	df = pd.read_csv('input_climate_files/%s_input_data.csv'%sc,index_col = 0, parse_dates = True)
# 	df['YRS_swe'] = df['YUB_swe']
# 	df['BND_swe'] = df['SHA_swe']
# 	df = df.drop(df[['YUB_swe','SHA_swe']],axis=1)
# 	df.to_csv('input_climate_files_2/%s_input_data.csv'%sc)