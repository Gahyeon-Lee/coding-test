# 20365.py
# 블로그2

n = int(input())
paint = input()

color_dict = {'R': 0, 'B': 0}
precolor = ''

for color in paint:
    if color != precolor:
        color_dict[color] += 1
    precolor = color

if color_dict['R'] > color_dict['B']:
    print(color_dict['B'] + 1)
else:
    print(color_dict['R'] + 1)

print(color_dict)