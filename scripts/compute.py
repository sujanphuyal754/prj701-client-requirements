import numpy as np, itertools, json
names=["Bai et al. [48]","Wu et al. [20]","Li et al. [42]","Yang et al. [77]","Wang et al. [78]","Wang et al. [79]","He et al. [80]","Lucas et al. [81]","Hao et al. [82]","Shang et al. [83]","Zhang et al. [84]","Zhang [85]"]
princ=["Cross-chain sharing","Smart contracts","Ledger management","Revocable sharing","Smart contracts","Dual-chain system","Multi-chain architecture","Blockchain authorization","Smart contracts","Cloud-edge-end with blockchain","Consensus and smart contracts","Node network theory"]
crit=["Multi-domain collaboration","Efficiency overhead","Poor traceability","Secure sharing","Legitimate fairness"]
X=np.array([[1,1,0,1,0],[0,1,0,0,1],[0,0,1,1,0],[0,1,0,1,1],[0,0,0,1,0],[1,1,0,0,0],[0,1,0,1,0],[1,1,0,0,0],[0,1,0,1,0],[0,1,0,1,0],[0,1,0,1,0],[0,1,0,1,0]],float)
m,n=X.shape
types=["Benefit"]*n
# AHP upper-triangle judgments A[i,j] for i<j (criteria order as above)
UP={(0,1):1/2,(0,2):1/3,(0,3):1/4,(0,4):2,(1,2):1/2,(1,3):1/3,(1,4):3,(2,3):1/2,(2,4):4,(3,4):6}
RI={1:0,2:0,3:.58,4:.9,5:1.12,6:1.24,7:1.32,8:1.41,9:1.45,10:1.49}
V_PARAM=0.5
def rk(x,desc=True):
    x=np.round(np.asarray(x,float),10)
    return [int(1+(x>v).sum()) if desc else int(1+(x<v).sum()) for v in x]
best=np.where(np.array(types)=="Cost",X.min(0),X.max(0)); worst=np.where(np.array(types)=="Cost",X.max(0),X.min(0))
R=(X-worst)/(best-worst)
def ahp():
    A=np.ones((n,n))
    for (i,j),v in UP.items(): A[i,j]=v; A[j,i]=1/v
    cs=A.sum(0); N=A/cs; w=N.mean(1); ws=A@w; lam=(ws/w).mean(); CI=(lam-n)/(n-1); CR=CI/RI[n]
    return dict(A=A,cs=cs,N=N,w=w,ws=ws,lam_i=ws/w,lam=lam,CI=CI,RI=RI[n],CR=CR)
def critic():
    sd=R.std(0,ddof=1); C=np.corrcoef(R.T); conf=1-C; sc=conf.sum(1); Cj=sd*sc; w=Cj/Cj.sum()
    return dict(R=R,sd=sd,C=C,conf=conf,sumconf=sc,Cj=Cj,w=w)
def entropy():
    cs=X.sum(0); r=X/cs; rl=np.where(r>0,r*np.log(np.where(r>0,r,1)),0); h=1/np.log(m); e=-h*rl.sum(0); d=1-e; w=d/d.sum()
    return dict(cs=cs,r=r,rl=rl,sl=rl.sum(0),h=h,e=e,d=d,w=w)
def topsis(w):
    den=np.sqrt((X**2).sum(0)); N=X/den; V=N*w
    vb=np.where(np.array(types)=="Cost",V.min(0),V.max(0)); vw=np.where(np.array(types)=="Cost",V.max(0),V.min(0))
    sp=np.sqrt(((V-vb)**2).sum(1)); sm=np.sqrt(((V-vw)**2).sum(1)); C=np.round(sm/(sp+sm),10)
    return dict(den=den,N=N,V=V,vb=vb,vw=vw,sp=sp,sm=sm,C=C,rank=rk(C))
