Complete the sequence of linux shell commands below if you are needed to complete this scenario -> Suppose you just cloned a repository that included one python file, my_first_file.py, and you now want to add a second file to your repository named my_second_file.py and push it to Github.com. (Note: create the file using the `touch` command)
		
		git clone git@github.com:my-name/my-imaginary-repo.git
		##complete the sequence
		cd my-imaginary-repo.git
		touch my_second_file.py
		git add .
		git commit -m "added new file"
		git push


Describe the workflow you adopted for this lab (i.e. did you develop on your VM and push/pull to get code to your RPi, did you edit files directly on your RPi, etc.).  Are there ways you might be more efficient in the next lab (i.e. learning a text-based editor so you can edit natively on the RPi, understanding Git commands better, etc.)?
	I started out editing in Sublime on my VM, pushing my changes to Git and pulling it down on my RPI to test. However, because I was making so many minor changes, it became tedious and a bit of a 
	hassle. So torwards the end, when I knew I was making minor changes that needed to be tested (especially since I was still learning how the grove-pi API worked), I edited natively with 'vim' in the RPI, before pushing to Git. I think in the next lab, I'll do a similar thing where I code directly on RPI if the changes I am making are minor and need testing. 

In the starter code, we added a 200 ms sleep. Suppose you needed to poll the ultrasonic ranger as fast as possible, so you removed the sleep function. Now, your code has just the function ultrasonicRead() inside a while loop. However, even though there are no other functions in the while loop, you notice there is a constant delay between each reading. Dig through the python library to find out why there is a constant delay. What is the delay amount? In addition, what communication protocol does the Raspberry Pi use to communicate with the Atmega328P on the GrovePi when it tries to read the ultrasonic ranger output using the `grovepi` python library?

	The function ultrasonicRead() is imported from 'grovepi', and in the function definition, there is a 60 ms delay, because the firmware has a time of 50ms. It uses the i2c protocol to communicate. s

