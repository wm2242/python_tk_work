with open('34-44/40/A.txt', 'r', encoding='utf-8') as f:
    a_content = f.read().strip()
with open('34-44/40/B.txt', 'r', encoding='utf-8') as f:
    b_content = f.read().strip()

merged = sorted(a_content + b_content)
with open('34-44/40/C.txt', 'w', encoding='utf-8') as f:
    f.write(''.join(merged))
print('合并完成，已生成 C.txt')