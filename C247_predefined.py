for nonce in range(10, 100):
	equation = 25-5+nonce
	if equation == 24:
		print("Verified, ", nonce)
		break
	else:
		print("not verified")