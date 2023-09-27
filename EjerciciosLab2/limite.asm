;rdi = n

	global asmFuncion
	section .text

asmFuncion:
	mov r8, 1
	cvtsi2sd xmm3, r8
	movsd xmm1, xmm3
	cvtsi2sd xmm2, rdi
	divsd xmm1, xmm2
	addsd xmm1, xmm3
	xor r8, r8
	movsd xmm0, xmm1
	inc r8
potencia_n:
	mulsd xmm0, xmm1
	inc r8
	cmp r8, rdi
	jne potencia_n

final:
	ret


