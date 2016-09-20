# Takk til Halvor Sakshaug for Lure Triks (tm)
# (bruk av radix sort med siffergrupper bestaaende av 11 bits).

from sys import stdin

def merge():
     bpg = 11
     bb = 0
     mv = 0
     siffergruppe_verdier = 1 << bpg
     siffergruppe_maks = siffergruppe_verdier-1
     siffer = [[] for i in range(siffergruppe_verdier)]
     for l in stdin:
          (bokstav, l_med_t) = l.split(":")
          for t in map(int, l_med_t.split(",")):
               if (t > mv):
                   mv = t
               siffer[t & siffergruppe_maks].append((t, bokstav))
     while(mv > siffergruppe_verdier):
          mv >>= bpg
          bb += bpg
          a = siffer
          siffer = [[] for i in range(siffergruppe_verdier)]
          # Foelgende plasserer noen tupler i siffer[0], disse staar da bakerst og er sortert
          for aa in a:
               for p in aa:
                    siffer[(p[0] >> bb) & siffergruppe_maks].append(p)

     print ("".join(["".join([d[1] for d in c]) for c in siffer]))

merge()
