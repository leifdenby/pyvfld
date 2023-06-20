from pathlib import Path

import pyvfld


def _get_examples(ftype):
    return list((Path(__file__).parent / "examples").glob(f"{ftype}*"))


def test_reader():
    fps_vfld = _get_examples(ftype="vfld")
    fps_vobs = _get_examples(ftype="vobs")

    for fp in fps_vfld + fps_vobs:
        import ipdb

        with ipdb.launch_ipdb_on_exception():
            df_synop, dfs_radiosondes = pyvfld.read_vlfd(fp=fp)
        # try:
        #     df_synop, dfs_radiosondes = pyvfld.read_vlfd(fp=fp)
        # except Exception as ex:
        #     raise Exception(f"There was an issue reading {fp}") from ex
