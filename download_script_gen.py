# youtube-dl -o '4_Definitely, Maybe.%(ext)s' 0oK4VOUmOkc
# ffmpeg -i "4_Definitely, Maybe"* -vf "select=eq(pict_type\,I)" -vsync vfr -qscale:v 3 Temp_Shit/thumbnails-%03d.jpeg
import csv

csv.register_dialect('semicolon', delimiter=';', doublequote=True, quotechar='"', quoting=csv.QUOTE_NONNUMERIC, strict=True)
with open('final_data.ssv') as csvfile:
	reader = csv.DictReader(csvfile,dialect='semicolon')
	counter = 1
	for row in reader:
		print "youtube-dl -o '" + str(counter) + "_" + row['movie_name'] + ".%(ext)s' " + row['video_id']
		print "mkdir " + str(counter) + "_clips"
		print "ffmpeg -i \"" + str(counter) + "_" + row['movie_name'] + "\"* -vf \"select=eq(pict_type\,I)\" -vsync vfr -qscale:v 3 " + str(counter) + "_clips/thumbnails-%03d.jpeg"
		counter += 1