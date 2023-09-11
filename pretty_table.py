from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Student Name", ["John", "Sam", "Peter", "Harry"])
table.align["Student Name"] = "l"
table.add_column("Student ID", ["101", "102", "103", "104"])
# table.align["Student ID"] = "r"
print(table)
