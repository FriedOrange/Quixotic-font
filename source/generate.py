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
CHARACTER_GAP = 200
VERTICAL_BALANCE_FACTOR = 0.5

SEGMENT_DEFINITIONS = {
	"space": "",
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
	"B": "abcgnil",
	"C": "afed",
	"D": "abcdil",
	"E": "afegnd",
	"F": "afegn",
	"G": "afedcgn",
	"H": "fegnbc",
	"I": "aeld",
	"J": "bcde",
	"K": "fegjn",
	"L": "fed",
	"M": "efhjbc",
	"N": "efimcb",
	"O": "abcdef",
	"P": "efabgn",
	"Q": "ebcdefm",
	"R": "efabgnm",
	"S": "afgncd",
	"T": "ail",
	"U": "fedcb",
	"V": "fekj",
	"W": "fekmcd",
	"X": "hjkm",
	"Y": "hjl",
	"Z": "ajkd",
}

def main():

	# initialise font
	font = fontforge.font()
	font.encoding = "UnicodeFull"
	font.em = EM_SIZE

	# calculate parameters
	width = int(CAP_HEIGHT * ASPECT_RATIO + CHARACTER_GAP)
	side_bearing = int(CHARACTER_GAP / 2)
	corner_gap = int(math.sqrt(SEGMENT_GAP**2 / 2))
	vertical_midpoint = CAP_HEIGHT * VERTICAL_BALANCE_FACTOR

	# draw unique segments
	font.createChar(-1, "segment-d")
	pen = font["segment-d"].glyphPen()
	pen.moveTo(side_bearing + SEGMENT_THICKNESS // 2 + corner_gap, SEGMENT_THICKNESS // 2)
	pen.lineTo(side_bearing + SEGMENT_THICKNESS + corner_gap, SEGMENT_THICKNESS)
	pen.lineTo(width - (side_bearing + SEGMENT_THICKNESS + corner_gap), SEGMENT_THICKNESS)
	pen.lineTo(width - (side_bearing + SEGMENT_THICKNESS // 2 + corner_gap), SEGMENT_THICKNESS // 2)
	pen.lineTo(width - (side_bearing + SEGMENT_THICKNESS + corner_gap), 0)
	pen.lineTo(side_bearing + SEGMENT_THICKNESS + corner_gap, 0)
	pen.closePath()
	pen = None
	font["segment-d"].width = width

	font.createChar(-1, "segment-e")
	pen = font["segment-e"].glyphPen()
	pen.moveTo(side_bearing + SEGMENT_THICKNESS // 2, SEGMENT_THICKNESS // 2 + corner_gap)
	pen.lineTo(side_bearing, SEGMENT_THICKNESS + corner_gap)
	pen.lineTo(side_bearing, vertical_midpoint - SEGMENT_THICKNESS // 2 - corner_gap)
	pen.lineTo(side_bearing + SEGMENT_THICKNESS // 2, vertical_midpoint - corner_gap)
	pen.lineTo(side_bearing + SEGMENT_THICKNESS, vertical_midpoint - SEGMENT_THICKNESS // 2 - corner_gap)
	pen.lineTo(side_bearing + SEGMENT_THICKNESS, SEGMENT_THICKNESS + corner_gap)
	pen.closePath()
	pen = None
	font["segment-e"].width = width

	font.createChar(-1, "segment-g")
	pen = font["segment-g"].glyphPen()
	pen.moveTo(0, SEGMENT_THICKNESS // 2)
	pen.lineTo(SEGMENT_THICKNESS // 2, SEGMENT_THICKNESS)
	pen.lineTo(width // 2 - SEGMENT_THICKNESS // 2 - corner_gap, SEGMENT_THICKNESS)
	pen.lineTo(width // 2 - corner_gap, SEGMENT_THICKNESS // 2)
	pen.lineTo(width // 2 - SEGMENT_THICKNESS // 2 -  corner_gap, 0)
	pen.lineTo(SEGMENT_THICKNESS // 2, 0)
	pen.closePath()
	pen = None
	font["segment-g"].width = width

	# create test glyph with all segments
	font.createChar(-1, "test")
	font["test"].addReference("segment-d", (1, 0, 0, 1, 0, 0))
	font["test"].addReference("segment-e", (1, 0, 0, 1, 0, 0))
	font["test"].width = width

	# finished
	font.save("source\\temp\\temp.sfd")

if __name__ == "__main__":
	main()