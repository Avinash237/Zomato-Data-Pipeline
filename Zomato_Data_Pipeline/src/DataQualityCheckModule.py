
import re



class DataQualityCheck:
    def __init__(self, file_path):
        self.file_path = file_path

    def validate_phone_numbers(self, phone):
        try:
            # Remove preceding "+" and spaces
            phone = re.sub(r'[+\s]', '', phone)


            # Ensure phone numbers are correctly formatted (customize the regex as needed)
            if re.match(r'^\d{10}$', phone):
                return phone
            else:
                return None

        except Exception as ex:
            exception_str = "Error in data qulity cheking module, while validating phone number" + str(ex)
            raise Exception(exception_str)
    def clean_descriptive_fields(self, field_data):
        try:
            # Remove special characters or junk characters
            cleaned_data = re.sub(r'[^a-zA-Z0-9\s]', '', field_data)
            return cleaned_data

        except Exception as ex:
            exception_str = "Error in data qulity cheking module, while clean descriptive fields" + str(ex)
            raise Exception(exception_str)

    def process_file(self):
        try:

            with open(self.file_path, 'r') as file:
                lines = file.readlines()

            cleaned_records = []
            bad_records = []

            for line in lines:
                record = line.split(',')

                # Check and clean phone field
                phone_field = record[1]  # Assuming phone field is at index 1, modify as needed
                cleaned_phone = self.validate_phone_numbers(phone_field)

                if cleaned_phone:
                    record[1] = cleaned_phone
                else:
                    # If phone number is not valid, consider it a bad record
                    bad_records.append(record)
                    continue

                # Check and clean descriptive fields
                address_field = record[2]  # Assuming address field is at index 2, modify as needed
                record[2] = self.clean_descriptive_fields(address_field)

                # Check for null values in required fields
                if None in record:
                    # If there are null values, consider it a bad record
                    bad_records.append(record)
                else:
                    cleaned_records.append(record)

            # Write cleaned records to a new file
            with open('cleaned_data.csv', 'w') as cleaned_file:
                for record in cleaned_records:
                    cleaned_file.write(','.join(record) + '\n')

            # Write bad records to a separate file
            with open('bad_records.csv', 'w') as bad_file:
                for record in bad_records:
                    bad_file.write(','.join(record) + '\n')

        except Exception as ex:
            exception_str = "Error in data qulity cheking module, while processing File" + str(ex)
            raise Exception(exception_str)






