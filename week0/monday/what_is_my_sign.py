def what_is_my_sign(day, month):
    signs = [
    	(121, "Aquarius"),
    	(220, "Pisces"),
    	(321, "Aries"),
    	(421, "Taurus"),
    	(522, "Gemini"),
    	(622, "Cancer"),
    	(723, "Leo"),
    	(823, "Virgo"),
    	(924, "Libra"),
    	(1024, "Scorpio"),
    	(1123, "Sagittarius"),
    	(1222, "Capricorn")
    ]

    # sign = month * 10 + day
    for i, sign in enumerate(signs):
    	if sign[0] // 100 == month:
    		if sign[0] % 100 >= day:
    			return signs[i - 1][1]
    		else:
    			return signs[i][1]
