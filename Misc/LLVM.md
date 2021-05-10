# LLDB

```bash

lldb a.out

lldb -- a.out args

r   # run
c   # continue
n   # next line
s   # step into
bt  # backtrace

(lldb) break set -f test.cpp -l 30

(lldb) br set -f test.cpp -l 30

(lldb) b test.cpp : l

(lldb) br list

(lldb) br del

(lldb) p varname

... frame / fr var

... fr select / frame no

... watchpoint set variable globalVariable

... watchpoint set variable -w read | write | read_write globalVariable

```

- gcc & llvm are toolchain
    - Preprocess
    - Syntax mistake
    - Assemble object
    - Link into executable
