def name():
	"""
	Method ini digunakan untuk
	mengambil input dari keyboard.

	:return String
	"""
	return input('Masukkan Nama : ')

def greeting(x):
	"""
	Method ini digunakan untuk membuat sapaan
	kepada seseorang.

	:param x: String
	"""
	print("Halo "+ x)

nama = name()
greeting(nama)
