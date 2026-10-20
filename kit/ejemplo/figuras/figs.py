import sys, numpy as np, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Circle
sys.path.insert(0,'/tmp/claude-0/solc'); import lw
from mols import MOLS
lw.COL.update({'B':'#8D6E63','Be':'#6D4C41','Al':'#78909C','Si':'#8D6E63'})
G='#1B5E20'; K='#333'
# ---------- Lewis 2D ----------
LAY={'AB₂':([180,0],[]),'AB₃':([90,210,330],[]),'AB₄':([90,180,0,270],[]),'AB₃E':([180,0,270],[90]),'AB₂E₂':([210,330],[60,120])}
def lewis(m):
    angs,lpc=LAY[m['tipo']]
    t=m['t']
    if m['id']=='HCN': angs=[180,0]
    at=[(m['c'],0,0)]; bonds=[]; lp=[(0,a) for a in lpc]
    for k,((s,o),a) in enumerate(zip(t,angs)):
        r=1.45 if o>1 or s in('Cl','S','Si') else (1.12 if s=='H' else 1.3)
        x,y=r*np.cos(np.radians(a)),r*np.sin(np.radians(a)); at.append((s,x,y)); bonds.append((0,k+1,o))
        if s!='H':
            npair=(8-2*o)//2
            offs={3:[0,90,-90],2:[55,-55],1:[0]}.get(npair,[])
            for d in offs: lp.append((k+1,a+d))
    mol={'atoms':at,'bonds':bonds,'lp':lp}
    if m['q']: mol['charge']='+'
    fig=plt.figure(figsize=(4.2,3.6),dpi=150); ax=fig.add_axes([0,0,1,1])
    ax.set_xlim(-2.5,2.5); ax.set_ylim(-2.1,2.2); ax.set_aspect('equal'); ax.axis('off')
    lw.draw(ax,mol,0,0,22)
    plt.savefig(f"img/lewis_{m['id']}.png",transparent=False,facecolor='white'); plt.close()
# ---------- geometría 3D ----------
CO={'H':'#ECEFF1','C':'#37474F','N':'#3949AB','O':'#E53935','F':'#7CB342','Cl':'#43A047','S':'#FDD835','P':'#FB8C00','B':'#A1887F','Be':'#8D6E63','Al':'#B0BEC5','Si':'#BCAAA4'}
RA={'H':.21,'C':.30,'N':.29,'O':.29,'F':.27,'B':.29,'Be':.29,'Cl':.33,'S':.33,'P':.33,'Al':.35,'Si':.35}
a=np.radians(109.47/2)
def dirs(tipo,mid):
    if tipo=='AB₂': return [(-1,0,0),(1,0,0)],[]
    if tipo=='AB₃':
        return [(np.cos(np.radians(t)),0,np.sin(np.radians(t))) for t in (90,210,330)],[]
    T2=[(-np.sin(a),0,-np.cos(a)),(np.sin(a),0,-np.cos(a))]; L2=[(0,np.sin(a),np.cos(a)),(0,-np.sin(a),np.cos(a))]
    if tipo=='AB₄': return T2+L2,[]
    if tipo=='AB₂E₂': return T2,L2
    if tipo=='AB₃E':
        th=np.radians(109.47); v=[]
        for ph in (-90,30,150):
            p=np.radians(ph); v.append((np.sin(th)*np.cos(p),np.sin(th)*np.sin(p),np.cos(th)))
        return v,[(0,0,1)]
RX,RZ=-15,-35
def rot(v):
    # leve giro para dar sensación 3D
    rx=np.radians(RX); ry=0; rz=np.radians(RZ)
    x,y,z=v
    x,y=x*np.cos(rz)-y*np.sin(rz),x*np.sin(rz)+y*np.cos(rz)
    y,z=y*np.cos(rx)-z*np.sin(rx),y*np.sin(rx)+z*np.cos(rx)
    return np.array([x,y,z])
def lobe(ax,p,d,L,w,z):
    t=np.linspace(0,2*np.pi,80); px=L*.5*(1+np.cos(t)); py=w*.5*np.sin(t)*(1+np.cos(t))*.9
    ang=np.arctan2(d[1],d[0]); X=p[0]+px*np.cos(ang)-py*np.sin(ang); Y=p[1]+px*np.sin(ang)+py*np.cos(ang)
    ax.add_patch(Polygon(np.c_[X,Y],fc='#FFE082',ec='#F9A825',lw=1.5,alpha=.85,zorder=z))
def geo(m):
    D,L=dirs(m['tipo'],m['id'])
    if m['tipo'] in ('AB₂','AB₃') or m['id']=='HCN':
        R=lambda v: np.array(v,float)*np.array([1,1,1])
        R=lambda v: np.array([v[0],-0.25*v[2]*0+v[1],v[2]])
    fig=plt.figure(figsize=(4.2,3.6),dpi=150); ax=fig.add_axes([0,0,1,1]); ax.set_xlim(-2.2,2.2); ax.set_ylim(-1.75,2.0); ax.set_aspect('equal'); ax.axis('off')
    planar = m['tipo'] in ('AB₂','AB₃')
    items=[]
    c=m['c']; rc=RA[c]
    for (s,o),v in zip(m['t'],D):
        v=np.array(v,float); w=v if planar else rot(v)
        bl=1.4 if s!='H' else 1.15
        p=np.array([w[0],w[2]])*bl; depth=w[1]
        items.append((depth,'b',p,o)); items.append((depth+0.001,'a',p,s))
    for v in L:
        w=rot(np.array(v,float)); items.append((w[1]-0.5,'l',np.array([w[0],w[2]]),None))
    items.append((0,'c',np.zeros(2),c))
    items.sort(key=lambda x:x[0])
    for dep,k,p,x in items:
        z=5+dep*2
        if k=='l':
            z=min(z,4.6)
            n=np.linalg.norm(p); lobe(ax,np.zeros(2),p/n if n>0 else np.array([0,1]),1.15*max(n,.45),0.85,z)
        elif k=='b':
            ax.plot([0,p[0]],[0,p[1]],color='#546E7A',lw=7 if x==1 else 9,solid_capstyle='round',zorder=z)
            if x>1: ax.plot([0,p[0]],[0,p[1]],color='white',lw=1.6,zorder=z+0.01)
        elif k in('a','c'):
            r=RA[x]*(1+0.18*dep)
            if k=='c': z=12
            ax.add_patch(Circle(p,r,fc=CO[x],ec='#263238',lw=1.4,zorder=z+0.5))
            ax.text(*p,x,ha='center',va='center',fontsize=11 if len(x)==1 else 10,fontweight='bold',color='white' if x in('C','N','Be','B') else '#212121',zorder=z+0.6)
    ax.text(0,1.8,f"{m['geom'].capitalize()} · {m['ang']}",ha='center',fontsize=12.5,fontweight='bold',color=G)
    if m['lp']: ax.text(0,-1.62,'en amarillo: pares solitarios',ha='center',fontsize=8.5,color='#B26A00')
    plt.savefig(f"img/geo_{m['id']}.png",facecolor='white'); plt.close()
for m in MOLS:

    RX,RZ={'AB₃E':(-25,-30),'AB₂E₂':(-15,-35),'AB₄':(-15,-35)}.get(m['tipo'],(-15,-35))
    lewis(m); geo(m)
print('ok')
