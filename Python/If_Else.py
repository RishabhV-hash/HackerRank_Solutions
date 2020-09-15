"""
if __name__ == '__main__'
Python uses this to determine whether the script is being run as the main script or being run as a module. 
So you can define different actions for your script based on the condition it is run.
"""
if __name__ == '__main__':
    n = int(input())
    if n % 2 != 0 or n > 5 and n < 21 :
        print("Weird")
    else: 
        print("Not Weird")