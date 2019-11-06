import numpy as np  
import pandas as pd 
import matplotlib.pyplot as plt  
import seaborn as sns 

# ## Read data into dataframe
data_name = 'pems-bay'
data_path = 'data/' + data_name + '.h5'
df = pd.read_hdf(data_path)
print(df.shape)
print(df)

# ## Get the critical info 
sensor_id_index = 0
sensor_id = list(df.keys())[sensor_id_index]
date_index = 0
time_start = 12 * 24 * date_index
time_end = 12 * 24 * (date_index + 1)

a_day_speed = df.iloc[time_start:time_end, sensor_id_index]
time_stamp = list(a_day_speed.index)
time_stamp_info = [x.strftime('%Y-%m-%d %H:%M:%S').split(' ')[1][0:5] for x in time_stamp]
date = time_stamp[0].strftime('%Y-%m-%d %H:%M:%S').split(' ')[0]
a_day_speed_value = a_day_speed.values


# ## Draw the figure
plt.figure(figsize=(30, 2))
plt.plot(time_stamp_info, a_day_speed_value, color='red', linewidth=1.0, linestyle='--')
plt.title(f'Traffic Speed of sensor {sensor_id} in {date}')
plt.xlabel('Time')
plt.ylabel('Average Speed')
show_ticks = np.arange(0, 289, 12)
plt.xticks(show_ticks)
plt.savefig(f'figures/{data_name}_{sensor_id}_{date}')
plt.show()

print('Test over'.center(50, '-'))