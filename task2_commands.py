import subprocess


cache_line = 1024
block_size = 8
nsets = 256
no_ways = 1

cache_line_counter = 0
block_size_counter = 0
example_list = ['fibbonaci', 'matmul', 'memcopy', 'whetstone']
for block_size_counter in range(0, 5):
    for exmaple_name in example_list:
        p1 = subprocess.run(
            f'./sim-cache -cache:il1 il1:128:64:1:l -cache:dl1 dl1:{nsets}:32:{no_ways}:l -cache:il2 dl2 -cache:dl2 ul2:1024:64:2:l ./benchmarks/{exmaple_name}', shell=True, stderr=subprocess.PIPE)
        x1 = p1.stderr.decode().find('dl1.miss_rate ')
        x2 = p1.stderr.decode().find('ul2.miss_rate ')
        print(exmaple_name, 'no_ways,', no_ways, 'nsets', nsets,
              ' dl1miss_rate ', p1.stderr.decode()[x1:x1+35], 'ul2miss_rate', p1.stderr.decode()[x2:x2+35])
    no_ways = no_ways*2
    nsets = int(nsets/2)

    # ./sim-cache -cache:il1 il1:128:64:1:l -cache:dl1 dl1:256:32:1:l -cache:il2 dl2 -cache:dl2 ul2:{nsets}:32:{no_ways}:l ./benchmarks/fibonacci
