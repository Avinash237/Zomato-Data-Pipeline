import os


class FileCheckModule:
    def __init__(self, source_dir, processed_dir, failed_dir):
        self.source_dir = source_dir
        self.processed_dir = processed_dir
        self.failed_dir = failed_dir
        self.processed_files = set()

    def is_new_file(self, file_name):
        try:
            return file_name not in self.processed_files

        except Exception as ex:
            exception_str = "Error is File Check Module, while checking new file.." + str(ex)
            raise Exception(exception_str)

    def is_file_empty(self, file_path):
        try:
            return os.path.getsize(file_path) == 0

        except Exception as ex:
            exception_str = "Error is File Check Module, while checking file is empty.." + str(ex)
            raise Exception(exception_str)

    def is_csv_file(self, file_name):
        try:
            return file_name.lower().endswith('.csv')

        except Exception as ex:
            exception_str = "Error is File Check Module, while checking file type" + str(ex)
            raise Exception(exception_str)

    def process_file(self, file_name):
        try:
            if self.is_new_file(file_name) and self.is_csv_file(file_name):
                file_path = os.path.join(self.source_dir, file_name)
                if not self.is_file_empty(file_path):
                    self.processed_files.add(file_name)
                    return True
                else:
                    self.move_file(file_path, self.failed_dir)
            return False

        except Exception as ex:
            exception_str = "Error is File Check Module, While processing file" + str(ex)
            raise Exception(exception_str)
    def move_file(self, file_path, destination_dir):
        # Move the file to the specified directory
        pass