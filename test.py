from marvel import Marvel

pubk = "ac937b80db7eb2286b74f2eb5a0587a0"
privk = "398782c53a08890a532da12b26a2f7480efe4737"

m = Marvel(pubk, privk)

#print(m.characters.all())

#print(m.comics.all())

print(m.creators.all())