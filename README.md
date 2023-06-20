# pyvfld

Read VFLD/Vobs files in python. The format is detailed in the [documentation for the Monitor tool](https://hirlam.github.io/Monitor/dev/#A-general-input-format-1). Assumptions made within Monitor about what the different variables mean (and their units) can partially be reconstructed from


## Usage

```python
>>> import pyvfld
>>> fp = "tests/examples/vfldAQ_Benelux_750m201807250000"
>>> df_synop, dfs_radiosondes = pyvfld.read_vlfd(fp=fp)
>>> df_synop.head()
   station_id        lat     lon         FI  ...           DSN         DSNP1         DSNP2  WSN
0        3488  52.949402  1.1225  19.200001  ...  8.722500e+18  8.722500e+18  7.566920e+19  0.0
1        3495  52.770000  1.3500  15.300000  ...  0.000000e+00  0.000000e+00  1.000002e+20  0.0
2        3590  52.123901  0.9575  85.800003  ...  0.000000e+00  0.000000e+00  1.000002e+20  0.0
3        3591  52.116699  0.9667  86.500000  ...  0.000000e+00  0.000000e+00  1.000002e+20  0.0
4        3693  51.554699  0.8269   1.200000  ...  0.000000e+00  0.000000e+00  1.000002e+20  0.0

[5 rows x 41 columns]
>>> ds_synop = pyvfld.to_dataset(df_synop)
>>> ds_synop
<xarray.Dataset>
Dimensions:     (station_id: 202)
Coordinates:
  * station_id  (station_id) int32 3488 3495 3590 3591 ... 10728 10729 10730
Data variables: (12/40)
    lat         (station_id) float32 52.95 52.77 52.12 ... 49.57 49.51 49.47
    lon         (station_id) float32 1.122 1.35 0.9575 ... 8.467 8.555 8.517
    FI          (station_id) float32 19.2 15.3 85.8 86.5 ... 92.4 100.8 94.4
    NN          (station_id) float32 0.0 6.0 1.0 1.0 2.0 ... 0.0 0.0 4.0 1.0 0.0
    DD          (station_id) float32 283.1 281.6 269.3 ... 93.17 114.8 127.9
    FF          (station_id) float32 2.767 1.074 3.044 ... 1.847 0.7879 1.84
    ...          ...
    PA1         (station_id) float32 1.0 1.0 1.0 1.0 ... -99.0 1.0 0.68 0.7237
    PA2         (station_id) float32 -99.0 -99.0 -99.0 ... -99.0 0.32 0.2763
    DSN         (station_id) float32 8.722e+18 0.0 0.0 0.0 ... 0.0 0.0 0.0 0.0
    DSNP1       (station_id) float32 8.722e+18 0.0 0.0 0.0 ... 1e+20 0.0 0.0 0.0
    DSNP2       (station_id) float32 7.567e+19 1e+20 1e+20 ... 9.391e+19 0.0 0.0
    WSN         (station_id) float32 0.0 0.0 0.0 0.0 0.0 ... 0.0 0.0 0.0 0.0 0.0
>>> ds_synop.CH
<xarray.DataArray 'CH' (station_id: 202)>
array([7500. , 7500. , 7500. , 7500. , 7500. , 3039.6, 7500. , 7500. ,
       7500. , 7500. , 2755.3, 1981.4, 7500. , 7500. , 2760.6, 7500. ,
       7500. , 7500. , 7500. , 7500. , 7500. , 7500. , 7500. , 7500. ,
       2904.4, 7500. , 7500. , 1867.6, 7500. , 7500. , 2906.3, 3053.3,
       2904.9, 7500. , 3207.3, 2904.5, 2908.4, 3202.6, 2108.6, 7500. ,
       7500. , 2766.5, 7500. , 7500. , 7500. , 7500. , 3202.6, 7500. ,
       7500. , 7500. , 7500. , 2905.3, 7500. , 7500. , 7500. , 3047.9,
       3203.6, 3204.1, 7500. , 7500. , 2356.7, 7500. , 7500. , 2488.9,
       7500. , 7500. , 3518.3, 3361.4, 7500. , 7500. , 3212.6, 2228.7,
       7500. , 2486.1, 7500. , 3356.7, 3198.7, 3358. , 3350.4, 3202.6,
       3042.5, 7500. , 7500. , 7500. , 3844.6, 7500. , 7500. , 7500. ,
       7500. , 3204.8, 7500. , 7500. , 1953.6, 7500. , 7500. , 7500. ,
       7500. , 7500. , 7500. , 7500. , 7500. , 7500. , 2848.9, 3319.4,
       3155.2, 2466.1, 7500. , 7500. , 7500. , 7500. , 7500. , 7500. ,
       7500. , 7500. , 3188.7, 7500. , 3039.4, 7500. , 7500. , 7500. ,
       7500. , 7500. , 7500. , 7500. , 7500. , 7500. , 7500. , 1772.1,
       7500. , 7500. , 7500. , 2628.8, 7500. , 7500. , 7500. , 7500. ,
       7500. , 7500. , 7500. , 7500. , 7500. , 7500. , 7500. , 7500. ,
       7500. , 7500. , 7500. , 7500. , 7500. , 7500. , 7500. , 7500. ,
       7500. , 7500. , 7500. , 7500. , 7500. , 7500. , 7500. , 7500. ,
       7500. , 7500. , 7500. , 7500. , 7500. , 7500. , 2444.3, 7500. ,
       7500. , 7500. , 7500. , 7500. , 7500. , 7500. , 7500. , 7500. ,
       7500. , 7500. , 7500. , 7500. , 7500. , 7500. , 7500. , 7500. ,
       7500. , 7500. , 2733.2, 7500. , 7500. , 7500. , 7500. , 7500. ,
       7500. , 7500. , 3164.9, 7500. , 7500. , 7500. , 7500. , 2910.7,
       7500. , 7500. ], dtype=float32)
Coordinates:
  * station_id  (station_id) int32 3488 3495 3590 3591 ... 10728 10729 10730
Attributes:
    units:      m
    long_name:  Cloud base
```

## Status

- [x] read VFLD and Vobs data from file
- [ ] merge all radiosonde dataframes into a single one using MultiIndex
- [ ] add accumulation mode info to data frames
- [x] add units and more descriptive rather than shorthand names for fields
- [ ] add ability to write VFLD/Vobs files
