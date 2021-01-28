import  subprocess 

cache_line = 1024
block_size = 8
nsets = 256
no_ways = 1

cache_line_counter = 0
block_size_counter = 0

for block_size_counter in range (0,5):
	p1 = subprocess.run(f'./sim-cache -cache:il1 il1:128:64:1:l -cache:dl1 dl1:{nsets}:32:{no_ways}:l -cache:il2 dl2 -cache:dl2 ul2:1024:64:2:l ./benchmarks/whetstone',shell  =True, stderr = subprocess.PIPE)
	x= p1.stderr.decode().find('dl1.miss_rate ')

	print('no_ways',no_ways,'  nsets',nsets,' miss_rate ',p1.stderr.decode()[x:x+35])
	no_ways =no_ways*2
	nsets = int(nsets/2)



	#./sim-cache -cache:il1 il1:128:64:1:l -cache:dl1 dl1:256:32:1:l -cache:il2 dl2 -cache:dl2 ul2:{nsets}:32:{no_ways}:l ./benchmarks/fibonacci


