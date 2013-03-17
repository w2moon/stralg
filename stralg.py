#O(m*n)
def kmp_simple(target,pattern,pos = 0):
	
	if target is None or pattern is None:
		return -1
	
	k = pos
	j = 0
	
	while k < len(target) and j < len(pattern):
		if target[k] == pattern[j]:
			k=k+1
			j=j+1
		else:
			k=k-j+1
			j=0
	if j==len(pattern):
		return k - len(pattern)
	else:
		return -1

def kmp_prepare(pattern):
	overlay = [-1]
	i=-1
	j=0
	for i in range(1,len(pattern)):
		preoverlay = overlay[i-1]
		while preoverlay >= 0 and pattern[i] != pattern[preoverlay+1]:
			preoverlay = overlay[preoverlay]
		if pattern[i] == pattern[preoverlay+1]:
			overlay.append(preoverlay + 1)
		else:
			overlay.append(-1)

	return overlay

def kmp_prefix(pattern):
	j = 0
	k = -1
	next = [-1]
	length = len(pattern)-1
	while j < length:
		if k == -1 or pattern[j] == pattern[k]:
			if pattern[j+1] != pattern[k+1]:
				next.append(k+1)
			else:
				next.append(next[k+1])
			j=j+1
			k=k+1
		else:
			k = next[k]
	return next
	
def kmp_prefix2(pattern):
        j = 0
        k = -1
        next = [-1]
        length = len(pattern)-1
        while j < length:
                if k == -1 or pattern[j] == pattern[k]:
                        next.append(k+1)
                        
                        j=j+1
                        k=k+1
                else:
                        k = next[k]
        return next


#O(m+n)
def kmp(target,pattern):
	index_pattern = 0
	index_target = 0
	#O(m)
	overlay = kmp_prepare(pattern)
	#O(n)
	t=0
	while index_pattern < len(pattern) and index_target < len(target):
		print(t)
		t=t+1
		if target[index_target] == pattern[index_pattern]:
			index_target=index_target+1
			index_pattern=index_pattern+1
		elif index_pattern == 0:
			index_target=index_target+1
		else:
			index_pattern=overlay[index_pattern-1]+1
	if index_pattern == len(pattern):
		return index_target - index_pattern
	else:
		return -1
