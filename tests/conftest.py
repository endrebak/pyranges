import pytest

from pyranges import GRanges

import pandas as pd

from io import StringIO


@pytest.fixture
def exons():

    c = """Chromosome Feature Source Start End Score Strand Frame GeneID TranscriptID ExonNumber ExonID Group Length
14 1 exon mirbase 17369 17436 . - . ENSG00000278267 ENST00000619216 1.0 ENSE00003746039 0-25 67
18 1 exon mirbase 30366 30503 . + . ENSG00000284332 ENST00000607096 1.0 ENSE00003695741 0-25 137
22 1 exon havana 52473 53312 . + . ENSG00000268020 ENST00000606857 1.0 ENSE00003698237 0-25 839
19 1 exon havana 35721 36081 . - . ENSG00000237613 ENST00000417324 1.0 ENSE00001656588 25-50 1527
20 1 exon havana 35277 35481 . - . ENSG00000237613 ENST00000417324 2.0 ENSE00001669267 25-50 1527
21 1 exon havana 34554 35174 . - . ENSG00000237613 ENST00000417324 3.0 ENSE00001727627 25-50 1527
15 1 exon havana 29554 30039 . + . ENSG00000243485 ENST00000473358 1.0 ENSE00001947070 25-50 1555
16 1 exon havana 30564 30667 . + . ENSG00000243485 ENST00000473358 2.0 ENSE00001922571 25-50 1555
17 1 exon havana 30976 31097 . + . ENSG00000243485 ENST00000473358 3.0 ENSE00001827679 25-50 1555
0 1 exon havana 11869 12227 . + . ENSG00000223972 ENST00000456328 1.0 ENSE00002234944 50-75 2540
1 1 exon havana 12613 12721 . + . ENSG00000223972 ENST00000456328 2.0 ENSE00003582793 50-75 2540
2 1 exon havana 13221 14409 . + . ENSG00000223972 ENST00000456328 3.0 ENSE00002312635 50-75 2540
26 1 exon havana 65419 65433 . + . ENSG00000186092 ENST00000641515 1.0 ENSE00003812156 50-75 6166
27 1 exon havana 65520 65573 . + . ENSG00000186092 ENST00000641515 2.0 ENSE00003813641 50-75 6166
28 1 exon havana 69037 71585 . + . ENSG00000186092 ENST00000641515 3.0 ENSE00003813949 50-75 6166
23 1 exon havana 57598 57653 . + . ENSG00000240361 ENST00000642116 1.0 ENSE00003812686 75-100 6518
24 1 exon havana 58700 58856 . + . ENSG00000240361 ENST00000642116 2.0 ENSE00003812505 75-100 6518
25 1 exon havana 62916 64116 . + . ENSG00000240361 ENST00000642116 3.0 ENSE00003811818 75-100 6518
3 1 exon havana 29534 29570 . - . ENSG00000227232 ENST00000488147 1.0 ENSE00001890219 75-100 15166
4 1 exon havana 24738 24891 . - . ENSG00000227232 ENST00000488147 2.0 ENSE00003507205 75-100 15166
5 1 exon havana 18268 18366 . - . ENSG00000227232 ENST00000488147 3.0 ENSE00003477500 75-100 15166
6 1 exon havana 17915 18061 . - . ENSG00000227232 ENST00000488147 4.0 ENSE00003565697 75-100 15166
7 1 exon havana 17606 17742 . - . ENSG00000227232 ENST00000488147 5.0 ENSE00003475637 75-100 15166
8 1 exon havana 17233 17368 . - . ENSG00000227232 ENST00000488147 6.0 ENSE00003502542 75-100 15166
9 1 exon havana 16858 17055 . - . ENSG00000227232 ENST00000488147 7.0 ENSE00003553898 75-100 15166
10 1 exon havana 16607 16765 . - . ENSG00000227232 ENST00000488147 8.0 ENSE00003621279 75-100 15166
11 1 exon havana 15796 15947 . - . ENSG00000227232 ENST00000488147 9.0 ENSE00002030414 75-100 15166
12 1 exon havana 15005 15038 . - . ENSG00000227232 ENST00000488147 10.0 ENSE00001935574 75-100 15166
13 1 exon havana 14404 14501 . - . ENSG00000227232 ENST00000488147 11.0 ENSE00001843071 75-100 15166
29 1 exon havana 129055 129217 . - . ENSG00000238009 ENST00000477740 1.0 ENSE00001919246 75-100 44428
30 1 exon havana 120721 120932 . - . ENSG00000238009 ENST00000477740 2.0 ENSE00001171005 75-100 44428
31 1 exon havana 112700 112804 . - . ENSG00000238009 ENST00000477740 3.0 ENSE00001957285 75-100 44428
32 1 exon havana 92230 92240 . - . ENSG00000238009 ENST00000477740 4.0 ENSE00001896976 75-100 44428"""

    df = pd.read_table(StringIO(c), sep=" ")

    return GRanges(df)

