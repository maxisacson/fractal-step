#from termcolor import colored


def main():
	def pascal(n):
		pas = [[1], [1, 1], [1, 2, 1]]
		for y in range(n-3):
			nth = [1]
			last = pas[len(pas)-1]
			for x in range(len(last)-1):
				nth.append(last[x]+last[x+1])
			nth.append(1)
			pas.append(nth)
		return pas

	def even_odd(pascal):
		for p in pascal:
			for x, b in enumerate(p):
				if not b % 2:
					p[x] = "#"
				else:
					p[x] = "."
		return pascal
	N = 100
	sier = even_odd(pascal(N))
	for s in sier:
		print(" ".join(s))
if __name__ == "__main__":
	main()
