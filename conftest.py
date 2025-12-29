import pytest

@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args):
    browser_type_launch_args["slow_mo"] = 500
    browser_type_launch_args["headless"] = False
    return browser_type_launch_args

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    browser_context_args["viewport"] = {"width": 1920, "height": 1080}
    return browser_context_args

