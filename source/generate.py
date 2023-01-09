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
	glyph_width = int(CAP_HEIGHT * ASPECT_RATIO)
	advance_width = int(glyph_width + CHARACTER_GAP)
	side_bearing = int(CHARACTER_GAP / 2)
	corner_gap = int(math.sqrt(SEGMENT_GAP**2 / 2))
	vertical_midpoint = int(CAP_HEIGHT * VERTICAL_BALANCE_FACTOR)
	horizontal_midpoint = advance_width // 2

	# draw unique segments
	font.createChar(-1, "segment-d")
	pen = font["segment-d"].glyphPen()
	pen.moveTo(side_bearing + SEGMENT_THICKNESS // 2 + corner_gap, SEGMENT_THICKNESS // 2)
	pen.lineTo(side_bearing + SEGMENT_THICKNESS + corner_gap, SEGMENT_THICKNESS)
	pen.lineTo(advance_width - (side_bearing + SEGMENT_THICKNESS + corner_gap), SEGMENT_THICKNESS)
	pen.lineTo(advance_width - (side_bearing + SEGMENT_THICKNESS // 2 + corner_gap), SEGMENT_THICKNESS // 2)
	pen.lineTo(advance_width - (side_bearing + SEGMENT_THICKNESS + corner_gap), 0)
	pen.lineTo(side_bearing + SEGMENT_THICKNESS + corner_gap, 0)
	pen.closePath()
	pen = None
	font["segment-d"].width = advance_width

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
	font["segment-e"].width = advance_width

	font.createChar(-1, "segment-g")
	pen = font["segment-g"].glyphPen()
	pen.moveTo(side_bearing + SEGMENT_THICKNESS // 2 + corner_gap, vertical_midpoint)
	pen.lineTo(side_bearing + SEGMENT_THICKNESS + corner_gap, vertical_midpoint + SEGMENT_THICKNESS // 2)
	pen.lineTo(horizontal_midpoint - SEGMENT_THICKNESS // 2 - corner_gap, vertical_midpoint + SEGMENT_THICKNESS // 2)
	pen.lineTo(horizontal_midpoint - corner_gap, vertical_midpoint)
	pen.lineTo(horizontal_midpoint - SEGMENT_THICKNESS // 2 - corner_gap, vertical_midpoint - SEGMENT_THICKNESS // 2)
	pen.lineTo(side_bearing + SEGMENT_THICKNESS + corner_gap, vertical_midpoint - SEGMENT_THICKNESS // 2)
	pen.closePath()
	pen = None
	font["segment-g"].width = advance_width

	font.createChar(-1, "segment-l")
	pen = font["segment-l"].glyphPen()
	pen.moveTo(horizontal_midpoint - SEGMENT_THICKNESS // 2, SEGMENT_THICKNESS + SEGMENT_GAP)
	pen.lineTo(horizontal_midpoint - SEGMENT_THICKNESS // 2, vertical_midpoint - SEGMENT_THICKNESS // 2 - corner_gap)
	pen.lineTo(horizontal_midpoint, vertical_midpoint - corner_gap)
	pen.lineTo(horizontal_midpoint + SEGMENT_THICKNESS // 2, vertical_midpoint - SEGMENT_THICKNESS // 2 - corner_gap)
	pen.lineTo(horizontal_midpoint + SEGMENT_THICKNESS // 2, SEGMENT_THICKNESS + SEGMENT_GAP)
	pen.closePath()
	pen = None
	font["segment-l"].width = advance_width

	# add other segments with references
	font.createChar(-1, "segment-a")
	font["segment-a"].addReference("segment-d", (1, 0, 0, 1, 0, CAP_HEIGHT - SEGMENT_THICKNESS))
	font.createChar(-1, "segment-b")
	font["segment-b"].addReference("segment-e", (1, 0, 0, 1, glyph_width - SEGMENT_THICKNESS, vertical_midpoint - SEGMENT_THICKNESS // 2))
	font.createChar(-1, "segment-c")
	font["segment-b"].addReference("segment-e", (1, 0, 0, 1, glyph_width - SEGMENT_THICKNESS, 0))
	font.createChar(-1, "segment-f")
	font["segment-f"].addReference("segment-e", (1, 0, 0, 1, 0, vertical_midpoint - SEGMENT_THICKNESS // 2))
	font.createChar(-1, "segment-h")
	font.createChar(-1, "segment-i")
	font["segment-i"].addReference("segment-l", (1, 0, 0, -1, 0, CAP_HEIGHT))
	font["segment-i"].unlinkRef()
	font["segment-i"].correctDirection()
	font.createChar(-1, "segment-j")
	font.createChar(-1, "segment-m")
	font.createChar(-1, "segment-n")
	font["segment-n"].addReference("segment-g", (1, 0, 0, 1, glyph_width // 2 - SEGMENT_THICKNESS // 2, 0))

	# create test glyph with all segments
	font.createChar(-1, "test")
	font["test"].addReference("segment-a", (1, 0, 0, 1, 0, 0))
	font["test"].addReference("segment-b", (1, 0, 0, 1, 0, 0))
	font["test"].addReference("segment-c", (1, 0, 0, 1, 0, 0))
	font["test"].addReference("segment-d", (1, 0, 0, 1, 0, 0))
	font["test"].addReference("segment-e", (1, 0, 0, 1, 0, 0))
	font["test"].addReference("segment-f", (1, 0, 0, 1, 0, 0))
	font["test"].addReference("segment-g", (1, 0, 0, 1, 0, 0))
	font["test"].addReference("segment-h", (1, 0, 0, 1, 0, 0))
	font["test"].addReference("segment-i", (1, 0, 0, 1, 0, 0))
	font["test"].addReference("segment-j", (1, 0, 0, 1, 0, 0))
	# font["test"].addReference("segment-k", (1, 0, 0, 1, 0, 0))
	font["test"].addReference("segment-l", (1, 0, 0, 1, 0, 0))
	font["test"].addReference("segment-m", (1, 0, 0, 1, 0, 0))
	font["test"].addReference("segment-n", (1, 0, 0, 1, 0, 0))
	font["test"].width = advance_width

	# finished
	font.save("source\\temp\\temp.sfd")

if __name__ == "__main__":
	main()