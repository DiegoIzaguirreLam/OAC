
section .data
	firstMsg db "Ingrese dos numeros: "
	len1 equ $ - firstMsg
	secondMsg db "La solucion es: "
	len2 equ $ - secondMsg
	char dq 0
	num1 dq 0
	num2 dq 0
	solution dq 0
	negativo dq 45

section .text
	global _start


_start: 
	
	mov rax, 1
	mov rdi, 1
	mov rsi, firstMsg
	mov rdx, len1
	syscall

	mov rax, 0
	mov rdi, 0
	mov rsi, num1
	mov rdx, 1
	syscall

	mov rax, 0
	mov rdi, 0
	mov rsi, char
	mov rdx, 1
	syscall

	mov rax, 0
	mov rdi, 0
	mov rsi, num2
	mov rdx, 1
	syscall

	mov rax, 0
	mov rdi, 0
	mov rsi, char
	mov rdx, 1
	syscall

inicia_programa:
	mov r8, [num1]
	sub r8, 30H
	mov rax, [num2]
	sub rax, 30H

	neg r8
	imul r8

	neg rax
	add rax, 30H
	mov [solution], rax

	mov rax, 1
	mov rdi, 1
	mov rsi, secondMsg
	mov rdx, len2
	syscall

    mov rax, 1
    mov rdi, 1
    mov rsi, negativo
    mov rdx, 1
    syscall

    mov rax, 1
    mov rdi, 1
    mov rsi, solution
    mov rdx, 1
    syscall

    mov rax, 1
    mov rdi, 1
    mov rsi, char
    mov rdx, 1
    syscall

	mov rax, 60
	mov rdi, 0
	syscall



