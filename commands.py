import  subprocess 

cache_line = 1024
block_size = 8

cache_line_counter = 0
block_size_counter = 0
for cache_line_counter in range(0,8):
	for block_size_counter in range (0,4):
		p1 = subprocess.run(f'./sim-cache -cache:il1 il1:256:32:1:l -cache:dl1 dl1:{cache_line}:{block_size}:1:l -cache:il2 dl2 -cache:dl2 ul2:1024:64:4:l ./benchmarks/whetstone',shell  =True, stderr = subprocess.PIPE)
		x= p1.stderr.decode().find('dl1.miss_rate ')
		#print ("x = 			",p1.stderr.decode()[x:x+100])
		print('-------->',cache_line,'  ',block_size,'  ',p1.stderr.decode()[x:x+35])
		block_size = 2*block_size
	block_size = 8

	
	cache_line = 2*cache_line

	

