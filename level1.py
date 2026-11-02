bug = {
    "title": "Login Button is not Working",
    "status": "New",
    "priority": "High"
}


bugs = [bug, {"title": "Drawer Button is not Working",
              "status": "New", "priority": "High"}, {"title": "Data is Missing", "status": "Assigned", "priority": "Medium"}, {"title": "Credentials are Missing", "status": "Closed", "priority": "High"}]

for b in bugs:
    if b["priority"] == "High":
        print(b["title"])


def get_high_priority(bugs):
    result = []
    for b in bugs:
        if b["priority"] == "High":
            result.append(b["title"])
    return result


# high_bugs = get_high_priority(bugs)
# print(high_bugs)
# print(len(high_bugs))


def get_by_status(bugs, status):
    res = []
    for b in bugs:
        if b["status"] == status:
            res.append(b["title"])
    return res


print(get_by_status(bugs, "New"))
print(get_by_status(bugs, "Assigned"))


def count_by_status(bugs):
    counts = {}
    for b in bugs:
        s = b["status"]
        print("bug ka status:", s, "| tally abhi:", counts)
        if s in counts:
            counts[s] += 1
        else:
            counts[s] = 1
    return counts


print(count_by_status(bugs))


def count_by_priority(bugs):
    count = {}
    for j in bugs:
        p = j["priority"]
        print("Bug ki priority:", p, "| tally abhi:", count)
        if p in count:
            count[p] += 1
        else:
            count[p] = 1
    return count


print(count_by_priority(bugs))
