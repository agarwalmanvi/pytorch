# Copyright (c) Facebook, Inc. and its affiliates.
# All rights reserved.
#
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.

"""
Global flags for aot autograd
"""
import os
import sys

use_functionalize: bool = True

use_fake_tensor: bool = True

# can be useful for debugging if we are incorrectly creating meta fake tensors
fake_tensor_allow_meta: bool = os.environ.get("FAKE_ALLOW_META", True)

# Enables optional asserts in hotpath code to check for errors.  If
# you are seeing weird accuracy problems, try turning this on.
# This is currently off by default as it will harm tracing time,
# but it is on by default for aot_eager.
debug_assert: bool = False

debug_fake_cross_ref: bool = os.environ.get("AOT_FAKE_CROSSREF", False)

debug_partitioner: bool = os.environ.get("AOT_PARTITIONER_DEBUG", False)

static_weight_shapes: bool = True

# Applies CSE to the graph before partitioning
cse: bool = True

# Restricts the amount of computation AOTAutograd can do.
max_dist_from_bw: bool = 3
