data_diaria = [
    # 0         1       2       3           4       5           6       7       8           9       10
    # ['fecha', 'dia', 'cuar', 'PR_Neg', 'PM_Neg', 'PR_Pos', 'PM_Pos', 'falle', 'recup', 'hospi.', 'UCI'],
    ['06-mar',    1,    0,         0,       154,        0,       1,        0,       0,     0,	    0],
    ['07-mar',    2,    0,         0,        59,        0,       5,        0,       0,     0,       0],
    ['08-mar',	  3,    0,         0,        30,        0,       1,        0,       0,     0,       0],
    ['09-mar',    4,    0,         0,        66,    	0,	     2,        0,	    0,     0,	    0],
    ['10-mar',    5,    0,         0,	     26,    	0,	     2,	       0,	    0,     0,	    0],
    ['11-mar',	  6,    0,	       0,	    306,    	0,	     6,	       0,	    0,     0,	    0],
    ['12-mar',	  7,    0,	       0,	    242,    	0,	     5,	       0,	    0,     0,	    0],
    ['13-mar',    8,    0,	       0,       311,    	0,	    16,	       0,	    0,     0,	    0],
    ['14-mar',	  9,    0,	       0,       308,    	0,	     5,	       0,	    0,     0,	    0],
    ['15-mar',	 10,	0,         0,       249,    	0,      28,	       0,	    0,	   0,	    0],
    ['16-mar',   11,	1,	       0,       478,    	0,      15,	       0,	    1,     8,	    3],
    ['17-mar',	 12,	2,	       0,       451,    	0,	    31,	       0,	    0,	   5,	    0],
    ['18-mar',	 13,	3,	       0,       250,    	0,	    28,	       0,	    0,	   6,	    2],
    ['19-mar',	 14,	4,	       0,       677,    	0,	    89,	       3,	    0,	   0,	    2],
    ['20-mar',	 15,	5,	       0,       428,    	0,	    29,	       1,	    0,	   9,	   -2],
    ['21-mar',	 16,	6,	       0,       835,    	0,	    52,	       1,	    0,	   0,	    0],
    ['22-mar',	 17,	7,	       0,       951,    	0,	    48,	       0,	    0,	   3,	    0],
    ['23-mar',	 18,	8,	       0,       448,	    0,	    32,	       0,	    0,	   5,	    2],
    ['24-mar',	 19,	9,	       0,       328,    	0,	    21,        2,	    3,	 -13,	    7],
    ['25-mar',	 20,    10,	       0,	    963,    	0,	    64,        2,	    2,	  15,       4],
    ['26-mar',	 21,	11,	       0,	   1079,    	0,	   100,        0,	    8,	  20,	   -4],
    ['27-mar',	 22,	12,	       0,	    791,    	0,	    55,	       2,	    2,	  21,	    7],
    ['28-mar',	 23,	13,	       0,	    795,    	0,	    36,	       5,	    0,	   5,	   12],
    ['29-mar',	 24,	14,	       0,	   1592,    	0,	   181,	       2,	    0,	  23,       7],
    ['30-mar',	 25,	15,	       0,	    685,    	0,	    98,	       6,	  253,	 131,	    9],
    ['31-mar',	 26,	16,	       0,	    896,    	0,	   115,	       6,	  125,	 -48,	    8],
    ['01-abr',	 27,	17,	       0,	    866,    	0,	   258,	      17,	   53,	   8,	   -1],
    ['02-abr',	 28,	18,	       0,	    840,    	0,	    91,	       8,	   90,	  -9,	   -5],
    ['03-abr',	 29,	19,	       0,	    635,    	0,	   181,	       6,	   90,	  54,	   21],
    ['04-abr',	 30,	20,	       0,	    356,    	0,	   151,	      12,	  287,	  43,	   16],
    ['05-abr',	 31,	21,	       0,	   1034,   	    0,	   535,	      10,	   75,	  35,	   -7],
    ['06-abr',	 32,	22,	       0,	    724,	    0,	   280,	       9,	    8,	  66,	    8],
    ['07-abr',	 33,	23,	       0,	    748,	    0,	   393,	      15,	  234,	 103,	   20],
    ['08-abr',	 34,	24,	   15616,	   1040,	  728,	   660,	      14,	  102,	  22,	    4],
    ['09-abr',	 35,	25,	    7304,	    648,	  407,	   507,	      17,	  105,	  88,	   11],
    ['10-abr',	 36,	26,	    6770,	    805,	  213,	   428,	      31,	  131,	  87,	    6],
    ['11-abr',	 37,	27,	    6916,	   1164,	  239,	   712, 	  12,	  170,	 101,	   12],
    ['12-abr',	 38,	28,	    6914,	   3209,	  165,	   506, 	  12,	   59,	  27,	   -8],
    ['13-abr',	 39,	29,	    7303,	   1042,	 1897,	   368, 	  23,	  844,	  86,	    9],
    ['14-abr',	 40,	30,	   14251,	    330,	  127,	   392, 	  14,	  227,	  13,	  -11],
    ['15-abr',	 41,	31,	    4755,	   1242,	  879,	   293, 	  24,	  239,	 199,	   14],
    ['16-abr',	 42,	32,	   10324,	    743,	  570,	   446, 	  20,	 3012,	 164,	   23],
    ['17-abr',	 43,	33,	    4212,	    835,	  561,	   437, 	  26,	  421,	 -58,	  -32],
    ['18-abr',	 44,	34,	    6631,	    820,	  651,	   280, 	  48,	  143,	  49,	  -20],
    ['19-abr',	 45,	35,	    5456,	   1186,	  828,	   380, 	  52,	  127,	  81,	   50],
    ['20-abr',	 46,	36,	    2842,	    727,	   96,	   601, 	  45,	  157,	 333,	  218],
    ['21-abr',	 47,	37,	    5316,	    885,	 1005,     507, 	  39,	   14,	 737,	   -5],
    ['22-abr',	 48,	38,	   12181,	   1082,	  822,	   591, 	  46,	   45,	  15,	   16],
    ['23-abr',	 49,	39,	   12626,	    548,	  918,	   746,	      42,	  395,	 352,	   71],
    ['24-abr',	 50,	40,	   11092,	   1285,	  110,	   624, 	  62,	   74,	 408,	   38],
    ['25-abr',	 51,	41,	   14654,	   1509,	 3270,	   413, 	  66,	  301,	 338,	   40],
    ['26-abr',	 52,	42,	   11476,	    890,	 1306,	   880,	      28,	  291,	 100,	    9],
    ['27-abr',	 53,	43,	    4685,	    949,	  775,	   407,	      54,	  337,	 336,	   44],
    ['28-abr',	 54,	44,	   24300,	   1258,	 1881,	   610,	      72,	  754,	 120,	    2],
    ['29-abr',	 55,	45,	   24695,	   1214,	 2099,	   642,	      89,	  858,	 201,	   23],
    ['30-abr',	 56,	46,	   17795,	   1150,	 2473,	   572,	     108,	  368,	 689,	   28],
    ['01-may',	 57,	47,	   19084,	   1679,	 2899,	   584,	      73,	  724,	 309,	    7],
    ['02-may',	 58,	48,	    9508,	   1523,	 1443,	   632,	      76,	 1305,	-189,	   13],
    ['03-may',	 59,	49,	   15014,	   1084,	 2836,	   558,	      86,	 1116,	 183,	    8],
    ['04-may',	 60,	50,	    7910,	   1042,	  872,	   572,	      58,	  877,	 154,	   15],
    ['05-may',	 61,	51,	   15911,	   1359,	 3405,	   412,	     100,	  986,	  74,	   15],
    ['06-may',	 62,	52,	   17260,	   1991,	 2838,	   790,	      89,	 2114,	 220,	    8],
    ['07-may',	 63,	53,	   13357,	   1496,	 2705,	  1004,	      94,	  861,	 251,	    5],
    ['08-may',	 64,	54,	   20612,	   1237,	 2500,	   821,	      87,	  624,	 175,	    8],
    ['09-may',	 65,	55,	   17506,	    386,	 2663,	   505,	     100,	 1234,	  65,	   18],
    ['10-may',	 66,	56,	    4751,	   3637,	 1816,	   476,	      75,	 1103,	 381,	   26],
    ['11-may',	 67,	57,	    3380,	   3044,	  789,	   726,       72,	 1057,	  47,	   11],
    ['12-may',	 68,	58,	   14844,      1219,     2538,	   699,       96,     918,   214,	   12],
    ['13-may',	 69,	59,	   15766,      1320,     3170,	  1077,      112,    1000,   117,	    9],
    ['14-may',	 70,	60,	   28244,      1248,     3439,	   859,       98,     827,   -38,	   36],
    ['15-may',	 71,	61,	   12186,      2014,     3278,	   613,      125,    1996,   144,	    9],
    ['16-may',	 72,	62,	   17981,      3072,     3096,	   950,      131,    1125,   190,	  -11],
    ['17-may',	 73,	63,	   13833,      2566,     3003,	   729,      125,     349,   133,	   10],
    ['18-may',	 74,	64,	    6035,      1824,     1687,	   973,      141,    1685,   101,	   16],
    ['19-may',	 75,	65,	   11944,      1956,     3718,	   832,      125,    6218,    17,	   17],
    ['20-may',	 76,	66,	   29372,      1932,     3615,	   922,      110,    5444,     7,	  -14],
    ['21-may',	 77,	67,	   13117,      3211,     4088,	   661,      124,    1619,   -78,	   17],
    ['22-may',	 78,	68,	    8441,      2656,     2457,	   472,       96,    1261,    90,	   15],
    ['23-may',	 79,	69,	   27015,      6744,     3532,	   524,      129,    3067,   129,	    8],
    ['24-may',	 80,	70,	   28401,        20,     3425,	   780,       83,    1880,   105,	   11],
    ['25-may',	 81,	71,	   15602,       333,     3011,	  1009,      173,    1154,   318,	  -11],
    ['26-may',	 82,	72,	   27110,      1917,     5126,	   646,      159,    1957,   110,	   14],
    ['27-may',	 83,	73,	   20599,      2804,     5355,	   799,      195,    3263,    60,	    3],
    ['28-may',	 84,	74,	   15908,      1737,     4823,	  1051,      116,    3273,   128,	   17],
    ['29-may',	 85,	75,	   25664,      2650,     5438,	  1068,      131,    3349,    38,	   -3],
    ['30-may',	 86,	76,	   39613,      2092,     6436,	   950,      141,    3656,    32,	    0],
    ['31-may',	 87,	77,	   34822,      2539,     7782,	  1023,      135,     761,   417,	   48],
    ['01-jun',	 88,	78,	   11807,       415,     4520,	  1043,      128,    1299,   -14,	  -13],
    ['02-jun',	 89,	79,	    7777,      3365,     4376,	   469,      133,     750,    62,	  -11],
    ['03-jun',	 90,	80,	   16586,      2353,     3614,	   416,      127,    3062,  1171,	   34],
    ['04-jun',	 91,	81,	   15606,       326,     3065,	  1219,      137,    3909, -1038,	    7],
    ['05-jun',	 92,	82,	   12611,      1824,     3616,	   586,      131,    2986,   135,	   36],
    ['06-jun',	 93,	83,	   12803,      1374,     2746,	  1612,      139,    3517,   302,	   21],
    ['07-jun',	 94,	84,	   11693,      2503,     2891,	  1866,      164,    3488,    83,	    0],
    ['08-jun',	 95,	85,	    5467,      3381,     1812,	  1369,      106,    3337,    78,	   10],
    ['09-jun',	 96,	86,	   17253,      2413,     3022,	  1018,      167,    3373,   242,	    5],
    ['10-jun',	 97,	87,	   20225,      2753,     3807,	  1280,      165,    5102,    13,	  -12],
    ['11-jun',	 98,	88,	   18139,      2618,     4971,	   994,      206,    4398,   110,	    4],
    ['12-jun',	 99,	89,	   24259,      2719,     4901,	  1060,      199,    4704,    95,	   20],
    ['13-jun',	100,	90,	   15611,      3066,     3155,	  1228,      190,    4591,   221,	   24],
    ['14-jun',	101,	91,	   15247,      2511,     3480,	  1124,      190,    3855,   -45,	   -2],
    ['15-jun',	102,	92,	    9706,      2677,     2410,	   846,      172,    3830,    -2,	   10],
    ['16-jun',	103,	93,	   13035,      2928,     2870,	  1294,      196,    5796,  -118,	   -9],
    ['17-jun',	104,	94,	   15239,      2315,     2632,	  1120,      201,    3417,    27,	   -1],
    ['18-jun',	105,	95,	   15461,      2915,     2224,	  1256,      204,    2568,    36,	   19],
    ['19-jun',	106,	96,	   15131,      2831,     2698,	   839,      199,    4330,   205,	   -4],
    ['20-jun',	107,	97,	   16554,      1330,     2839,	   574,      201,    3243,   132,	   17],
    ['21-jun',	108,	98,	   15362,      2686,     2348,	  1250,      184,    3204,   -11,	   -6],
    ['22-jun',	109,	99,	    9546,      1664,     1893,	   618,      178,    3353,   148,	    7],
    ['23-jun',	110,   100,	   15524,      2929,     2267,	  1096,      181,    3117,  -126,	   17]
    # 0         1       2       3           4       5           6       7       8           9       10
    # ['fecha', 'dia', 'cuar', 'PR_Neg', 'PM_Neg', 'PR_Pos', 'PM_Pos', 'falle', 'recup', 'hospi.', 'UCI'],
]
