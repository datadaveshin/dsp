# Install software on your computer


### Install [git](http://git-scm.com/).

You have it installed if you can run `git --version` at the command
line and get output like `git version 2.3.5`.


### Install [Anaconda](http://continuum.io/downloads).

There are two things you can verify to check your install.

First, from the command line, all of the following should start up
some kind of Python interpreter:

```bash
python
ipython
ipython notebook
spyder
```

Second, inside any of those Python interpreters, you should be able to
do all of these without error:

```python
import numpy
import scipy
import matplotlib
import pandas
import statsmodels
import sklearn
```

### Install [Homebrew](http://brew.sh/) on Mac

If you use a Mac, install Homebrew if you don't
have it yet. You could use Homebrew to manage your `git` and `python`
installs as well, but the methods given above are very good and more
cross-platform.

---

###Q1. Python Version 2 or 3

Did you install Python 2 or 3? Why?  

>>1) I have anaconda installations of both. I started with Python 2, but you can run both, so I went ahead and set up Python 3. 

>>2) I use Python 2 more often, as more packages are available and there are supposedly more users, and there is more Python 2 code out there. 
However, I am making an effort to remember to preserve compatability if possible, such as put my print statements in ()'s. 
Also, I have found that when following some tutorials, that Python 2 or 3 may be required, this includes using other people's iPython notebooks.
 
###Q2. Which Python Version Installed   

How can you check the version of Python installed if you happen to be on an unfamiliar computer?

>> If you type "python" the first line will have the Python version in it:
example:
>> $ `python`
>> Python 2.7.11 |Anaconda 2.5.0 (x86_64)| (default, Dec  6 2015, 18:57:58)

>> You can also type:
>> `python --version`

>> which is quicker is debatable.

