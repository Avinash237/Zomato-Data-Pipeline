import os


from src.FileCheckModule import FileCheckModule
from src.DataQualityCheckModule import DataQualityCheck

# Example usage
source_dir = 'H:/Python_Code/Zomato_Data_Pipeline/Source_file'
processed_dir = 'H:/Python_Code/Zomato_Data_Pipeline/Processed_file'
failed_dir = 'H:/Python_Code/Zomato_Data_Pipeline/Failed_file'
output_dir = 'H:/Python_Code/Zomato_Data_Pipeline/Output_file'


def main():
    file_check_module = FileCheckModule(source_dir, processed_dir, failed_dir)
    data_quality_check_module = DataQualityCheck(output_dir)

    files_to_process = os.listdir(source_dir)
    for file_name in files_to_process:
        if file_check_module.process_file(file_name):
            data_quality_check_module.process_file(file_name)


if __name__ == "main":
    main()
