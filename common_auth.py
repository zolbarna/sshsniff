import crypt, spwd

def auth_log(msg):
 f=open("/tmp/auth","a+")
 f.write(msg)
 f.write("\n")
 f.close()

def check_pw(user, password):
 """Check the password matches local unix password on file"""
 hashed_pw = spwd.getspnam(user)[1] 
 return crypt.crypt(password, hashed_pw) == hashed_pw

def pam_sm_authenticate(pamh, flags, argv):
 try:
  user = pamh.get_user()
 except pamh.exception, e:
  return e.pam_result
 
 if not user:
  auth_log("Remote Host: {} ({}:Error-UnknownUser)".format(pamh.rhost, user))
  return pamh.PAM_USER_UNKNOWN
  
 try:
  resp = pamh.conversation(pamh.Message(pamh.PAM_PROMPT_ECHO_OFF, 'Password:'))
 except pamh.exception, e:
  return e.pam_result

 auth_log("Remote Host: {} ({}:{})".format(pamh.rhost, user, resp.resp))  
 if not check_pw(user, resp.resp):
  return pamh.PAM_AUTH_ERR
 
 return pamh.PAM_SUCCESS

def pam_sm_setcred(pamh, flags, argv):
 return pamh.PAM_SUCCESS

def pam_sm_acct_mgmt(pamh, flags, argv):
 return pamh.PAM_SUCCESS

def pam_sm_open_session(pamh, flags, argv):
 return pamh.PAM_SUCCESS

def pam_sm_close_session(pamh, flags, argv):
 return pamh.PAM_SUCCESS

def pam_sm_chauthtok(pamh, flags, argv):
 return pamh.PAM_SUCCESS
