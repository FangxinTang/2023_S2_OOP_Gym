from column_output import columnOutput
# dbData is a list of tuples
# cols is a dictionary with column name as the key and data type as the item
# formatStr uses the following format, with one set of curly braces {} for each column.


class Trainer:

    def __init__(self, full_name, expertise):
        self.__full_name = full_name
        self.__expertise = expertise
        self.__assigned_classes = []

    @property
    def full_name(self):
        return self.__full_name
    
    @full_name.setter
    def full_name(self, name):
        self.__full_name = name

    
    @property
    def expertise(self):
        return self.__expertise
    
    @expertise.setter
    def expertise(self, new_expertise):
        self.expertise = new_expertise
    

    @property
    def assigned_classes(self):
        return self.__assigned_classes
    
    @assigned_classes.setter
    def assigned_classes(self, class_obj_list):
        self.__assigned_classes = class_obj_list


    # functions
    
    def display_assigned_classes(self):
        # prepare for the dbData - list of tuple
        assigned_classes_data = []
        class_names_list = [class_obj.class_name for class_obj in self.__assigned_classes]
        class_names_str = ", ".join(class_names_list)
        data_tuple = (self.__full_name, class_names_str)
        assigned_classes_data.append(data_tuple)

        # define col names
        assigned_classes_cols = {
            'Name': str,
            'Assigned Classes': str
        }
    
        # define the format string for the table
        format_str = "|{: <20} | {: <100}|"

        print(f"{self.__full_name}'s Classes: ")
        columnOutput(assigned_classes_data, assigned_classes_cols, format_str)

    
    def add_class(self, class_obj):
        if class_obj in self.__assigned_classes:
            print(f"{class_obj.class_name} is already assigned to {self.__full_name}.")
        else:
            self.__assigned_classes.append(class_obj)
            print(f"{class_obj.class_name} has been assigned to {self.__full_name}.")

    
    def __str__(self):
        assigned_classes_str = ", ".join([class_obj.class_name for class_obj in self.__assigned_classes])
        return f"Name: {self.__full_name} | Expertise: {self.__expertise} | Assigned Classes: {assigned_classes_str}"
