Quixotic: fonts for Quikscript
==============================

Version 1.001
Copyright Brad Neil, 2023

These fonts are distributed in two formats: TTF for installation on computers; and WOFF for embedding in Web pages. The source code for generating the fonts is available on Github [1]. The Quikscript characters are mapped to the Unicode Private Use Area, so you’ll need to install a special keyboard layout to type with them. Finally, the fonts are all available under the SIL Open Font License 1.1 [2]. This means they may be freely used, distributed, extended and adapted.

* * *

To design functional Quikscript and Shavian glyphs for a traditional segmented display seemed like a nearly-impossible—indeed, *quixotic*—task. As it turns out, the results of this experiment are surprisingly legible, considering its limitations. I do not claim it to be a very pretty Quikscript font, though!

Since no descenders are possible with these types of digital displays, I differentiated the short and long letters with the same method used in some of Haley Wakamatsu’s Shavian fonts [3].

After deciding upon dimensions and designs for the segments, a Python script was used to automatically draw them and composite the glyphs from a list of simple definitions, specifying which segments are “on” in each glyph. This also allowed me to specify the font weight and slant as parameters, so those font variants could be produced quickly and accurately.

There are three variants of Quixotic. All come with a subtly slanted “italic” form in imitation of many real displays:

- Seven: based on the 7-segment display, as used in clocks, calculators and countless other electronic numeric displays. Certain words are viable, like PLAY, HELP, Error and so on, but many Latin letters are non-unique or unrecognisable. In fact, Quikscript fares somewhat better here, as all letters except ·Loch and ·Eat have a recognisable representation even if the deep (descending) letters sit high on the baseline. In imitation of real 7-segment displays, the full stop (period) is a non-spacing character, so it sits between two numbers as a decimal point. This variant is available in five weights, from Light to Bold.

- Fourteen: based on the 14-segment display, also known as the “Union Jack” or “starburst” display; often used in microwave ovens, CD and DVD players, and other devices that require an alphanumeric display. Here, all Quikscript letters have a unique representation, and the Latin capitals are now viable too. This variant is only available in a light weight, as there is not enough room for the diagonal segments when they are any heavier.

- Sixteen: based on the 16-segment display. This provides little benefit to Latin and Quikscript, but is necessary for a satisfactory rendering of Shavian.

The Quixotic family replaces my earlier font, QS Segment [4].

* * *

Links
-----
[1] https://github.com/FriedOrange/Quixotic-font
[2] https://scripts.sil.org/OFL (see OFL.txt)
[3] https://2gd4.me/tidbit/shavian-fonts
[4] http://friedorange.xyz/quikscript/myfonts.html
