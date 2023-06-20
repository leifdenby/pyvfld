import io
from collections import OrderedDict

import numpy as np
import pandas as pd

RADIOSONDE_STATION_VARS = ["station_id", "lat", "lon", "altitude"]


def _parse_variables(fh, n_vars):
    variables = OrderedDict()
    for i in range(n_vars):
        line = fh.readline()
        var_name, accumulation_mode = line.split()
        variables[var_name] = accumulation_mode
    return variables


def _parse_synop_data_to_dataframe(fh, variables, n_stations):
    #     03488   52.94940    1.12250    19.2    0.0000E+00  283.1223E+00
    #     03495   52.77000    1.35000    15.3    6.0000E+00  281.5686E+00
    #     03590   52.12390    0.95750    85.8    1.0000E+00  269.2976E+00
    # .123456789.123456789.123456789.123456789.123456789.123456789.1234567
    #
    #     01010   69.307   16.131     2.0   4.9432E+00   9.4658E+00 275.5978E+00  80.0883E+00   1.0080E+0
    #     01014   69.234   17.903    29.3 231.7240E+00   2.2136E+00 273.3647E+00  84.0209E+00   1.0017E+0
    #     01015   69.601   17.837    -6.4 285.2777E+00   6.7298E+00 274.8446E+00  89.6737E+00   1.0079E+0
    #     01018   69.241   16.003   126.7 356.9360E+00   5.5123E+00 273.9615E+00  87.2850E+00 991.7290E+0
    # .123456789.123456789.123456789.123456789.123456789.123456789.123456789.123456789.123456789.123456789

    col_names = ["station_id", "lat", "lon"]
    if "FI" not in variables:
        # vobs files always includes data for "FI" (geopotential), but isn't
        # given in the variable list, so we need to include it here if it is
        # missing
        col_names.append("FI")
    col_names += variables
    dtypes = {v: v != "station_id" and np.float32 or np.int32 for v in col_names}

    # XXX: have to load the lines ourselves because pd.read_csv reads messes up
    # the read position
    txt = "\n".join(fh.readline() for _ in range(n_stations))
    df = pd.read_csv(
        io.StringIO(txt),
        nrows=n_stations,
        delimiter=r"\s+",
        names=col_names,
        dtype=dtypes,
    )

    return df


def _parse_radiosonde_data_to_dataframe(fh, variables, n_levels):
    # 1000.   123. 296.6  57.0 236.   7.   10.258E-03 287.5
    #  925.   800. 292.7  57.6 210.   5.    8.825E-03 284.1
    #  850.  1520. 286.2  79.7 194.   6.    8.787E-03 282.7
    #  700.  3123. 276.2  67.3 217.   9.    4.575E-03 270.8
    # .123456789.123456789.123456789.123456789.123456789.123456789.1234567
    col_names = variables
    # TODO: work out what the format spec is here, it isn't obvious to me...

    # XXX: have to load the lines ourselves because pd.read_csv reads messes up
    # the read position
    txt = "\n".join(fh.readline() for _ in range(n_levels))
    return pd.read_csv(
        io.StringIO(txt), nrows=n_levels, delimiter=r"\s+", names=col_names, dtype=float
    )


def read_vlfd(fp):
    """
    Read VFLD/Vobs file in path given by `fp` and return as `pd.DateFrame`
    `df_synop, dfs_radiosondes`
    """
    df_synop = None
    dfs_radiosondes = {}
    with open(fp) as fh:
        n_synop_stations, n_radiosonde_stations, version = map(
            int, fh.readline().split()
        )
        if version != 4:
            raise NotImplementedError(version)

        if n_synop_stations > 0:
            n_synop_variables = int(fh.readline())
            synop_variables = _parse_variables(fh, n_synop_variables)

            df_synop = _parse_synop_data_to_dataframe(
                fh=fh,
                variables=list(synop_variables.keys()),
                n_stations=n_synop_stations,
            )

        if n_radiosonde_stations > 0:
            n_radiosonde_levels = int(fh.readline())
            n_radiosonde_variables = int(fh.readline())
            radiosonde_variables = _parse_variables(fh, n_radiosonde_variables)

            for i in range(n_radiosonde_stations):
                line = fh.readline()
                station_info_strs = line.split()

                station_info = {
                    k: k == "station_id" and int(v) or float(v)
                    for (k, v) in zip(RADIOSONDE_STATION_VARS, station_info_strs)
                }
                df_radiosonde = _parse_radiosonde_data_to_dataframe(
                    fh=fh,
                    variables=list(radiosonde_variables.keys()),
                    n_levels=n_radiosonde_levels,
                )
                dfs_radiosondes[station_info["station_id"]] = df_radiosonde

    return df_synop, dfs_radiosondes
