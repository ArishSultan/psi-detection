from os import chdir
from os.path import join
from pathlib import Path
from pandas import read_csv

from src.data.transformer import *
from src.data.transformers import *
from src.features.encodings import *


DATA = {
    'H.sapiens100': False,
    'H.sapiens495': True,
}


def _resolve_data_splitter(data: object):
    if 'set' in data:
        return DataSplitter(split_column='set')
    else:
        return DataTransformerStep()


def main():
    in_dir = Path(join('..', 'data', 'raw'))
    out_dir = Path(join('..', 'data', 'intermediate'))

    transformer = DataTransformer(steps=[
        HeaderRename(),
        LabelRename(),
        EncodeSequence(encodings=[
            DNC()
        ]),
        Conditional(_resolve_data_splitter)
    ])

    for name, flag in DATA.items():
        file = in_dir / (name + '.csv')
        data = read_csv(file, header=None if flag else 'infer')

        data = transformer.transform(data)
        for item in data:
            data[item].to_csv(Path(name + item), index=False)

    # TODO(ArishSultan): Add more date directories


if __name__ == '__main__':
    chdir(Path(__file__).parent)

    main()
