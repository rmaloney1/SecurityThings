def CI(text):
	freqs = {}
	for let in text:
		if let not in freqs:
			freqs[let] = 1
		else:
			freqs[let] += 1
	numerator = 0
	for let in freqs:
		numerator += freqs[let] * (freqs[let] - 1)
	denominator = len(text) * (len(text) - 1)

	return 26 * numerator / denominator

if __name__ == "__main__":
	text = input()
	text = text.replace(" ", "")
	text = text.replace("\n", "")
	print(CI(text))