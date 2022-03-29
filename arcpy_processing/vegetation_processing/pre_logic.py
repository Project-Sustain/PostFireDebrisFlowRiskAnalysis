import math


def get_lambda(vv):
    dict = {3072: {'lamb': 0.608876, 'kap': 9.554256}, 3074: {'lamb': 0.595276, 'kap': 12.689444},
     3075: {'lamb': 0.603175, 'kap': 13.493303}, 3076: {'lamb': 0.568508, 'kap': 19.890487},
     3077: {'lamb': 0.601173, 'kap': 10.759144000000001}, 3078: {'lamb': 0.593225, 'kap': 22.948819},
     3079: {'lamb': 0.636734, 'kap': 11.344964}, 3080: {'lamb': 0.6246010000000001, 'kap': 10.803938},
     3081: {'lamb': 0.599614, 'kap': 12.082208}, 3082: {'lamb': 0.601524, 'kap': 11.185928},
     3083: {'lamb': 0.7263069999999999, 'kap': 7.633421}, 3084: {'lamb': 0.67981, 'kap': 6.273912},
     3085: {'lamb': 0.640443, 'kap': 5.517478}, 3086: {'lamb': 0.665588, 'kap': 6.146408999999999},
     3087: {'lamb': 0.588298, 'kap': 12.600827}, 3088: {'lamb': 0.6671739999999999, 'kap': 11.21568},
     3090: {'lamb': 0.550409, 'kap': 17.774182}, 3091: {'lamb': 0.598849, 'kap': 16.470602},
     3092: {'lamb': 0.6504409999999999, 'kap': 7.6431130000000005}, 3093: {'lamb': 0.611408, 'kap': 9.942192},
     3094: {'lamb': 0.5719489999999999, 'kap': 16.430422}, 3095: {'lamb': 0.58827, 'kap': 12.435880000000001},
     3096: {'lamb': 0.6990109999999999, 'kap': 8.150509}, 3097: {'lamb': 0.7057640000000001, 'kap': 7.955055000000001},
     3098: {'lamb': 0.802425, 'kap': 7.453416000000001}, 3099: {'lamb': 0.6739569999999999, 'kap': 7.352289},
     3100: {'lamb': 0.593441, 'kap': 13.122897}, 3101: {'lamb': 0.61365, 'kap': 13.993376000000001},
     3103: {'lamb': 0.6611560000000001, 'kap': 8.506929}, 3104: {'lamb': 0.640868, 'kap': 8.657786},
     3105: {'lamb': 0.691721, 'kap': 7.821115}, 3106: {'lamb': 0.686529, 'kap': 6.343075},
     3107: {'lamb': 0.678304, 'kap': 7.090649000000001}, 3108: {'lamb': 0.688427, 'kap': 9.177896},
     3109: {'lamb': 0.579543, 'kap': 12.059941}, 3110: {'lamb': 0.6786479999999999, 'kap': 7.917302},
     3111: {'lamb': 0.566117, 'kap': 16.049973}, 3112: {'lamb': 0.642429, 'kap': 6.224311},
     3113: {'lamb': 0.712126, 'kap': 8.100275}, 3114: {'lamb': 0.687451, 'kap': 8.058461999999999},
     3115: {'lamb': 0.656496, 'kap': 10.119860000000001}, 3116: {'lamb': 0.596608, 'kap': 11.456971000000001},
     3117: {'lamb': 0.636522, 'kap': 8.217602000000001}, 3118: {'lamb': 0.7515029999999999, 'kap': 7.066463000000001},
     3119: {'lamb': 0.599672, 'kap': 15.591541000000001}, 3121: {'lamb': 0.5836640000000001, 'kap': 10.978747},
     3122: {'lamb': 0.5781029999999999, 'kap': 24.549737}, 3123: {'lamb': 0.632791, 'kap': 8.410206},
     3124: {'lamb': 0.622892, 'kap': 10.638791000000001}, 3125: {'lamb': 0.634029, 'kap': 10.297422000000001},
     3126: {'lamb': 0.658222, 'kap': 8.714561}, 3127: {'lamb': 0.626424, 'kap': 10.224508},
     3128: {'lamb': 0.652786, 'kap': 7.184285000000001}, 3129: {'lamb': 0.685063, 'kap': 7.893296},
     3130: {'lamb': 0.661845, 'kap': 8.48207}, 3131: {'lamb': 0.817102, 'kap': 11.776172},
     3132: {'lamb': 0.603831, 'kap': 17.601837}, 3133: {'lamb': 0.576926, 'kap': 15.629403},
     3134: {'lamb': 0.655752, 'kap': 8.886499}, 3135: {'lamb': 0.675245, 'kap': 6.822644},
     3137: {'lamb': 0.745613, 'kap': 8.612923}, 3138: {'lamb': 0.8246530000000001, 'kap': 7.567721000000001},
     3139: {'lamb': 0.728486, 'kap': 6.162368}, 3140: {'lamb': 0.8277899999999999, 'kap': 7.284992},
     3141: {'lamb': 0.6645840000000001, 'kap': 6.960683}, 3142: {'lamb': 0.646487, 'kap': 9.428351},
     3143: {'lamb': 0.588245, 'kap': 6.638936}, 3144: {'lamb': 0.642137, 'kap': 6.340822},
     3145: {'lamb': 0.7341270000000001, 'kap': 5.982246}, 3146: {'lamb': 0.752462, 'kap': 5.5196629999999995},
     3147: {'lamb': 0.617524, 'kap': 9.916105}, 3148: {'lamb': 0.636359, 'kap': 9.430411999999999},
     3149: {'lamb': 0.589646, 'kap': 10.752298}, 3151: {'lamb': 0.66973, 'kap': 9.111936},
     3152: {'lamb': 0.70898, 'kap': 6.509723999999999}, 3153: {'lamb': 0.6154850000000001, 'kap': 8.874967999999999},
     3154: {'lamb': 0.6624800000000001, 'kap': 8.380697}, 3155: {'lamb': 0.631836, 'kap': 7.849353},
     3156: {'lamb': 0.682704, 'kap': 6.613065}, 3157: {'lamb': 0.713232, 'kap': 6.113748},
     3158: {'lamb': 0.724286, 'kap': 5.854808}, 3159: {'lamb': 0.6768569999999999, 'kap': 6.137937},
     3160: {'lamb': 0.667077, 'kap': 6.159486}, 3161: {'lamb': 0.735789, 'kap': 5.897436},
     3162: {'lamb': 0.678106, 'kap': 7.055992999999999}, 3163: {'lamb': 0.629798, 'kap': 10.246064},
     3164: {'lamb': 0.634853, 'kap': 5.686743}, 3165: {'lamb': 0.681354, 'kap': 7.854475},
     3166: {'lamb': 0.745417, 'kap': 5.894642}, 3167: {'lamb': 0.764379, 'kap': 6.047857},
     3168: {'lamb': 0.696558, 'kap': 7.543603999999999}, 3169: {'lamb': 0.6797810000000001, 'kap': 7.236514},
     3170: {'lamb': 0.6502600000000001, 'kap': 10.618886}, 3171: {'lamb': 0.800742, 'kap': 6.516868},
     3172: {'lamb': 0.7408560000000001, 'kap': 6.941702}, 3173: {'lamb': 0.680733, 'kap': 7.345917999999999},
     3174: {'lamb': 0.7791359999999999, 'kap': 5.809551}, 3177: {'lamb': 0.6349090000000001, 'kap': 12.009025999999999},
     3178: {'lamb': 0.779, 'kap': 6.337798}, 3179: {'lamb': 0.697527, 'kap': 7.912414},
     3180: {'lamb': 0.67067, 'kap': 7.222474000000001}, 3181: {'lamb': 0.617426, 'kap': 10.341983},
     3182: {'lamb': 0.663225, 'kap': 6.862074000000001}, 3183: {'lamb': 0.629574, 'kap': 9.840602},
     3184: {'lamb': 0.672324, 'kap': 7.436881}, 3186: {'lamb': 0.672786, 'kap': 9.07408},
     3195: {'lamb': 0.597086, 'kap': 5.908623}, 3198: {'lamb': 0.659714, 'kap': 7.620064999999999},
     3200: {'lamb': 0.665303, 'kap': 6.915078}, 3201: {'lamb': 0.676913, 'kap': 7.083305},
     3202: {'lamb': 0.61695, 'kap': 6.088512000000001}, 3203: {'lamb': 0.6367010000000001, 'kap': 7.641017},
     3204: {'lamb': 0.570802, 'kap': 25.348731}, 3206: {'lamb': 0.708617, 'kap': 6.608194999999999},
     3208: {'lamb': 0.722634, 'kap': 6.773067}, 3210: {'lamb': 0.616672, 'kap': 13.730604999999999},
     3211: {'lamb': 0.6146550000000001, 'kap': 13.210264000000002}, 3212: {'lamb': 0.573217, 'kap': 16.457179},
     3213: {'lamb': 0.5676329999999999, 'kap': 16.116451}, 3214: {'lamb': 0.65778, 'kap': 9.574225},
     3215: {'lamb': 0.646093, 'kap': 8.807856}, 3216: {'lamb': 0.695516, 'kap': 8.344719},
     3217: {'lamb': 0.6956180000000001, 'kap': 6.471208}, 3218: {'lamb': 0.606417, 'kap': 8.273922},
     3219: {'lamb': 0.621206, 'kap': 12.521192999999998}, 3220: {'lamb': 0.660725, 'kap': 9.476563},
     3221: {'lamb': 0.6356069999999999, 'kap': 7.104800999999999}, 3222: {'lamb': 0.6597270000000001, 'kap': 9.266706},
     3227: {'lamb': 0.753627, 'kap': 5.995462}, 3228: {'lamb': 0.732049, 'kap': 5.583948},
     3230: {'lamb': 0.70309, 'kap': 8.7159}, 3231: {'lamb': 0.716932, 'kap': 5.136423000000001},
     3232: {'lamb': 0.7265199999999999, 'kap': 5.783837999999999}, 3233: {'lamb': 0.700166, 'kap': 6.080787},
     3234: {'lamb': 0.691195, 'kap': 6.12919}, 3235: {'lamb': 0.71877, 'kap': 6.103695},
     3236: {'lamb': 0.666756, 'kap': 6.089024}, 3237: {'lamb': 0.601816, 'kap': 10.005522000000001},
     3250: {'lamb': 0.6099859999999999, 'kap': 8.940577000000001}, 3251: {'lamb': 0.6477310000000001, 'kap': 7.131933},
     3252: {'lamb': 0.6920430000000001, 'kap': 7.6452539999999996}, 3253: {'lamb': 0.705749, 'kap': 8.199177},
     3254: {'lamb': 0.742317, 'kap': 6.1292290000000005}, 3255: {'lamb': 0.664176, 'kap': 8.48668},
     3256: {'lamb': 0.6153569999999999, 'kap': 9.088341}, 3258: {'lamb': 0.704509, 'kap': 7.063811},
     3259: {'lamb': 0.739606, 'kap': 10.534496}, 3260: {'lamb': 0.72415, 'kap': 9.594017},
     3261: {'lamb': 0.702588, 'kap': 6.960286}, 3262: {'lamb': 0.622804, 'kap': 14.867572000000001},
     3263: {'lamb': 0.631422, 'kap': 9.880709}, 3264: {'lamb': 0.657018, 'kap': 9.0444},
     3265: {'lamb': 0.692772, 'kap': 9.006765}, 3266: {'lamb': 0.748238, 'kap': 6.186673000000001},
     3267: {'lamb': 0.705997, 'kap': 5.861149}, 3292: {'lamb': 0.606672, 'kap': 5.211508},
     3293: {'lamb': 0.574769, 'kap': 6.370316000000001}, 3294: {'lamb': 0.592199, 'kap': 9.022155},
     3295: {'lamb': 0.60247, 'kap': 8.099817999999999}, 3296: {'lamb': 0.6804140000000001, 'kap': 5.715173},
     3297: {'lamb': 0.6707529999999999, 'kap': 5.861445}, 3298: {'lamb': 0.666361, 'kap': 6.630944},
     3299: {'lamb': 0.6509659999999999, 'kap': 7.50623}, 3541: {'lamb': 0.678946, 'kap': 7.515647},
     3542: {'lamb': 0.672941, 'kap': 6.525685}, 3543: {'lamb': 0.6916859999999999, 'kap': 8.166815},
     3544: {'lamb': 0.631962, 'kap': 9.602994}, 3545: {'lamb': 0.656208, 'kap': 8.795045},
     3548: {'lamb': 0.663275, 'kap': 7.3068029999999995}, 3549: {'lamb': 0.670623, 'kap': 8.090195},
     3385: {'lamb': 0.5930300000000001, 'kap': 7.403039}, 3900: {'lamb': 0.646809, 'kap': 7.694555},
     3901: {'lamb': 0.64103, 'kap': 6.986128}, 3902: {'lamb': 0.66982, 'kap': 7.664855},
     3903: {'lamb': 0.674953, 'kap': 6.204025}, 3904: {'lamb': 0.668092, 'kap': 5.635228},
     3910: {'lamb': 0.66928, 'kap': 7.292333999999999}, 3911: {'lamb': 0.674569, 'kap': 6.593017},
     3912: {'lamb': 0.6737890000000001, 'kap': 8.783192999999999}, 3913: {'lamb': 0.661555, 'kap': 7.192363},
     3914: {'lamb': 0.681898, 'kap': 6.0658769999999995}, 3920: {'lamb': 0.684815, 'kap': 6.878709},
     3921: {'lamb': 0.670814, 'kap': 6.855111}, 3922: {'lamb': 0.6607310000000001, 'kap': 21.023518},
     3923: {'lamb': 0.654663, 'kap': 7.551755}, 3924: {'lamb': 0.655816, 'kap': 7.582474},
     3925: {'lamb': 0.741942, 'kap': 7.872522}, 3926: {'lamb': 0.6288699999999999, 'kap': 9.803202},
     3927: {'lamb': 0.624202, 'kap': 12.772528999999999}, 3928: {'lamb': 0.753324, 'kap': 7.226752},
     3929: {'lamb': 0.666659, 'kap': 8.935941999999999}, 3941: {'lamb': 0.603988, 'kap': 9.728315},
     3943: {'lamb': 0.64485, 'kap': 7.302919999999999}, 3944: {'lamb': 0.710109, 'kap': 5.700809},
     3945: {'lamb': 0.704511, 'kap': 12.803496}, 3948: {'lamb': 0.702117, 'kap': 6.128476},
     3949: {'lamb': 0.6189819999999999, 'kap': 15.833986}, 3960: {'lamb': 0.62642, 'kap': 5.943006},
     3961: {'lamb': 0.642508, 'kap': 6.873025}, 3962: {'lamb': 0.638862, 'kap': 17.353013},
     3963: {'lamb': 0.5585640000000001, 'kap': 21.666421}, 3964: {'lamb': 0.67804, 'kap': 4.912529},
     3965: {'lamb': 0.623267, 'kap': 6.630356}, 3966: {'lamb': 0.6559159999999999, 'kap': 8.600867},
     3967: {'lamb': 0.682815, 'kap': 8.699487}, 3968: {'lamb': 0.68829, 'kap': 5.136817},
     3980: {'lamb': 0.742987, 'kap': 8.137224}, 3981: {'lamb': 0.686562, 'kap': 12.067155},
     3983: {'lamb': 0.721653, 'kap': 6.1891739999999995}, 3984: {'lamb': 0.6193569999999999, 'kap': 10.584835},
     3985: {'lamb': 0.679779, 'kap': 7.457021000000001}, 3986: {'lamb': 0.596504, 'kap': 8.931851},
     3987: {'lamb': 0.721641, 'kap': 9.877735000000001}, 3988: {'lamb': 0.5394800000000001, 'kap': 4.709144},
     3495: {'lamb': 0.707325, 'kap': 7.451296000000001}, 3503: {'lamb': 0.58706, 'kap': 13.54606},
     3504: {'lamb': 0.60995, 'kap': 13.412417000000001}, 3001: {'lamb': 0.632514, 'kap': 8.408742},
     3002: {'lamb': 0.632444, 'kap': 9.325526}, 3003: {'lamb': 0.6534310000000001, 'kap': 6.778563},
     3004: {'lamb': 0.5836680000000001, 'kap': 11.017458999999999}, 3006: {'lamb': 0.643514, 'kap': 7.642705},
     3007: {'lamb': 0.582511, 'kap': 10.815818}, 3008: {'lamb': 0.706348, 'kap': 8.195769},
     3009: {'lamb': 0.7078909999999999, 'kap': 7.000488000000001}, 3011: {'lamb': 0.69898, 'kap': 6.955144000000001},
     3012: {'lamb': 0.722278, 'kap': 6.886242}, 3014: {'lamb': 0.773143, 'kap': 7.918473},
     3015: {'lamb': 0.647936, 'kap': 8.099978}, 3016: {'lamb': 0.6685479999999999, 'kap': 7.90239},
     3017: {'lamb': 0.638473, 'kap': 8.835191}, 3018: {'lamb': 0.728296, 'kap': 5.920661},
     3019: {'lamb': 0.668816, 'kap': 9.481709}, 3020: {'lamb': 0.671331, 'kap': 7.593489},
     3021: {'lamb': 0.763766, 'kap': 7.924175}, 3022: {'lamb': 0.7743800000000001, 'kap': 7.449428999999999},
     3023: {'lamb': 0.6639609999999999, 'kap': 8.075642}, 3024: {'lamb': 0.692509, 'kap': 7.267266},
     3025: {'lamb': 0.663195, 'kap': 7.387946}, 3026: {'lamb': 0.687602, 'kap': 7.752852000000001},
     3027: {'lamb': 0.736717, 'kap': 6.493999}, 3028: {'lamb': 0.731633, 'kap': 5.979007},
     3029: {'lamb': 0.733078, 'kap': 7.114673}, 3030: {'lamb': 0.730038, 'kap': 6.852595},
     3031: {'lamb': 0.719615, 'kap': 7.028214999999999}, 3032: {'lamb': 0.684612, 'kap': 6.265625},
     3033: {'lamb': 0.662587, 'kap': 7.677532000000001}, 3034: {'lamb': 0.67718, 'kap': 8.071193},
     3035: {'lamb': 0.738176, 'kap': 6.078228}, 3036: {'lamb': 0.687317, 'kap': 14.380870999999999},
     3037: {'lamb': 0.747749, 'kap': 5.959131}, 3038: {'lamb': 0.7748109999999999, 'kap': 5.055087},
     3039: {'lamb': 0.707391, 'kap': 6.776358}, 3041: {'lamb': 0.790366, 'kap': 6.48035},
     3042: {'lamb': 0.773405, 'kap': 6.037758}, 3043: {'lamb': 0.76385, 'kap': 6.30255},
     3044: {'lamb': 0.71536, 'kap': 6.499391999999999}, 3045: {'lamb': 0.7432989999999999, 'kap': 5.74584},
     3046: {'lamb': 0.779638, 'kap': 6.118671}, 3047: {'lamb': 0.7192, 'kap': 5.697763},
     3048: {'lamb': 0.819185, 'kap': 6.503533}, 3049: {'lamb': 0.6733939999999999, 'kap': 6.8478449999999995},
     3050: {'lamb': 0.800137, 'kap': 6.22125}, 3051: {'lamb': 0.701717, 'kap': 6.770211},
     3052: {'lamb': 0.729264, 'kap': 6.451631}, 3053: {'lamb': 0.684154, 'kap': 6.759456},
     3054: {'lamb': 0.652131, 'kap': 7.095453}, 3055: {'lamb': 0.79814, 'kap': 6.264928},
     3056: {'lamb': 0.79814, 'kap': 5.937163}, 3057: {'lamb': 0.690934, 'kap': 7.25091},
     3058: {'lamb': 0.690592, 'kap': 6.133401999999999}, 3059: {'lamb': 0.631867, 'kap': 8.617233},
     3060: {'lamb': 0.616876, 'kap': 9.332206}, 3061: {'lamb': 0.71006, 'kap': 6.566425},
     3062: {'lamb': 0.706436, 'kap': 6.925667999999999}, 3063: {'lamb': 0.669763, 'kap': 8.055613000000001},
     3064: {'lamb': 0.636309, 'kap': 9.294118}, 3065: {'lamb': 0.633478, 'kap': 9.620666},
     3066: {'lamb': 0.558978, 'kap': 14.025179000000001}, 3068: {'lamb': 0.841242, 'kap': 9.105216},
     3070: {'lamb': 0.647833, 'kap': 6.925736}, 3071: {'lamb': 0.6379729999999999, 'kap': 9.624375}}

    kk = int(vv)
    if kk in dict:
        lamb = dict[kk]['lamb']
        k = dict[kk]['kap']
        dnbr = math.pow(math.log(0.1)*-1, (1/k))
        dnbr = dnbr*2000*lamb - 1000
        return int(dnbr)
    else:
        return 0

print(get_lambda(3070))