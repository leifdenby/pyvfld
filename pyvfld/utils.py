import xarray as xr

from . import nomenclature


def to_dataset(df):
    var_names = df.columns
    ds = xr.Dataset.from_dataframe(df.set_index("station_id"))

    for v in var_names:
        v_attrs = nomenclature.VARIABLES.get(v)
        if v_attrs is not None:
            if "UNIT" in v_attrs:
                ds[v].attrs["units"] = v_attrs["UNIT"]
            if "TEXT" in v_attrs:
                ds[v].attrs["long_name"] = v_attrs["TEXT"]

    return ds
