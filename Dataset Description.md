# Dataset Description

> In this document, multiple frequently used datasets in traffic flow prediction will be introduced. They vary in their size, content, publicity and accessibility. A fraction of them are accompanied with visualizations. Besides, frequent measurements used will also be displayed along with the easy Python code.

## METR-LA

This dataset comes from the communications of the ACM, 2014 Big Data and Its Technical Challenges. It’s the speed captured from the loop detectors installed in the highway of Los Angeles County. There are **207** sensors and the data are collected for 4 months from May 1st 2012 to Jun 30th 2012. The data was processed into **5 min windows**. Thus for each day, there are **288 samples/day** . The file is stored in `.h5` file and should be opened with python module `hd5y`. The data can be read with the following code

```Python
# ## Read the meta_la data
data_path = 'DCRNN-master/data/METR-LA/df_highway_2012_4mon_sample.h5'
h5 = h5py.File(data_path, 'r')
data = h5['df']
speeds = data['block0_values'][:]
```

The structure of the h5 file is `df -> axis0/axis1/block0_items/block0_values`.The real life correspondence are illustrated with the following table:

| Name | Real life correspondence |
| ---- | ----|
| axis0 | (207, ) sensor_id |
| axis1 | (34272, ) time_stamp, start from |
| block0_items | |
| block0_values | |
