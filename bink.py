"""Bink Test"""

# Imports
import csv
import operator
from datetime import datetime
from tabulate import tabulate
from dateutil import parser


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
            self.print_container(sorted_data[0:5])

        if option in (self.USER_OPTION_ALL, self.USER_OPTION_2):
            filtered_data = self._filter_by_field_value('Lease Years', operator.eq, 25.0)
            self.print_container(filtered_data)

        if option in (self.USER_OPTION_ALL, self.USER_OPTION_3):
            count_dict = self._count_occurrence_of_field('Tenant Name')
            self.print_container(count_dict, headers=['Tenant Name', 'Count'])

        if option in (self.USER_OPTION_ALL, self.USER_OPTION_4):
            # The _filter_by_field_value method is designed to be called sequentially
            # by passing in the previous list to further filter it.
            filtered_data = self._filter_by_field_value('Lease Start Date',
                                                        operator.ge,
                                                        datetime(year=1999, month=6, day=1))
            filtered_data = self._filter_by_field_value('Lease Start Date',
                                                        operator.le,
                                                        datetime(year=2007, month=8, day=31),
                                                        filtered_data)

            # Reformat Lease Start Date column
            for i in filtered_data:
                i['Lease Start Date'] = parser.parse(i['Lease Start Date']).strftime('%d/%m/%Y')

            self.print_container(filtered_data)

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
        # Function to sort the data by field
        if self.data:
            if field in self.data[0].keys():
                sorted_list = sorted(self.data, key=lambda k: k[field])
                return sorted_list

        return self.data

    def _filter_by_field_value(self, field, oper, value_test, in_list=None):
        def compare_field(value_data):
            # Special behaviour for datetime fields
            if isinstance(value_test, datetime):
                # Make use of the handy datetime parser
                value_data = parser.parse(value_data)

            return oper(value_data, value_test)

        # Function to filter the data by field and value, infer field
        if in_list is None:
            in_list = self.data

        if in_list:
            if field in in_list[0].keys():
                # pylint: disable=unnecessary-comprehension
                # Justification: The task explicitly asks for a list comprehension to be used.
                filtered_list = [i for i in filter(lambda x: compare_field(x[field]), in_list)]
                return filtered_list

    def _count_occurrence_of_field(self, key_field):
        # Function to count the occurrences of the key_field and return a dict
        count_dict = {}
        if self.data:
            if key_field in self.data[0].keys():
                for i in self.data:
                    if i[key_field] in count_dict.keys():
                        # Already been added, update
                        count_dict[i[key_field]] += 1
                    else:
                        # Doesn't already exist so insert
                        count_dict.update({i[key_field]: 1})

        return count_dict

    @staticmethod
    def print_container(in_container, headers=None):
        """ Print human readable container output """
        # Different functionality for lists or dicts
        if isinstance(in_container, dict):
            print(tabulate([[k, v] for k, v in in_container.items()], headers=headers))
        elif isinstance(in_container, list):

            print(tabulate([[v for k, v in i.items()] for i in in_container],
                           headers=[k for k in in_container[0].keys()]))


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
