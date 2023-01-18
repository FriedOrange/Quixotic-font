import sys
import math
import fontforge

# constants
EM_SIZE = 1000
CAP_HEIGHT = 800
# ASPECT_RATIO = -(1 - math.sqrt(5)) / 2
ASPECT_RATIO = float(sys.argv[4])
SEGMENT_THICKNESS = int(sys.argv[1]) # 56 good for 14 segment
SEGMENT_GAP = 20
ADVANCE_WIDTH = 583
SEGMENT_COUNT = int(sys.argv[2])
MAX_CORNER_SIZE = 38
FONTNAME_MAP = {
	7: "Seven",
	14: "Fourteen",
	16: "Sixteen",
	56: "Light",
	76: "Regular",
	94: "Medium",
	112: "Semibold",
	130: "Bold"
}
FAMILYNAME_MAP = {
	56: " Light",
	76: "",
	94: " Medium",
	112: " Semibold",
	130: ""
}
WEIGHT_MAP = {
	56: 300,
	76: 400,
	94: 500,
	112: 600,
	130: 700
}

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
character_gap = ADVANCE_WIDTH - glyph_width
side_bearing = round(character_gap / 2)
corner_gap = round(math.sqrt(SEGMENT_GAP**2 / 2))
vertical_midpoint = round(CAP_HEIGHT / 2)
horizontal_midpoint = round(ADVANCE_WIDTH / 2)
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
font[".notdef"].width = ADVANCE_WIDTH

