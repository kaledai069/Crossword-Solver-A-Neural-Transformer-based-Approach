#!/usr/bin/env python3
# Copyright (c) Facebook, Inc. and its affiliates.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.

import importlib

"""
 'Router'-like set of methods for component initialization with lazy imports 
"""


def init_hf_bert_biencoder(args, **kwargs):
    from .hf_models import get_bert_biencoder_components
    return get_bert_biencoder_components(args, **kwargs)

def init_hf_albert_biencoder(args, **kwargs):
    from .hf_models import get_albert_biencoder_components
    return get_albert_biencoder_components(args, **kwargs)

def init_hf_mobilebert_biencoder(args, **kwargs):
    from .hf_models import get_mobilebert_biencoder_components
    return get_mobilebert_biencoder_components(args, **kwargs)

def init_hf_roberta_biencoder(args, **kwargs):
    from .hf_models import get_roberta_biencoder_components
    return get_roberta_biencoder_components(args, **kwargs)

def init_hf_electra_biencoder(args, **kwargs):
    from .hf_models import get_electra_biencoder_components
    return get_electra_biencoder_components(args, **kwargs)

def init_hf_tinybert_biencoder(args, **kwargs):
    from .hf_models import get_tinybert_biencoder_components
    return get_tinybert_biencoder_components(args, **kwargs)

def init_hf_distilbert_biencoder(args, **kwargs):
    from .hf_models import get_distilbert_biencoder_components
    return get_distilbert_biencoder_components(args, **kwargs)

def init_hf_distilroberta_biencoder(args, **kwargs):
    from .hf_models import get_distilroberta_biencoder_components
    return get_distilroberta_biencoder_components(args, **kwargs)

def init_hf_bert_reader(args, **kwargs):
    from .hf_models import get_bert_reader_components
    return get_bert_reader_components(args, **kwargs)


def init_pytext_bert_biencoder(args, **kwargs):
    if importlib.util.find_spec("pytext") is None:
        raise RuntimeError('Please install pytext lib')
    from .pytext_models import get_bert_biencoder_components
    return get_bert_biencoder_components(args, **kwargs)


def init_fairseq_roberta_biencoder(args, **kwargs):
    if importlib.util.find_spec("fairseq") is None:
        raise RuntimeError('Please install fairseq lib')
    from .fairseq_models import get_roberta_biencoder_components
    return get_roberta_biencoder_components(args, **kwargs)


def init_hf_bert_tenzorizer(args, **kwargs):
    from .hf_models import get_bert_tensorizer
    return get_bert_tensorizer(args)

def init_hf_albert_tenzorizer(args, **kwargs):
    from .hf_models import get_albert_tensorizer
    return get_albert_tensorizer(args)

def init_hf_mobilebert_tenzorizer(args, **kwargs):
    from .hf_models import get_mobilebert_tensorizer
    return get_mobilebert_tensorizer(args)

def init_hf_electra_tenzorizer(args, **kwargs):
    from .hf_models import get_electra_tensorizer
    return get_electra_tensorizer(args)

def init_hf_roberta_tenzorizer(args, **kwargs):
    from .hf_models import get_roberta_tensorizer
    return get_roberta_tensorizer(args)

def init_hf_tinybert_tenzorizer(args, **kwargs):
    from .hf_models import get_tinybert_tensorizer
    return get_tinybert_tensorizer(args)

def init_hf_distilbert_tenzorizer(args, **kwargs):
    from .hf_models import get_distilbert_tensorizer
    return get_distilbert_tensorizer(args)


BIENCODER_INITIALIZERS = {
    'hf_bert': init_hf_bert_biencoder,
    'hf_electra': init_hf_electra_biencoder,
    'hf_roberta': init_hf_roberta_biencoder,
    'pytext_bert': init_pytext_bert_biencoder,
    'fairseq_roberta': init_fairseq_roberta_biencoder,
    'hf_albert': init_hf_albert_biencoder,
    'hf_mobilebert': init_hf_mobilebert_biencoder, 
    'hf_tinybert': init_hf_tinybert_biencoder,
    'hf_distilbert': init_hf_distilbert_biencoder, 
    'hf_distilroberta': init_hf_distilroberta_biencoder
}

READER_INITIALIZERS = {
    'hf_bert': init_hf_bert_reader,
}

TENSORIZER_INITIALIZERS = {
    'hf_bert': init_hf_bert_tenzorizer,
    'hf_electra': init_hf_electra_tenzorizer,
    'hf_roberta': init_hf_roberta_tenzorizer,
    'pytext_bert': init_hf_bert_tenzorizer,  # using HF's code as of now
    'fairseq_roberta': init_hf_roberta_tenzorizer,  # using HF's code as of now
    'hf_albert': init_hf_albert_tenzorizer,
    'hf_mobilebert': init_hf_mobilebert_tenzorizer, 
    'hf_tinybert': init_hf_tinybert_tenzorizer,
    'hf_distilbert': init_hf_distilbert_tenzorizer, 
    'hf_distilroberta': init_hf_roberta_tenzorizer
}

def init_comp(initializers_dict, type, args, **kwargs):
    if type in initializers_dict:
        return initializers_dict[type](args, **kwargs)
    else:
        raise RuntimeError('unsupported model type: {}'.format(type))

def init_biencoder_components(encoder_type: str, args, **kwargs):
    return init_comp(BIENCODER_INITIALIZERS, encoder_type, args, **kwargs)

def init_reader_components(encoder_type: str, args, **kwargs):
    return init_comp(READER_INITIALIZERS, encoder_type, args, **kwargs)

def init_tenzorizer(encoder_type: str, args, **kwargs):
    return init_comp(TENSORIZER_INITIALIZERS, encoder_type, args, **kwargs)