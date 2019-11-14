# VSCO.CO Downloader

## [Download](https://github.com/NicholasDawson/VSCO-Downloader/raw/master/VSCO%20Downloader.exe "Download")

## How to Use:
 1. Run VSCO Downloader.exe
 2. Enter a command

## Basic Examples:

##### All media downloads to the directory the application is running in. Media is saved in folders by username.

#### Download All Images/Videos from a profile:
```
<username> -i
OR
<username> --getImages
```

#### Download Journals from a profile:
```
<username> -j
OR
<username> --getJournal
```

#### Download Everything from a profile:
```
<username> -i -j
OR
<username> --getImages --getJournal
```

#### Download Images/Videos from multiple users (Bulk Downloading):
##### Don't forget to add a '.txt' to the end of a text file!

##### If you don't want to type the whole file path to the text file, ensure it is in the same directory or folder as your executable.
```
<usernames_list.txt> -m
OR
<usernames_list.txt> --multiple
```

#### Download Journals from multiple users (Bulk Downloading Journals):
```
<usernames_list.txt> -mj
OR
<usernames_list.txt> --multipleJournal
```

#### Download Everything from multiple users (Bulk Downloading Everything):
```
<usernames_list.txt> -a
OR
<usernames_list.txt> --all
```
## Parameters Reference Table

Option | Secondary Options | Description
------ | ------------- | -----------
--getImages | -i | Downloads all of the user's images/videos
--getJournal | -j | Downloads all of the images/videos in the user's journals and creates a directory for each journal
--multiple | -m | Downloads multiple user's images/videos
--multipleJournal | -mj | Downloads multiple user's journals
--all | -a | Downloads multiple users journals and images, will download journal if they have one

## Acknowledgments
The bulk of the code is taken directly from Mustafa Abdi and his vsco-scraper application.
https://github.com/mvabdi/vsco-scraper

I modified some of his code for usability and turned it into an executable.

## Questions/Suggestions
If you have any questions about the program and how it was made feel free to contact me at dunkindawson@gmail.com.
If you find any bugs or want to suggest an improvement feel free to email me or submit a pull request.

## Copyright &copy; 2019 Nicholas Dawson
