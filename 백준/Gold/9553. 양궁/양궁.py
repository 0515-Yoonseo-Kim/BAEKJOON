import math

def calculate_angle(x1, y1, x2, y2):
    dot_product = x1 * x2 + y1 * y2
    magnitude_u = math.sqrt(x1**2 + y1**2)
    magnitude_v = math.sqrt(x2**2 + y2**2)
    cos_theta = dot_product / (magnitude_u * magnitude_v)
    cos_theta = max(-1.0, min(1.0, cos_theta))
    theta_radian = math.acos(cos_theta)
    theta_degree = math.degrees(theta_radian)
    return theta_degree
while True:
    try:
        T = int(input())
        for _ in range(T):
            N = int(input())
            angles = []
            for _ in range(N):
                x1,y1,x2,y2 = map(int,input().split())
                angle = calculate_angle(x1,y1,x2,y2)
                angles.append(angle/360)
            print("{:.5f}".format(round(sum(angles),5)))
    except Exception:
        break

