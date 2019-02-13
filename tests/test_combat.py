#!/usr/bin/env python

import os
import time
import warnings

from combat import combat
import numpy as np
import pandas as pd
import patsy
import pytest
from rpy2.rinterface import RRuntimeWarning
from rpy2.robjects import r
from types import FunctionType


@pytest.fixture
def r_result():
    warnings.filterwarnings("ignore", category=RRuntimeWarning)
    r['source'](os.path.join("tests", "R-combat.R"))
    return pd.read_csv("r-batch.csv", index_col=0)


class TestCombat():
    def test_import_is_function(self):
        assert isinstance(combat, FunctionType)

    def test_combat(self, r_result):
        pheno = pd.read_csv('bladder-pheno.csv', index_col=0)
        data = pd.read_csv('bladder-expr.csv', index_col=0)
        model = patsy.dmatrix("~ age + cancer", pheno, return_type="dataframe")

        t = time.time()
        p_result = combat(data, pheno['batch'], model, "age")

        print("{:.2f} seconds\n".format(time.time() - t))
        print(str(p_result.iloc[:5, :5]))

        p_result.to_csv("py-batch.csv")

        print((p_result - r_result).max().max())

        assert np.allclose(r_result, p_result)
