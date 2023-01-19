
for style in ("Light", "Medium", "Semibold"):
	for italic in (False, True):
		ttx = f"""<?xml version="1.0" encoding="UTF-8"?>
<ttFont sfntVersion="\\x00\\x01\\x00\\x00" ttLibVersion="4.38">

  <name>
    <namerecord nameID="0" platformID="3" platEncID="1" langID="0x409">
      Copyright 2023 Brad Neil
    </namerecord>
    <namerecord nameID="1" platformID="3" platEncID="1" langID="0x409">
      Quixotic Seven {style}
    </namerecord>
    <namerecord nameID="2" platformID="3" platEncID="1" langID="0x409">
    {"Italic" if italic else "Regular"}
    </namerecord>
    <namerecord nameID="3" platformID="3" platEncID="1" langID="0x409">
      1.000;NONE;QuixoticSeven-{style}{"Italic" if italic else ""}
    </namerecord>
    <namerecord nameID="4" platformID="3" platEncID="1" langID="0x409">
      Quixotic Seven {style}{" Italic" if italic else ""}
    </namerecord>
    <namerecord nameID="5" platformID="3" platEncID="1" langID="0x409">
      Version 1.000; ttfautohint (v1.8.4.7-5d5b-dirty)
    </namerecord>
    <namerecord nameID="6" platformID="3" platEncID="1" langID="0x409">
      QuixoticSeven-{style}{"Italic" if italic else ""}
    </namerecord>
    <namerecord nameID="9" platformID="3" platEncID="1" langID="0x409">
      Brad Neil
    </namerecord>
    <namerecord nameID="12" platformID="3" platEncID="1" langID="0x409">
      http://friedorange.xyz/
    </namerecord>
    <namerecord nameID="13" platformID="3" platEncID="1" langID="0x409">
      This Font Software is licensed under the SIL Open Font License, Version 1.1. This license is available with a FAQ at: https://scripts.sil.org/OFL
    </namerecord>
    <namerecord nameID="14" platformID="3" platEncID="1" langID="0x409">
      https://scripts.sil.org/OFL
    </namerecord>
	<namerecord nameID="16" platformID="3" platEncID="1" langID="0x409">
	Quixotic Seven
	</namerecord>
	<namerecord nameID="17" platformID="3" platEncID="1" langID="0x409">
	{style}{" Italic" if italic else ""}
	</namerecord>
  </name>

</ttFont>
		"""

		with open(f"QuixoticSeven-{style}{'Italic' if italic else ''}.ttx", "w") as output_file:
			output_file.write(ttx)
