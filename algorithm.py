import math
import pandas as pd
from pandas.core import construction

data = pd.read_csv('input\sitting_coordinates.csv')
concern_data = data[[
    'right_hip_x', 'right_hip_y', 'right_knee_x', 'right_knee_y', 'right_ankle_x', 'right_ankle_y',
    'left_hip_x','left_hip_y', 'left_knee_x','left_knee_y', 'left_ankle_x', 'left_ankle_y'
    ]]
P1 = concern_data[['right_knee_x', 'right_knee_y']].values[0]
P2 = concern_data[['right_ankle_x', 'right_ankle_y']].values[0]
P3 = concern_data[['right_hip_x', 'right_hip_y']].values[0]

angle = math.atan2(P3[1] - P1[1], P3[0] - P1[0]) - math.atan2(P2[1] - P1[1], P2[0] - P1[0])

P1 = concern_data[['left_knee_x', 'left_knee_y']].values[0]
P2 = concern_data[['left_ankle_x', 'left_ankle_y']].values[0]
P3 = concern_data[['left_hip_x', 'left_hip_y']].values[0]

angle = math.atan2(P3[1] - P1[1], P3[0] - P1[0]) - math.atan2(P2[1] - P1[1], P2[0] - P1[0])
