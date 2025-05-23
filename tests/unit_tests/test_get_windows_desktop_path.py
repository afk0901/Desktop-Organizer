from unittest.mock import patch
from win_reg_reader import get_windows_desktop_path


class TestGetWindowsDesktopPath:

    @patch("win_reg_reader._query_windows_registry")
    def test_get_windows_desktop_path_successful(self, query_windows_desktop_path_mock):
        get_windows_desktop_path()
        assert query_windows_desktop_path_mock.call_count == 1

    @patch("win_reg_reader.error_message_prompt_and_exit")
    @patch("win_reg_reader._query_windows_registry", side_effect=OSError)
    def test_get_windows_desktop_path_should_not_raise_OSError(
        self, query_windows_desktop_path_mock, error_message_mock
    ):
        get_windows_desktop_path()
        assert error_message_mock.call_count == 1

    @patch("win_reg_reader.error_message_prompt_and_exit")
    @patch("win_reg_reader._query_windows_registry", side_effect=Exception)
    def test_get_windows_desktop_path_should_not_raise_Exception(
        self, query_windows_desktop_path_mock,  error_message_mock
    ):
        get_windows_desktop_path()
        assert error_message_mock.call_count == 1
