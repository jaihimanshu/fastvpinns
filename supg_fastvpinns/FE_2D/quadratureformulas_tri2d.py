# Purpose   : Defines the Quadrature Formulas for the 2D Triangle elements.
# Reference : ParMooN -  File: 
# Author    : Thivin Anandh D
# Date      : 31/Aug/2023

import numpy as np


class Quadratureformulas_Tri2D:
    """
    Defines the Quadrature Formulas for the 2D Triangle elements.
    """

    def __init__(self, quad_order: int):
        """
        The constructor of the Triaformulas_2D class.
        """
        self.quad_order = quad_order
        # self.num_quad_points = quad_order * quad_order
        # Available Quad orders 
        self.available_quad_order =  [1, 3, 107, 3, 7, 15, 19, 27, 73, 21, 16]
        self.available_description = ["BaryCenter","MidPoint","SevenPoint", "Vertex", "Gauss3",  "Degree8", "Degree9", "Degree11","Degree19", "CompGauss3", "Gauss_Degree8"]
        
        if self.quad_order not in self.available_quad_order:
            print(" The available quadrature orders are : ", self.available_quad_order)
            #print the file name and class name where the error occured
            print("Error occured in file : ", __file__, " and in class : ", self.__class__.__name__)
            raise Exception("Quadrature order should be from list of available quads.")
        
        else:
            # find the index of the quad order in the available quad order list
            index = self.available_quad_order.index(self.quad_order)
            # assign the quad type based on the index
            self.quad_type = self.available_description[index]
        
        # for MidPoint: 88
        if self.quad_type == "MidPoint":
            self.quad_weights = np.array([
                0.16666666666666666666666667, 0.16666666666666666666666667,
                0.16666666666666666666666667
            ])

            self.xi_quad = np.array([
                0.5, 0.5, 0.0
            ])

            self.eta_quad = np.array([
                0.0, 0.5, 0.5
            ])

        # for BaryCenter: 99
        if self.quad_type == "BaryCenter":
            self.quad_weights = np.array([
                0.5
            ])

            self.xi_quad = np.array([
                0.33333333333333333333333333
            ])

            self.eta_quad = np.array([
                0.33333333333333333333333333
            ])
            
            
        # for Vertex: 2
        if self.quad_type == "Vertex":
            self.quad_weights = np.array([
                0.16666666666666666666666667, 0.16666666666666666666666667,
                0.16666666666666666666666667
            ])

            self.xi_quad = np.array([
                0.0, 1.0, 0.0
            ])

            self.eta_quad = np.array([
                0.0, 0.0, 1.0
            ])
        
        # for Gauss3 : 33
        if self.quad_type == "Gauss3":
            self.quad_weights = np.array([
                0.1125,
                0.0629695902724135762978419727500906,
                0.0629695902724135762978419727500906,
                0.0629695902724135762978419727500906,
                0.0661970763942530903688246939165759,
                0.0661970763942530903688246939165759,
                0.0661970763942530903688246939165759
            ])

            self.xi_quad = np.array([
                0.333333333333333333333333333333333,
                0.797426985353087322398025276169754,
                0.101286507323456338800987361915123,
                0.101286507323456338800987361915123,
                0.059715871789769820459117580973106,
                0.470142064105115089770441209513447,
                0.470142064105115089770441209513447
            ])

            self.eta_quad = np.array([
                0.333333333333333333333333333333333,
                0.101286507323456338800987361915123,
                0.797426985353087322398025276169754,
                0.101286507323456338800987361915123,
                0.470142064105115089770441209513447,
                0.059715871789769820459117580973106,
                0.470142064105115089770441209513447
            ])
            
        # for SevenPoint: 
        if self.quad_type == "SevenPoint":
            self.quad_weights = np.array([
                                0.225,                     # weight 1
                                0.06666666666666667,       # weight 2
                                0.06666666666666667,       # weight 3
                                0.06666666666666667,       # weight 4
                                0.025,                     # weight 5
                                0.025,                     # weight 6
                                0.025                      # weight 7
                            ])

            # Initialize xi coordinates for quadrature points
            self.xi_quad = np.array([
                0.3333333333333333,        # xi for point 1
                0.5,                       # xi for point 2
                0.5,                       # xi for point 3
                0.0,                       # xi for point 4
                0.0,                       # xi for point 5
                1.0,                       # xi for point 6
                0.0                        # xi for point 7
            ])

            # Initialize eta coordinates for quadrature points
            self.eta_quad = np.array([
                0.3333333333333333,        # eta for point 1
                0.0,                       # eta for point 2
                0.5,                       # eta for point 3
                0.5,                       # eta for point 4
                0.0,                       # eta for point 5
                0.0,                       # eta for point 6
                1.0                        # eta for point 7
            ])

            
        if self.quad_type == "Degree8":

            self.xi_quad = np.array([0.5133469206394541, 0.3132512106717253, 0.6517753036487957,
                        0.06510199345893917, 0.345792011168269, 0.2810412473151104,
                        0.6306214343189561, 0.313477887523733, 0.8701651015635631,
                        3.623168221569262, 0.2056118320454355, 0.05612735500931855,
                        0.03474680882747129, 0.06473290497749777, -2.968960232737531])

            self.eta_quad = np.array([0.2810412473151104, 0.6306214343189561, 0.313477887523733,
                        0.8701651015635631, 3.623168221569262, 0.2056118320454355,
                        0.05612735500931855, 0.03474680882747129, 0.06473290497749777,
                        -2.968960232737531, 0.5133469206394541, 0.3132512106717253,
                        0.6517753036487957, 0.06510199345893917, 0.345792011168269])

            self.quad_weights = np.array([0.06694076763991617, 0.04390955679122078, 0.02928571764016589,
                        0.02653062443478038, 1.605834385668122e-10, 0.06694076763991617,
                        0.04390955679122078, 0.02928571764016589, 0.02653062443478038,
                        1.605834385668122e-10, 0.06694076763991617, 0.04390955679122078,
                        0.02928571764016589, 0.02653062443478038, 1.605834385668122e-10])


        if self.quad_type == "Degree9":
            self.xi_quad = np.array([0.333333333333333333333333333333333,
                                          0.489682519198737627783706924836192,
                                          0.489682519198737627783706924836192,
                                          0.020634961602524744432586150327616,
                                          0.437089591492936637269930364435354,
                                          0.437089591492936637269930364435354,
                                          0.125820817014126725460139271129292,
                                          0.188203535619032730240961280467335,
                                          0.188203535619032730240961280467335,
                                          0.623592928761934539518077439065330,
                                          0.0447295133944527098651065899662763,
                                          0.0447295133944527098651065899662763,
                                          0.910540973211094580269786820067447,
                                          0.741198598784498020690079873523423,
                                          0.0368384120547362836348175987833851,
                                          0.741198598784498020690079873523423,
                                          0.221962989160765695675102527693192,
                                          0.0368384120547362836348175987833851,
                                          0.221962989160765695675102527693192])

            self.eta_quad = np.array([0.333333333333333333333333333333333,
                                     0.489682519198737627783706924836192,
                                     0.020634961602524744432586150327616,
                                     0.489682519198737627783706924836192,
                                     0.437089591492936637269930364435354,
                                     0.125820817014126725460139271129292,
                                     0.437089591492936637269930364435354,
                                     0.188203535619032730240961280467335,
                                     0.623592928761934539518077439065330,
                                     0.188203535619032730240961280467335,
                                     0.0447295133944527098651065899662763,
                                     0.910540973211094580269786820067447,
                                     0.0447295133944527098651065899662763,
                                     0.0368384120547362836348175987833851,
                                     0.741198598784498020690079873523423,
                                     0.221962989160765695675102527693192,
                                     0.741198598784498020690079873523423,
                                     0.221962989160765695675102527693192,
                                     0.0368384120547362836348175987833851])

            self.quad_weights = np.array([0.0485678981413994169096209912536443,
                                      0.0156673501135695352684274156436046,
                                      0.0156673501135695352684274156436046,
                                      0.0156673501135695352684274156436046,
                                      0.0389137705023871396583696781497019,
                                      0.0389137705023871396583696781497019,
                                      0.0389137705023871396583696781497019,
                                      0.0398238694636051265164458871320226,
                                      0.0398238694636051265164458871320226,
                                      0.0398238694636051265164458871320226,
                                      0.0127888378293490156308393992794999,
                                      0.0127888378293490156308393992794999,
                                      0.0127888378293490156308393992794999,
                                      0.0216417696886446886446886446886446,
                                      0.0216417696886446886446886446886446,
                                      0.0216417696886446886446886446886446,
                                      0.0216417696886446886446886446886446,
                                      0.0216417696886446886446886446886446,
                                      0.0216417696886446886446886446886446])

        if self.quad_type == "Degree11":
            self.xi_quad = np.array([0.0323649481112758931588480911328593,
                                          0.0323649481112758931588480911328593,
                                          0.9352701037774482136823038177342814,
                                          0.119350912282581309581102091581736,
                                          0.119350912282581309581102091581736,
                                          0.761298175434837380837795816836528,
                                          0.534611048270758309358680864963778,
                                          0.534611048270758309358680864963778,
                                          -0.069222096541516618717361729927556,
                                          0.203309900431282473351326588944569,
                                          0.203309900431282473351326588944569,
                                          0.593380199137435053297346822110862,
                                          0.398969302965855222611381867187058,
                                          0.398969302965855222611381867187058,
                                          0.202061394068289554777236265625884,
                                          0.593201213428212752488840882179699,
                                          0.0501781383104946650738269077613887,
                                          0.3566206482612925824373322100589123,
                                          0.593201213428212752488840882179699,
                                          0.0501781383104946650738269077613887,
                                          0.3566206482612925824373322100589123,
                                          0.807489003159792153166724890348745,
                                          0.0210220165361662971236385570923633,
                                          0.1714889803040415497096365525588917,
                                          0.807489003159792153166724890348745,
                                          0.0210220165361662971236385570923633,
                                          0.1714889803040415497096365525588917])

            self.eta_quad = np.array([0.0323649481112758931588480911328593,
                                     0.9352701037774482136823038177342814,
                                     0.0323649481112758931588480911328593,
                                     0.119350912282581309581102091581736,
                                     0.761298175434837380837795816836528,
                                     0.119350912282581309581102091581736,
                                     0.534611048270758309358680864963778,
                                     -0.069222096541516618717361729927556,
                                     0.534611048270758309358680864963778,
                                     0.203309900431282473351326588944569,
                                     0.593380199137435053297346822110862,
                                     0.203309900431282473351326588944569,
                                     0.398969302965855222611381867187058,
                                     0.202061394068289554777236265625884,
                                     0.398969302965855222611381867187058,
                                     0.0501781383104946650738269077613887,
                                     0.3566206482612925824373322100589123,
                                     0.593201213428212752488840882179699,
                                     0.3566206482612925824373322100589123,
                                     0.593201213428212752488840882179699,
                                     0.0501781383104946650738269077613887,
                                     0.0210220165361662971236385570923633,
                                     0.1714889803040415497096365525588917,
                                     0.807489003159792153166724890348745,
                                     0.1714889803040415497096365525588917,
                                     0.807489003159792153166724890348745,
                                     0.0210220165361662971236385570923633])

            self.quad_weights = np.array([6.82986550133893097935968864728942e-3,
                                      6.82986550133893097935968864728942e-3,
                                      6.82986550133893097935968864728942e-3,
                                      0.0180922702517090396691439677721401,
                                      0.0180922702517090396691439677721401,
                                      0.0180922702517090396691439677721401,
                                      4.63503164480338025330042487596786e-4,
                                      4.63503164480338025330042487596786e-4,
                                      4.63503164480338025330042487596786e-4,
                                      0.0296614886903870365579061947507576,
                                      0.0296614886903870365579061947507576,
                                      0.0296614886903870365579061947507576,
                                      0.0385747674574065614307555344183042,
                                      0.0385747674574065614307555344183042,
                                      0.0385747674574065614307555344183042,
                                      0.0261685559811020355585694685067805,
                                      0.0261685559811020355585694685067805,
                                      0.0261685559811020355585694685067805,
                                      0.0261685559811020355585694685067805,
                                      0.0261685559811020355585694685067805,
                                      0.0261685559811020355585694685067805,
                                      0.0103538298195703444435161507885086,
                                      0.0103538298195703444435161507885086,
                                      0.0103538298195703444435161507885086,
                                      0.0103538298195703444435161507885086,
                                      0.0103538298195703444435161507885086,
                                      0.0103538298195703444435161507885086])

        if self.quad_type == "Degree19":
            self.xi_quad = np.array([0.3333333333333333333333,
                                          0.020780025853987, 0.489609987073006, 0.489609987073006,
                                          0.090926214604215, 0.454536892697893, 0.454536892697893,
                                          0.197166638701138, 0.401416680649431, 0.401416680649431,
                                          0.488896691193805, 0.255551654403098, 0.255551654403098,
                                          0.645844115695741, 0.177077942152130, 0.177077942152130,
                                          0.779877893544096, 0.110061053227952, 0.110061053227952,
                                          0.888942751496321, 0.055528624251840, 0.055528624251840,
                                          0.974756272445543, 0.012621863777229, 0.012621863777229,
                                          0.003611417848412, 0.003611417848412, 0.395754787356943,
                                          0.395754787356943, 0.600633794794645, 0.600633794794645,
                                          0.134466754530780, 0.134466754530780, 0.307929983880436,
                                          0.307929983880436, 0.557603261588784, 0.557603261588784,
                                          0.014446025776115, 0.014446025776115, 0.264566948406520,
                                          0.264566948406520, 0.720987025817365, 0.720987025817365,
                                          0.046933578838178, 0.046933578838178, 0.358539352205951,
                                          0.358539352205951, 0.594527068955871, 0.594527068955871,
                                          0.002861120350567, 0.002861120350567, 0.157807405968595,
                                          0.157807405968595, 0.839331473680839, 0.839331473680839,
                                          0.223861424097916, 0.223861424097916, 0.075050596975911,
                                          0.075050596975911, 0.701087978926173, 0.701087978926173,
                                          0.034647074816760, 0.034647074816760, 0.142421601113383,
                                          0.142421601113383, 0.822931324069857, 0.822931324069857,
                                          0.010161119296278, 0.010161119296278, 0.065494628082938,
                                          0.065494628082938, 0.924344252620784, 0.924344252620784])

            self.eta_quad = np.array([0.3333333333333333333333,
                                     0.489609987073006, 0.020780025853987, 0.489609987073006,
                                     0.454536892697893, 0.090926214604215, 0.454536892697893,
                                     0.401416680649431, 0.197166638701138, 0.401416680649431,
                                     0.255551654403098, 0.488896691193805, 0.255551654403098,
                                     0.177077942152130, 0.645844115695741, 0.177077942152130,
                                     0.110061053227952, 0.779877893544096, 0.110061053227952,
                                     0.055528624251840, 0.888942751496321, 0.055528624251840,
                                     0.012621863777229, 0.974756272445543, 0.012621863777229,
                                     0.395754787356943, 0.600633794794645, 0.003611417848412,
                                     0.600633794794645, 0.003611417848412, 0.395754787356943,
                                     0.307929983880436, 0.557603261588784, 0.134466754530780,
                                     0.557603261588784, 0.134466754530780, 0.307929983880436,
                                     0.264566948406520, 0.720987025817365, 0.014446025776115,
                                     0.720987025817365, 0.014446025776115, 0.264566948406520,
                                     0.358539352205951, 0.594527068955871, 0.046933578838178,
                                     0.594527068955871, 0.046933578838178, 0.358539352205951,
                                     0.157807405968595, 0.839331473680839, 0.002861120350567,
                                     0.839331473680839, 0.002861120350567, 0.157807405968595,
                                     0.075050596975911, 0.701087978926173, 0.223861424097916,
                                     0.701087978926173, 0.223861424097916, 0.075050596975911,
                                     0.142421601113383, 0.822931324069857, 0.034647074816760,
                                     0.822931324069857, 0.034647074816760, 0.142421601113383,
                                     0.065494628082938, 0.924344252620784, 0.010161119296278,
                                     0.924344252620784, 0.010161119296278, 0.065494628082938])

            self.quad_weights = np.array([0.0164531656944595,
                                      0.005165365945636,  0.005165365945636,  0.005165365945636,
                                      0.011193623631508,  0.011193623631508,  0.011193623631508,
                                      0.015133062934734,  0.015133062934734,  0.015133062934734,
                                      0.015245483901099,  0.015245483901099,  0.015245483901099,
                                      0.0120796063708205, 0.0120796063708205, 0.0120796063708205,
                                      0.0080254017934005, 0.0080254017934005, 0.0080254017934005,
                                      0.004042290130892,  0.004042290130892,  0.004042290130892,
                                      0.0010396810137425, 0.0010396810137425, 0.0010396810137425,
                                      0.0019424384524905, 0.0019424384524905, 0.0019424384524905,
                                      0.0019424384524905, 0.0019424384524905, 0.0019424384524905,
                                      0.012787080306011,  0.012787080306011,  0.012787080306011,
                                      0.012787080306011,  0.012787080306011,  0.012787080306011,
                                      0.004440451786669,  0.004440451786669,  0.004440451786669,
                                      0.004440451786669,  0.004440451786669,  0.004440451786669,
                                      0.0080622733808655, 0.0080622733808655, 0.0080622733808655,
                                      0.0080622733808655, 0.0080622733808655, 0.0080622733808655,
                                      0.0012459709087455, 0.0012459709087455, 0.0012459709087455,
                                      0.0012459709087455, 0.0012459709087455, 0.0012459709087455,
                                      0.0091214200594755, 0.0091214200594755, 0.0091214200594755,
                                      0.0091214200594755, 0.0091214200594755, 0.0091214200594755,
                                      0.0051292818680995, 0.0051292818680995, 0.0051292818680995,
                                      0.0051292818680995, 0.0051292818680995, 0.0051292818680995,
                                      0.001899964427651,  0.001899964427651,  0.001899964427651,
                                      0.001899964427651,  0.001899964427651,  0.001899964427651000])


        # for CompGauss3: 
        if self.quad_type == "CompGauss3":
            self.quad_weights = np.array([
                0.0375,
                0.0209898634241378587659473242500302,
                0.0209898634241378587659473242500302,
                0.0209898634241378587659473242500302,
                0.0220656921314176967896082313055253,
                0.0220656921314176967896082313055253,
                0.0220656921314176967896082313055253,

                0.0375,
                0.0209898634241378587659473242500302,
                0.0209898634241378587659473242500302,
                0.0209898634241378587659473242500302,
                0.0220656921314176967896082313055253,
                0.0220656921314176967896082313055253,
                0.0220656921314176967896082313055253,

                0.0375,
                0.0209898634241378587659473242500302,
                0.0209898634241378587659473242500302,
                0.0209898634241378587659473242500302,
                0.0220656921314176967896082313055253,
                0.0220656921314176967896082313055253,
                0.0220656921314176967896082313055253
            ])

            self.xi_quad = np.array([
                0.444444444444444444444444444444444,
                0.831189154460906101998354396808128,
                0.367095502441152112933662453971708,
                0.135048676431275118401316482553497,
                0.216429893158141517049264650810922,
                0.490047354701705029923480403171149,
                0.626856085473486786360588279351263,

                0.444444444444444444444444444444445,
                0.135048676431275118401316482553497,
                0.367095502441152112933662453971708,
                0.831189154460906101998354396808128,
                0.626856085473486786360588279351263,
                0.490047354701705029923480403171149,
                0.216429893158141517049264650810922,

                0.111111111111111111111111111111111,
                0.0337621691078187796003291206383743,
                0.265808995117695774132675092056585,
                0.0337621691078187796003291206383743,
                0.156714021368371696590147069837816,
                0.0199052905965899401530391936577020,
                0.156714021368371696590147069837816
            ])

            self.eta_quad = np.array([
                0.111111111111111111111111111111111,
                0.0337621691078187796003291206383743,
                0.265808995117695774132675092056585,
                0.0337621691078187796003291206383743,
                0.156714021368371696590147069837816,
                0.0199052905965899401530391936577020,
                0.156714021368371696590147069837816,

                0.444444444444444444444444444444444,
                0.831189154460906101998354396808128,
                0.367095502441152112933662453971708,
                0.135048676431275118401316482553497,
                0.216429893158141517049264650810922,
                0.490047354701705029923480403171149,
                0.626856085473486786360588279351263,

                0.444444444444444444444444444444445,
                0.135048676431275118401316482553497,
                0.367095502441152112933662453971708,
                0.831189154460906101998354396808128,
                0.626856085473486786360588279351263,
                0.490047354701705029923480403171149,
                0.216429893158141517049264650810922
            ])

        # for Gauss_Degree8: 888
        if self.quad_type == "Gauss_Degree8":
            self.quad_weights = np.array([
                0.0721578038388935028014,
                0.0475458171336424970100,
                0.0475458171336424970100,
                0.0475458171336424970100,
                0.0516086852673589974172,
                0.0516086852673589974172,
                0.0516086852673589974172,
                0.0162292488115990014841,
                0.0162292488115990014841,
                0.0162292488115990014841,
                0.0136151570872174998428,
                0.0136151570872174998428,
                0.0136151570872174998428,
                0.0136151570872174998428,
                0.0136151570872174998428,
                0.0136151570872174998428
            ])

            self.xi_quad = np.array([
                0.333333333333333333333333333333333,
                0.081414823414554,
                0.459292588292723,
                0.459292588292723,
                0.658861384496480,
                0.170569307751760,
                0.170569307751760,
                0.898905543365938,
                0.050547228317031,
                0.050547228317031,
                0.008394777409958,
                0.263112829634638,
                0.008394777409958,
                0.728492392955404,
                0.263112829634638,
                0.728492392955404
            ])

            self.eta_quad = np.array([
                0.333333333333333333333333333333333,
                0.459292588292723,
                0.081414823414554,
                0.459292588292723,
                0.170569307751760,
                0.658861384496480,
                0.170569307751760,
                0.050547228317031,
                0.898905543365938,
                0.050547228317031,
                0.263112829634638,
                0.008394777409958,
                0.728492392955404,
                0.008394777409958,
                0.728492392955404,
                0.263112829634638
            ])
            
    def get_quad_weights(self):
        return self.quad_weights
    
    def get_quad_values(self):
        return self.quad_weights, self.xi_quad, self.eta_quad