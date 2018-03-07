import math

#pythag baseball. winning pct = rs^2/(rs^2+ra^2)

def is_playoffs(rs, ra):
	num = (rs * rs)
	den = ((rs * rs) + (ra * ra))

	pythag = (((rs ** 2) / ((rs ** 2) + (ra ** 2) )) * (162))
	status = " "

	#division > 95, WC < 95 and > 90, WS > 105
	if pythag > 95 and pythag < 105:
		print("Congrats, you won the division!")
	elif pythag > 90 and pythag < 105:
		print("You made the WC game, you still have work to do")
	elif pythag <90 and pythag > 82:
		print("Try again next year, at least you had a winning record")
	elif pythag == 81:
		print(".500 aint so terrible, but its not very good!")
	elif pythag < 81:
		print("Good luck in the draft, you suck!!")
	elif pythag > 105:
		print("World Series Caliber. I like those odds!")

	return status

print(is_playoffs(199999999900000, 1))
print(is_playoffs(1, 300))
print(is_playoffs(100, 100))
print(is_playoffs(400, 320))
	
		
