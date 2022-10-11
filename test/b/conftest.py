def pytest_addoption(parser):
    parser.addoption(
        '--step',
        action='store',
        default=None,
        help='Task step id or @ for \'everything\''
    )


def pytest_generate_tests(metafunc):
    if 'step' not in metafunc.fixturenames:
        return
    step = metafunc.config.getoption('step')
    if step is not None:
        step = int(step)
    metafunc.parametrize('step', [step])


def pytest_assertrepr_compare(op, left, right):
    if isinstance(left, int) and isinstance(right, int):
        return [f'Ожидалось, но не выполняется: {left} {op} {right}']
