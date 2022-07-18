"""Tests suite for `volttron_bacnet_proxy`."""

import pytest
import json
import socket

from pathlib import Path

from volttron_bacnet_proxy.agent import initialize_agent

TESTS_DIR = Path(__file__).parent
TMP_DIR = TESTS_DIR / "tmp"
FIXTURES_DIR = TESTS_DIR / "fixtures"
"""Configuration for the pytest test suite."""


@pytest.fixture()
def bacnet_proxy():
    config_path = f"{TESTS_DIR}/cfg.json"
    device_address = socket.gethostbyname(f"{socket.gethostname()}.local")
    config_json = {
        "device_address": device_address,
        "max_apdu_length": 1024,
        "object_id": 599,
        "object_name": "Volttron BACnet driver",
        "vendor_id": 5,
        "segmentation_supported": "segmentedBoth"
    }

    with open(config_path, 'w') as fp:
        json.dump(config_json, fp)

    yield initialize_agent(config_path)

    Path(config_path).unlink(missing_ok=True)
