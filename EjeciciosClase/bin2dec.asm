section .data
    binstr db "10101010"
    res db 0

section .text
    global _start

_start:
    mov r15, binstr
    mov r14, 128
    mov r13, 2
    mov r12,0

mulbuc:
    mov al, [r15]
    sub al, 48      ;sub al, '0'
    mul r14         ; rax = rax*r14
    add r12, rax    ; r12 = r12+rax

sigpa:
    xor rdx,rdx     ;    mov rdx,0
    mov rax, r14
    div r13
    mov r14, rax
    inc r15
    cmp r14, 0
    jne mulbuc

fin:
    mov [res], r12b
    mov rax, 60
    mov rdi,0
    syscall