# Text_Generation_Based_On_Head_Movement

Generate text-letters on the console with the help of head movements.

##Description:

Before the program maps head movements to text entry, it first simulates the average head positions for a user. 
It is crucial to simulate this at the beginning of the execution of program since the head movement - [left| right | up | down] would be different for distinct users.
Average of head positions is calculated over 19 consecutive frames. Couple of initial frames are skipped so that User could relocate to a proper head position. 
>Note: During simulation of head movement user is required to shift the head towards the direction mentioned in the top left corner of the  window 

There are 5 basic head position for the successful execution of the program. This head positions and there explanation is as follows:
```
1. Normal: 
    This is the base position or say the most comfortable position. This position describes the user's basic head position when (s)he faces in the straight direction.
During simulation of head positions, user is required face straight or stay relaxed, so that system could calibrate user's head position for the base position.
During the execution of the program users head movement is shown in the top left corner of the window. 
After every selection that is made, user is required to return back to the normal position, so that next selection could be made.

2.Left: 
    During simulation of head positions, user is required to shift the head towards left, so that system could calibrate user's head position for the left direction
During the execution of the program user's head movement is shown in the top left corner of the window. Based on Left head movement, the selection available in the left direction is chosen. 
Once the selection has been made, users choice is highlighed unless its an unit value.  
After the selection has been made, user is required to move back to Normal position.

3.Right: 
    During simulation of head positions, user is required to shift the head towards right direction, so that system could calibrate user's head position for the right direction.
During the execution of the program users head movement is shown in the top left corner of the window. Based on Right head movement, the selection available in the right direction is chosen.  
Once the selection has been made, users choice is highlighed unless its an unit value.  
After the selection has been made, user is required to move back to Normal position.

4.Down: 
    During simulation of head positions, user is required to shift the head towards downward direction, so that system could calibrate user's head position for the downward direction.
During the execution of the program users head movement is shown in the top left corner of the window. Based on Down head movement, the selection available in the downward direction is chosen.  
Once the selection has been made, users choice is highlighed unless its an unit value.  
After the selection has been made, user is required to move back to Normal position.

5.Up: 
    During simulation of head positions, user is required to shift the head towards upward direction, so that system could calibrate user's head position for the upward direction.
During the execution of the program users head movement is shown in the top left corner of the window. Based on Up head movement, the selection available in the Upward direction is chosen.  
Once the selection has been made, users choice is highlighed unless its an unit value.  
After the selection has been made, user is required to move back to Normal position.

```
Once the program has calibrated head positions, A new window appears depicting the available options for the user to select from. Once the selection is made, the chosen option is highlighted for the ease of understanding the current choice. User is further required to make the selection unless the option selected maps to a final character. 
After the selection is made with the help of head movement, user is required to return back to the normal / base position, the same message is written on the top left corner of the window. 

Following command is required to be passed in order to execute the program.
>python Directory_Path_to_Text_Generation_Based_On_Head_Movement/GenerateTextFromHeadMovement.py

##Dependencies:
1. python 2.7
2. openCV 3.0 library
3. numpy library
4. math library
5. Face Dectection Using haarcascade_frontalface_default.xml. _File is distributed from Intel, kindly follow the license agreement before using and redistributing the file_

>At any point during the execution of system, a user could Hit ESC or q or Q to quit the program.


-Gaurav