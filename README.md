# Semester Two 2023 | COMP642 Advanced Programming | Invididual Assignment 1
-----------------------------------------
#### Marks: 93/100
-----------------------------------------
Design and implement a system to manage group exercise classes in a gym. The goal is to create a system that efficiently manages class enrolments, tracks attendance, and calculates payments for gym members participating in group exercise sessions.

### Required Classes

#### The GroupExercise Class:
• The GroupExercise class represents a single group exercise session at the gym.

• Attributes:
  o The name of the group exercise class.
  
  o The trainer assigned to conduct the class (an object of the Trainer class).
  
  o The maximum capacity of the class.
  
  o A list of participants (objects of the Member class) who have enrolled in the class.
  
  o A list of gym members who are on the waitlist for the class.
  
  o The fee amount for the class.
  
  o A list of gym members (objects of the Member class) who have checked-in for the class.
  
• Methods:
  o Enrols a gym member into the group exercise class. If the class is full, the member will be added to the waitlist.
  
  o Removes a gym member from the enrolled list.
  
  o Displays all gym members currently enrolled in the group exercise class.
  
  o Assigns a trainer to conduct the group exercise class.
  
  o Returns the number of gym members currently enrolled in the class.
  
  o Returns the number of available slots for enrolment in the class.
  o Sets the fee amount for the class.
  
  o Calculates and returns the total payment received for the group exercise class based on the number of enrolled members and the class fee.
  
  o Marks a gym member's attendance for the class.
  
  o Calculates and returns the attendance percentage for the class, representing the ratio of members checked-in to the total number of enrolled members.
  
#### The Member Class:
• The Member class represents a gym member.

• Attributes:
  o The full name of the gym member.
  
  o A unique membership number for the gym member.
  
  o A list of group exercise classes (objects of the GroupExercise class) in which the member is enrolled.
  
  
• Methods:
  o Books enrolment in a group exercise class. If the class is already full, the member will be added to the waitlist.
  
  o Cancels enrolment in a group exercise class.
  
  o Displays all booked group exercise classes.
  
  
#### The Trainer Class:
• The Trainer class represents a gym trainer.

• Attributes:
  o The full name of the trainer.
  
  o The specialisation or expertise of the trainer.
  
  o A list of group exercise classes (objects of the GroupExercise class) assigned to the trainer.
  
• Methods:
  o Displays the list of group exercise classes assigned to the trainer.
  
  o Adds a group exercise class to the list of classes assigned to the trainer.
  
