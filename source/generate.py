import sys
import math
import fontforge

# constants
EM_SIZE = 1000
CAP_HEIGHT = 800
# ASPECT_RATIO = -(1 - math.sqrt(5)) / 2
ASPECT_RATIO = 0.5
SEGMENT_THICKNESS = int(sys.argv[1]) # 56 good for 14 segment
SEGMENT_GAP = 20
CHARACTER_GAP = 200
SEGMENT_COUNT = int(sys.argv[2])

# read segment definitions (CSV)
with open(sys.argv[3]) as csv_file:
	segment_definitions = []
	for line in csv_file:
		segment_definitions.append(line.strip().split(","))

# initialise font
font = fontforge.font()
font.encoding = "UnicodeFull"
font.em = EM_SIZE

# calculate parameters
glyph_width = round(CAP_HEIGHT * ASPECT_RATIO)
advance_width = round(glyph_width + CHARACTER_GAP)
side_bearing = round(CHARACTER_GAP / 2)
corner_gap = round(math.sqrt(SEGMENT_GAP**2 / 2))
vertical_midpoint = round(CAP_HEIGHT / 2)
horizontal_midpoint = round(advance_width / 2)
half_thickness = round(SEGMENT_THICKNESS / 2)
quadrant_w = glyph_width / 2 - 1.5 * SEGMENT_THICKNESS - 2 * SEGMENT_GAP
quadrant_h = vertical_midpoint - 1.5 * SEGMENT_THICKNESS - 2 * SEGMENT_GAP
# diagonal_x_offset = round(SEGMENT_THICKNESS * 0.2 + SEGMENT_THICKNESS * ASPECT_RATIO * 0.2) # perfect for golden ratio width
# diagonal_y_offset = round(SEGMENT_THICKNESS * 4 * (1 - ASPECT_RATIO)) # perfect for golden ratio width
# diagonal_x_offset = round(SEGMENT_THICKNESS * 0.1 + SEGMENT_THICKNESS * ASPECT_RATIO * 0.3)
diagonal_x_offset = SEGMENT_GAP // 2
diagonal_y_offset = round(SEGMENT_THICKNESS * 4.1 * (1 - ASPECT_RATIO))

# draw .notdef
font.createChar(-1, ".notdef")
pen = font[".notdef"].glyphPen()
pen.moveTo(side_bearing, 0)
pen.lineTo(side_bearing, CAP_HEIGHT)
pen.lineTo(side_bearing + glyph_width, CAP_HEIGHT)
pen.lineTo(side_bearing + glyph_width, 0)
pen.closePath()
pen.moveTo(side_bearing + SEGMENT_THICKNESS, SEGMENT_THICKNESS)
pen.lineTo(side_bearing + glyph_width - SEGMENT_THICKNESS, SEGMENT_THICKNESS)
pen.lineTo(side_bearing + glyph_width - SEGMENT_THICKNESS, CAP_HEIGHT - SEGMENT_THICKNESS)
pen.lineTo(side_bearing + SEGMENT_THICKNESS, CAP_HEIGHT - SEGMENT_THICKNESS)
pen.closePath()
pen = None
font[".notdef"].width = advance_width

