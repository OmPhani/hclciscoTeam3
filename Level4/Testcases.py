import pytest
from Level1.SearchFile import FileFinder
from Level1.SystemDriveFinder import SystemDriveFinder
class Test_Drive:
    def test_DriveCase(self):
        obj=SystemDriveFinder()
        self.expected=obj.find_drives()
        self.actual=['C']
        assert self.expected==self.actual
    def test_searchfile(self):
        obj=FileFinder()
        d=obj.find_file('demo.txt','C:\\')
       # exp = ['C:\\hcl\\demo.txt', 'C:\\hcl1\\demo.txt']
        self.expected_filename=d[0]
        self.actual_res = 'C:\\hcl\\demo.txt'
        assert self.expected_filename==self.actual_res