@pytest.fixture
def introns():

    c = """Chromosome Feature Source Start End Score Strand Frame GeneID TranscriptID ExonNumber ExonID
0 1 intron havana 35175.0 35276 . - . ENSG00000237613 ENST00000417324 2.0 ENSE00001669267
1 1 intron havana 35482.0 35720 . - . ENSG00000237613 ENST00000417324 1.0 ENSE00001656588
2 1 intron havana 12228.0 12612 . + . ENSG00000223972 ENST00000456328 2.0 ENSE00003582793
3 1 intron havana 12722.0 13220 . + . ENSG00000223972 ENST00000456328 3.0 ENSE00002312635
4 1 intron havana 30040.0 30563 . + . ENSG00000243485 ENST00000473358 2.0 ENSE00001922571
5 1 intron havana 30668.0 30975 . + . ENSG00000243485 ENST00000473358 3.0 ENSE00001827679
6 1 intron havana 92241.0 112699 . - . ENSG00000238009 ENST00000477740 3.0 ENSE00001957285
7 1 intron havana 112805.0 120720 . - . ENSG00000238009 ENST00000477740 2.0 ENSE00001171005
8 1 intron havana 120933.0 129054 . - . ENSG00000238009 ENST00000477740 1.0 ENSE00001919246
9 1 intron havana 14502.0 15004 . - . ENSG00000227232 ENST00000488147 10.0 ENSE00001935574
10 1 intron havana 15039.0 15795 . - . ENSG00000227232 ENST00000488147 9.0 ENSE00002030414
11 1 intron havana 15948.0 16606 . - . ENSG00000227232 ENST00000488147 8.0 ENSE00003621279
12 1 intron havana 16766.0 16857 . - . ENSG00000227232 ENST00000488147 7.0 ENSE00003553898
13 1 intron havana 17056.0 17232 . - . ENSG00000227232 ENST00000488147 6.0 ENSE00003502542
14 1 intron havana 17369.0 17605 . - . ENSG00000227232 ENST00000488147 5.0 ENSE00003475637
15 1 intron havana 17743.0 17914 . - . ENSG00000227232 ENST00000488147 4.0 ENSE00003565697
16 1 intron havana 18062.0 18267 . - . ENSG00000227232 ENST00000488147 3.0 ENSE00003477500
17 1 intron havana 18367.0 24737 . - . ENSG00000227232 ENST00000488147 2.0 ENSE00003507205
18 1 intron havana 24892.0 29533 . - . ENSG00000227232 ENST00000488147 1.0 ENSE00001890219
19 1 intron havana 65434.0 65519 . + . ENSG00000186092 ENST00000641515 2.0 ENSE00003813641
20 1 intron havana 65574.0 69036 . + . ENSG00000186092 ENST00000641515 3.0 ENSE00003813949
21 1 intron havana 57654.0 58699 . + . ENSG00000240361 ENST00000642116 2.0 ENSE00003812505
22 1 intron havana 58857.0 62915 . + . ENSG00000240361 ENST00000642116 3.0 ENSE00003811818"""

    df = pd.read_table(StringIO(c), sep=" ")

    return GRanges(df)
