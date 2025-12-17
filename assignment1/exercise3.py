#full_name = input("Enter full name: ").strip()
#parts = full_name.split()
#first_name = parts[0]
#last_name = parts[-1]
#print("First Name: ", first_name)
#print("Last Name: ", last_name)

seconds = int(input("Enter time in seconds:"))
hours = seconds // 3600
seconds %= 3600

minutes = seconds // 60
seconds %= 60

print(hours, "hours", minutes, "minutes", seconds, "seconds")


