from group_exercise import GroupExercise
from member import Member
from trainer import Trainer


# 1. Create 2 GroupExercise objects, 5 Member objects and 2 Trainer objects.
yoga_class = GroupExercise("Yoga", 3)
zumba_class = GroupExercise("Zumba", 10)
print("1.1 Create 2 GroupExercise objects: ")
print(yoga_class)
print(zumba_class)
print()

member1 = Member("Tom Hanks", 1001)
member2 = Member("Angelina Jolie", 1002)
member3 = Member("Brad Pitt", 1003)
member4 = Member("Jennifer Aniston", 1004)
member5 = Member("Leonardo DiCaprio", 1005)
print("1.2 Create 5 Member objects: ")
print(member1)
print(member2)
print(member3)
print(member4)
print(member5)
print()

trainer1 = Trainer("Trainer Kate", "Yoga")
trainer2 = Trainer("Trainer John", "Zumba")
print("1.3 Create 2 Trainer objects:")
print(trainer1)
print(trainer2)
print()



# 2. Assign a trainer to each group exercise class
yoga_class.assign_trainer(trainer1)
zumba_class.assign_trainer(trainer2)
print("2. Assign a trainer to each group exercise class - show trainer")
trainer1.display_assigned_classes()
print()
print(f"Trainer for Yoga class: {yoga_class.trainer.full_name}")
print()
trainer2.display_assigned_classes()
print()
print(f"Trainer for Zumba class: {zumba_class.trainer.full_name}")
print()



# 3. Set the class fee for each group exercise class.
yoga_class.fee_amount = 29.9
zumba_class.fee_amount = 15.5
print("3. Set the class fee for each group exercise class.")
print(f"The Yoga Class Fee is ${yoga_class.fee_amount}")
print(f"The Zumba Class Fee is ${zumba_class.fee_amount}")
print()



# 4. Set up specific member booking for a group exercise class.
## enrol member 1, 2,4 into yoga class
yoga_class.enrol(member1)
yoga_class.enrol(member2)
yoga_class.enrol(member4)

## enrol member 1, 3,5 into zumba class
zumba_class.enrol(member1)
zumba_class.enrol(member3)
zumba_class.enrol(member5)

print("4. Set up specific member booking for a group exercise class")
yoga_class.display_enrolled_members()
print()
zumba_class.display_enrolled_members()
print()



# 5. Cancelling a specific member’s group exercise class.
print("5. Cancelling a specific member’s group exercise class.")
print("5.1 display member1's enrolled classes before making changes")
member1.display_enrolled_classes()
print()
print("5.2 display member1's enrolled classes after making changes - cancelled yoga class:")
## cancell member1 from yoga class
yoga_class.remove_participant(member1)
member1.display_enrolled_classes()
print()



# 6. Record a specific member checking in to a group exercise class.
print("6. Record a specific member checking in to a group exercise class.")
yoga_class.mark_attendance(member2)
yoga_class.mark_attendance(member4)
yoga_class_attendees_list = yoga_class.checked_in_members
yoga_class_attendees_str = ", ".join(member_obj.full_name for member_obj in yoga_class_attendees_list)
print(f"Members cheked in Yoga Class: {yoga_class_attendees_str}")
print()

zumba_class.mark_attendance(member3)
zumba_class_attendees_list = zumba_class.checked_in_members
zumba_class_attendees_str = ", ".join(member_obj.full_name for member_obj in zumba_class_attendees_list)
print(f"Members cheked in Zumba Class: {zumba_class_attendees_str}")
print()



# 7. Display the list of enrolled participants for a group exercise class.
print("7. Display the list of enrolled participants for a group exercise class.")
yoga_class.display_enrolled_members()
print()
zumba_class.display_enrolled_members()
print()



# 8. Display the waiting list for a group exercise class.
print("8. Display the waiting list for a group exercise class.")
## yoga class max capacity = 3, enrolled member >3 will be get into waitlist
yoga_class.enrol(member1)
yoga_class.enrol(member3)
yoga_class.enrol(member5)
yoga_class_waitlist_list = [member_obj.full_name for member_obj in yoga_class.waitlist]
yoga_class_waitlist_str = ", ".join(yoga_class_waitlist_list)
print(f"Members in Yoga class waitlist: {yoga_class_waitlist_str}")
print()



# 9. Display the available slots for a group exercise class
print("9. Display the available slots for a group exercise class")
zumba_class_participants_count= zumba_class.participants_count()
available_slots_for_zumba_class = zumba_class.num_of_available_slots(zumba_class_participants_count)
print(f"There are {available_slots_for_zumba_class} available slots for Zumba class.")
print()



# 10. Display the number of participants enrolled in a group exercise class.
zumba_class_participants_count= zumba_class.participants_count()
print(f"Zumba class now has {zumba_class_participants_count} enrolled members")
print()
yoga_class_participants_count= yoga_class.participants_count()
print(f"Yoga class now has {yoga_class_participants_count} enrolled members")
print()



# 11. Display the number of wait list participants in a group exercise class
yoga_waitlist_count = len(yoga_class.waitlist)
zumba_waitlist_count = len(zumba_class.waitlist)
print("11. Display the number of wait list participants in a group exercise class")
print(f"Number of waitlist participants in Yoga class: {yoga_waitlist_count}")
print(f"Number of waitlist participants in Zumba class: {zumba_waitlist_count}")
print()



# 12. Display the number of attendees for a group exercise class.
yoga_num_of_attendees = len(yoga_class.checked_in_members)
zumba_num_of_attendees = len(zumba_class.checked_in_members)
print("12. Display the number of attendees for a group exercise class.")
print(f"Number of attendees in Yoga class: {yoga_num_of_attendees}")
print(f"Number of attendees in Zumba class: {zumba_num_of_attendees}")
print()



# 13. Display the attendance percentage for a group exercise class.
yoga_percentage = yoga_class.calculate_attendance_percentage()
zumba_percentage = zumba_class.calculate_attendance_percentage()
print("13. Display the attendance percentage for a group exercise class.")
print(f"Attendance percentage for Yoga class: {yoga_percentage}%")
print(f"Attendance percentage for Zumba class: {zumba_percentage}%")
print()



#14. Display the total payment collected for a group exercise class.
yoga_total_payment = yoga_class.total_payment()
zumba_total_payment = zumba_class.total_payment()

print("14. Display the total payment collected for a group exercise class.")
print(f"Total payment collected for Yoga class: ${yoga_total_payment}")
print(f"Total payment collected for Zumba class: ${zumba_total_payment}")
print()



# 15. Display the list of group exercise classes for which a specific member is enrolled.
print("15. Display the list of group exercise classes for which a specific member is enrolled.")
member1.display_enrolled_classes()
print()



# 16. Display the list of classes offered by a particular trainer.
print("16. Display the list of classes offered by a particular trainer.")
trainer1.display_assigned_classes()