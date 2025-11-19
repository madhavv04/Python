# 1. Create a set courses with the names of 5 courses: "Python", "Java", "C++", "HTML", "SQL". 

set_courses = {"Python", "Java", "C++", "HTML", "SQL"}
# 2. Display all courses. 
print(set_courses)

# 3. Add a new course "Data Science" to the set. 
set_courses.add("Data Science")
print(set_courses)

# 4. Try adding "Python" again to the set (observe what happens to duplicates).
set_courses.add("Python")
print(set_courses)

# 5. Remove "HTML" from the set.
set_courses.remove("HTML") 
print(set_courses)

# 6. Check if "Java" exists in the set. Print the result. 

check = "Java"
for course in set_courses:
    if check in course:
        print(f"{check} is present in {course}")
    else :
        print(f"{check} is not present in {course}")
        
# 7. Create another set new_courses = {"ReactJS", "NodeJS", "SQL"} and perform union with your main set. 
set_courses2 = {"ReactJS", "NodeJS", "SQL"}
union_courses = set_courses.union(set_courses2)
print(union_courses)
# 8. Perform intersection of both sets to find the common courses. 

intersection_courses = set_courses.intersection(set_courses2)
print(intersection_courses)

# 9. Perform difference to find which courses are only in your main set but
# not in new_courses.

difference_courses = set_courses.difference(set_courses2)
print(difference_courses)

# 10. Clear the entire courses set after the semester ends. Display it to 
# confirm it is empty. 

set_courses.clear()
print(set_courses)