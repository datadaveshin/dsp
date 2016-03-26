# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.

---

###Q1.  Cheat Sheet of Commands  

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

> > 1) `mkdir -p dirname1/dirname2/dirname3`

> > Allows you to make intemediate directories that have yet to be created.

> > 2) `mkdir "this is a directory with spaces"` or
> > `cd "this is a directory with spaces"`

> > Using quotes allows you to make directories with spaces,
> > though I have no idea why you would want to ever do this.
> > Same for cd to change directories to directories with spaces, 
> > this allows to not have to use escape characters.

> > 3) `ls -R` 

> > See what's in the directory and its subdirectories recursively.
 
> > 4) `pushd` and `popd`

> > `pushd` adds a directory to a stack, then moves to that directory.
> > `popd` pops the highest directory in the stack, then moves to that directory.
> > `pushd` without an argument will go back and forth betweent the top two items 
> > in the stack.
> > `dirs -c` will clear the stack (useful if a directory no longer exists).

> > 5) `touch` for bash shell

> > Makes an empty file, sometimes useful for scripts.

> > 6) using `spacebar` for more/less commands

> > The spacebar will page down similar to `<ctrl>F`.

> > 7) `cat < filename`

> > Supply input to the preceding command.  
> > Likewise `>` will output to a file.

> > 8) `>>`

> > I use this in scripts to append to files,
> > never used it on the command line. 

> > 9) `find . -name "*.txt" -print | less`
> > `find . -name "*.txt" -print` 
> > `find . -name "*.txt"`

> > `find` is used to search for files. 
> > Note, it appears that the `-print` here is not needed on my machine,
> > so the third example is likely the most useful.

> > The dot is to start at the current directory, but you can use specify another:
> > `find /home/user3131/ -name "log.???"`

> > 10) `cat > file`
> >     `text`
> >     `text`
> >     `text`
> >     `<ctrl>D`

> > Way to insert text into a file.
> > I would probably use vi though.

> > 11) `grep -i` 
> > Flag will ignore case.

> > `grep -A 2`
> > `-A` flag will show x lines after. 

> > `grep -B 3`
> > `-B` flag will show x lines before.

> > `grep -C 2`
> > `-C` flag will show around a number.

> > `ls -lrt | grep -o 'drwxr-xr-x'`
> > `-o` flag only prints the matching part within the lines.

> > `grep -r`
> > Will work recursively through subdirectories.

> > `grep -x`
> > Entire line must match the input string or re.

> > `grep -z` or `zgrep`
> > Acts on compressed files.

> > 12) `apropos <search term>`

> > `apropos` seems to be a pre-internet search engine help search function to match you 
> > with an appropriate command.
> > Likely hard to remember due to infrequency of use.

> > 13) `env`
> > Show's what's in my environment.

> > 14) `export TESTING='1,2,3'`
> > `echo $TESTING`

> > How to set a an env variable in the bash shell.

> > 15) $ `export TESTING="bada bada bing"`
> > $ `echo $TESTING`
> > bada bada bing
> > $ `unset TESTING`
> > $ `echo $TESTING`

> > You have to 'unset' env variables to get rid of them.

> > 16) `cd -`

> > Changes directory to previous directory stored as env variable OLDPWD.

---

###Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

> > `ls` outputs to stdout the standard "view" of a list of all contents of a directory.

> > `ls -a` is ls but shows hidden files (those that are preceded by dot).

> > `ls -l` lists in one column, by alphanumeric order of file/directory names,
> > it will also show the permissions, owner, timestamps, filesizes...

> > `ls -lh` same as ls -l except for filesizes, uses strings B, KB, MB, etc.
> > to reduce having huge number of numeric characters.

> > `ls -lah` same as above but shows hidden files.

> > `ls -t` same as ls, but sorts by time, newest files first.

> > `ls -Glp` Here, the 'G' changes the output to color, 
> > where 'regular' files remain the same color, 
> > but hidden files, executable files, directories will be 
> > colored differently. The 'l' we have discussed already, 
> > output will be in a line. The 'p' adds a '/' after the directories. 

---

###Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> > The first two I list are the ones I use the most. 
> > (I think this will hold true after reading the article), 
> > then some new combos that may be useful:

> > 1) `ls -lrt` or `ls -lrtFG` 

> > This outputs in single column format with the most recent file at the bottom
> > so that it is near your prompt.

> > 2) `ls -al` 

> > I prefer the single column format most of the time, and hidden files will be up at the top.

> > 3) `ls -1`

> > Just print the file names on one line... 
> > equivalent to and better than 
> > `ls -l | awk '{print $9}'`
> > because the first blank is now eliminated!

> > 4) `ls -m`

> > Lists files in a comma-space delimited list.
> > `ls -m | sed 's/ //g'` could be useful for scripting and making .csv files

> > 5) `ls -d` 
> > lists only directories, but doesn't work on the machine I'm using,
> > despite being in man ls.

---

###Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > xargs takes in input (x number of arguments) from stdin, 
> > then echo's it back,
> > this in conjunction with other commands can help your scripts

> > Example:
> > The script below will will copy your current path to the clipboard, you can then go to another target terminal window and paste with \<cmd\>V and you will then have changed to the same directory as the original directory in the source terminal window that you ran the command in:

> > `#!/bin/sh`

> > `echo cd \``pwd | xargs\`` | xargs | pbcopy`
