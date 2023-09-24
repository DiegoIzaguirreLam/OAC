
;RDI -> arrLongitud
;RSI -> arrLatitud
;RDX -> cant
;RCX -> distancia
;xmm0 -> multiplicador
global asmHallaDistancias
	section .text


asmHallaDistancias:
	xorpd xmm2, xmm2
	xorpd xmm3, xmm3
	movsd xmm5, [rdi]
	movsd xmm1, [rsi]
	xor r10,r10
	inc r10

loop:
	movsd xmm2, [rdi+8*r10]
	movsd xmm3, [rsi+8*r10]
	subsd xmm2, xmm5
	subsd xmm3, xmm1
	mulsd xmm2, xmm2
	mulsd xmm3, xmm3
	addsd xmm3, xmm2
	sqrtsd xmm3, xmm3
	mulsd xmm3, xmm0
	movsd [rcx+8*r10-8], xmm3
	inc r10
	cmp r10, rdx
	jne loop

final:
	ret




