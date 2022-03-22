# EIS_API_demo  
  
**This is just a testing case of EIS api.**

Mainly, it can save the file that uploaded by user from the server to a local computer. 
Then it execute EIS analysis (including modeling and fitting) automatically.
Finally, it will return a file that stores analysis solution to the user in .json file.

*Problem that I met*

This program can run normally with exit code 0 and corresponding url.
![image](https://user-images.githubusercontent.com/97633833/159564395-90da1faf-e594-43bf-b035-53ef99db0a0d.png)  
But when I used postman to 'POST' a .json file into that url, it raised an error.  
![image](https://user-images.githubusercontent.com/97633833/159564680-b56f3f3c-a878-438d-852e-034f51349249.png)  

If I copy these codes about EIS automatic analysis and paste it into a new python file, it runs successfully.  
![image](https://user-images.githubusercontent.com/97633833/159565316-1a20ba6f-297e-4e57-850d-658a1e8d544a.png)  

I've googled it without finding any helpful information. And the python used by PyCall in JULIA and that used here are the same.


