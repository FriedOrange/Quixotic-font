import sys
import math
import fontforge

EM_SIZE = 1000
CAP_HEIGHT = 800
# ASPECT_RATIO = sys.argv[1]
ASPECT_RATIO = -(1 - math.sqrt(5)) / 2
# SEGMENT_THICKNESS = sys.argv[2]
SEGMENT_THICKNESS = 80
SEGMENT_GAP = 10

SEGMENT_DEFINITIONS = {
	"zero": "abcdef",
	"one": "bc",
	"two": "abgned",
	"three": "abgncd",
	"four": "fghbc",
	"five": "afgncd",
	"six": "afedcgn",
	"seven": "abc",
	"eight": "abcdefgh",
	"nine": "gnfabcd",
	"A": "abcefgn",
	"B": "",
	"C": "",
	"D": "",
	"E": "",
	"F": "",
	"G": "",
	"H": "",
	"I": "",
	"J": "",
	"K": "",
	"L": "",
	"M": "",
	"N": "",
	"O": "",
	"P": "",
	"Q": "",
	"R": "",
	"S": "",
	"T": "",
	"U": "",
	"V": "",
	"W": "",
	"X": "",
	"Y": "",
	"Z": "",
	"": "",
	"": "",
}

def main():

	# initialise font
	font = fontforge.font()
	font.encoding = "UnicodeFull"
	font.em = EM_SIZE

if __name__ == "__main__":
	main()