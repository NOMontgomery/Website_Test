import pytest

import os

from integration_tests.pages.demo.file_upload_page import FileUploadPage


# @pytest.mark.deep
class TestFileUpload():

    @pytest.fixture
    def file_upload(self, driver):
        return FileUploadPage(driver)
    
    filename = "somefile.txt"
    file = os.path.join(os.getcwd(), "resources/" + filename)

    def test_file_upload(self, file_upload):
        file_upload.upload_file(self.file)
        assert(file_upload.file_is_uploaded(self.filename))

