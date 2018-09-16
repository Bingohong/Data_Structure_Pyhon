# 贪心算法实例-活动安排问题
def activity(meeting):
	length = len(meeting)
	meeting.sort(key=lambda x:x[1])
	result = [False for i in range(length)]
	j=0 #当前选中活动 
	result = True #选中第一个活动
	for i in range(1,length):
		if meeting[i][0] >= meeting[j][1]: #判断能否安排活动
			j=i
			result[j] = True
	return result

# 贪心算法实例-近似算法-集合覆盖问题
def covering():
	states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])

	stations = {}
	stations["kone"] = set(["id", "nv", "ut"])
	stations["ktwo"] = set(["wa", "id", "mt"])
	stations["kthree"] = set(["or", "nv", "ca"])
	stations["kfour"] = set(["nv", "ut"])
	stations["kfive"] = set(["ca", "az"])

	final_stations = set()

	while states_needed:
		best_station = None
		states_covered = set()
		for station, states in stations.items():
			covered = states & states_needed
			if len(covered) > len(states_covered):
				best_station = station
				states_covered = covered

		states_needed -= states_covered
		final_stations.add(best_station)

	print(final_stations)
