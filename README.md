# PythonScriptForLinux
the python is script to make the assignments easier and remove repetition

the cache.c and cache.h files are updated to include the new replacement policy NRU

NRU: The OpenSparc T1/T2 processors implement a not-recently-used (NRU) replacement
policy for the unified second level cache. This section describes a (simplified) NRU policy
that you are required to implement inside the SimpleScalar sim-cache simulator. The NRU
replacement policy is based on a used-bit scheme. Each cache line has a used bit associated
with it. Initially, all bits are reset (i.e., all used bits in the cache are zero). The used bit is set
each time a cache line is accessed or when initially fetched/filled from memory. If setting the
used bit for the current line causes all used bits within the corresponding cache set to be set to
one, all other bits are reset. This ensures that at any time there is at least one cache line within
a set that has its used bit clear. On a cache miss, a cache line with its used bit clear is chosen
to be replaced. The L2 cache has a single rotating replacement pointer, which is the “starting
point” to find the way to replace. On a miss, the L2 looks for the first line within the set with
its used bit clear, starting with the way pointed at by the replacement pointer. The replacement
2
pointer is then rotated forward one way. Using the same replacement pointer for all sets of
the L2 cache makes the replacement be more random than if each set had its own replacement
pointer. Initially, the replacement pointer points to the first way (i.e., way zero).

