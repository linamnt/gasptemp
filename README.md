##Instructions for Maintaining GASP Website:

#Preparation:

-Install Python https://www.continuum.io/downloads  
-Install Git (and Bash if using windows): Install Git https://git-scm.com/downloads  
-Make a github account https://github.com/  
-Use Bash to do the following to get the site onto your laptop: cd "desired/folder/" conda install pelican git clone https://github.com/linamnt/gasptemp.git  
-Install Filezilla and login with the information given by previous webmaster.  

##To Update Council Members page:

-Crop images to be all of equal size (e.g. 300x400px)  
-Save each as Full_First_Name.jpg sucht that Full_First_Name matches the pelicanconf.py listing  
-Transfer images to uoftgasp/content/images/  
-Open pelicanconf.py. EXECMEMBERS lists Executive Members, COUNCILMEMBERS lists council members. Each individual is formatted as (row_number, Role_Name, First_Name, Last_Name, Email). Each row can list at most three members, so the position of an individual in the chart is indicated by row_number, and order listed; hence, there can be no more than three individuals with the same row_number. Edit EXECMEMBERS and COUNCILMEMBERS accordingly. Photo .jpg filenames MUST MATCH the First_Name listed here

##Add New Posting:

-Postings are organized into categories listed under uoftgasp/content/category/  
-Choose the category you would like to post in and make a new text file in that directory named like 2016-10-25-post-name.m  
-Open the file and edit: 

```
Title: Post Title - no colons (':') can be used
Date: yyyy-mm-dd date of posting

Content using markdown.
```

Some tips:  
-add an image into the uoftgasp/content/posters folder, and in the post using `![alt]({filename}/posters/poster_name.png)`
-make use of headings using ## at the start of the line (the more #'s indicate the level of heading with one being the highest)
-bold using `**bolded word**` or italicize with `__emphasis__`
-link with `[displayed words](link)`

##To Change Sidebar for Upcoming Events:

-Open pelicanconf.py
-Under UPCOMING_EVENTS, remove any events that have passed, and add new ones in the format: ('Event Name', 'Date/Time', 'Location', 'post-title') where 'post-title' will be the lowercase version of event title joined by dashes (-). Each event bracket must be separated by a commma. Events with no posting can have a 'post-title' as ''.
## To Push Changes to Github and Website:
Using shell:

```
git status
git add .
git commit -m'write message for changes'
git push origin master
# provide username and password

bash upload.sh
```
Changes should be updated within 10-15 minutes.
