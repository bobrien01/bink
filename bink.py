"""Bink Test"""

# Imports
import csv


class ReadFileError(ValueError):
    """ Exception to be raised with error reading file """


class BinkTest():
    """Class to hold the data and functionality for the Bink Test"""
    USER_OPTION_ALL = 0
    USER_OPTION_1 = 1
    USER_OPTION_2 = 2
    USER_OPTION_3 = 3
    USER_OPTION_4 = 4

    def __init__(self, filename='Mobile Phone Masts.csv'):
        self.filename = filename
        self.data = []

    def process_user_input(self, option=None):
        """
        Takes a user input and executes the relevant functions
        """

        # Check user input
        try:
            option = int(option)
        except:
            raise ValueError

        if option < self.USER_OPTION_ALL or option > self.USER_OPTION_4:
            raise ValueError

        if not self.data:
            try:
                self._read_csv_data()
            except Exception as exception:
                raise exception

        if option in (self.USER_OPTION_ALL, self.USER_OPTION_1):
            sorted_data = self._sort_by_field('Current Rent')
            self.print_rows(headers=True, rows=sorted_data[0:5])

        if option in (self.USER_OPTION_ALL, self.USER_OPTION_2):
            pass

        if option in (self.USER_OPTION_ALL, self.USER_OPTION_3):
            pass

        if option in (self.USER_OPTION_ALL, self.USER_OPTION_4):
            pass

    def _read_csv_data(self):
        self.data = []
        # Open the file as read ony and read into a dict
        try:
            with open(self.filename, mode='r') as csv_file:
                # Read the data into rows of type OrderedDict
                csv_reader = csv.DictReader(csv_file)
                for row in csv_reader:
                    self.data.append(row)

                self._clean_data()
        except:
            raise ReadFileError

        if not self.data:
            raise ReadFileError

    def _clean_data(self):
        # Function to clean some data for example ensure that
        # float parameters are stored as floats not strings
        for row in self.data:
            for i, val in row.items():
                try:
                    row[i] = float(val)
                except ValueError:
                    pass

    def _sort_by_field(self, field):
        if self.data:
            if field in self.data[0].keys():
                sorted_list = sorted(self.data, key=lambda k: k[field])
                return sorted_list

        return self.data

    @staticmethod
    def print_rows(rows=None, headers=True):
        """
        Prints rows with optional headers
        """
        output_string = ''
        if rows:
            if headers:
                output_string += ','.join(rows[0].keys()) + '\n'

            for row in rows:
                output_string += ','.join([str(v) for i, v in row.items()]) + '\n'

        if output_string:
            print(output_string)


def main():
    """
    Main function, loop until user quitsx
    """
    blink_test = BinkTest()
    while True:
        print("Please enter an option")
        print("0 - Do all of the following")
        print("1 - Sort by Current Rent and select the lowest 5")
        print("2 - Filter on lease = 25 years")
        print("3 - Create dict of tenant name and mast counts")
        print("4 - Filter leases between 1 June 1999 and 31 Aug 2007")
        print("quit to quit")

        user_input = input()
        if user_input.lower() == 'quit':
            break

        try:
            user_input = int(user_input)
            blink_test.process_user_input(user_input)
        except ValueError:
            print("Invalid value, please retry")
            continue


if __name__ == "__main__":
    main()
