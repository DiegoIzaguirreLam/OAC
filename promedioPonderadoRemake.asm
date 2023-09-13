


section .data
	firstMsg db "Peso de las practicas: "
	len1 equ $ - firstMsg
	secondMsg db "Peso de los laboratorios: "
	len2 equ $ - secondMsg
	thirdMsg db "Peso del examen parcial: "
	len3 equ $ - thirdMsg
	fourthMsg db "Peso del examen final: "
	len4 equ $ - fourthMsg
	fifthMsg db "Nota final calculada: "
	len5 equ $ - fifthMsg
	
	pesoA dq 0
	pesoB dq 0
	pesoE1 dq 0
	pesoE2 dq 0
	solution dq 0
	char dq 0

	arregloPesos times 4 dq 0
	arregloNotas dq 15, 18, 12, 15


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
	mov rsi, pesoA
	mov rdx, 1
	syscall

	mov rax, 0
	mov rdi, 0
	mov rsi, char
	mov rdx, 1
	syscall


	mov rax, 1
	mov rdi, 1
	mov rsi, secondMsg
	mov rdx, len2
	syscall

	mov rax, 0
	mov rdi, 0
	mov rsi, pesoB
	mov rdx, 1
	syscall

	mov rax, 0
	mov rdi, 0
	mov rsi, char
	mov rdx, 1
	syscall


	mov rax, 1
	mov rdi, 1
	mov rsi, thirdMsg
	mov rdx, len3
	syscall

	mov rax, 0
	mov rdi, 0
	mov rsi, pesoE1
	mov rdx, 1
	syscall

	mov rax, 0
	mov rdi, 0
	mov rsi, char
	mov rdx, 1
	syscall


	mov rax, 1
	mov rdi, 1
	mov rsi, fourthMsg
	mov rdx, len4
	syscall

	mov rax, 0
	mov rdi, 0
	mov rsi, pesoE2
	mov rdx, 1
	syscall

	mov rax, 0
	mov rdi, 0
	mov rsi, char
	mov rdx, 1
	syscall

	xor rbx, rbx
carga_pesos:
	mov rbx, [pesoA]
	sub rbx, 30H
	mov [arregloPesos], rbx
	mov rbx, [pesoB]
	sub rbx, 30H
	mov [arregloPesos+8], rbx
	mov rbx, [pesoE1]
	sub rbx, 30H	
	mov [arregloPesos+16], rbx
	mov rbx, [pesoE2]
	sub rbx, 30H
	mov [arregloPesos+24], rbx

	xor rcx, rcx
	xor rbx, rbx
	xor r10, r10
loop_promedio:
	cmp rcx, 4
	jge fin_loop
	mov rax, [arregloNotas + 8*rcx]
	mov r8, [arregloPesos + 8*rcx]
	add r10, r8
	mul r8
	add rbx, rax
	xor rdx, rdx
	inc rcx
	jmp loop_promedio

fin_loop:
	xor rdx, rdx
	mov rax, rbx
	div r10
	mov [solution], rax
	xor rdx, rdx

	mov rax, 1
	mov rdi, 1
	mov rsi, fifthMsg
	mov rdx, len5
	syscall

test:;pushea en pila el resultado digito por digito
    xor rcx, rcx
    mov r8, 10
    mov rcx, [solution]
    xor rbx, rbx
    xor rdx, rdx

division:; para imprimir el numero con cantidad de digitos desconocida, guardaremos digito a digito en la pila y los iremos sacando 
    mov rax, rcx
    cmp rax, r8 ;si el numero es de 1 digito (<10, almacenado en r8) entonces sale del bucle
    jl aux
    
    ;despues del div, rdx: residuo y rax: cociente
    div r8 ; saca el menor digito y lo guarda en la pila (esto solo se ejecuta cuando ya se sabe que el numero es de mas de 1 digito)
    inc rbx
    push rdx;rdx contiene el residuo al dividir el numero entre 10
    
    mov rcx, rax
    jmp division

aux:
    push rax
    inc rbx ; rbx almacena el numero de digitos de la solucion, para luego saber cuantos numeros hay que retirar de la pila


loopprint:
    cmp rbx, 0 
    je final
    dec rbx 
    pop rcx

    add rcx, 30H ; hallamos el valor ASCII del numero para imprimirlo (numero equivalente para el caracter)
    mov [solution], rcx ; movemos el numero que vamos a imprimir a solution

    mov rax, 1
    mov rdi, 1
    mov rsi, solution
    mov rdx, 1
    syscall
    jmp loopprint


final:

	mov rax, 1
	mov rdi, 1
	mov rsi, char
	mov rdx, 1
	syscall


	mov rax, 60
	mov rdi, 0
	syscall


