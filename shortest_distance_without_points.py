import math

#finding lenght between points
def lenght(a,b):
	return (math.sqrt( ((a[0]-b[0])**2)+ ((a[1]-b[1])**2)) )

#bruteforce for searching shortest disance for halves.
def halves_search(a,m):
	#if array include two points we find distance, and compare it to shortest one
	if len(a)==2:
		dist=lenght(a[0],a[1])
		if dist<m: m=dist
	#if array include more then two points we find distances between all of them and compare it to shortest one
	else:
		for x in range(0,len(a)-1):
			for y in range (x+1, len(a)):
				if m>lenght(a[x],a[y]): m=lenght(a[x],a[y])
	return m

#searching shortest distance (main function) (-array of points, p, q - points with shortest distance and m shortest distance)
def search_pair(a,m):
	l=len(a) #saving lenght of array in l
	if l<=(3): return (halves_search(a,m)) #if array lenght 3 or less we use bruteforce
	#finding middle of array, x position of this middle point and splitting array to two (L-left part, R-right part)
	midl=l//2
	midx=a[midl][0]
	L=a[:midl]
	R=a[midl:]

	#searching points and shorting distances in left side, right side and finally at strip
	m=search_pair(L,m)
	m=search_pair(R,m)
	m=get_strip(a,midx,m)
	
	#returning points and distance
	return (m)
		       
#getting strip for counting
def get_strip(a,xcoordinate,m):
	#initialize empty array for strip and setting borders
	strip = []
	right,left = xcoordinate+int(m), xcoordinate-int(m)
	#searching for points that fits to strip till a[x] not bigger then right border of strip, otherwise there is no more points
	for x in a:
		if x[0]>right: break
		elif left<=x[0]<=right: strip.append(x)
	#sorting strip according y coordinate
	strip.sort(key=lambda x:x[1]) 
	#checking distances in strip and compare to shortest one. And we need to check out only 6 closest points.
	for x in range (0,len(strip)):
		for y in range (x+1, min ((x+7),len(strip))):
			dist= lenght(strip[x],strip[y])
			if dist<m: m=dist
	return (m)

#main function/program
points = [(637, -932), (-993, 176), (693, 817), (418, -676), (-266, -531), (-179, -874), (-926, -332), (-379, 757), (-8, 183), (-991, 262), (880, 978), (-346, 528), (-258, -852), (-41, -124), (806, 901), (-189, -707), (393, -95), (905, -461), (127, -367), (-236, -204), (-527, 538), (-519, 552), (259, 330), (506, -730), (818, 821), (337, 283), (856, -879), (-511, 907), (-450, -145), (960, -344), (237, 338), (-38, -236), (-142, -238), (-95, 941), (-920, 764), (-464, 506), (-506, 636), (-153, 318), (-537, 826), (322, -616), (134, 561), (-13, 49), (-633, 179), (273, 289), (559, -67), (825, -477), (220, 830), (595, 736), (-329, 783), (447, 428), (451, 473), (929, 4), (281, -1000), (-695, 714), (-272, 15), (353, -92), (718, 3), (-697, -320), (-308, 304), (-46, -21), (464, -456), (395, -240), (-563, 569), (-126, 483), (150, -397), (-277, -522), (955, 960), (906, -576), (-960, 710), (37, -12), (-785, -988), (875, 311), (-538, -288), (-21, -836), (-961, -88), (-355, -211), (171, 835), (859, -420), (-300, -252), (178, -751), (385, 254), (-808, -114), (-895, -453), (-574, 167), (330, -750), (-496, -386), (-17, -416), (-756, -195), (832, 36), (-566, 123), (294, -449), (-366, 754), (431, 565), (9, -29), (-398, -214), (248, -236), (669, -700), (-794, -181), (-391, -855), (-45, -775), (391, -176), (694, -205), (569, 704), (-348, -110), (-669, 343), (933, -642), (226, 393), (223, -667), (763, 727), (739, -901), (-390, 771), (660, 393), (620, -71), (167, -624), (-325, 697), (584, 90), (-751, -574), (-73, -569), (938, -647), (-179, 598), (-681, 566), (-511, 520), (-258, -331), (13, 930), (656, -995), (907, -377), (634, -691), (89, -982), (-408, -816), (-544, 168), (804, -599), (-544, -401), (108, -30), (217, -166), (298, 405), (-773, -102), (-853, -370), (15, 629), (83, 944), (441, -484), (232, 381), (901, 80), (-819, -657), (-886, -665), (-691, 61), (-140, -271), (106, 20), (-156, 119), (726, -148), (-922, 448)]
points.sort() #sorting points
p,q = points[0],points[1] #taking first p,q
m=lenght (points[0],points[1]) #and first distance (as current minimum)
distance=search_pair(points,m) #finding and printing results
print (distance)