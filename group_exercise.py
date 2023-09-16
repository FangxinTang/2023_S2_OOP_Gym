from column_output import columnOutput # 3 params: dbData, cols, formatStr
# dbData is a list of tuples
# cols is a dictionary with column name as the key and data type as the item
# formatStr uses the following format, with one set of curly braces {} for each column.


class GroupExercise:

    def __init__(self, class_name, max_capacity):
        self.__class_name = class_name
        self.__max_capacity = max_capacity    
        self.__fee_amount = 0.0
        self.__trainer = None
        self.__participants = [] #people who enrolled
        self.__waitlist = []
        self.__checked_in_members = [] #people who attended

    # getter & setter:

    @property
    def class_name(self):
        return self.__class_name
    
    @class_name.setter
    def class_name(self, name):
        self.__class_name = name
    

    @property
    def max_capacity(self):
        return self.__max_capacity
    
    @max_capacity.setter
    def max_capacity(self, capacity):
        self.__max_capacity = capacity


    @property
    def fee_amount(self):
        return self.__fee_amount
    
    @fee_amount.setter
    def fee_amount(self, amount):
        try:
            # Check if the input amount is a number (integer or float)
            if not isinstance(amount, (int, float)):
                raise ValueError("Fee amount must be a number.")

            # covert the input amount variable to a float
            amount = float(amount)
            if amount < 0:
                raise ValueError("Fee amount cannot be negative.")
            elif amount != round(amount, 2):
                raise ValueError("Fee amount can have at most two decimal places.")
            
            # if pass the checks
            self.__fee_amount = amount
        except ValueError as e:
            print(f"Error: {e}")
    

    @property
    def trainer(self):
        return self.__trainer 
    
    @trainer.setter
    def trainer(self, trainer_obj):
        self.__trainer = trainer_obj


    @property
    def participants(self):
        return self.__participants
    
    @property
    def waitlist(self):
        return self.__waitlist
    
    @property
    def checked_in_members(self):
        return self.__checked_in_members


    # functions

    def enrol(self, member_obj):
        if len(self.__participants) < self.__max_capacity:
            self.__participants.append(member_obj)
            member_obj.enrol_in_class(self) # add the GroupExercise object to the member object's enrolled_classes list
        else:
            self.__waitlist.append(member_obj)


    def remove_participant(self, member_obj):
        if member_obj in self.__participants:
            self.__participants.remove(member_obj)
            member_obj.cancel_enrollment(self)
        else:
            print(f"{member_obj.full_name} is not enrolled in {self.__class_name} class.")


    def assign_trainer(self, trainer_obj):
        self.__trainer = trainer_obj
        trainer_obj.assigned_classes.append(self)
        return f"{trainer_obj.full_name} has been assigned as the trainer for {self.__class_name} class."


    def display_enrolled_members(self):
        # prepare the data for columnOutput(dbData,cols,formatStr) function
        enrolled_members_data = [
            (member_obj.full_name, member_obj.membership_number) for member_obj in self.__participants
        ]
        
        # define column names and their data types
        enrolled_members_cols = {
            'Member Name': str,
            'Membership Number': int,
        }

        # define the format string for the table
        format_str = "| {: <20} | {: >20} |"

        # print the table using the columnOutput function
        print(f"Enrolled Members for {self.__class_name} class:")
        columnOutput(enrolled_members_data, enrolled_members_cols, format_str)


    def participants_count(self):
        return len(self.__participants)
    

    def num_of_available_slots(self, participants_count):
        return self.__max_capacity - participants_count
    

    def total_payment(self):
        total = self.__fee_amount * len(self.__participants)
        return round(total, 2)
    

    def mark_attendance(self, member_obj):
        if member_obj not in self.__participants:
            print(f"{member_obj.full_name} is not enrolled in {self.__class_name} class.")
        else:
            if member_obj in self.__checked_in_members:
                print(f"{member_obj.full_name} is already marked for {self.__class_name} class.")
            else:
                self.checked_in_members.append(member_obj)
                print(f"{member_obj.full_name} has been marked for {self.__class_name} class.")


    def calculate_attendance_percentage(self):
        total_present = len(self.checked_in_members)
        total_enrolled = len(self.__participants)
        
        if total_enrolled == 0:
            return 0     
        
        attendance_percentage = round((total_present / total_enrolled) * 100, 1)
        return attendance_percentage
    
    
    def __str__(self):
        participants_str = ", ".join(member.full_name for member in self.__participants)
        return "Class Name: {} | Max Capacity: {} | Class Fee: {} | Trainer: {} | Participants: {}".format(
            self.__class_name,
            self.__max_capacity,
            self.__fee_amount,
            self.__trainer,
            participants_str
        )