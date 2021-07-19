medida = float(input('uma distancia em metros'))
km = medida/1000
hm = medida/100
dam = medida/10
dm = medida*10
cm = medida*100
mm = medida*1000
print('a medida de {}m, equivale a {}km, {}hm, {}dam, {}dm, {}cm e {}mm'.format(medida, km, hm, dam, dm, cm, mm))
