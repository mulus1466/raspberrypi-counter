# Raspberry Pi counter and notifier
This is one of the projects that I'm working on right now.

The idea is to make your Raspberry Pi notify you with some
information every day/week/month.

In my case, the Raspberry will be monitoring the use of two
pumps, and will upload to the cloud an Exel file with some
information like how much time have they been on every day,
every week or so an average of how much have they been
working every day, and if we find the datasheet of the pumps,
how much energy have they used and how many water have they
pumped, among other things (or at least I hope so :D ), and
then send an e-mail to notify that the file has been uploaded
and maybe some of the information.

I'm trying to separate every part of the project in a different
file, so it will be easier for you to make changes or just
take the part that you need for your project. Also, I'm trying
to comment every program as best as I can (every line), so if
you are starting with Python you'll have an idea of what
every line does.

I'll put the schematics of my project here, so you can see
and hopefully use them in one of your projects. Right now
I'm working on the software, so please be patient.

# File overview
All the files has been tested on my machine, so it should
also work in yours :)

-   dependencies.txt : This file contains all the libraries needed
                     for this project.
-   email-notifier.py : This is the program containing (almost)
                      everything needed and related with the
		      e-mail notifications.
-   notification-message.txt : This file contains the message that
                             email-notifier.py will send.
-   seconds-to-hms.py : This program takes a number of seconds as
                      an argument and turns them into a list
		      containing the amount of seconds converted
		      to hours, minutes and seconds in a list
		      [hours, minutes, seconds]
