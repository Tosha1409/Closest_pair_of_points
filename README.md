# Closest_pair_of_points  
I was doing Codility *Rubidium* challenge while and at some point it required to check algorithm for finding **pair of points with smallest distance** between them. I didnt used it in the end for *Rubidium* cause task was a bit different, but it was good to refresh memory(i did saw it before) and i decided to write my version from scratch later.  
So i started to make it yesterday and when it was almost done i decided to recheck links that i saw before:  
https://medium.com/@andriylazorenko/closest-pair-of-points-in-python-79e2409fc0b2  
https://www.geeksforgeeks.org/closest-pair-of-points-using-divide-and-conquer-algorithm/  
2nd link was in C++, and first in Python and i decided to take a closer look at python solution and realized that it is pretty much
rewritten program from previous. Python is more flexible language and allow to makes more elegancy, so i got excited to see differences.  
  
**shortest_distance.py** - my implementation of algoritm.  
**shortest_distance_without_points.py** - almost same program, but without keeping points itself(and works little bit faster).  
**testcases.py** - 5 different arrays for tests.  

so i runned tests (*Python -m cProfile*):  
**mine.txt** - those are results for mine.  
**original.txt** - those are results for Andriy Lazorenko code.  
so it shows basicly double difference in speed.  
  
Other thing that bothered me was this *"maximum 6 points at strip"*:  
C++ article was saying  
>This is a proven fact that this loop runs at most 6 times.  
  
and at other link it was:  
> In short: it is enough to check only seven points following each point on the s_y subarray. You should really look through the proof of correctness, because it explains a lot better this ‘trick’ that allows for great running speed increase.  
  
so that left me pretty puzzled, is it running 6 times(because there is no more points) or you need check only seven points(but there can be more). So decided to experiment and replaced line number 55  
>		for y in range (x+1, min ((x+7),len(strip))):  
with  
>		for y in range (x+1, len(strip)):  
and results improved even a bit more.  
  
**shortest_distance2.py** - mine code without limiting loop for checking strip.  
**mine2.txt**	- test results  
  
so it looks like this check/choosing minimum was unnecessary and perfomance a bit improved a bit more.
