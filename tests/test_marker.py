import pytest
import logging

logger = logging.getLogger(__name__)


@pytest.mark.slow(reason="This is a slow test")
def test_slow_code():
    logger.info("hello slow test")