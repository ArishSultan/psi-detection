import pandas as pd
import src.features as feature


def encode_PseKNC(data: pd.DataFrame):
    sequences = data['x']
    if len(sequences) <= 0:
        raise 'At-least one sequence must be provided'

    return pd.concat([
        data,
        pd.DataFrame(
            sequences.map(feature.pse_knc).tolist(),
            columns=['x' + str(x + 1) for x in range(len(sequences[0]) * 4)],
        )
    ], axis=1).drop('x', axis=1)
