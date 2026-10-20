import numpy as np, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
K='#333'; LPC='#555'; R='#B71C1C'; G='#1B5E20'
COL={'O':'#D32F2F','N':'#3949AB','C':'#263238','H':'#616161','Cl':'#2E7D32','F':'#2E7D32','Br':'#8C1F1F','S':'#9A8A00','P':'#D46A00','I':'#7A007A'}
def draw(ax,mol,ox=0,oy=0,fs=20):
    at=mol['atoms']; P=[(x+ox,y+oy) for _,x,y in at]
    for b in mol.get('bonds',[]):
        i,j,n=b[:3]; p=np.array(P[i]);q=np.array(P[j]);d=q-p;u=d/np.linalg.norm(d);nn=np.array([-u[1],u[0]])
        offs={1:[0],2:[-.07,.07],3:[-.12,0,.12]}[n]
        for o in offs:
            s=p+u*0.33+nn*o; e=q-u*0.33+nn*o; ax.plot(*zip(s,e),color=K,lw=2.2)
    for k,(s,x,y) in enumerate(at):
        ax.text(*P[k],s,ha='center',va='center',fontsize=fs,fontweight='bold',color=COL.get(s,K))
    for (i,ang) in mol.get('lp',[]):
        t=np.radians(ang); x,y=P[i][0]+0.42*np.cos(t),P[i][1]+0.42*np.sin(t); s=0.1
        for kk in (-1,1): ax.plot(x-kk*s*np.sin(t),y+kk*s*np.cos(t),'o',ms=4.5,color=LPC)
    for (i,ch,ang) in mol.get('fc',[]):
        t=np.radians(ang); ax.text(P[i][0]+0.55*np.cos(t),P[i][1]+0.55*np.sin(t),ch,ha='center',va='center',fontsize=fs*0.55,color=R,fontweight='bold')
    if 'charge' in mol:
        xs=[p[0] for p in P]; ys=[p[1] for p in P]; x0,x1=min(xs)-0.85,max(xs)+0.85; y0,y1=min(ys)-0.85,max(ys)+0.85
        ax.plot([x0+.12,x0,x0,x0+.12],[y1,y1,y0,y0],color=K,lw=1.4); ax.plot([x1-.12,x1,x1,x1-.12],[y1,y1,y0,y0],color=K,lw=1.4)
        ax.text(x1+0.08,y1-0.05,mol['charge'],fontsize=fs*0.65,fontweight='bold',va='top')
def grid(mols,path,ncol=3,cell=(5.2,3.4),fs=20,titles=True):
    n=len(mols); nrow=(n+ncol-1)//ncol
    fig=plt.figure(figsize=(cell[0]*ncol/1.6,cell[1]*nrow/1.6),dpi=170)
    for k,m in enumerate(mols):
        r,c=divmod(k,ncol)
        ax=fig.add_axes([c/ncol,1-(r+1)/nrow,1/ncol,1/nrow]); ax.set_xlim(-cell[0]/2,cell[0]/2); ax.set_ylim(-cell[1]/2-0.35,cell[1]/2+0.7); ax.set_aspect('equal'); ax.axis('off')
        if titles and m.get('title'): ax.text(0,cell[1]/2+0.55,m['title'],ha='center',va='top',fontsize=fs*0.6,color=G,fontweight='bold')
        draw(ax,m,0,-0.15,fs)
        if m.get('note'): ax.text(0,-cell[1]/2+0.25,m['note'],ha='center',va='bottom',fontsize=fs*0.45,color='#757575')
    plt.savefig(path,bbox_inches='tight',pad_inches=0.1); plt.close()
