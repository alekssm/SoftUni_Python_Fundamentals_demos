version_of_now = (input().split("."))
version_of_str = "".join(version_of_now)
version_of_int = int(version_of_str) + 1
update_version_now = ".".join(str(version_of_int))
print(update_version_now)