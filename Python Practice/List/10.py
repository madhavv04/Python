#  Clear the entire students list after the batch is finished. Display it to confirm it is empty.

students = ["Shubham","Vidhi","Zeel","Madhav","Dharmil"]
new_batch = ["Arjun", "Meera"]

students.extend(new_batch)
print(students)

students.clear()
print(students)