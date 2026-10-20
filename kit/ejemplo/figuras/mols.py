# Datos de las moléculas sorpresa (comprobados con N–D–C–S)
VAL={'H':1,'Be':2,'B':3,'Al':3,'C':4,'Si':4,'N':5,'P':5,'O':6,'S':6,'F':7,'Cl':7}
NEED={'H':2,'Be':4,'B':6,'Al':6}
MOLS=[
 # id, formula, nombre, central, terminales [(sym, orden_enlace)], pares_central, carga, tipo, disp, geom, ang, hib, polar, fuerzas, nota
 dict(id='BeCl2',f='BeCl₂',n='dicloruro de berilio',c='Be',t=[('Cl',1),('Cl',1)],lp=0,q=0,tipo='AB₂',disp='lineal',geom='lineal',ang='180°',hib='sp',pol='apolar',fz='London (dispersión)',nota='Hipovalente: el Be se queda con 4 e⁻.'),
 dict(id='CO2',f='CO₂',n='dióxido de carbono',c='C',t=[('O',2),('O',2)],lp=0,q=0,tipo='AB₂',disp='lineal',geom='lineal',ang='180°',hib='sp',pol='apolar',fz='London (dispersión)',nota='Cada doble enlace cuenta como una sola zona.'),
 dict(id='CS2',f='CS₂',n='disulfuro de carbono',c='C',t=[('S',2),('S',2)],lp=0,q=0,tipo='AB₂',disp='lineal',geom='lineal',ang='180°',hib='sp',pol='apolar',fz='London (dispersión)',nota='El S está en el grupo del O: igual que el CO₂.'),
 dict(id='HCN',f='HCN',n='cianuro de hidrógeno',c='C',t=[('H',1),('N',3)],lp=0,q=0,tipo='AB₂',disp='lineal',geom='lineal',ang='180°',hib='sp',pol='polar',fz='dipolo-dipolo y London',nota='Lineal pero polar: los dos átomos unidos al C son distintos.'),
 dict(id='BF3',f='BF₃',n='trifluoruro de boro',c='B',t=[('F',1)]*3,lp=0,q=0,tipo='AB₃',disp='trigonal plana',geom='trigonal plana',ang='120°',hib='sp²',pol='apolar',fz='London (dispersión)',nota='Hipovalente: el B se queda con 6 e⁻.'),
 dict(id='AlCl3',f='AlCl₃',n='tricloruro de aluminio',c='Al',t=[('Cl',1)]*3,lp=0,q=0,tipo='AB₃',disp='trigonal plana',geom='trigonal plana',ang='120°',hib='sp²',pol='apolar',fz='London (dispersión)',nota='El Al está en el grupo del B: hipovalente como el BF₃ (6 e⁻).'),
 dict(id='CH2O',f='CH₂O',n='metanal',c='C',t=[('O',2),('H',1),('H',1)],lp=0,q=0,tipo='AB₃',disp='trigonal plana',geom='trigonal plana',ang='≈ 120°',hib='sp²',pol='polar',fz='dipolo-dipolo y London',nota='Trigonal plana pero polar: un O y dos H unidos al C.'),
 dict(id='CH4',f='CH₄',n='metano',c='C',t=[('H',1)]*4,lp=0,q=0,tipo='AB₄',disp='tetraédrica',geom='tetraédrica',ang='109,5°',hib='sp³',pol='apolar',fz='London (dispersión)',nota=''),
 dict(id='SiCl4',f='SiCl₄',n='tetracloruro de silicio',c='Si',t=[('Cl',1)]*4,lp=0,q=0,tipo='AB₄',disp='tetraédrica',geom='tetraédrica',ang='109,5°',hib='sp³',pol='apolar',fz='London (dispersión)',nota='El Si está en el grupo del C: igual que el CCl₄.'),
 dict(id='CHCl3',f='CHCl₃',n='triclorometano (cloroformo)',c='C',t=[('H',1),('Cl',1),('Cl',1),('Cl',1)],lp=0,q=0,tipo='AB₄',disp='tetraédrica',geom='tetraédrica',ang='≈ 109,5°',hib='sp³',pol='polar',fz='dipolo-dipolo y London',nota='Tetraédrica pero polar: un H y tres Cl unidos al C.'),
 dict(id='NH4',f='NH₄⁺',n='ion amonio',c='N',t=[('H',1)]*4,lp=0,q=1,tipo='AB₄',disp='tetraédrica',geom='tetraédrica',ang='109,5°',hib='sp³',pol='es un ion (los 4 enlaces son iguales)',fz='—',nota='Uno de los enlaces N–H es coordinado (dativo): NH₃ + H⁺ → NH₄⁺. Carga formal del N: +1.'),
 dict(id='NH3',f='NH₃',n='amoníaco',c='N',t=[('H',1)]*3,lp=1,q=0,tipo='AB₃E',disp='tetraédrica',geom='pirámide trigonal',ang='≈ 107°',hib='sp³',pol='polar',fz='puentes de hidrógeno (además de dipolo-dipolo y London)',nota='El par solitario cierra el ángulo por debajo de 109,5°.'),
 dict(id='PH3',f='PH₃',n='fosfano (fosfina)',c='P',t=[('H',1)]*3,lp=1,q=0,tipo='AB₃E',disp='tetraédrica',geom='pirámide trigonal',ang='< 109,5°',hib='sp³',pol='polar',fz='dipolo-dipolo y London (no forma puentes de hidrógeno)',nota='El P está en el grupo del N: igual que el NH₃, pero sin puentes de H.'),
 dict(id='NF3',f='NF₃',n='trifluoruro de nitrógeno',c='N',t=[('F',1)]*3,lp=1,q=0,tipo='AB₃E',disp='tetraédrica',geom='pirámide trigonal',ang='< 109,5°',hib='sp³',pol='polar',fz='dipolo-dipolo y London (no tiene H: no hay puentes de H)',nota=''),
 dict(id='PCl3',f='PCl₃',n='tricloruro de fósforo',c='P',t=[('Cl',1)]*3,lp=1,q=0,tipo='AB₃E',disp='tetraédrica',geom='pirámide trigonal',ang='< 109,5°',hib='sp³',pol='polar',fz='dipolo-dipolo y London',nota=''),
 dict(id='H2O',f='H₂O',n='agua',c='O',t=[('H',1)]*2,lp=2,q=0,tipo='AB₂E₂',disp='tetraédrica',geom='angular',ang='≈ 104,5°',hib='sp³',pol='polar',fz='puentes de hidrógeno (además de dipolo-dipolo y London)',nota='Los dos pares solitarios cierran el ángulo.'),
 dict(id='H2S',f='H₂S',n='sulfuro de hidrógeno',c='S',t=[('H',1)]*2,lp=2,q=0,tipo='AB₂E₂',disp='tetraédrica',geom='angular',ang='< 109,5°',hib='sp³',pol='polar',fz='dipolo-dipolo y London (no forma puentes de hidrógeno)',nota='El S está en el grupo del O: angular como el agua.'),
 dict(id='OF2',f='OF₂',n='difluoruro de oxígeno',c='O',t=[('F',1)]*2,lp=2,q=0,tipo='AB₂E₂',disp='tetraédrica',geom='angular',ang='< 109,5°',hib='sp³',pol='polar',fz='dipolo-dipolo y London',nota='Se escribe OF₂ (y no F₂O) porque el F es más electronegativo.'),
]
def ndcs(m):
    atoms=[m['c']]+[a for a,_ in m['t']]
    N=sum(NEED.get(a,8) for a in atoms)
    D=sum(VAL[a] for a in atoms)-m['q']
    C=N-D; S=D-C
    return N,D,C,S
if __name__=='__main__':
    for m in MOLS:
        N,D,C,S=ndcs(m)
        bonds=sum(o for _,o in m['t'])
        # comprobación: C/2 = pares enlazantes = suma de órdenes; S/2 = pares solitarios totales
        lpt=m['lp']+sum((3 if a in('F','Cl') else (3-o+1 if a in('O','S','N') else 0)) if a!='H' else 0 for a,o in m['t'])
        # pares solitarios terminales: halógeno simple 3; O/S: 4-orden ... N triple:1
        def lpterm(a,o):
            if a=='H': return 0
            return (8-2*o- (0))//2 - 0
        lpt=m['lp']+sum((8-2*o)//2 - (0) for a,o in m['t'] if a!='H')
        ok = (C//2==bonds) and (S//2==lpt)
        print(f"{m['f']:6} N={N:2} D={D:2} C={C:2} ({C//2} pares, órdenes={bonds}) S={S:2} ({S//2} pares, esperados {lpt}) {'OK' if ok else 'REVISAR'}")
