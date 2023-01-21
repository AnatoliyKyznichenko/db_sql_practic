import sqlite3
from PIL import Image
import io

with sqlite3.connect("users-avatar.db") as db:
	cursor = db.cursor()
	cursor.row_factory = sqlite3.Row

	cursor.execute("CREATE TABLE avatars(photo BLOB)")
	r = ('/home/hp/Загрузки/Terminator2poster.jpg')
	with open(r, "rb") as file:
		cursor.execute("INSERT INTO avatars VALUES(?)", [file.read()])

	data = cursor.execute("SELECT photo FROM avatars").fetchone()["photo"]
	img = Image.open(io.BytesIO(data))
	img.show()