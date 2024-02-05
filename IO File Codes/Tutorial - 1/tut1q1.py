outp = open("tut1q1.txt", "w")
for t in range(0, 26, 5):
	print("velocity at time = ", t, "(in minutes)", " is ", 4*(10**5) + 600*t )
	outp.write("velocity at time = "+ str(t) + "(in minutes)" + " is " + str( 4*(10**5) + 600*t)+"\n" )
outp.close()