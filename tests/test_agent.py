"""Unit tests"""


def test_agent(bacnet_proxy):
    assert bacnet_proxy is not None
    assert bacnet_proxy.bacnet_application is not None
