# Remove the student with roll number 103 from the dictionary. 



dict = [{"roll" : 101,"Name" : "Alice"},
        {"roll" : 102,"Name" : "Peter"},
        {"roll" : 103,"Name" : "Bob"},
        {"roll" : 104,"Name" : "Sneha"}
        ]


dict.remove({"roll":103 , "Name" : "Bob"})
print(dict)