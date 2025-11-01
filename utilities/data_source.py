import config
from utilities import read_data

class DataSource:
    valid_login_data = [("admin","pass","OpenEMR"),
                        ("physician","physician", "OpenEMR")]

    invalid_data=read_data.get_sheet_into_list(config.project_path+r"/test_data/open-emr-data.xlsx")

    valid_login_data_excel=read_data.get_sheet_into_list(r"D:\Balaji\Company\Siemens Oct 2025\PythonPytestFramework\test_data\open_emr_data.xlsx","test_valid_login")


