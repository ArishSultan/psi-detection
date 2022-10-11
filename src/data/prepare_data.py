import pandas as pd
from pathlib import Path

import src.utils as utils


def prepare_data(path: Path, out_path: Path, has_split_logic=False, no_title=False):
    data = pd.read_csv(path, header=None if no_title else 'infer')

    data.replace({'class': {'POS': 1, 'Neg': 0}}, inplace=True)

    if has_split_logic:
        test_set = data.loc[data['set'] == 'test'].drop('set', axis=1)
        train_set = data.loc[data['set'] == 'train'].drop('set', axis=1)
        valid_set = data.loc[data['set'] == 'valid'].drop('set', axis=1)
    else:
        # TODO: Prepare some logic here for data split.
        test_set = pd.DataFrame()
        train_set = data
        valid_set = pd.DataFrame()

    out_path.mkdir(parents=True, exist_ok=True)

    test_set.to_csv(out_path / 'test.csv', index=False, header=False)
    train_set.to_csv(out_path / 'train.csv', index=False, header=False)
    valid_set.to_csv(out_path / 'valid.csv', index=False, header=False)
