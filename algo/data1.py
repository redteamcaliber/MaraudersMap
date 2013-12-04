import numpy as np

data1 = map(np.array,
    [ [(10,0), (9,24), (26,-1)] # stations
    ,  [(0,0),(1,0),(2,0),(5,0),(6,0),(7,0),(8,0),(9,0),(10,0),(11,0),(13,0),(14,0),(16,0),(17,0),(18,0),(19,0),(20,0),(21,0),(22,0),(23,0),(24,0),(25,0),(26,0),(10,0),(10,1),(10,2),(10,3),(10,4),(10,6),(10,7),(10,8),(10,9),(10,10),(10,11),(10,12),(10,13),(10,14),(10,15),(10,16),(10,17),(10,18),(10,19),(10,20),(10,21),(10,22),(10,23),(10,24)] # calibration locations
    , [(-74, -79, -75),(-69, -66, -71),(-74, -80, -71),(-57, -65, -71),(-51, -77, -75),(-53, -77, -61),(-49, -71, -71),(-59, -76, -64),(-50, -70, -61),(-55, -75, -60),(-69, -71, -71),(-70, -73, -57),(-67, -77, -60),(-66, -74, -55),(-80, -70, -62),(-78, -73, -64),(-77, -73, -66),(-80, -73, -61),(-77, -74, -54),(-76, -82, -55),(-74, -75, -55),(-76, -74, -61),(-73, -75, -64),(-50, -72, -52),(-61, -73, -67),(-61, -74, -66),(-56, -71, -55),(-54, -60, -71),(-51, -51, -64),(-49, -68, -70),(-69, -67, -57),(-60, -67, -61),(-51, -70, -66),(-52, -63, -55),(-61, -62, -53),(-60, -63, -47),(-61, -63, -53),(-59, -67, -54),(-60, -64, -61),(-60, -61, -49),(-64, -60, -50),(-63, -60, -41),(-67, -60, -52),(-67, -59, -52),(-66, -63, -51),(-63, -52, -50),(-64, -46, -64)] # signal strengths
    ])