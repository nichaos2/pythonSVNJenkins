Final creation to test the steps to create an SVN in GIT with eclipse and Subclipse
Set up SVN for a project
First of all if Windows have the svn version 1.6; need to uprade to 1.7 Tortoise Eclipse with plugin Subclipse included. 
So we use Tortoise and Subclipse in Eclipse.

1.	create repository in git; copy the url 
  - create a readme file
2.	create a folder <svn_project> in the eclipse workspace, which includes the sub folders "branch" and "trunk"
3.	create the eclipse project in the trunk
4.	right-click on the <svn_project> and export using the url
5.	find the readme in the trunk folder and then right-click on it and then on checkout
**** The the <svn_project> will show a green check ****
4.	right-click on the <svn_project folder> and then on Svn Commit 
  - click on the folders you want to commit and press ok; attention empty folders are not supported and the procedure will stop.
5.	Finally, in eclipse right-click on the project Team > Share > SVN 
  - a message will show that the project is already shared appears; click ok.
6.	change something and then click on the outgoing changes and commit (notice that a * shows in the project)
