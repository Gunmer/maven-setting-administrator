import unittest
from unittest.mock import patch

from msa.model.setting import Setting
from msa.services.file_service import FileService
from msa.utils.config import Config
from msa.utils.log import Log


class FileServiceTest(unittest.TestCase):

    def setUp(self):
        self.service = FileService(Log(False), Config())

    @patch('os.listdir')
    def test_list_all__when_execute__should_return_xml_only(self, listdir):
        listdir.return_value = ['se1.xml', 'se2.xml', 'msa.db', 'se3.xml']

        all_settings = self.service.list_all()

        self.assertEqual(all_settings, ['se1.xml', 'se2.xml', 'se3.xml'])

    @patch('os.remove')
    def test_remove_setting__when_setting_have_file__should_be_removed(self, remove):
        setting = Setting('alias', 'file')

        self.service.remove_setting(setting)

        remove.assert_called()

    @patch('os.remove')
    def test_remove_setting__when_setting_have_not_file__should_be_removed(self, remove):
        setting = Setting('alias', '')

        self.service.remove_setting(setting)

        remove.assert_not_called()

    @patch('os.path.exists')
    def test_directory_exist__when_os_path_exists__should_return_true(self, exists):
        exists.return_value = True

        result = self.service.directory_exist()

        self.assertTrue(result)

    @patch('os.path.exists')
    def test_directory_exist__when_os_path_not_exists__should_return_false(self, exists):
        exists.return_value = False

        result = self.service.directory_exist()

        self.assertFalse(result)

    @patch('os.mkdir')
    def test_create_directory__when_executed__should_call_mkdir(self, mkdir):
        self.service.create_directory()

        mkdir.assert_called()

    @patch('os.path.exists')
    @patch('os.remove')
    def test_deactivate_setting__when_setting_not_exists__should_not_call_remove(self, mock_remove, mock_exists):
        mock_exists.return_value = False

        self.service.deactivate_setting()

        mock_remove.assert_not_called()

    @patch('os.path.exists')
    @patch('os.remove')
    def test_deactivate_setting__when_setting_exists__should_call_remove(self, mock_remove, mock_exists):
        mock_exists.return_value = True

        self.service.deactivate_setting()

        mock_remove.assert_called()
