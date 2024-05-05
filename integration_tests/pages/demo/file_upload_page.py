from selenium.webdriver.common.by import By
<<<<<<< HEAD
from ..base_page import BasePage
=======
from integration_tests.pages.demo.base_demo_page import BaseDemoPage
>>>>>>> b86817008229294af85971a22ae94a69875f969e


class FileUploadPage(BaseDemoPage):
    _upload_file = {"by": By.ID, "value": "file-upload"}
    _file_submit = {"by": By.ID, "value": "file-submit"}
    _uploaded_files = {"by": By.ID, "value": "uploaded-files"}


    def ___init___(self, driver):
        super.__init__(driver)

    def upload_file(self, file):
<<<<<<< HEAD
        self._load("/upload")
        self._type(self.upload_file, file)
=======
        self._demo_load("/upload")
        self._type(self._upload_file, file)
>>>>>>> b86817008229294af85971a22ae94a69875f969e
        self._click(self._file_submit)

    def file_is_uploaded(self, filename):
        upload_file = self._find(self._uploaded_files).text
        return upload_file == filename
