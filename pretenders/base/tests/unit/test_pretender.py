from nose.tools import assert_true, assert_false
from mock import patch

from pretenders.base.pretender import Pretender


@patch('pretenders.base.pretender.BossClient')
@patch('pretenders.base.pretender.in_parent_process')
@patch('pretenders.base.pretender.save_pid_file')
def test_pretender_save_pid_on_creation(
        save_pid_file, in_parent_process, BossClient):
    "Test that only saves if in_parent_process is ``True``"
    in_parent_process.return_value = True

    Pretender(1, 2, 3, 4)
    assert_true(save_pid_file.called)

    save_pid_file.reset_mock()

    in_parent_process.return_value = False

    Pretender(1, 2, 3, 4)
    assert_false(save_pid_file.called)
