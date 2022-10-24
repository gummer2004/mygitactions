#bad examples

cursor.execute("SELECT admin FROM users WHERE username = '" + username + '");
cursor.execute("SELECT admin FROM users WHERE username = '%s' % username);
cursor.execute("SELECT admin FROM users WHERE username = '{}'".format(username));
cursor.execute(f"SELECT admin FROM users WHERE username = '{username}'");


# Good Examples

cursor.execute("SELECT admin FROM users WHERE username = %s", (username, ));
cursor.execute("SELECT admin FROM users WHERE username = %(username)s", {'username': username});