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
so it shows basicly double difference in speed  
