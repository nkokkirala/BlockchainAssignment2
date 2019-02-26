# Blockchain Assignment 2
By Nikhita Kokkirala

Instructions: 	
**There are three different files**

	1) Hashscript.py	
	2) test.py 
    3) Optimal.py 
 **IDE Used**	
 Pycharm 
 
 **HashScript.py**	
 *HashScript.py solves parts a-c of the assignment.*
 
 1) To run the file in your terminal and you would like to find the password of a simple or medium hacker hash: 
 	*		python Hashscript.py b7a875fc1ea228b9061041b7cec4bd3c52ab3ce3
 	*	Then the program will return *found if found, the original string password, number of attempts, and time taken*
 2) To run the file in your terminal and you would like to find the password of a leet hacker hash
 	*		python Hashscript.py b7a875fc1ea228b9061041b7cec4bd3c52ab3ce3 f0744d60dd500c92c0d37c16174cc58d3c4bdd8e
 	*	The first argument is the hash and the second argument is the salt term
 	* Then the program will return *the original string password, number of attempts, and time taken*
 	
 
 **test.py**	
 *test.py solves part d of the assignment*
 
 1) Iterates through two text files and finds whether a combination of two words with a space in between returns the  hash input(put in by user)
*		python test.py 34302959e138917ce9339c0b30ec50e650ce6b40
 
 **Optimal.py**
 1) A hash of all the words in the text file will be in a dictionary. 
 2) This will make cross-checking an input hash much more quickly as we just need to find the key. Practically O(1) run time.  
 *		python Optimal.py 801cdea58224c921c21fd2b183ff28ffa910ce31
 *	returns actual password string

**Solutions**
	
   	1) PART A: 
    Password was found
	Password is: letmein
	Number of attempts is: 16
	Time Taken: 0.000776052474976	
    
	2) PART B: 
    Password was found
	Password is: vjhtrhsvdctcegth
	Number of attempts is: 999968
	Time Taken: 2.9163339138
    
    3) PART C:
    slayerharib is ece4bb07f2580ed8b39aa52b7f7f918e43033ea1
	Number of attempts is: 545938
	Time Taken: 1.78987908363
    
    4) PART D: 
 	Works for all cases. Was not able to run program long enough to find required output
    5) Optimal:
    	Solutions are same as found for part A-C
    
 
    
	
