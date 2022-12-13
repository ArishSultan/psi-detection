from shutil import rmtree
from pathlib import Path

from pandas import read_csv

from src.features import encodings
from src.features import reducers
from src.data import DataTransformer, steps

RAW_DATA_DIR = Path('..') / 'data' / 'raw'
PROCESSED_DATA_DIR = Path('..') / 'data' / 'processed'

FILES = {
    'H.sapiens100': True,
    'H.sapiens495': False,
    'M.musculus472': False,
    'S.cerevisiae100': True,
    'S.cerevisiae314': False,
}


def main():
    data_transformer = DataTransformer(steps=[
        steps.LabelRename(),
        steps.EncodeSequence(encodings=[
            encodings.ANF(),
            encodings.Binary(),
            encodings.CKSNAP(gap=2, kind='RNA'),
            encodings.CKSNAP(gap=3, kind='RNA'),
            encodings.CKSNAP(gap=4, kind='RNA'),
            encodings.CKSNAP(gap=5, kind='RNA'),
            encodings.CKSNAP(gap=6, kind='RNA'),
            encodings.CKSNAP(gap=7, kind='RNA'),
            encodings.CKSNAP(gap=8, kind='RNA'),
            encodings.DNC(),
            encodings.EIIP(),
            encodings.ENAC(window=2),
            encodings.ENAC(window=3),
            encodings.ENAC(window=4),
            encodings.ENAC(window=5),
            encodings.ENAC(window=6),
            encodings.ENAC(window=7),
            encodings.ENAC(window=8),
            encodings.Kmer(k=2),
            encodings.Kmer(k=3),
            encodings.Kmer(k=4),
            encodings.Kmer(k=5),
            encodings.Kmer(k=6),
            encodings.Kmer(k=7),
            encodings.Kmer(k=8),
            encodings.KmerText(k=2),
            encodings.KmerText(k=3),
            encodings.KmerText(k=4),
            encodings.KmerText(k=5),
            encodings.KmerText(k=6),
            encodings.KmerText(k=7),
            encodings.KmerText(k=8),
            encodings.KNC(k=2),
            encodings.KNC(k=3),
            encodings.KNC(k=4),
            encodings.KNC(k=5),
            encodings.KNC(k=6),
            encodings.KNC(k=7),
            encodings.KNC(k=8),
            encodings.MCN(),
            encodings.MCN(split=True),
            encodings.NAC(),
            encodings.NCP(),
            encodings.ND(),
            # encodings.PSDP(),
            encodings.PseEIIP(),
            # encodings.PseKNC(),
            # encodings.PSNP(),
            # encodings.PSTP(),
            encodings.RCKmer(k=2),
            encodings.RCKmer(k=3),
            encodings.RCKmer(k=4),
            encodings.RCKmer(k=5),
            encodings.RCKmer(k=6),
            encodings.RCKmer(k=7),
            encodings.RCKmer(k=8),
            encodings.TNC()
        ]),
        steps.Splitter(),
    ])

    rmtree(PROCESSED_DATA_DIR, ignore_errors=True)

    for file, flag in FILES.items():
        filename = str(RAW_DATA_DIR / file) + '.csv'
        data = read_csv(filename, header='infer' if flag else None)

        result = data_transformer.transform(data)

        for key, value in result.iter():
            sub_path = key.replace('>', '/')
            if sub_path[0] == '/':
                sub_path = sub_path[1:]

            sub_path = Path(sub_path)

            filename = PROCESSED_DATA_DIR / file / sub_path.parent
            filename.mkdir(parents=True, exist_ok=True)

            if len(key) == 0:
                filename = filename / 'all'
            else:
                filename = filename / sub_path.name

            value.to_csv(str(filename) + '.csv', index=False)


if __name__ == '__main__':
    main()