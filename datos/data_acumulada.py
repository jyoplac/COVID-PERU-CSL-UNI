data_acumulada = [
    # 0         1       2       3           4       5           6       7       8           9       10
    # ['fecha', 'dia', 'cuar', 'PR_Neg', 'PM_Neg', 'PR_Pos', 'PM_Pos', 'falle', 'recup', 'hospi.', 'UCI'],
    ['06-mar',    1,    0,         0,       154,        0,       1,        0,       0,     0,	    0],
    ['07-mar',    2,    0,         0,       213,        0,       6,        0,       0,     0,       0],
    ['08-mar',	  3,    0,         0,       243,        0,       7,        0,       0,     0,       0],
    ['09-mar',    4,    0,         0,       309,    	0,	     9,        0,	    0,     0,	    0],
    ['10-mar',    5,    0,         0,	    335,    	0,	    11,	       0,	    0,     0,	    0],
    ['11-mar',	  6,    0,	       0,	    641,    	0,	    17,	       0,	    0,     0,	    0],
    ['12-mar',	  7,    0,	       0,	    883,    	0,	    22,	       0,	    0,     0,	    0],
    ['13-mar',    8,    0,	       0,      1194,    	0,	    38,	       0,	    0,     0,	    0],
    ['14-mar',	  9,    0,	       0,      1502,    	0,	    43,	       0,	    0,     0,	    0],
    ['15-mar',	 10,	0,         0,      1751,    	0,      71,	       0,	    0,	   0,	    0],
    ['16-mar',   11,	1,	       0,      2229,    	0,      86,	       0,	    1,     8,	    3],
    ['17-mar',	 12,	2,	       0,      2680,    	0,	   117,	       0,	    1,	  13,	    3],
    ['18-mar',	 13,	3,	       0,      2930,    	0,	   145,	       0,	    1,	  19,	    5],
    ['19-mar',	 14,	4,	       0,      3607,    	0,	   234,	       3,	    1,	  19,	    7],
    ['20-mar',	 15,	5,	       0,      4035,    	0,	   263,	       4,	    1,	  28,	    5],
    ['21-mar',	 16,	6,	       0,      4870,    	0,	   315,	       5,	    1,	  28,	    5],
    ['22-mar',	 17,	7,	       0,      5821,    	0,	   363,	       5,	    1,	  31,	    5],
    ['23-mar',	 18,	8,	       0,      6269,	    0,	   395,	       5,	    1,	  36,	    7],
    ['24-mar',	 19,	9,	       0,      6597,    	0,	   416,        7,	    4,	  23,	   14],
    ['25-mar',	 20,    10,	       0,	   7560,    	0,	   480,        9,	    6,	  38,      18],
    ['26-mar',	 21,	11,	       0,	   8639,    	0,	   580,        9,	   14,	  58,	   14],
    ['27-mar',	 22,	12,	       0,	   9430,    	0,	   635,	      11,	   16,	  79,	   21],
    ['28-mar',	 23,	13,	       0,	  10225,    	0,	   671,	      16,	   16,	  84,	   33],
    ['29-mar',	 24,	14,	       0,	  11817,    	0,	   852,	      18,	   16,	 107,      40],
    ['30-mar',	 25,	15,	       0,	  12502,    	0,	   950,	      24,	  269,	 238,	   49],
    ['31-mar',	 26,	16,	       0,	  13398,    	0,	  1065,	      30,	  394,	 190,	   57],
    ['01-abr',	 27,	17,	       0,	  14264,    	0,	  1323,	      47,	  447,	 198,	   56],
    ['02-abr',	 28,	18,	       0,	  15104,    	0,	  1414,	      55,	  537,	 189,	   51],
    ['03-abr',	 29,	19,	       0,	  15739,    	0,	  1595,	      61,	  627,	 243,	   72],
    ['04-abr',	 30,	20,	       0,	  16095,    	0,	  1746,	      73,	  914,	 286,	   88],
    ['05-abr',	 31,	21,	       0,	  17129,   	    0,	  2281,	      83,	  989,	 321,	   81],
    ['06-abr',	 32,	22,	       0,	  17853,	    0,	  2561,	      92,	  997,	 387,	   89],
    ['07-abr',	 33,	23,	       0,	  18601,	    0,	  2954,	     107,	 1231,	 490,	  109],
    ['08-abr',	 34,	24,	   15616,	  19641,	  728,	  3614,	     121,	 1333,	 512,	  113],
    ['09-abr',	 35,	25,	   22920,	  20289,	 1135,	  4121,	     138,	 1438,	 600,	  124],
    ['10-abr',	 36,	26,	   29690,	  21094,	 1348,	  4549,	     169,	 1569,	 687,	  130],
    ['11-abr',	 37,	27,	   36606,	  22258,	 1587,	  5261, 	 181,	 1739,	 788,	  142],
    ['12-abr',	 38,	28,	   43520,	  25467,	 1752,	  5767, 	 193,	 1798,	 815,	  134],
    ['13-abr',	 39,	29,	   50823,	  26509,	 3649,	  6135, 	 216,	 2642,	 901,	  143],
    ['14-abr',	 40,	30,	   65074,	  26839,	 3776,	  6527, 	 230,	 2869,	 914,	  132],
    ['15-abr',	 41,	31,	   69829,	  28081,	 4655,	  6820, 	 254,	 3108,	1113,	  146],
    ['16-abr',	 42,	32,	   80153,	  28824,	 5225,	  7266, 	 274,	 6120,	1277,	  169],
    ['17-abr',	 43,	33,	   84365,	  29659,	 5786,	  7703, 	 300,	 6541,	1219,	  137],
    ['18-abr',	 44,	34,	   90996,	  30479,	 6437,	  7983, 	 348,	 6684,	1268,	  117],
    ['19-abr',	 45,	35,	   96452,	  31665,	 7265,	  8363, 	 400,	 6811,	1349,	  167],
    ['20-abr',	 46,	36,	   99294,	  32392,	 7361,	  8964, 	 445,	 6968,	1682,	  385],
    ['21-abr',	 47,	37,	  104610,	  33277,	 8366,    9471, 	 484,	 6982,	2419,	  380],
    ['22-abr',	 48,	38,	  116791,	  34359,	 9188,	 10062, 	 530,	 7027,	2434,	  396],
    ['23-abr',	 49,	39,	  129417,	  34907,	10106,	 10808,	     572,	 7422,	2786,	  467],
    ['24-abr',	 50,	40,	  140509,	  36192,	10216,	 11432, 	 634,	 7496,	3194,	  505],
    ['25-abr',	 51,	41,	  155163,	  37701,	13486,	 11845, 	 700,	 7797,	3532,	  545],
    ['26-abr',	 52,	42,	  166639,	  38591,	14792,	 12725,	     728,	 8088,	3632,	  554],
    ['27-abr',	 53,	43,	  171324,	  39540,	15567,	 13132,	     782,	 8425,	3968,	  598],
    ['28-abr',	 54,	44,	  195624,	  40798,	17448,	 13742,	     854,	 9179,	4088,	  600],
    ['29-abr',	 55,	45,	  220319,	  42012,	19547,	 14384,	     943,	10037,	4289,	  623],
    ['30-abr',	 56,	46,	  238114,	  43162,	22020,	 14956,	    1051,	10405,	4978,	  651],
    ['01-may',	 57,	47,	  257198,	  44841,	24919,	 15540,	    1124,	11129,	5287,	  658],
    ['02-may',	 58,	48,	  266706,	  46364,	26362,	 16172,	    1200,	12434,	5098,	  671],
    ['03-may',	 59,	49,	  281720,	  47448,	29198,	 16730,	    1286,	13550,	5281,	  679],
    ['04-may',	 60,	50,	  289630,	  48490,	30070,	 17302,	    1344,	14427,	5435,	  694],
    ['05-may',	 61,	51,	  305541,	  49849,	33475,	 17714,	    1444,	15413,	5509,	  709],
    ['06-may',	 62,	52,	  322801,	  51840,	36313,	 18504,	    1533,	17527,	5729,	  717],
    ['07-may',	 63,	53,	  336158,	  53336,	39018,	 19508,	    1627,	18388,	5980,	  722],
    ['08-may',	 64,	54,	  356770,	  54573,	41518,	 20329,	    1714,	19012,	6155,	  730],
    ['09-may',	 65,	55,	  374276,	  54959,	44181,	 20834,	    1814,	20246,	6220,	  748],
    ['10-may',	 66,	56,	  379027,	  58596,	45997,	 21310,	    1889,	21349,	6601,	  774],
    ['11-may',	 67,	57,	  382407,	  61640,	46786,	 22036,     1961,	22406,	6648,	  785],
    ['12-may',	 68,	58,	  397251,     62859,    49324,	 22735,     2057,   23324,  6862,	  797],
    ['13-may',	 69,	59,	  413017,     64179,    52494,	 23812,     2169,   24324,  6979,	  806],
    ['14-may',	 70,	60,	  441261,     65427,    55933,	 24671,     2267,   25151,  6941,	  842],
    ['15-may',	 71,	61,	  453447,     67441,    59211,	 25284,     2392,   27147,  7085,	  851],
    ['16-may',	 72,	62,	  471428,     70513,    62307,	 26234,     2523,   28272,  7275,	  840],
    ['17-may',	 73,	63,	  485261,     73079,    65310,	 26963,     2648,   28621,  7408,	  850],
    ['18-may',	 74,	64,	  491296,     74903,    66997,	 27936,     2789,   30306,  7509,	  866],
    ['19-may',	 75,	65,	  503240,     76859,    70715,	 28768,     2914,   36524,  7526,	  883],
    ['20-may',	 76,	66,	  532612,     78791,    74330,	 29690,     3024,   41968,  7533,	  869],
    ['21-may',	 77,	67,	  545729,     82002,    78418,	 30351,     3148,   43587,  7455,	  886],
    ['22-may',	 78,	68,	  554170,     84658,    80875,	 30823,     3244,   44848,  7545,	  901],
    ['23-may',	 79,	69,	  581185,     91402,    84407,	 31347,     3373,   47915,  7674,	  909],
    ['24-may',	 80,	70,	  609586,     91422,    87832,	 32127,     3456,   49795,  7779,	  920],
    ['25-may',	 81,	71,	  625188,     91755,    90843,	 33136,     3629,   50949,  8097,	  909],
    ['26-may',	 82,	72,	  652298,     93672,    95969,	 33782,     3788,   52906,  8207,	  923],
    ['27-may',	 83,	73,	  672897,     96476,   101324,	 34581,     3983,   56169,  8267,	  926],
    ['28-may',	 84,	74,	  688805,     98213,   106147,	 35632,     4099,   59442,  8395,	  943],
    ['29-may',	 85,	75,	  714469,    100863,   111585,	 36700,     4230,   62791,  8433,	  940],
    ['30-may',	 86,	76,	  754082,    102955,   118021,	 37650,     4371,   66447,  8465,	  940],
    ['31-may',	 87,	77,	  788904,    105494,   125803,	 38673,     4506,   67208,  8882,	  988],
    ['01-jun',	 88,	78,	  800711,    105909,   130323,	 39716,     4634,   68507,  8868,	  975],
    ['02-jun',	 89,	79,	  808488,    109274,   134699,	 40185,     4767,   69257,  8930,	  964],
    ['03-jun',	 90,	80,	  825074,    111627,   138313,	 40601,     4894,   72319, 10101,	  998],
    ['04-jun',	 91,	81,	  840680,    111953,   141378,	 41820,     5031,   76228,  9063,	 1005],
    ['05-jun',	 92,	82,	  853291,    113777,   144994,	 42406,     5162,   79214,  9198,	 1041],
    ['06-jun',	 93,	83,	  866094,    115151,   147740,	 44018,     5301,   82731,  9500,	 1062],
    ['07-jun',	 94,	84,	  877787,    117654,   150631,	 45884,     5465,   86219,  9583,	 1062],
    ['08-jun',	 95,	85,	  883254,    121035,   152443,	 47253,     5571,   89556,  9661,	 1072],
    ['09-jun',	 96,	86,	  900507,    123448,   155465,	 48271,     5738,   92929,  9903,	 1077],
    ['10-jun',	 97,	87,	  920732,    126201,   159272,	 49551,     5903,   98031,  9916,	 1065],
    ['11-jun',	 98,	88,	  938871,    128819,   164243,	 50545,     6109,  102429, 10026,	 1069],
    ['12-jun',	 99,	89,	  963130,    131538,   169144,	 51605,     6308,  107133, 10121,	 1089],
    ['13-jun',	100,	90,	  978741,    134604,   172299,	 52833,     6498,  111724, 10342,	 1113],
    ['14-jun',	101,	91,	  993988,    137115,   175779,	 53957,     6688,  115579, 10297,	 1111],
    ['15-jun',	102,	92,	 1003694,    139792,   178189,	 54803,     6860,  119409, 10295,	 1121],
    ['16-jun',	103,	93,	 1016729,    142720,   181059,	 56097,     7056,  125205, 10177,	 1112],
    ['17-jun',	104,	94,	 1031968,    145035,   183691,	 57217,     7257,  128622, 10204,	 1111],
    ['18-jun',	105,	95,	 1047429,    147950,   185915,	 58473,     7461,  131190, 10240,	 1130],
    ['19-jun',	106,	96,	 1062560,    150781,   188613,	 59312,     7660,  135520, 10445,	 1126],
    ['20-jun',	107,	97,	 1079114,    152111,   191452,	 59886,     7861,  138763, 10577,	 1143],
    ['21-jun',	108,	98,	 1094476,    154797,   193800,	 61136,     8045,  141967, 10566,	 1137],
    ['22-jun',	109,	99,	 1104022,    156461,   195693,	 61754,     8223,  145320, 10714,	 1144],
    ['23-jun',	110,   100,	 1119546,    159390,   197960,	 62850,     8404,  148437, 10588,	 1161],
    ['24-jun',	111,   101,	 1133972,    162992,   200288,	 64401,     8586,  151589, 10599,	 1166],
    ['25-jun',	112,   102,	 1148274,    166729,   202601,	 66001,     8761,  156074, 10587,	 1144],
    ['26-jun',	113,   103,	 1161760,    170397,   204873,	 67491,     8939,  159806, 10964,	 1172],
    ['27-jun',	114,   104,	 1175018,    174128,   207308,	 68681,     9135,  164024, 10762,	 1169],
    ['28-jun',	115,   105,	 1189907,    175786,   209890,	 69529,     9317,  167998, 10861,	 1178],
    ['29-jun',	116,   106,	 1201763,    177196,   212150,	 70215,     9504,  171159, 11000,	 1183],
    ['30-jun',	117,   107,	 1215028,    179145,   214084,	 71129,     9677,  174535, 11049,	 1185],
    ['01-jul',	118,   108,	 1230107,    180785,   216524,	 71953,     9860,  178245, 11108,	 1212],
    ['02-jul',	119,   109,	 1245340,    182917,   218922,	 73082,    10045,  182097, 11179,	 1220],
    ['03-jul',	120,   110,	 1260377,    184993,   221556,	 74043,    10226,  185852, 11131,	 1210],
    ['04-jul',	121,   111,	 1276096,    186734,   224211,	 74869,    10412,  189621, 11273,	 1224],
    ['05-jul',	122,   112,	 1291184,    188944,   226871,	 75847,    10589,  193957, 11302,	 1227],
    ['06-jul',	123,   113,	 1303796,    191191,   228760,	 76943,    10772,  197619, 11399,	 1236],
    ['07-jul',	124,   114,	 1318277,    193773,   231104,	 78174,    10952,  200938, 11646,	 1265],
    ['08-jul',	125,   115,	 1332573,    196832,   233123,	 79788,    11133,  204748, 11626,	 1265]
    # 0         1       2       3           4       5           6       7       8           9       10
    # ['fecha', 'dia', 'cuar', 'PR_Neg', 'PM_Neg', 'PR_Pos', 'PM_Pos', 'falle', 'recup', 'hospi.', 'UCI'],
]
