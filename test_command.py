import subprocess
cache_line = 1024
block_size = 8
p1 = subprocess.run(f'./sim-cache -cache:il1 il1:256:32:1:l -cache:dl1 dl1:{cache_line}:{block_size}:1:l -cache:il2 dl2 -cache:dl2 ul2:1024:64:4:l ./benchmarks/pi',shell  =True, stderr = subprocess.PIPE)

print(p1.stderr.decode())
