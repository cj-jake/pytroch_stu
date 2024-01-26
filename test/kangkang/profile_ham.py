import warnings

import torch
from ham import Hamburger  # Assuming that your Hamburger model is defined in 'ham.py'
from torchprofile import profile_macs
warnings.filterwarnings("ignore")
if __name__ == '__main__':
    embed_size = 512
    num_tokens = 30

    # Instantiate the Hamburger model instead of Transformer
    model = Hamburger(3, 32*32, 64)  # Adjust the parameters based on your Hamburger model

    # Generate input tensors
    inputs = torch.randn(64, 3, 32, 32)

    # Profile the MACs
    macs = profile_macs(model, inputs)
    print('Hamburger: {:.4g} G'.format(macs / 1e9))