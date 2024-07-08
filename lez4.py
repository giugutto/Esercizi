#/bin/python3
'''

     Create a function that takes a student's name and their scores in different subjects as input.
    The function calculates the average score and prints the student's name, average, and a message indicating whether the student passed the exam (average >= 60) or failed.
    Create a for loop to iterate over a list of students and scores, calling the function for each student.
'''




def average(name:str, sub_1:int, sub_2:int, sub_3:int) -> str:
	if (sub_1 + sub_2 + sub_3) / 3 > 60:
		return (f"{name}" + str((sub_1 + sub_2 + sub_3) / 3)) + (" you pass the exam")
	else:
		return (f"{name}" + str((sub_1 + sub_2 + sub_3) / 3)) + (" you didn't pass the exam")

print(average("Giuseppe",100,92,94))
