

young_driver_age_limit = 25
older_driver_age = 70
elderly_driver_age = 80

young_driver_premium_multiplier = 2
older_driver_premium_multiplier = 1.5
elderly_driver_premium_multiplier = 2
young_driver_experience_multiplier = 2
no_multiplier = 1


young_driver_experience = 2
older_driver_experience = 5

def agecheck (age, experience):

	# Assigns a premium multiplier depending on the age and experience of the driver

	multiplier = no_multiplier
	if age <= young_driver_age_limit:
		if experience <= young_driver_experience:
			multiplier = young_driver_premium_multiplier * young_driver_experience_multiplier
		else:
			multiplier = young_driver_premium_multiplier
	else:
		if age > older_driver_age and age <= elderly_driver_age:
			if experience <= older_driver_experience:
				multiplier = older_driver_premium_multiplier
			else:
				multiplier = no_multiplier
		else:
			if age > elderly_driver_age:
				multiplier = elderly_driver_premium_multiplier
	return multiplier


def agecheck_with_guards (age, experience):

	if age <= young_driver_age_limit and experience <= young_driver_experience: 
		return young_driver_premium_multiplier * young_driver_experience_multiplier
	if age <= young_driver_age_limit:
		return young_driver_premium_multiplier
	if (age > older_driver_age and age <= elderly_driver_age) and experience <= older_driver_experience:
		return older_driver_premium_multiplier
	if age > elderly_driver_age:
		return elderly_driver_premium_multiplier
	return no_multiplier





def main ():
	print ('Young driver with experience - should be ', young_driver_premium_multiplier, ' is ', agecheck_with_guards (19, 2.5))
	print ('Young driver with no experience- should be ', young_driver_premium_multiplier*young_driver_experience_multiplier, ' is ', agecheck_with_guards (19, 0.5))
	print ('Older driver with experience- should be 1', ' is ', agecheck_with_guards (72, 40))
	print ('Older driver without experience- should be ', older_driver_premium_multiplier, ' is ', agecheck_with_guards (73, 2))
	print ('Elderly driver- should be ', elderly_driver_premium_multiplier, ' is ', agecheck_with_guards (84, 30))
	print ('Middle-aged driver- should be ', 1, ' is ', agecheck_with_guards (45, 20))
	

if __name__ == '__main__':
	main()