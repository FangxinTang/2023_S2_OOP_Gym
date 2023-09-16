from column_output import columnOutput # 3 params: dbData, cols, formatStr
# dbData is a list of tuples
# cols is a dictionary with column name as the key and data type as the item
# formatStr uses the following format, with one set of curly braces {} for each column.


class Member:

    def __init__(self, full_name, membership_number):
        self.__full_name = full_name
        self.__membership_number = membership_number   
        self.__enrolled_classes = []

    # getter and setter

    @property
    def full_name(self):
        return self.__full_name
    
    @full_name.setter
    def full_name(self, new_full_name):
        self.__full_name = new_full_name


    @property
    def membership_number(self):
        return self.__membership_number
    
    @membership_number.setter
    def membership_number(self, number):
        self.__membership_number = number


    @property
    def enrolled_classes(self):
        return self.__enrolled_classes
    

    # functions

    def enrol_in_class(self, calss_obj):
        self.__enrolled_classes.append(calss_obj)


    def cancel_enrollment(self, calss_obj):
        self.__enrolled_classes.remove(calss_obj)

    
    def display_enrolled_classes(self):
        # prepare the data for columnOutput(dbData,cols,formatStr) function
        enrolled_classes_data = [
            (class_obj.class_name, class_obj.max_capacity) for class_obj in self.__enrolled_classes
        ]
        
        # define column names and their data types
        enrolled_classes_cols = {
            'Class Name': str,
            'Max Capacity': int
        }

        # define the format string for the table
        format_str = "| {: <20} | {: >20} |"

        # print the table using the columnOutput function
        print(f"{self.membership_number} {self.full_name} Enrolled Classes:")
        columnOutput(enrolled_classes_data, enrolled_classes_cols, format_str)

    
    def __str__(self):
        enrolled_classes_str = ", ".join(class_obj.class_name for class_obj in self.__enrolled_classes)
        return ("Name: {} | Membership Number: {} | Enrolled Classes: {}".format(
            self.full_name, 
            self.membership_number, 
            enrolled_classes_str)
        )
            