# draw unique segments
font.createChar(-1, "segment-d")
pen = font["segment-d"].glyphPen()
pen.moveTo(side_bearing + half_thickness + corner_gap, half_thickness)
pen.lineTo(side_bearing + SEGMENT_THICKNESS + corner_gap, SEGMENT_THICKNESS)
if SEGMENT_COUNT == 16:
	pen.lineTo(horizontal_midpoint - SEGMENT_GAP // 2, SEGMENT_THICKNESS)
	pen.lineTo(horizontal_midpoint - SEGMENT_GAP // 2, 0)
else:
	pen.lineTo(advance_width - (side_bearing + SEGMENT_THICKNESS + corner_gap), SEGMENT_THICKNESS)
	pen.lineTo(advance_width - (side_bearing + half_thickness + corner_gap), half_thickness)
	pen.lineTo(advance_width - (side_bearing + SEGMENT_THICKNESS + corner_gap), 0)
pen.lineTo(side_bearing + SEGMENT_THICKNESS + corner_gap, 0)
pen.closePath()
pen = None

font.createChar(-1, "segment-e")
pen = font["segment-e"].glyphPen()
pen.moveTo(side_bearing + half_thickness, half_thickness + corner_gap)
pen.lineTo(side_bearing, SEGMENT_THICKNESS + corner_gap)
pen.lineTo(side_bearing, vertical_midpoint - half_thickness - corner_gap)
pen.lineTo(side_bearing + half_thickness, vertical_midpoint - corner_gap)
pen.lineTo(side_bearing + SEGMENT_THICKNESS, vertical_midpoint - half_thickness - corner_gap)
pen.lineTo(side_bearing + SEGMENT_THICKNESS, SEGMENT_THICKNESS + corner_gap)
pen.closePath()
pen = None

font.createChar(-1, "segment-g")
pen = font["segment-g"].glyphPen()
if SEGMENT_COUNT == 7:
	pass
else:
	pen.moveTo(side_bearing + half_thickness + corner_gap, vertical_midpoint)
	pen.lineTo(side_bearing + SEGMENT_THICKNESS + corner_gap, vertical_midpoint + half_thickness)
	pen.lineTo(horizontal_midpoint - half_thickness - corner_gap, vertical_midpoint + half_thickness)
	pen.lineTo(horizontal_midpoint - corner_gap, vertical_midpoint)
	pen.lineTo(horizontal_midpoint - half_thickness - corner_gap, vertical_midpoint - half_thickness)
	pen.lineTo(side_bearing + SEGMENT_THICKNESS + corner_gap, vertical_midpoint - half_thickness)
pen.closePath()
pen = None

font.createChar(-1, "segment-l")
pen = font["segment-l"].glyphPen()
pen.moveTo(horizontal_midpoint - half_thickness, SEGMENT_THICKNESS + SEGMENT_GAP)
pen.lineTo(horizontal_midpoint - half_thickness, vertical_midpoint - half_thickness - corner_gap)
pen.lineTo(horizontal_midpoint, vertical_midpoint - corner_gap)
pen.lineTo(horizontal_midpoint + half_thickness, vertical_midpoint - half_thickness - corner_gap)
pen.lineTo(horizontal_midpoint + half_thickness, SEGMENT_THICKNESS + SEGMENT_GAP)
pen.closePath()
pen = None

font.createChar(-1, "segment-k")
pen = font["segment-k"].glyphPen()
pen.moveTo(0, 0)
pen.lineTo(0, diagonal_y_offset)
pen.lineTo(quadrant_w - diagonal_x_offset, quadrant_h)
pen.lineTo(quadrant_w, quadrant_h)
pen.lineTo(quadrant_w, quadrant_h - diagonal_y_offset)
pen.lineTo(diagonal_x_offset, 0)
pen.closePath()
pen = None
font["segment-k"].transform((1, 0, 0, 1, side_bearing + SEGMENT_THICKNESS + SEGMENT_GAP, SEGMENT_THICKNESS + SEGMENT_GAP))

font.createChar(-1, "segment-r")
circle = fontforge.unitShape(0) # creates a unit circle
circle.draw(font["segment-r"].glyphPen()) # draws the circle into the glyph, replacing previous outlines
font["segment-r"].transform((SEGMENT_THICKNESS * 0.75, 0.0, 0.0, SEGMENT_THICKNESS * 0.75, advance_width, SEGMENT_THICKNESS * 0.375))
font["segment-r"].round()

# add other segments with references
font.createChar(-1, "segment-a")
font["segment-a"].addReference("segment-d", (1, 0, 0, 1, 0, CAP_HEIGHT - SEGMENT_THICKNESS))
font.createChar(-1, "segment-b")
font["segment-b"].addReference("segment-e", (1, 0, 0, 1, glyph_width - SEGMENT_THICKNESS, vertical_midpoint - half_thickness))
font.createChar(-1, "segment-c")
font["segment-c"].addReference("segment-e", (1, 0, 0, 1, glyph_width - SEGMENT_THICKNESS, 0))
font.createChar(-1, "segment-f")
font["segment-f"].addReference("segment-e", (1, 0, 0, 1, 0, vertical_midpoint - half_thickness))
font.createChar(-1, "segment-h")
font["segment-h"].addReference("segment-k", (1, 0, 0, -1, 0, CAP_HEIGHT))
font["segment-h"].unlinkRef()
font["segment-h"].correctDirection()
font.createChar(-1, "segment-i")
font["segment-i"].addReference("segment-l", (1, 0, 0, -1, 0, CAP_HEIGHT))
font["segment-i"].unlinkRef()
font["segment-i"].correctDirection()
font.createChar(-1, "segment-j")
font["segment-j"].addReference("segment-k", (-1, 0, 0, -1, advance_width, CAP_HEIGHT))
font["segment-j"].unlinkRef()
font.createChar(-1, "segment-m")
font["segment-m"].addReference("segment-h", (-1, 0, 0, -1, advance_width, CAP_HEIGHT))
font["segment-m"].unlinkRef()
font.createChar(-1, "segment-n")
font["segment-n"].addReference("segment-g", (1, 0, 0, 1, glyph_width // 2 - half_thickness, 0))
font.createChar(-1, "segment-o")
font["segment-o"].addReference("segment-d", (-1, 0, 0, -1, advance_width, CAP_HEIGHT))
font.createChar(-1, "segment-p")
font["segment-p"].addReference("segment-a", (-1, 0, 0, -1, advance_width, CAP_HEIGHT))

# add defined glyphs
for glyph, segments in segment_definitions:
	font.createChar(fontforge.unicodeFromName(glyph), glyph)
	if segments and segments[0] == "=": # for glyphs that are simply copies of existing glyphs
		font[glyph].addReference(segments[1:], (1, 0, 0, 1, 0, 0))
		font[glyph].useRefsMetrics(segments[1:])
	else: # for glyphs built up from segments
		for x in segments:
			font[glyph].addReference("segment-" + x, (1, 0, 0, 1, 0, 0))
		font[glyph].width = advance_width

# exception for width of full stop
# font["period"].transform((1, 0, 0, 1, -advance_width, 0))

# finished
font.save("source\\temp\\temp.sfd")
