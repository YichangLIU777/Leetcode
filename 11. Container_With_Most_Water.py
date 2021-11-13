def Container_With_Most_Water(height):
    square_list = []
    for i in range(len(height)-1):
        for j in range(i+1,len(height)):
            square_list.append(min(height[i],height[j])*(j-i))
    return max(square_list)

print(Container_With_Most_Water([1,8,6,2,5,4,8,3,7]))
print(Container_With_Most_Water([4,3,2,1,4]))
print(Container_With_Most_Water([1,1]))