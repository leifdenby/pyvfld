# pyvfld

Read VFLD/Vobs files in python


## Usage

```python
>>> import pyvfld
>>> fp = "tests/examples/vfldAQ_Benelux_750m201807250000"
>>> df_synop, dfs_radiosondes = pyvfld.read_vlfd(fp=fp)
>>> df_synop.head()
   station_id       lat       lon         FI   NN  ...   PA2  DSN  DSNP1  DSNP2  WSN
0         -96  52.93750  1.122070  19.203125  0.0  ... -99.0  inf    inf    inf  0.0
1         -89  52.78125  1.349609  15.296875  6.0  ... -99.0  0.0    0.0    inf  0.0
2           6  52.12500  0.957520  85.812500  1.0  ... -99.0  0.0    0.0    inf  0.0
3           7  52.12500  0.966797  86.500000  1.0  ... -99.0  0.0    0.0    inf  0.0
4         109  51.56250  0.826660   1.200195  2.0  ... -99.0  0.0    0.0    inf  0.0

[5 rows x 41 columns]
```

## Status

- [x] read VFLD and Vobs data from file
- [ ] merge all radiosonde dataframes into a single one using MultiIndex
- [ ] add accumulation mode info to data frames
- [ ] add units and more descriptive rather than shorthand names for fields