def vikor(w,v=V_PARAM):
    T=w*(best-X)/(best-worst); S=T.sum(1); Rr=T.max(1)
    Ss,Sm,Rs,Rm=S.min(),S.max(),Rr.min(),Rr.max()
    Q=np.round(v*(S-Ss)/(Sm-Ss)+(1-v)*(Rr-Rs)/(Rm-Rs),10); rank=rk(Q,False)
    DQ=1/(m-1); q1=Q.min(); srt=np.sort(Q); q2=next((x for x in srt if x>q1+1e-12),None)
    a1=int(np.argmin(Q)); gap=None if q2 is None else q2-q1
    c1=gap is not None and gap>=DQ-1e-12; c2=(abs(S[a1]-Ss)<1e-12) or (abs(Rr[a1]-Rs)<1e-12)
    comp=[]
    for i in range(m):
        if abs(Q[i]-q1)<1e-12: comp.append("Yes")
        elif not c1: comp.append("Yes" if Q[i]-q1<DQ else "No")
        elif not c2: comp.append("Yes" if q2 is not None and abs(Q[i]-q2)<1e-12 else "No")
        else: comp.append("No")
    return dict(T=T,S=S,R=Rr,Ss=Ss,Sm=Sm,Rs=Rs,Rm=Rm,Q=Q,rank=rank,DQ=DQ,a1=a1,q1=q1,q2=q2,gap=gap,c1=bool(c1),c2=bool(c2),comp=comp)
def promethee(w):
    pi=np.zeros((m,m))
    for a in range(m):
        for b in range(m):
            if a!=b: pi[a,b]=(w*np.maximum(0,R[a]-R[b])).sum()/w.sum()
    pp=pi.sum(1)/(m-1); pm=pi.sum(0)/(m-1); phi=np.round(pp-pm,10)
    return dict(pi=pi,pp=pp,pm=pm,phi=phi,rank=rk(phi))
def sens(w):
    P=np.round(R@w,12); rank=rk(P); pairs=list(itertools.combinations(range(m),2))
    top=int(np.argmax(P)); D=[];F=[];Dp=[]
    for i,j in pairs:
        dr=[];fr=[];pr=[]
        for k in range(n):
            den=R[j,k]-R[i,k]
            if abs(P[j]-P[i])<1e-12 or abs(den)<1e-12: dr.append(None);fr.append(None);pr.append(None);continue
            d=(P[j]-P[i])/den; dr.append(d)
            if d<=w[k]+1e-12: fr.append(d); pr.append(d*100/w[k])
            else: fr.append(None); pr.append(None)
        D.append(dr);F.append(fr);Dp.append(pr)
    absd=[[None if v is None else abs(v) for v in r] for r in Dp]
    flag=[1 if top in p else 0 for p in pairs]
    def colmin(rows,k,sel=None):
        v=[(r[k],idx) for idx,r in enumerate(rows) if r[k] is not None and (sel is None or sel[idx])]
        return min(v) if v else None
    allmin=[colmin(absd,k) for k in range(n)]; topmin=[colmin(absd,k,flag) for k in range(n)]
    return dict(P=P,rank=rank,pairs=pairs,top=top,D=D,F=F,Dp=Dp,absd=absd,flag=flag,allmin=allmin,topmin=topmin)
def whatif(w,P,k,pct):
    w2=w.copy(); w2[k]=w[k]*(1-pct/100); P2=np.round(R@w2,12); return w2,P2,rk(P2)
def all_results():
    a=ahp(); c=critic(); e=entropy(); comb=(a['w']+c['w']+e['w'])/3
    sets={"Combined":comb,"AHP":a['w'],"CRITIC":c['w'],"Entropy":e['w']}
    res=dict(ahp=a,critic=c,entropy=e,comb=comb,sets=sets,topsis={},vikor={},prom={})
    for k,w in sets.items(): res['topsis'][k]=topsis(w); res['vikor'][k]=vikor(w); res['prom'][k]=promethee(w)
    res['sens']=sens(comb)
    return res
if __name__=="__main__":
    r=all_results()
    print("CR",r['ahp']['CR']); print({k:v.round(4) for k,v in r['sets'].items()})
    s=r['sens']; print("top",names[s['top']],"rank",s['rank']); print("allmin",[(round(x[0],2),s['pairs'][x[1]]) if x else None for x in s['allmin']]); print("topmin",[(round(x[0],2),s['pairs'][x[1]]) if x else None for x in s['topmin']])
    # overall mean ranks
    allr=np.array([r[mm][k]['rank'] for k in r['sets'] for mm in ('topsis','vikor','prom')],float)
    print("mean rank all 12:",dict(zip([x.split()[0]+x.split()[1] for x in names],allr.mean(0).round(2))))
    comb3=np.array([r[mm]['Combined']['rank'] for mm in ('topsis','vikor','prom')],float).mean(0); print("mean rank comb:",comb3.round(2))
    v=r['vikor']['Combined']; print("vikor cond",names[v['a1']],v['q1'],v['q2'],v['gap'],v['DQ'],v['c1'],v['c2'],[names[i][:6] for i in range(m) if v['comp'][i]=='Yes'])
    w2,P2,rk2=whatif(r['comb'],s['P'],0,3.5); print("whatif",rk2)