# draw unique segments
font.createChar(-1, "segment_d")
pen = font["segment_d"].glyphPen()
pen.moveTo(side_bearing + min(half_thickness, MAX_CORNER_SIZE) + corner_gap, min(half_thickness, MAX_CORNER_SIZE))
pen.lineTo(side_bearing + SEGMENT_THICKNESS + corner_gap, SEGMENT_THICKNESS)
if SEGMENT_COUNT == 16:
	pen.lineTo(horizontal_midpoint - SEGMENT_GAP // 2, SEGMENT_THICKNESS)
	pen.lineTo(horizontal_midpoint - SEGMENT_GAP // 2, 0)
else:
	pen.lineTo(ADVANCE_WIDTH - (side_bearing + SEGMENT_THICKNESS + corner_gap), SEGMENT_THICKNESS)
	pen.lineTo(ADVANCE_WIDTH - (side_bearing + min(half_thickness, MAX_CORNER_SIZE) + corner_gap), min(half_thickness, MAX_CORNER_SIZE))
	pen.lineTo(ADVANCE_WIDTH - (side_bearing + min(SEGMENT_THICKNESS, MAX_CORNER_SIZE * 2) + corner_gap), 0)
pen.lineTo(side_bearing + min(SEGMENT_THICKNESS, MAX_CORNER_SIZE * 2) + corner_gap, 0)
pen.closePath()
pen = None

# font.createChar(-1, "segment_e")
# pen = font["segment_e"].glyphPen()
# pen.moveTo(side_bearing + half_thickness, half_thickness + corner_gap)
# pen.lineTo(side_bearing, SEGMENT_THICKNESS + corner_gap)
# pen.lineTo(side_bearing, vertical_midpoint - half_thickness - corner_gap)
# pen.lineTo(side_bearing + half_thickness, vertical_midpoint - corner_gap)
# pen.lineTo(side_bearing + SEGMENT_THICKNESS, vertical_midpoint - half_thickness - corner_gap)
# pen.lineTo(side_bearing + SEGMENT_THICKNESS, SEGMENT_THICKNESS + corner_gap)
# pen.closePath()
# pen = None

font.createChar(-1, "segment_e")
pen = font["segment_e"].glyphPen()
pen.moveTo(side_bearing + min(half_thickness, MAX_CORNER_SIZE), min(half_thickness, MAX_CORNER_SIZE) + corner_gap)
pen.lineTo(side_bearing, min(SEGMENT_THICKNESS, 2 * MAX_CORNER_SIZE) + corner_gap)
pen.lineTo(side_bearing, vertical_midpoint - min(half_thickness, MAX_CORNER_SIZE) - corner_gap)
pen.lineTo(side_bearing + min(half_thickness, MAX_CORNER_SIZE), vertical_midpoint - corner_gap)
pen.lineTo(side_bearing + SEGMENT_THICKNESS, vertical_midpoint - SEGMENT_THICKNESS + min(half_thickness, MAX_CORNER_SIZE) - corner_gap)
pen.lineTo(side_bearing + SEGMENT_THICKNESS, SEGMENT_THICKNESS + corner_gap)
pen.closePath()
pen = None

font.createChar(-1, "segment_g")
pen = font["segment_g"].glyphPen()
if SEGMENT_COUNT == 7:
	pen.moveTo(side_bearing + min(half_thickness, MAX_CORNER_SIZE) + corner_gap, vertical_midpoint)
	pen.lineTo(side_bearing + half_thickness + min(half_thickness, MAX_CORNER_SIZE) + corner_gap, vertical_midpoint + half_thickness)
	pen.lineTo(ADVANCE_WIDTH - side_bearing - half_thickness - min(half_thickness, MAX_CORNER_SIZE) - corner_gap, vertical_midpoint + half_thickness)
	pen.lineTo(ADVANCE_WIDTH - side_bearing - min(half_thickness, MAX_CORNER_SIZE) - corner_gap, vertical_midpoint)
	pen.lineTo(ADVANCE_WIDTH - side_bearing - half_thickness - min(half_thickness, MAX_CORNER_SIZE) - corner_gap, vertical_midpoint - half_thickness)
	pen.lineTo(side_bearing + half_thickness + min(half_thickness, MAX_CORNER_SIZE) + corner_gap, vertical_midpoint - half_thickness)
else:
	pen.moveTo(side_bearing + half_thickness + corner_gap, vertical_midpoint)
	pen.lineTo(side_bearing + SEGMENT_THICKNESS + corner_gap, vertical_midpoint + half_thickness)
	pen.lineTo(horizontal_midpoint - half_thickness - corner_gap, vertical_midpoint + half_thickness)
	pen.lineTo(horizontal_midpoint - corner_gap, vertical_midpoint)
	pen.lineTo(horizontal_midpoint - half_thickness - corner_gap, vertical_midpoint - half_thickness)
	pen.lineTo(side_bearing + SEGMENT_THICKNESS + corner_gap, vertical_midpoint - half_thickness)
pen.closePath()
pen = None

if SEGMENT_COUNT > 7:
	font.createChar(-1, "segment_l")
	pen = font["segment_l"].glyphPen()
	pen.moveTo(horizontal_midpoint - half_thickness, SEGMENT_THICKNESS + SEGMENT_GAP)
	pen.lineTo(horizontal_midpoint - half_thickness, vertical_midpoint - half_thickness - corner_gap)
	pen.lineTo(horizontal_midpoint, vertical_midpoint - corner_gap)
	pen.lineTo(horizontal_midpoint + half_thickness, vertical_midpoint - half_thickness - corner_gap)
	pen.lineTo(horizontal_midpoint + half_thickness, SEGMENT_THICKNESS + SEGMENT_GAP)
	pen.closePath()
	pen = None

	font.createChar(-1, "segment_k")
	pen = font["segment_k"].glyphPen()
	pen.moveTo(0, 0)
	pen.lineTo(0, diagonal_y_offset)
	pen.lineTo(quadrant_w - diagonal_x_offset, quadrant_h)
	pen.lineTo(quadrant_w, quadrant_h)
	pen.lineTo(quadrant_w, quadrant_h - diagonal_y_offset)
	pen.lineTo(diagonal_x_offset, 0)
	pen.closePath()
	pen = None
	font["segment_k"].transform((1, 0, 0, 1, side_bearing + SEGMENT_THICKNESS + SEGMENT_GAP, SEGMENT_THICKNESS + SEGMENT_GAP))

font.createChar(-1, "segment_r")
circle = fontforge.unitShape(0) # creates a unit circle
circle.draw(font["segment_r"].glyphPen()) # draws the circle into the glyph, replacing previous outlines
font["segment_r"].transform((min(half_thickness * 1.25, 70), 0.0, 0.0, min(half_thickness * 1.25, 70), ADVANCE_WIDTH, 0))
font["segment_r"].round()

# add other segments with references
font.createChar(-1, "segment_a")
if SEGMENT_COUNT == 7:
	font["segment_a"].addReference("segment_d", (-1, 0, 0, -1, ADVANCE_WIDTH, CAP_HEIGHT))
else:
	font["segment_a"].addReference("segment_d", (1, 0, 0, 1, 0, CAP_HEIGHT - SEGMENT_THICKNESS))
font.createChar(-1, "segment_c")
font["segment_c"].addReference("segment_e", (-1, 0, 0, 1, character_gap + glyph_width, 0))
font["segment_c"].unlinkRef()
font["segment_c"].correctDirection()
font.createChar(-1, "segment_b")
font["segment_b"].addReference("segment_c", (1, 0, 0, 1, 0, vertical_midpoint - min(half_thickness, MAX_CORNER_SIZE)))
font["segment_b"].unlinkRef()
font.createChar(-1, "segment_f")
font["segment_f"].addReference("segment_e", (1, 0, 0, 1, 0, vertical_midpoint - min(half_thickness, MAX_CORNER_SIZE)))
font["segment_f"].unlinkRef()
if SEGMENT_COUNT > 7:
	font.createChar(-1, "segment_h")
	font["segment_h"].addReference("segment_k", (1, 0, 0, -1, 0, CAP_HEIGHT))
	font["segment_h"].unlinkRef()
	font["segment_h"].correctDirection()
	font.createChar(-1, "segment_i")
	font["segment_i"].addReference("segment_l", (1, 0, 0, -1, 0, CAP_HEIGHT))
	font["segment_i"].unlinkRef()
	font["segment_i"].correctDirection()
	font.createChar(-1, "segment_j")
	font["segment_j"].addReference("segment_k", (-1, 0, 0, -1, ADVANCE_WIDTH, CAP_HEIGHT))
	font["segment_j"].unlinkRef()
	font.createChar(-1, "segment_m")
	font["segment_m"].addReference("segment_h", (-1, 0, 0, -1, ADVANCE_WIDTH, CAP_HEIGHT))
	font["segment_m"].unlinkRef()
	font.createChar(-1, "segment_n")
	font["segment_n"].addReference("segment_g", (1, 0, 0, 1, glyph_width // 2 - half_thickness, 0))
if SEGMENT_COUNT == 16:
	font.createChar(-1, "segment_o")
	font["segment_o"].addReference("segment_d", (-1, 0, 0, -1, ADVANCE_WIDTH, CAP_HEIGHT))
	font.createChar(-1, "segment_p")
	font["segment_p"].addReference("segment_a", (-1, 0, 0, -1, ADVANCE_WIDTH, CAP_HEIGHT))

# add defined glyphs
memo = {}
for glyph, segments in segment_definitions:
	font.createChar(fontforge.unicodeFromName(glyph), glyph)
	segments = "".join(sorted(segments))
	if segments in memo:
		font[glyph].addReference(memo[segments], (1, 0, 0, 1, 0, 0))
		font[glyph].useRefsMetrics(memo[segments])
	else:
		for segment in segments:
			font[glyph].addReference("segment_" + segment, (1, 0, 0, 1, 0, 0))
		font[glyph].width = ADVANCE_WIDTH
		memo[segments] = glyph

# exception for seven segment style
if SEGMENT_COUNT == 7:
	font["period"].transform((1, 0, 0, 1, -ADVANCE_WIDTH, 0))
	font["colon"].clear()
	font["colon"].addReference("segment_r", (1, 0, 0, 1, horizontal_midpoint // 3 - ADVANCE_WIDTH, 3 * CAP_HEIGHT // 10))
	font["colon"].addReference("segment_r", (1, 0, 0, 1, horizontal_midpoint // 3 - ADVANCE_WIDTH, 7 * CAP_HEIGHT // 10))
	font["colon"].width = ADVANCE_WIDTH // 3

# eliminate segment glyphs
font["segment_a"].unlinkThisGlyph()
font["segment_b"].unlinkThisGlyph()
font["segment_c"].unlinkThisGlyph()
font["segment_d"].unlinkThisGlyph()
font["segment_e"].unlinkThisGlyph()
font["segment_f"].unlinkThisGlyph()
font["segment_g"].unlinkThisGlyph()
font["segment_r"].unlinkThisGlyph()
font["segment_a"].clear()
font["segment_b"].clear()
font["segment_c"].clear()
font["segment_d"].clear()
font["segment_e"].clear()
font["segment_f"].clear()
font["segment_g"].clear()
font["segment_r"].clear()
if SEGMENT_COUNT > 7:
	font["segment_h"].unlinkThisGlyph()
	font["segment_i"].unlinkThisGlyph()
	font["segment_j"].unlinkThisGlyph()
	font["segment_k"].unlinkThisGlyph()
	font["segment_l"].unlinkThisGlyph()
	font["segment_m"].unlinkThisGlyph()
	font["segment_n"].unlinkThisGlyph()
	font["segment_h"].clear()
	font["segment_i"].clear()
	font["segment_j"].clear()
	font["segment_k"].clear()
	font["segment_l"].clear()
	font["segment_m"].clear()
	font["segment_n"].clear()
if SEGMENT_COUNT > 14:
	font["segment_o"].unlinkThisGlyph()
	font["segment_p"].unlinkThisGlyph()
	font["segment_o"].clear()
	font["segment_p"].clear()

# add font names
font.fontname = "Quixotic" + FONTNAME_MAP[SEGMENT_COUNT] + "-" + (FONTNAME_MAP[SEGMENT_THICKNESS] if SEGMENT_COUNT == 7 else "Regular")
font.familyname = "Quixotic " + FONTNAME_MAP[SEGMENT_COUNT] + (FAMILYNAME_MAP[SEGMENT_THICKNESS] if SEGMENT_COUNT == 7 else "")
font.fullname = font.familyname + (" Bold" if SEGMENT_THICKNESS == 130 else "")
font.copyright = "Copyright 2023 Brad Neil"
if SEGMENT_COUNT == 7 and SEGMENT_THICKNESS != 76 and SEGMENT_THICKNESS != 130:
	font.appendSFNTName("English (US)", 16, "Quixotic " + FONTNAME_MAP[SEGMENT_COUNT])
	font.appendSFNTName("English (US)", 17, FONTNAME_MAP[SEGMENT_THICKNESS])
font.appendSFNTName("English (US)", 9, "Brad Neil")
font.appendSFNTName("English (US)", 12, "http://friedorange.xyz/")
font.appendSFNTName("English (US)", 13, "This Font Software is licensed under the SIL Open Font License, Version 1.1. This license is available with a FAQ at: https://scripts.sil.org/OFL")
font.appendSFNTName("English (US)", 14, "https://scripts.sil.org/OFL")
font.version = "1.000"

# set metrics etc
font.os2_winascent_add = False
font.os2_winascent = 800
font.os2_windescent_add = False
font.os2_windescent = 70 # value from bold weight
font.os2_typoascent_add = False
font.os2_typoascent = 1000
font.os2_typodescent_add = False
font.os2_typodescent = -200
font.os2_typolinegap = 0
font.hhea_ascent_add = False
font.hhea_ascent = 1000
font.hhea_descent_add = False
font.hhea_descent = -200
font.hhea_linegap = 0
font.os2_use_typo_metrics = True
font.os2_weight_width_slope_only = True
font.os2_weight = WEIGHT_MAP[SEGMENT_THICKNESS]
font.upos = int(SEGMENT_THICKNESS * 1.5)
font.uwidth = SEGMENT_THICKNESS
font.os2_strikeypos = vertical_midpoint - half_thickness
font.os2_strikeysize = SEGMENT_THICKNESS
if SEGMENT_COUNT == 7:
	font.os2_panose = (2, 0, 0, 0, 0, 0, 0, 0, 0, 0) # proportion was being automatically (and wrongly) set to Monospace

# finished
font.save("source\\temp\\temp.sfd")
