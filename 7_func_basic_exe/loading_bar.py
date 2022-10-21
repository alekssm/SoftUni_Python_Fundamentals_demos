def the_loading_bar(num):
    loading = [".", ".", ".", ".", ".", ".", ".", ".", ".", "."]
    if num == 0:
        pass
    elif num < 100:
        times = num // 10
        for ind in range (0, times):
            loading[ind] = "%"
    else:
       # for ind in range [0, len(loading)]:
           # loading[ind] = "%"
       loading = ["%", "%", "%", "%", "%", "%", "%", "%", "%", "%"]
    result = "".join(loading)
    return result

num = int(input())
if num == 100:
    print(f"{num}% Complete!")
    print(f"[{the_loading_bar(num)}]")
else:
    print(f"{num}% [{the_loading_bar(num)}]")
    print("Still loading...")
