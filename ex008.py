m = float(input('Digite quantos metros vamos converter: '))
km = m*0.001
hm = m*0.01
dam = m*0.1
dm = m*10
cm = m*100
mm = m*1000
print('A medida de {} metros corresponde a \n{}km \n{}hm \n{:.1f}dam \n{:.0f}dm \n{:.0f}cm \n{:.0f}mm'.format(m, km, hm, dam, dm, cm, mm))
