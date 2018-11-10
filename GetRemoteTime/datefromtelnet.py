import telnetlib

USER = "root"
PASS = "antslq"
# HOST = "10.64.31.21"
COMMAND = "date"
HOSTRANGE = ["10.64.31.21", "10.64.31.22"]
HOSTEXCEPT = []

def realhost(host):
	if host in HOSTEXCEPT:
		return False
	return True

def getdatefromsinglehost(tn, host):
	try:
		tn.open(host)
	except:
		return "Cannot open host %s" % host
	tn.read_until("login:")
	tn.write(USER + '\n')
	tn.read_until("Password:")
	tn.write(PASS + '\n')
	tn.write(COMMAND + '\n')
	tn.write("exit\n")
	return tn.read_all()



def getdatefromtelnet():
	dateres = ""
	tn = telnetlib.Telnet()
	if len(HOSTRANGE) == 1:
		dateres = getdatefromsinglehost(tn, HOSTRANGE[0])
	elif len(HOSTRANGE) == 2:
		hosthead = HOSTRANGE[0][: HOSTRANGE[0].rfind('.') + 1]
		first = int(HOSTRANGE[0][HOSTRANGE[0].rfind('.') + 1:])
		last = int(HOSTRANGE[1][HOSTRANGE[1].rfind('.') + 1:])
		for number in range(first, last + 1):
			host = hosthead + str(number)
			dateres = dateres + getdatefromsinglehost(tn, host)
	else:
		print "wrong host range"
	tn.close()
	del tn
	print dateres

if __name__ == '__main__':
	getdatefromtelnet()