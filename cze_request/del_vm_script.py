import requests
falg = 0  #防误删开关
del_vm_list = [455142531, 128030112, 128085384, 128023285, 108027072, 215003541, 128030130, 128023941, 128023874, 800000847, 128030907, 128085900, 122016318, 128030957, 128030766, 128023792, 455142436, 128085463, 128030522, 404157430, 128085805, 128023197, 800000101, 128023919, 128023153, 128023856, 128030054, 128023840, 405876364, 128030675, 128023347, 128095493, 128023373, 128030758, 128023651, 128030999, 128030223, 128023261, 128085471, 128023523, 128023436, 128023397, 128030948, 128023538, 128023384, 128030941, 457710013, 128030822, 128023379, 128115681, 128023603, 128030064, 455435855, 457710215, 128030554, 128085341, 128023095, 128023151, 128085730, 108027843, 128095219, 128023121, 128085242, 128023709, 128030932, 123012900, 128085877, 128023850, 455347202, 222010300, 131018279, 128023430, 128030736, 128030067, 128030752, 128023018, 455142101, 128030433, 128023755, 128023592, 128030548, 128023256, 128030323, 128085241, 131017318, 128023412, 128030426, 128095291, 457710870, 128023082, 566415605, 128030600, 128023541, 128023807, 128030443, 128023001, 128030559, 128023907, 128030884, 455347786, 128023661, 128023528, 566921103, 128030898, 128085956, 128085559, 128030020, 317000956, 455435882, 128030998, 128095376, 128023507, 128030212, 128023016, 128023915, 128023989, 131018458, 128023181, 128023580, 108007071, 128023022, 128023617, 128095402, 128030260, 128023083, 800000122, 128085163, 455911997, 128030123, 128023522, 455911982, 128023799, 128034280, 128023894, 128023821, 128023389, 128023062, 404527549, 455911197, 128030461, 128023722, 128023427, 128030343, 128023930, 455347793, 215003277, 128030687, 128030705, 128030284, 128023368, 128030735, 455773389, 128030397, 128030595, 128085721, 457710176, 128023597, 128030018, 128030506, 128023639, 128085148, 128023666, 128030219, 128030903, 128023117, 128023687, 128030677, 128023186, 128023691, 128030006, 455292827, 128030234, 128030474, 128030891, 128023526, 128023826, 455292849, 128023450, 128023390, 128030586, 128030259, 128023171, 128023411, 128023647, 128023726, 128030292, 128023464, 128085445, 128023817, 800000550, 128023380, 128023876, 128023754, 128030281, 128030274, 128023474, 128085728, 128030300, 128023189, 128085136, 128085156, 128085325, 128023135, 128023535, 128023985, 128085406, 404527139, 455142691, 128030978, 128023924, 455347022, 128023317, 128023521, 128030226, 128023607, 128023394, 128023495, 128030523, 128085080, 128030431, 128023772, 455142250, 128030087, 566921900, 128023982, 454510222, 128085477, 457710611, 128030592, 108007396, 128023326, 128085644, 800000049, 128023144, 455142308, 128023680, 800000302, 128023097, 128023971, 455773435, 128023480, 128030061, 128030875, 131019671, 128106196, 128030588, 128023354, 457710406, 128023547, 128085391, 128085603, 131017097, 404527033, 128030003, 128095594, 128085176, 128091507, 128115123, 128030771, 128095454, 128023213, 128030777, 122021978, 128023518, 800000996, 128030120, 128023293, 128023106, 800000962, 128023837, 128023329, 316001520, 128030810, 128085716, 128023065, 800000121, 128030996, 128023670, 128023551, 128030652, 128023116, 122007435, 128085622, 128023682, 128023141, 128085981, 128030391, 128023100, 128085965, 800000878, 800000515, 128030745, 128023690, 800000526, 128023554, 128030068, 128023768, 455142251, 128023544, 128023698, 455142061, 128095552, 128023575, 128030312, 128115454, 128030100, 128023997, 128023156, 128085299, 128030279, 128030995, 128023711, 128085112, 128095533, 128023048, 455773053, 128095063, 128023619, 128085893, 128023626, 128030403, 128023124, 128030813, 128023115, 128023596, 215115669, 316004920, 455292420, 123012952, 128030608, 128023645, 128023694, 457710077, 457710392, 128030439, 128091833, 455347140, 128023227, 128091296, 128030648, 455347153, 131019854, 217012791, 128095756, 128023546, 128030339, 128023343, 131019460, 455773476, 455292126, 128085867, 317000380, 455142904, 800000621, 128084828, 128085143, 128030869, 128085942, 128023608, 128023301, 128023180, 455292021, 128023669, 128095568, 128095785, 128030465, 128030728, 128023246, 128030833, 128023558, 128023775, 800000599, 128030023, 128023453, 128085708, 128023732, 128030814, 108024825, 800000828, 128030888, 128030046, 128030499, 128023298, 128030230, 128030878, 215003403, 128023350, 128085036, 128085944, 128023143, 131019211, 128030232, 108007853, 128030319, 128023978, 128023967, 128023654, 128023485, 128085290, 128085515, 128023834, 128030316, 128023892, 128030632, 128030783, 128030258, 123012968, 128030569, 454510951, 455142219, 128023927, 128115564, 128023723, 128085970, 128023237, 128030609, 128023313, 128030692, 128023377, 128023943, 128030790, 455142030, 128023036, 128085961, 128023855, 128030137, 128023974, 128023632, 455347539, 128030906, 215051416, 128023996, 128030059, 128030764, 128023865, 128023234, 135002277, 128023309, 128030972, 128085182, 128023668, 128030557, 128023057, 128023207, 128030566, 128151105, 128023637, 128023689, 455142240, 455435715, 128023333, 131019525, 128023149, 128030475, 128023292, 800000093, 128030215, 128240920, 128023179, 128030635, 128030298, 128085123, 128023214, 128023224, 128095969, 800000852, 217012724, 128023987, 128085142, 128085096, 128030374, 215011484, 128085519, 128085557, 455773402, 128023491, 128023763, 128023885, 800000501, 800000420, 128023663, 128030841, 128030229, 454510329, 122002989, 128023471, 128023221, 128095703, 128023714, 128023399, 800000564, 128030044, 128023452, 128030657, 128023249, 455142302, 128023770, 128030124, 404157948, 128023797, 131018985, 128023497, 128030997, 128085369, 128023804, 128023136, 128115101, 128023147, 128030897, 128085691, 128030447, 128085912, 128091842, 455911631, 128091564, 128023869, 128030984, 128023794, 128030199, 457710148, 128023683, 128023381, 128023777, 128023288, 128023731, 128023139, 128030019, 128023881, 128030195, 128023902, 128030560, 128030847, 127042377, 128023372, 128030890, 128023279, 128030009, 128030038, 128030221, 455142138, 128085470, 131018068, 128023702, 215003414, 128023500, 128023942, 128030956, 128023533, 123013008, 128023052, 128085401, 128023727, 128030975, 128030901, 128030727, 128030493, 128023564, 457710387, 128085593, 128023386, 128023046, 128023980, 128023646, 128146577, 128030220, 128023773, 128085795, 455292123, 128023304, 317000618, 128030495, 455142905, 128023119, 128023740, 128023969, 128030532, 128030496, 128023764, 128085082, 128030631, 128085971, 128023185, 128030852, 455292248, 455142039, 128085012, 131017521, 128023830, 128023977, 128023320, 128030193, 128030508, 128030482, 128023571, 405876607, 128023801, 128023445, 128023901, 128023178, 128085025, 128085274, 128023013, 128023791, 128030748, 800000675, 215065296, 128030487, 128023955, 128023756, 128023266, 128030071, 455142957, 405876844, 128023602, 128023262, 128030874, 128023299, 455773785, 128023031, 128023244, 128030412, 128023325, 128023940, 455435301, 128023259, 122016305, 128023345, 457710399, 128023456, 128023150, 128085949, 128085359, 128023573, 128030498, 128023748, 128023947, 128023129, 128030146, 128085286, 128085014, 128085533, 128030180, 800000507, 128023111, 128030866, 128023357, 128023015, 128030209, 128023710, 455773339, 455292053, 800000927, 128023998, 455142864, 128095795, 128023087, 128030962, 455142919, 128030294, 455142095, 128085119, 128030049, 128115614, 128023418, 455142514, 128106331, 128085104, 128030141, 128040851, 128023478, 128095220, 800000381, 128079511, 123013917, 128023462, 455142767, 455292515, 128023570, 128023781, 128023800, 128023793, 128023561, 128023900, 455142264, 128030562, 128085975, 128030794, 128023676, 128106272, 128095763, 128095929, 128023638, 128030602, 128030476, 457710020, 128023633, 128023243, 800000483, 128030726, 128023205, 128023583, 455142007, 128085843, 128023873, 128030701, 128030854, 128030217, 128023757, 128023202, 128023421, 128030886, 128023921, 128023871, 128091598, 403659664, 128023437, 128030492, 128023909, 128085278, 128023043, 128085162, 455911683, 128023922, 128095114, 128023159, 128030723, 128023275, 128030010, 128023158, 128023590, 128030993, 128030005, 800000390, 128030455, 128085062, 800000793, 128085393, 128023566, 128023640, 128023577, 128023636, 128023606, 128023414, 128023771, 128023622, 128085265, 128023282, 128023463, 128030788, 128095766, 128023223, 455142262, 128023406, 128085061, 128023378, 131018819, 128085499, 128030589, 457710059, 128023906, 800000171, 108027909, 128095116, 128023435, 128030876, 128023910, 455911542, 128023477, 131018100, 128095405, 128030158, 128023310, 455435264, 128030311, 128030734, 128030249, 128085548, 128023644, 128085235, 128023222, 800000580, 128023704, 128030007, 128023724, 128030241, 128085513, 128030291, 128030497, 457710871, 128030816, 128030347, 800000826, 455347293, 128030016, 128023845, 128023665, 128030367, 128095710, 128023024, 128023509, 128023175, 455292588, 128023148, 455142205, 457710028, 128023494, 128085838, 217013380, 128023188, 128030939, 128030871, 128023058, 128030870, 128023743, 128085851, 128034996, 128030205, 128023890, 128023868, 405876717, 128085373, 128030026, 131019141, 128023667, 128030407, 128085709, 128095627, 128023348, 455435601, 108007219, 800000752, 128023814, 128030074, 128023278, 128023042, 128023769, 128030564, 128023451, 455142257, 128085589, 128023349, 128095879, 128023238, 128095398, 128085005, 128023653, 128085334, 455347211, 128030964, 128023318, 457710779, 128030660, 128023789, 128030389, 128030672, 128030383, 800000463, 128095893, 128030578, 455142645, 217013433, 128023049, 128095701, 128023945, 128030740, 128023442, 128085178, 128023002, 128030547, 800000041, 128091358, 800000965, 128030011, 127041323, 128085472, 128085705, 455435164, 128030819, 128023656, 128030919, 800000686, 128085572, 128030828, 128023916, 128030836, 800000477, 128030616, 128023934, 128023041, 128030408, 128023620, 128023697, 128085511, 128023952, 128085315, 128030142, 128023508, 128030676, 455911030, 128023093, 122007810, 457710061, 316005523, 128085804, 128085042, 457710124, 128085146, 128030851, 128023655, 128023140, 128030823, 128091840, 128023759, 455292328, 128023066, 128023578, 128023643, 128030612, 128023410, 455347409, 128030207, 128023302, 128023539, 800000403, 128023426, 128030053, 128023084, 128030052, 128030189, 128030988, 404076011, 128023413, 128023631, 455142327, 128023070, 128023502, 128023020, 128085922, 128023204, 128030622, 131017320, 128085338, 128023795, 128030159, 128030923, 128023882, 128023543, 457710560, 128023984, 128023569, 128030895, 128023858, 128023751, 800000677, 455142648, 128030720, 128085529, 128030640, 128023506, 122007318, 131018437, 128023339, 128030963, 128091143, 457710740, 128023201, 128023492, 128023994, 128023432, 128023499, 128030504, 128106279, 128085270, 128030309, 128023277, 128106881, 131017558, 128030321, 457710484, 128030795, 128085158, 128085411, 128023490, 800000411, 128085512, 455142462, 128030593, 128023154, 128095232, 128030183, 128023229, 128023498, 128085940, 405876439, 128106358, 128085057, 128023382, 128023405, 128023231, 128030114, 405876997, 108007640, 128023174, 128023312, 128023363, 128085714, 128023926, 455347797, 128030680, 128023055, 128023678, 128030804, 128085328, 128085824, 128240661, 455347646, 128023904, 800000856, 128085994, 128023362, 128095018, 457710279, 128030787, 457710637, 128023730, 128023517, 800000070, 128085353, 128085483, 128030021, 128023233, 128023454, 800000605, 128023988, 455347272, 128023593, 128023257, 128085026, 800000150, 455142926, 455142667, 128030090, 215011100, 455911785, 455292919, 128023741, 455142242, 128023417, 128023515, 455292874, 128030877, 128030364, 128085492, 455347197, 128023944, 128085902, 128023859, 455142827, 128085218, 128085081, 128085611, 455347871, 128023601, 455142637, 128023931, 128030744, 128023966, 128023176, 128023192, 215115271, 128115398, 128023893, 128023086, 128095502, 128023008, 128095794, 128030380, 128023780, 128023327, 128023431, 128023367, 128095803, 455911591, 128030167, 131018357, 800000631, 455911130, 457710920, 128085317, 128030797, 455815998, 128030333, 457710424, 455435122, 499000504, 128085899, 128023513, 128106232, 128023145, 128030346, 128023356, 128023567, 128023720, 128085375, 128023778, 800000799, 128095321, 128030959, 455911383, 128030525, 128095067, 128023358, 128023905, 128023514, 128030808, 800000312, 128095176, 128030422, 128023765, 128030954, 128030904, 128095549, 215115744, 800000610, 131019085, 800000207, 455435332, 128023565, 455142089, 128030237, 128085329, 128023648, 128023415, 128023470, 128023976, 455911555, 455142158, 455142422, 128030131, 128023938, 128023735, 128023835, 125011773, 800000654, 128023812, 128023584, 128023342, 455347736, 128023212, 128115962, 128023166, 128030341, 455347287, 128030667, 455142203, 128030305, 128085600, 128030688, 128085468, 128023194, 128095837, 128023403, 128023716, 128030469, 128023284, 128085500, 128085630, 128030178, 128030048, 128023860, 128106131, 128030153, 128030186, 800000803, 128030306, 128023090, 128085347, 128023783, 128030782, 128085780, 128085003, 128085837, 128023879, 128023160, 133022311, 800000432, 128030031, 128023023, 215111506, 128085555, 128030857, 800000815, 128030104, 128030802, 215003802, 128023025, 128023134, 215114681, 123012334, 128085425, 128023088, 128030417, 215093362, 128023424, 128023215, 128095374, 128023613, 128085839, 128023660, 128023823, 128023078, 128023679, 128030765, 128023270, 128023746, 128023007, 128085679, 128023624, 128023420, 128023627, 128030024, 128023504, 128091531, 128023658, 128085034, 128106583, 108027905, 128023392, 128030252, 128023053, 128030545, 128023742, 128030960, 455435358, 128030709, 128030707, 215116322, 800000119, 128023273, 128023695, 128085710, 455773437, 128023045, 128030151, 128084767, 128095730, 457710716, 128030605, 128023511, 128095068, 128023071, 215003921, 128085113, 128023822, 128085446, 128030971, 128085556, 128030930, 128030908, 128085170, 128085417, 566415696, 455773198, 128030423, 128023634, 800000246, 128023004, 128023364, 128030721, 455347295, 128023642, 131018791, 128023530, 455142231, 128030881, 215011797, 455142786, 128030666, 128030789, 455142127, 455142679, 455292246, 457710854, 128023408, 455347828, 128095841, 128023854, 405876985, 217012711, 128030661, 128023118, 128023662, 455142005, 128030334, 128023550, 128085052, 128030591, 128085982, 455435117, 128023434, 128023072, 128023784, 128030598, 128023322, 405876279, 128095999, 128095586, 128023242, 128023440, 128030806, 128030843, 457710832, 800000785, 128023516, 128085687, 128030315, 128030213, 128030392, 128030168, 128030684, 128023501, 800000069, 403659423, 128023260, 128030944, 128030537, 128030873, 128023493, 455142704, 128151004, 128023033, 128095071, 128023923, 128030386, 128095340, 128023076, 128023641, 128023512, 128023401, 128023483, 128030004, 128023672, 128023034, 128095392, 128030681, 455142184, 800000873, 128030028, 128030946, 128023056, 128023872, 128030225, 215051477, 128030761, 128023962, 128030037, 455347052, 128023258, 128023061, 800000247, 128023460, 128023105, 128023027, 455773532, 128023560, 128030155, 215116269, 128023168, 128023805, 128023796, 128030069, 800000480, 128030396, 128023157, 128095305, 128030489, 128023939, 128030934, 128030717, 128030181, 128023051, 128030775, 455773621, 128030032, 128030575, 455347977, 128023582, 128023824, 128085188, 128023321, 128030135, 455142489, 128023861, 128030610, 128085009, 128030103, 800000853, 455773187, 455773088, 128023096, 128023481, 128023209, 800000539, 455773355, 128023295, 128023063, 215003830, 128085332, 128030204, 128023198, 128023598, 128023128, 128023818, 128023649, 128085221, 128023054, 128030834, 128023820, 128095312, 128095375, 128085993, 128023545, 128023761, 566921525, 128023396, 128030540, 128023290, 128085561, 128030977, 128030986, 128030550, 128023883, 128023717, 405876126, 128023935, 128095408, 128023383, 128023467, 128085596, 455292335, 128030373, 128023810, 128023745, 128085402, 128023486, 128030973, 455292105, 128095295, 128085092, 128030464, 800000205, 128106997, 128023289, 128030955, 128085595, 405768981, 457710045, 128023303, 800000193, 122007814, 128095528, 128023429, 128023255, 128030922, 128023067, 128023857, 128023707, 128085807, 128030381, 128030261, 455347468, 128023359, 128030510, 128023621, 800000337, 128023524, 128030262, 215011399, 215011770, 128023749, 128023281, 128023050, 128106471, 128030320, 404527858, 128085754, 128030283, 128030776, 215011442, 128030266, 455142027, 128023949, 128023398, 128030224, 128030785, 128023274, 128023447, 128023123, 128023959, 131019505, 128023595, 455142040, 128095597, 128023878, 455435668, 128030194, 215114099, 128023307, 128023323, 128023314, 128030663, 128030733, 128085204, 128023782, 128023393, 128030094, 128106498, 128023183, 128030415, 128095410, 128023081, 128095490, 131017439, 128023387, 128095852, 455292950, 128095084, 128030513, 128085786, 128023039, 455347522, 405768845, 128085643, 800000665, 128030359, 128095994, 455292281, 215110641, 800000148, 128023587, 128085261, 128085809, 128030742, 128085412, 455292187, 128023092, 128023226, 800000744, 128023659, 128023841, 128023187, 455142595, 128023335, 128030080, 128030628, 800000161, 128030759, 128095109, 128023842, 128023875, 128095891, 128030430, 128023537, 128023529, 128023014, 128023948, 128085905, 128023534, 128023245, 128023758, 455292523, 128085629, 128023594, 128085361, 128023037, 128030269, 128030893, 128023448, 128095331, 128023133, 457710862, 128030361, 128023250, 128030615, 133022679, 128023472, 128085957, 128023162, 800000321, 128023191, 215011615, 128023920, 128030425, 128030644, 455142542, 317000768, 128085658, 128023786, 128085539, 128023674, 128030145, 128023449, 128030769, 128030811, 128023391, 128106008, 128085891, 800000911, 128023958, 128030133, 128023248, 128023137, 128023079, 455347892, 122016661, 128030101, 457710623, 455347767, 128030379, 128085678, 128030303, 128023849, 133022505, 128085577, 128030527, 128030943, 128023972, 128030931, 128023409, 128023064, 131019868, 128030920, 128030440, 128085217, 128023811, 128085833, 128023503, 128023142, 128023466, 128023576, 217013578, 128023579, 128030421, 455142818, 567530983, 128023951, 128023196, 566415506, 455142769, 567530562, 455142197, 455142944, 455142080, 455142449, 567530078, 128085041, 455142281, 128023344, 128030277, 455142398, 128023802, 128095332, 457710005, 128023831, 128023103, 128095982, 128030827, 128023696, 128023863, 128085573, 128085898, 128030132, 128023232, 128095347, 455142929, 128030203, 128023540, 128095252, 128030405, 128023853, 128085753, 800000132, 128030172, 128213650, 122021228, 128085984, 128085133, 128030222, 455142940, 128106750, 128095043, 128023946, 800000273, 108024734, 128085257, 128023352, 800000841, 128023225, 128085624, 128023280, 128085974, 128023950, 128095661, 455347610, 128023827, 128085167, 128085466, 128091615, 405876066, 128023912, 128023268, 455292181, 128030427, 128095616, 128030570, 128085404, 128023217, 128023609, 128023089, 123012285, 128023182, 455142830, 128023862, 455142420, 128030929, 128023604, 455142688, 108007748, 128023510, 128023867, 128030214, 128095626, 128023999, 455142547, 128023351, 128023120, 800000228, 128023068, 128023195, 455142255, 128023585, 455142134, 128023750, 128023684, 128023968, 128030987, 128030845, 455142296, 455142166, 128023899, 128023574, 128023918, 128023888, 800000606, 128023487, 128023870, 455142887, 128023774, 128023889, 455142070, 455142334, 455142614, 128091580, 215003057, 455142171, 128023107, 128023657, 128023355, 128023110, 455142408, 128023808, 128023833, 128023336, 128023563, 455142935, 128023671, 128023798, 455142416, 128023692, 128023699, 455142558, 128023776, 128023581, 215003970, 128085203, 128023953, 128023557, 128023819, 128023599, 455142921, 128023738]
for i in range(len(del_vm_list)):
    if falg == 1:
        re = requests.post(r"http://192.168.235.143:18080/nvmp/delete/%d" %del_vm_list[i])
        print(i+1,re.text)
