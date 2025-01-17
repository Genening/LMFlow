#!/bin/env/python3
# coding=utf-8
"""A one-line summary of the module or program, terminated by a period.

Leave one blank line.  The rest of this docstring should contain an
overall description of the module or program.  Optionally, it may also
contain a brief description of exported classes and functions and/or usage
examples.

Typical usage example:

  foo = ClassFoo()
  bar = foo.FunctionBar()
"""
from __future__ import absolute_import
import unittest

import json
import os
from pathlib import Path

from lmflow.args import DatasetArguments
from lmflow.datasets.dataset import Dataset


class DatasetTest(unittest.TestCase):

    def test_init(self):
        dataset_dir = 'data/example_dataset/train'
        data_args = DatasetArguments(
            dataset_path=dataset_dir
        )
        dataset = Dataset(data_args, backend='huggingface')
        hf_dataset = dataset.get_backend_dataset()

        with open(os.path.join(Path(dataset_dir), 'train_50.json'), 'r') as fin:
            json_obj = json.load(fin)
            for i in range(len(hf_dataset)):
                self.assertEqual(json_obj['instances'][i], hf_dataset[i])
