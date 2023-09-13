

section .data
	firstMsg db "La solucion es: "
	len1 equ $ - firstMsg
	;arrNum dq 3, 4, 5
	arrNum dq 20, 31, 13
	nNum dq 3
	solution dq 0
	char dq 10

section .text
	global _start


_start:

	mov rax, [arrNum]
	mov rcx, 1
	mov rdx, [nNum]

loop_mayor:
	mov rbx, [arrNum+8*rcx]
	cmp rbx, rax
	jl skip
	;aca lo cambia si no skipea
	mov rax, rbx
	skip:
	inc rcx
	cmp rcx, rdx
	jl loop_mayor

	mov r9, rax ; r9 guardara el mayor, ya que usaremos rax
	mov r8, [nNum]

loop_incrementa:
	xor rcx, rcx
	mov rax, r9
	loop_divide:
		xor rdx, rdx
		mov rbx, [arrNum+8*rcx]
		div rbx
		cmp rdx, 0
		jne sigue_buscando
		inc rcx
		cmp rcx, r8
		jl loop_divide
		jmp imprime_solucion
	sigue_buscando:
	inc r9
	jmp loop_incrementa


imprime_solucion:
    mov rax, 1
    mov rdi, 1
    mov rsi, firstMsg
    mov rdx, len1
    syscall
	mov [solution], r9

;pushea en pila el resultado digito por digito
    xor rcx, rcx
    mov r8, 10
    mov rcx, [solution]
    mov rbx, 0
    xor rdx, rdx

division:; para imprimir el numero con cantidad de digitos desconocida, guardaremos digito a digito en la pila y los iremos sacando 
    mov rax, rcx
    cmp rax, r8 ;si el numero es de 1 digito (<10, almacenado en r8) entonces sale del bucle
    jl aux
    
    ;despues del div, rdx: residuo y rax: cociente
    div r8 ; saca el menor digito y lo guarda en la pila (esto solo se ejecuta cuando ya se sabe que el numero es de mas de 1 digito)
    inc rbx
    push rdx;rdx contiene el residuo al dividir el numero entre 10
    xor rdx, rdx
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

;sys_exit
	mov rax, 60
	mov rdi, 0
	syscall



	
	
