import numpy as np

viridis = np.array([
    [0.267004, 0.004874, 0.329415],
    [0.269944, 0.014625, 0.341379],
    [0.273809, 0.031497, 0.358853],
    [0.276022, 0.044167, 0.370164],
    [0.278791, 0.062145, 0.386592],
    [0.280267, 0.073417, 0.397163],
    [0.281924, 0.089666, 0.412415],
    [0.28291 , 0.105393, 0.426902],
    [0.283197, 0.11568 , 0.436115],
    [0.283072, 0.130895, 0.449241],
    [0.282623, 0.140926, 0.457517],
    [0.281412, 0.155834, 0.469201],
    [0.279574, 0.170599, 0.479997],
    [0.278012, 0.180367, 0.486697],
    [0.275191, 0.194905, 0.496005],
    [0.273006, 0.20452 , 0.501721],
    [0.269308, 0.218818, 0.509577],
    [0.26658 , 0.228262, 0.514349],
    [0.262138, 0.242286, 0.520837],
    [0.257322, 0.25613 , 0.526563],
    [0.253935, 0.265254, 0.529983],
    [0.248629, 0.278775, 0.534556],
    [0.244972, 0.287675, 0.53726 ],
    [0.239346, 0.300855, 0.540844],
    [0.233603, 0.313828, 0.543914],
    [0.229739, 0.322361, 0.545706],
    [0.223925, 0.334994, 0.548053],
    [0.220057, 0.343307, 0.549413],
    [0.214298, 0.355619, 0.551184],
    [0.210503, 0.363727, 0.552206],
    [0.204903, 0.375746, 0.553533],
    [0.19943 , 0.387607, 0.554642],
    [0.19586 , 0.395433, 0.555276],
    [0.190631, 0.407061, 0.556089],
    [0.187231, 0.414746, 0.556547],
    [0.182256, 0.426184, 0.55712 ],
    [0.177423, 0.437527, 0.557565],
    [0.174274, 0.445044, 0.557792],
    [0.169646, 0.456262, 0.55803 ],
    [0.166617, 0.463708, 0.558119],
    [0.162142, 0.474838, 0.55814 ],
    [0.157729, 0.485932, 0.558013],
    [0.154815, 0.493313, 0.55784 ],
    [0.150476, 0.504369, 0.55743 ],
    [0.147607, 0.511733, 0.557049],
    [0.143343, 0.522773, 0.556295],
    [0.140536, 0.530132, 0.555659],
    [0.136408, 0.541173, 0.554483],
    [0.132444, 0.552216, 0.553018],
    [0.129933, 0.559582, 0.551864],
    [0.126453, 0.570633, 0.549841],
    [0.124395, 0.578002, 0.548287],
    [0.121831, 0.589055, 0.545623],
    [0.120092, 0.600104, 0.54253 ],
    [0.119512, 0.607464, 0.540218],
    [0.119699, 0.61849 , 0.536347],
    [0.120638, 0.625828, 0.533488],
    [0.123444, 0.636809, 0.528763],
    [0.126326, 0.644107, 0.525311],
    [0.132268, 0.655014, 0.519661],
    [0.14021 , 0.665859, 0.513427],
    [0.146616, 0.67305 , 0.508936],
    [0.157851, 0.683765, 0.501686],
    [0.166383, 0.690856, 0.496502],
    [0.180653, 0.701402, 0.488189],
    [0.196571, 0.711827, 0.479221],
    [0.20803 , 0.718701, 0.472873],
    [0.226397, 0.728888, 0.462789],
    [0.239374, 0.735588, 0.455688],
    [0.259857, 0.745492, 0.444467],
    [0.281477, 0.755203, 0.432552],
    [0.296479, 0.761561, 0.424223],
    [0.319809, 0.770914, 0.411152],
    [0.335885, 0.777018, 0.402049],
    [0.360741, 0.785964, 0.387814],
    [0.377779, 0.791781, 0.377939],
    [0.404001, 0.800275, 0.362552],
    [0.430983, 0.808473, 0.346476],
    [0.449368, 0.813768, 0.335384],
    [0.477504, 0.821444, 0.318195],
    [0.496615, 0.826376, 0.306377],
    [0.525776, 0.833491, 0.288127],
    [0.555484, 0.840254, 0.269281],
    [0.575563, 0.844566, 0.256415],
    [0.606045, 0.850733, 0.236712],
    [0.626579, 0.854645, 0.223353],
    [0.657642, 0.860219, 0.203082],
    [0.678489, 0.863742, 0.189503],
    [0.709898, 0.868751, 0.169257],
    [0.741388, 0.873449, 0.149561],
    [0.762373, 0.876424, 0.137064],
    [0.79376 , 0.880678, 0.120005],
    [0.814576, 0.883393, 0.110347],
    [0.845561, 0.887322, 0.099702],
    [0.876168, 0.891125, 0.09525 ],
    [0.89632 , 0.893616, 0.096335],
    [0.926106, 0.89733 , 0.104071],
    [0.945636, 0.899815, 0.112838],
    [0.974417, 0.90359 , 0.130215],
    [0.993248, 0.906157, 0.143936],
])

def get_color(value0to1):
    return viridis[int(value0to1 * 99)]
