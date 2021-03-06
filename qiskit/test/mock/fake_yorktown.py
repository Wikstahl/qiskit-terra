# -*- coding: utf-8 -*-

# This code is part of Qiskit.
#
# (C) Copyright IBM 2019.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

"""
Fake Yorktown device (5 qubit).
"""

from qiskit.providers.models import GateConfig, QasmBackendConfiguration
from .fake_backend import FakeBackend


class FakeYorktown(FakeBackend):
    """A fake 5 qubit backend."""

    def __init__(self):
        """
            1
          / |
        0 - 2 - 3
            | /
            4
        """
        cmap = [[0, 1], [0, 2], [1, 2], [3, 2], [3, 4], [4, 2]]

        configuration = QasmBackendConfiguration(
            backend_name='fake_yorktown',
            backend_version='0.0.0',
            n_qubits=5,
            basis_gates=['u1', 'u2', 'u3', 'cx', 'id'],
            simulator=False,
            local=True,
            conditional=False,
            open_pulse=False,
            memory=False,
            max_shots=65536,
            gates=[GateConfig(name='TODO', parameters=[], qasm_def='TODO')],
            coupling_map=cmap,
        )

        super().__init__(configuration)
