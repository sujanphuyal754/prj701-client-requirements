import json, numpy as np
from openpyxl import load_workbook
from openpyxl.utils import get_column_letter as L
from compute import *
lay=json.load(open("layout.json")); wb=load_workbook("../workbook/MCDM_Complete_Analysis.xlsx",data_only=True)
r=all_results(); bad=0
def chk(name,a,b,tol=1e-6):
    global bad
    a=np.array(a,float); b=np.array(b,float)
    ok=np.allclose(a,b,atol=tol,equal_nan=True)
    if not ok: bad+=1; print("MISMATCH",name,"\n xl",a.round(5),"\n py",b.round(5))
    else: print("ok",name)
g=lambda ws,c: wb[ws][c].value
# AHP, CRITIC, Entropy, Weights
chk("AHP w",[g("AHP",f"G{15+k}") for k in range(n)],r['ahp']['w']); chk("AHP CR",[g("AHP","B34")],[r['ahp']['CR']]); chk("AHP lam",[g("AHP","B31")],[r['ahp']['lam']])
chk("CRITIC sd",[g("CRITIC",f"{L(2+k)}18") for k in range(n)],r['critic']['sd']); chk("CRITIC corr",[[g("CRITIC",f"{L(2+j)}{22+i}") for j in range(n)] for i in range(n)],r['critic']['C'])
chk("CRITIC w",[g("CRITIC",f"E{38+k}") for k in range(n)],r['critic']['w'])
chk("Entropy e",[g("Entropy",f"{L(2+k)}55") for k in range(n)],r['entropy']['e']); chk("Entropy w",[g("Entropy",f"{L(2+k)}57") for k in range(n)],r['entropy']['w'])
for key,row in {"AHP":6,"CRITIC":7,"Entropy":8,"Combined":9}.items(): chk("Weights "+key,[g("Weights",f"{L(2+k)}{row}") for k in range(n)],r['sets'][key])
for key in r['sets']:
    s=lay['T'][key]; t=r['topsis'][key]
    chk(f"TOPSIS C {key}",[g("TOPSIS",f"I{s+5+i}") for i in range(m)],t['C']); chk(f"TOPSIS rank {key}",[g("TOPSIS",f"J{s+5+i}") for i in range(m)],t['rank'])
    chk(f"TOPSIS V {key}",[[g("TOPSIS",f"{L(2+k)}{s+5+i}") for k in range(n)] for i in range(m)],t['V'])
    s=lay['V'][key]; v=r['vikor'][key]
    chk(f"VIKOR Q {key}",[g("VIKOR",f"I{s+3+i}") for i in range(m)],v['Q']); chk(f"VIKOR rank {key}",[g("VIKOR",f"J{s+3+i}") for i in range(m)],v['rank'])
    xc=[g("VIKOR",f"K{s+3+i}") for i in range(m)]
    if xc!=v['comp']: bad+=1; print("MISMATCH comp",key,xc,v['comp'])
    else: print("ok VIKOR comp",key)
    print("   conditions:",g("VIKOR",f"B{s+18}"),g("VIKOR",f"B{s+21}"),g("VIKOR",f"B{s+22}"),g("VIKOR",f"B{s+23}"), "| py",names[v['a1']],round(v['gap'],4),v['c1'],v['c2'])
    s=lay['P'][key]; p=r['prom'][key]
    chk(f"PROM phi {key}",[g("PROMETHEE-II",f"P{s+3+i}") for i in range(m)],p['phi']); chk(f"PROM rank {key}",[g("PROMETHEE-II",f"Q{s+3+i}") for i in range(m)],p['rank'])
chk("PROM pi comb",[[0 if a==b else g("PROMETHEE-II",f"{L(2+b)}{lay['P']['Combined']+3+a}") for b in range(m)] for a in range(m)],r['prom']['Combined']['pi'])
# Summary
mr=np.array([r[mm]['Combined']['rank'] for mm in ('topsis','vikor','prom')],float).mean(0)
chk("Summary mean comb",[g("Summary",f"H{13+i}") for i in range(m)],mr)
allr=np.array([r[mm][k]['rank'] for k in r['sets'] for mm in ('topsis','vikor','prom')],float).mean(0)
chk("Summary mean all12",[g("Summary",f"N{29+i}") for i in range(m)],allr)
print("Final ranks (comb):",[g("Summary",f"I{13+i}") for i in range(m)],"overall:",[g("Summary",f"O{29+i}") for i in range(m)])
# Sensitivity
s=r['sens']; ts=lay['tstart']
chk("Sens P",[g("Sensitivity",f"G{7+i}") for i in range(m)],s['P']); chk("Sens rank",[g("Sensitivity",f"H{7+i}") for i in range(m)],s['rank'])
def tab(t,key=None):
    out=[]
    for p in range(lay['NP']):
        row=[]
        for k in range(n):
            v=g("Sensitivity",f"{L(4+k)}{ts[t]+2+p}"); row.append(np.nan if (v is None or isinstance(v,str)) else v)
        out.append(row)
    return np.array(out,float)
py=lambda rows: np.array([[np.nan if v is None else v for v in rr] for rr in rows],float)
chk("Sens T1 delta",tab(0),py(s['D'])); chk("Sens T2 feasible",tab(1),py(s['F'])); chk("Sens T3 delta'",tab(2),py(s['Dp']))
print("Sens summary xl all:",[g("Sensitivity",f"{L(2+k)}24") for k in range(n)]); print("   py all:",[None if x is None else round(x[0],4) for x in s['allmin']])
print("Sens summary xl top:",[g("Sensitivity",f"{L(2+k)}25") for k in range(n)]); print("   py top:",[None if x is None else round(x[0],4) for x in s['topmin']])
print("crit rank",[g("Sensitivity",f"{L(2+k)}27") for k in range(n)],"most critical:",g("Sensitivity","B28"),"| pair:",g("Sensitivity","B29"),"| top crit:",g("Sensitivity","B30"),"| top alt:",g("Sensitivity","C19"))
w2,P2,rk2=whatif(r['comb'],s['P'],0,3.5); chk("whatif rank",[g("Sensitivity",f"C{39+i}") for i in range(m)],rk2); chk("whatif Pi",[g("Sensitivity",f"B{39+i}") for i in range(m)],P2)
ws1=wb["PROMETHEE-I"]
for b,k in enumerate(["Combined","AHP","CRITIC","Entropy"]):
    st=4+22*b; p1=promethee1(r["sets"][k]); xl=dict(zip(">=?",[ws1.cell(st+14,3).value,ws1.cell(st+14,5).value,ws1.cell(st+14,7).value]))
    for sy,nm in ((">","pairs"),("=","indiff"),("?","incomp")): chk("PROMETHEE-I "+nm+" "+k,[xl[sy]],[p1["cnt"][sy]])
    for a in range(12):
        for c2 in range(12):
            if a!=c2 and ws1.cell(st+2+a,2+c2).value!=p1["M"][a][c2]: bad+=1; print("MISMATCH rel",k,a,c2)
print("BAD:",bad)
