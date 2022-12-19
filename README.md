# Introduction
A background program that constantly checks your studying progress.
After you set a standard for yourself in how much work you should complete in how much time, this program will check your progress. 
If you fail to ever fail to meet your standards, the program will sound an alarm. You can pause the alarm anytime and doing so will make the program continue running. 
If you succeed to meet your standards, the program will congratulate you and display how many times you've succeded for this session. 

# Instructions
This program works under the assumption that you follow a certain framework, that framework having two fundamental components - note and time. 

This program will run as your background progress and read a file of your choice, ex. a notepad txt file. 
This program will read your file every λ minutes. Whenever it reads the file, it checks if you wrote a "divider". A divider is a string set by "---" on default.

The basis of assumption in such a framework is that the divider, *d*, is used as a "section" in recording progress or taking notes. 
Ex. in the case of a textbook - under the assumption that a textbook has *n* chapters that are each named *t*; and each such chapters have sections named *c*; the total number of sections are:
$$\sum_{k=1}^n |t_k|$$
where 
$$t_k = \sum_{z=1}^{|t_k|} c_z$$

The end of each such sections can be represented by a divider.

Lambda, divider, file_name, and alarm_sound are all adjustable parameters located at the top of the main function. 
A blank file called "note.txt" and a pixabay royalty-free alarm sound called "alarm.mp3" is provided as default. 
