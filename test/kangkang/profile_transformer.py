import warnings

import torch
from torch.nn import Transformer
from torchprofile import profile_macs
warnings.filterwarnings("ignore")

if __name__ == '__main__':
    embed_size = 512
    num_tokens = 30

    model = Transformer(4096)

    inputs = (
        torch.randn(30, 64, 512),
        torch.randn(30, 64, 512),
    )
    macs = profile_macs(model, inputs)
    print('transformer: {:.4g} G'.format(macs / 1e9))

