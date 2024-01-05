#Música - Grupo 33

#declaração de varíaveis das notas musicais

midtone = 2**(1/12)
la4 = 440.00
la4s = la4 * midtone
si4 = la4s * midtone
do5 = si4 * midtone
sol4s = la4/midtone
sol4 = sol4s/midtone
fa4s = sol4/midtone
fa4 = fa4s/midtone
mi4 = fa4/midtone
do4 = do5/2
do4s = do4 * midtone
re4 = do4s * midtone
re4s = re4 * midtone
re3 = re4/2
mi3 = mi4/2
fa3s = fa4s/2
sol3 = sol4/2
la3 = la4/2
si3 = si4/2

samplingrate = 16000
t=timevar(1)
x = seqsin(0, 0.7, sol4, 0.1, fa4s, 0.1, sol4, 0.2, si4, 0.1, do5, 0.1, si4, 0.8, 0, 0.2, fa4s, 0.1, sol4, 0.1, fa4s, 0.2, sol4, 0.1, la4, 0.1, sol4, 0.8, 0, 0.2, fa4s, 0.1, mi4, 0.1, fa4s, 0.2, si4, 0.1, do5, 0.1, si4, 0.8, 0, 0.2, fa4s, 0.1, mi4, 0.1, fa4s, 1.0, 0, 0.7)

#Extra
y = seqsin(0, 0.5, mi4, 0.2, si3, 0.2, mi4, 0.2, si3, 0.2, mi4, 0.2, si3, 0.2, mi4, 0.2, si3, 0.2, re4, 0.2, si3, 0.2, re4, 0.2, si3, 0.2, re4, 0.2, si3, 0.2, re4, 0.2, si3, 0.2, re4, 0.2, si3, 0.2, re4, 0.2, si3, 0.2, re4, 0.2, si3, 0.2, re4, 0.2, si3, 0.2, re4, 0.2, la3, 0.2, re4, 0.2, la3, 0.2, re4, 0.2, la3, 0.2, re4, 0.2, la3, 0.2, 0, 0.5)   

z = seqsin(0, 0.5, mi3, 0.4, sol3, 0.4, mi3, 0.4, sol3, 0.4, re3, 0.4, sol3, 0.4, re3, 0.4, sol3, 0.4, re3, 0.4, fa3s , 0.4, re3, 0.4, fa3s, 0.4, re3, 0.4, fa3s, 0.4, re3, 0.4, fa3s, 0.4, 0, 0.5)

play(0.5*x + 0.25*y + 0.25*z)
