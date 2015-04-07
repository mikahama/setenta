

Setenta member database
=======================

This project is a database system for student association Setenta at the University of Helsinki. It allows members to log in and edit their profile, and administrators to see which members are active. Members have to update their profile once a year during the summer or their profiles will be deactivated.

Things to do after creating a fork
----------------------------------
Frist of all, rename the file `settings_template` to `settings.py` in `setenta/setenta/.` You'll need to edit, at least, the lines followed by #TODO comment.

Go to `setenta/setenta_members/` and rename `secret_keys_template` to `secret_keys.py`. You'll need to edit this file to enable reCaptcha.

After you have done all the previous steps, go to `setenta/` directory and run `python manage.py migrate`. You'll have to have Django and Python installed to run the command.

Now you should have the project ready to run. Use `python manage.py runserver` to test the application.

You can add admin users to the service by executing `python add_admin.py <username> <password>`. 

When you publish the application on your own web server, you should configure `cronjob.py` to run periodically. It will clear expired sessions and authorization keys.

License - GPL-3.0
-------
Copyright (C) 2015 Mika Hämäläinen

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program.  If not, see <http://www.gnu.org/licenses/>.

Questions?
-------

[http://mikakalevi.com/feedback/](http://mikakalevi.com/feedback/)



> Written with [StackEdit](https://stackedit.io/).