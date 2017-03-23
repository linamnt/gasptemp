##Instructions for Maintaining GASP Website:

#Preparation:

- Install Anaconda Python 3.x.x https://www.continuum.io/downloads  
- Install Git (and Bash if using windows): https://git-scm.com/downloads  
- Make a github account https://github.com/ and keep your credentials handy
- Previous owner will transfer you a folder with the appropriate make/config files
  - Transfer these to your computer
- Use Bash to do the following to get the site onto your laptop:
```
cd "/desired/folder/with/transferred/files"  
conda install pelican  
git clone https://github.com/linamnt/gasptemp.git    
```


##To Update Council Members page:

- Crop images to be all of equal size (e.g. 300x400px)  
- Save each as First_Name.jpg such that First_Name matches the pelicanconf.py listing  
- Transfer images to uoftgasp/content/images/  
- Open pelicanconf.py. EXECMEMBERS lists Executive Members, COUNCILMEMBERS lists council members. Each individual is formatted as (row_number, Role_Name, First_Name, Last_Name, Email).
  - e.g. (3, 'President', 'Jane', 'Smith', 'j23.smith@utoronto.ca')
- Each row can list at most three members, so the position of an individual in the chart is indicated by row_number, and order listed; hence, **there can be no more than three individuals with the same row_number.** Edit EXECMEMBERS and COUNCILMEMBERS accordingly.
- .jpg filenames MUST MATCH the First_Name listed in EXECMEMBERS

##Add New Posting:

- Postings are organized into categories listed under uoftgasp/content/category/
- Choose the category you would like to post in (i.e. Events, Gallery or General) and make a new .md file in that directory named like 2016-10-25-post-name.md or copy another pre-existing file and edit contents
- Open the file and edit using the following format:

```
Title: Post Title - no colons (':') can be used
Date: yyyy-mm-dd date of posting

Content using markdown.
```
- You do not need to put a title in the main content body as it will be generated automatically from the Title: yaml header.

### Some tips:
- add an image into the uoftgasp/content/posters folder, and in the post using `![alt]({filename}/posters/year/poster_name.png)`
- make use of headings using ## at the start of the line (the more #'s indicate the level of heading with one being the highest)
- bold using `**bolded word**` or italicize with `__emphasis__`
- link with `[displayed words](link)`

##To Change Sidebar for Upcoming Events:

- Open pelicanconf.py
- Under UPCOMING_EVENTS, remove any events that have passed, and add new ones in the format: ('Event Name', 'Date/Time', 'Location', 'post-title') where 'post-title' will be the lowercase version of event title joined by dashes (-). Each event bracket must be separated by a commma. Events with no posting can have a 'post-title' as ''.

## To Push Changes to Github and Website:
Using shell:

```
cd /path/to/uoftgasp/
# push changes to html
make html
#push to github for version control
make github
#enter username and password

#to sync server with local changes to html
bash upload.sh
```
Changes should be updated within 5min minutes, may require a refresh of browser.
