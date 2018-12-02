month_names = [ "January", "February", "March", "April", "May", "June" ]

num_days = [ 31, 28, 31, 30, 31, 30 ]

for i in range(len(num_days)):
		print("Month", i+1, "is", month_names[i], ". It contains", num_days[i], "days.")


month_names.append("July")
month_names.append("August")
num_days.append(31)
num_days.append(31)

for i in range(len(num_days)):
		print("Month", i+1, "is", month_names[i], ". It contains", num_days[i], "days.")

