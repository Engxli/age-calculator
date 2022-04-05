from datetime import date


def get_dob():
    # write code here
	year = input("Enter year of birth: ")
	month = str(input("Enter month of birth: "))
	day = str(input("Enter day of birth: "))
	month.replace("0", "")
	day.replace("0", "")
	return date(int(year), int(month), int(day))


def get_age(dob):
    # write code here
	today = date.today()
	return (int(str(today-dob).split(" ")[0])//365)


def main():
	# write code here
	dob = get_dob()
	if dob < date.today():
		print("You are " + str(get_age(dob)) + " years old.")
		return
	print("The date of birth is invalid!")


if __name__ == '__main__':
    main()
