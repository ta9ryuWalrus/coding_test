#%%
path = 'input.txt'
with open(path) as f:
    l = f.readlines()

# %%
m = l.pop(-1)
l = [s.split(':') for s in l]
# %%
l1 = [[int(s[0]), s[1]] for s in l]

# %%
l1.sort(key = lambda x: x[0])

# %%
l1 = [[s[0], s[1].rstrip('\n')] for s in l1]

# %%
cnt = 0
ans = ''
for s in l1:
    if int(m) % s[0] == 0:
        ans += s[1]
        cnt += 1

if cnt == 0:
    ans += m

print(ans)

# %%
