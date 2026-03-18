def collect_festival_points(points):
   pass
   # input: stack -> each item representing points from a single booth
   # output: int -> sum of points collected after visiting all booths

   # plan:

   # initalize a sum
   # loop while there's still something in the stack:
      # pop item in stack and add it to the sum
   
   # return the sum

   sum = 0
   while points:
      sum += points.pop()

   return sum

print(collect_festival_points([5, 8, 3, 10])) 
print(collect_festival_points([2, 7, 4, 6])) 
print(collect_festival_points([1, 5, 9, 2, 8]))
   