version_of_now = input().split(".")
int_version_now = [int(ele) for ele in version_of_now]
n_1 = version_of_now[0]
n_2 = version_of_now[1]
n_3 = version_of_now[2]

if int_version_now[2] < 9:
    int_version_now[2] += 1
    version_of_now[2] = str(int_version_now[2])
    print(".".join(version_of_now))
else:
    if int_version_now[1] < 9:
        int_version_now[2] = 0
        version_of_now[2] = str(int_version_now[2])
        int_version_now[1] += 1
        version_of_now[1] = str(int_version_now[1])
        print(".".join(version_of_now))
    else:
        int_version_now[2] = 0
        version_of_now[2] = str(int_version_now[2])
        int_version_now[1] = 0
        version_of_now[1] = str(int_version_now[1])
        int_version_now[0] += 1
        version_of_now[0] = str(int_version_now[0])
        print(".".join(version_of_now))