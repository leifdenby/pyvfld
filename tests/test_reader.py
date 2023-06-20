from pathlib import Path

import pyvfld


def _get_examples(ftype):
    return list((Path(__file__).parent / "examples").glob(f"{ftype}*"))


def test_reader():
    fps_vfld = _get_examples(ftype="vfld")
    fps_vobs = _get_examples(ftype="vobs")

    for fp in fps_vfld + fps_vobs:
        df_synop, dfs_radiosondes = pyvfld.read_vlfd(fp=fp)


def test_to_dataset():
    fps_vfld = _get_examples(ftype="vfld")
    fps_vobs = _get_examples(ftype="vobs")

    for fp in fps_vfld + fps_vobs:
        df_synop, dfs_radiosondes = pyvfld.read_vlfd(fp=fp)
        ds_synop = pyvfld.to_dataset(df=df_synop)
        assert set(df_synop.columns).difference(ds_synop.data_vars.keys()) == {
            "station_id"
        }
