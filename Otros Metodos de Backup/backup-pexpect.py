import os
import pxssh
import pexpect
 
#DB BACKUP LOCAL IN LOCAL FOLDER
#BELOW LINE EXCUTE DUMP COMMAND SYNTAX(PG_DUMP -U {USER-NAME} {SOURCE_DB} -F {DUMPFILENAME.SQL})
#CHANGE UR APPROPIATE NAMES
 
os.system('pg_dump -U openerp test_001 -f dump_test.backup')
print "backup_successfull"
 
######################################################################
 
#BACKUP FILE SEND TO SERVER
#SCP(SECURED COPY) SYNTAX "SCP 'SOURCE-PATH' 'DESTINATION-PATH'"---CHANGE SOURCE-PATH AND DESTINATION-PATH
 
child = pexpect.spawn('scp /home/usr_name/Desktop/dump_test.backup  usr_name@123.123.123.123:///home/usr_name')
child.expect('.*password:*')
 
#CHANGE PASSWORD IN BELOW LINE
child.sendline('secret_passwd')
child.expect(pexpect.EOF)
#####################################################################
 
#CREATE A SERVER LOGIN AND RESTORE DB
s = pxssh.pxssh()
#CHANGE UR HOSTID, USERNAME, PASSWORD
if not s.login ('123.123.123.111', 'username', 'secret_passwd'):
    print "SSH session failed on login."
    print str(s)
else:
    print "SSH session login successful in 123.123.123.111"
   #BELOW LINE EXCUTE RESTORE COMMAND SYNTAX(PSQL -U {USER-NAME} -D {DESINTATION_DB}-F {DUMPFILENAME.SQL}})
   s.sendline('psql -U db_user -d dump_ssh -f dump_test.backup')
   s.prompt()
   print s.before     # PRINT EVERYTHING BEFORE THE PROMPT.
   s.logout()
 
#END OF CODE