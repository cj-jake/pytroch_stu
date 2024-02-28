n=int(input())
heights=list(map(int,input().split(' ')))

st=[-1]
heights.append(0)
maxarea=0
for i,height in enumerate(heights):
    while st and heights[st[-1]]>height:
        mid=st.pop()
        area=heights[mid]*(i-1-st[-1])
        if area>maxarea:maxarea=area
    st.append(i)
print(maxarea)