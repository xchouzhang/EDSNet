from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os

from yacs.config import CfgNode as CN


_C = CN()
# common params for NETWORK
_C.MODEL = CN()
_C.MODEL.NAME = 'seg_hrnet'
_C.MODEL.PRETRAINED = ''
_C.MODEL.ALIGN_CORNERS = True
_C.MODEL.NUM_OUTPUTS = 1
_C.MODEL.EXTRA = CN(new_allowed=True)



def update_config(cfg,newcfg_file):

    cfg.defrost()
    cfg.merge_from_file(newcfg_file)
    cfg.freeze()

    print('*'*100)
    print("Configuration:")
    print(cfg)
    print('*' * 100)

    return cfg


if __name__ == "__main__":
       cfg = update_config(_C, '../seg_hrnet.yaml')


