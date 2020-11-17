n = int(input())
s = input()
time = 0
public,like = s.split(' опубликовал пост, количество просмотров: ')
d = {public:[int(like),'root',time]}
for i in range(1,n):
    s = input()
    time += 1
    if ' отрепостил пост у ' in s:
        repost,s = s.split(' отрепостил пост у ')
        if ', количество просмотров: ' in s: 
            autor,like = s.split(', количество просмотров: ')
            like = int(like)
            d[repost] = [like,autor,time]
            while autor != 'root':
                d[autor][0] += like
                autor = d[autor][1]
    elif 'количество просмотров: ' in s:
        s,like = s.split('количество просмотров: ')
        d[public][0] += int(like)
for x in sorted(d,key = lambda y: d[y][2]):
    print(d[x][0])
