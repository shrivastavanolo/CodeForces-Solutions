n = int(input())
cameras = []
for _ in range(n):
    ti, si = map(int, input().split())
    cameras.append((ti, si))

cameras.sort(key=lambda x: x[1])  # Sort cameras by their disable time in ascending order
first_diamond_stolen = False
second_diamond_stolen = False
time = 0

for ti, si in cameras:
    if ti == 1:  # Camera monitoring the first diamond
        if not first_diamond_stolen:
            first_diamond_stolen = True
        elif not second_diamond_stolen:
            second_diamond_stolen = True
        else:
            break  # We have already stolen both diamonds
    elif ti == 2:  # Camera monitoring the second diamond
        if not second_diamond_stolen:
            second_diamond_stolen = True
        else:
            break  # We have already stolen both diamonds
    else:  # Camera monitoring both diamonds
        if not first_diamond_stolen:
            first_diamond_stolen = True
        elif not second_diamond_stolen:
            second_diamond_stolen = True
        else:
            break  # We have already stolen both diamonds

    time += 1  # Hacking the camera takes 1 second

if first_diamond_stolen and second_diamond_stolen:
    print(time)
else:
    print(-1)

