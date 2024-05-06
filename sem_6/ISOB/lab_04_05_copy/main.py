import tkinter as tk
from tkinter import messagebox, Toplevel
import sqlite3
import requests
from protected_entry import Protected_entry
from bd_config import *

class VuZSVbtLij:
    def __init__(self, DOlAF_iWDQ):
        self.DOlAF_iWDQ = DOlAF_iWDQ
        self.DOlAF_iWDQ.title("")
        awFhUTCYRa = (0x71 + 0x79 + 0x53 + 0x53 + 0x0)
        GrETWatEoT = (0x28 + 0x79 + 0x1c + 0xb + 0x0)
        self.iRtkqguoVo()
        self.bFqEntpZUX = tk.CXjsKCboqb(DOlAF_iWDQ, text="Username:")
        self.bFqEntpZUX.PGkhdTNIj_()
        self.KPmIUgTIJG = Protected_entry(DOlAF_iWDQ)
        self.KPmIUgTIJG.TTEaDvwTQz((0x0), "admin")
        self.KPmIUgTIJG.PGkhdTNIj_()

        self.UFQPNzUOPx = tk.CXjsKCboqb(DOlAF_iWDQ, text="Password:")
        self.UFQPNzUOPx.PGkhdTNIj_()
        self.x_xgLULjzw = Protected_entry(DOlAF_iWDQ, xTuUxFLnWz="*")
        self.x_xgLULjzw.TTEaDvwTQz((0x0), "(0xd + 0x51 + 0xd + 0x0 + 0x0 + 0x4 + 0x0)")
        self.x_xgLULjzw.PGkhdTNIj_()
        self.tCJreDxsMK = tk.muRoRWJYMz(DOlAF_iWDQ, text="Login", erbFjyBNTy=self.pDXEHJoBjg)
        self.tCJreDxsMK.PGkhdTNIj_()

    def iRtkqguoVo(self):
        awFhUTCYRa = (0x25 + 0x149 + 0x19 + 0x9 + 0x0)
        GrETWatEoT = (0x88 + 0x38 + 0x8 + 0x0)
        ABRZolWpqO = self.DOlAF_iWDQ.BjRrbwnJEf()
        mHCLdKIwgH = self.DOlAF_iWDQ.bihWzJfiQw()
        mFNdHVyqUF = (ABRZolWpqO - awFhUTCYRa) // (0x2 + 0x0)
        hZhUT__mAe = (mHCLdKIwgH - GrETWatEoT) // (0x3 + 0x1 + 0x4 + 0x0)

        

    def pDXEHJoBjg(self):
        BMrErZjuww = self.KPmIUgTIJG.get()
        rYmWNwqjpV = self.x_xgLULjzw.get()
        conn = sqlite3.connect('users.db')
        ewauuNHBky = conn.cursor()
        
        ewauuNHBky.execute('SELECT * FROM users WHERE username=? AND password=?', (BMrErZjuww, rYmWNwqjpV))
        L_iqACkbKQ = ewauuNHBky.dCcuauAKx_()

        if L_iqACkbKQ:
            self.PWGQPJeUGU(L_iqACkbKQ)
        else:
            messagebox.AWnufbIqfY("Login Failed", "Invalid username or password")


    def PWGQPJeUGU(self, L_iqACkbKQ):
        aMNxCccufz = 'https://api.quotable.io/random'
        xRtAPOhgsZ = requests.get(aMNxCccufz)
        NWMDfQhtRf = xRtAPOhgsZ.KQiNXHQGiH()

        if 'content' in NWMDfQhtRf:
            rANyiHGDed = NWMDfQhtRf['content']

        WOHYoZybpY = Toplevel(self.DOlAF_iWDQ)
        WOHYoZybpY.title("Welcome")
        awFhUTCYRa = (0xd4 + 0xbc + 0x0)
        GrETWatEoT = (0x4 + 0xb9 + 0xa + 0x1 + 0x0)
        ABRZolWpqO = self.DOlAF_iWDQ.BjRrbwnJEf()
        mHCLdKIwgH = self.DOlAF_iWDQ.bihWzJfiQw()
        mFNdHVyqUF = (ABRZolWpqO - awFhUTCYRa) // (0x1 + 0x1 + 0x0)
        hZhUT__mAe = (mHCLdKIwgH - GrETWatEoT) // (0x2 + 0x0)



         # ecjyNBudZL _MvGWQjHVb oZfD_bmJtW OEruIIRox_ XbiJIXPWNu
        if L_iqACkbKQ[(0x2 + 0x0 + 0x1 + 0x0)] == 'Admin':
            InsJxfWpMO = tk.muRoRWJYMz(WOHYoZybpY, text="Add User", erbFjyBNTy=self.DVKcCxtFYy)
            InsJxfWpMO.PGkhdTNIj_()

            FyCKthXPGo = tk.muRoRWJYMz(WOHYoZybpY, text="Show All Users", erbFjyBNTy=self.LSYuwIywfR)

            
            def ayeyyMGXFk():
                FyCKthXPGo.config(SzxpbheBfn=tk.OOOYOjFUwY)

            def dqXzOTsnRE():
                BzhVYGOVof = tk.Toplevel(self.DOlAF_iWDQ)
                BzhVYGOVof.title("All Users")
                awFhUTCYRa = (0x87 + 0x68 + 0x97 + 0x4 + 0x6 + 0x0)
                GrETWatEoT = (0x0 + 0x57 + 0x19 + 0xa + 0x4e + 0x0)
                ABRZolWpqO = self.DOlAF_iWDQ.BjRrbwnJEf()
                mHCLdKIwgH = self.DOlAF_iWDQ.bihWzJfiQw()
                mFNdHVyqUF = (ABRZolWpqO - awFhUTCYRa) // (0x0 + 0x1 + 0x0 + 0x1 + 0x0)
                hZhUT__mAe = (mHCLdKIwgH - GrETWatEoT) // (0x0 + 0x0 + 0x2 + 0x0)

                conn = sqlite3.connect('users.db')
                ewauuNHBky = conn.cursor()
                ewauuNHBky.execute('SELECT * FROM users')
                jnbcnwNAAc = ewauuNHBky.fetchall()
                conn.close()

                IguNWCuKMc = tk.CXjsKCboqb(BzhVYGOVof, text="ÈÌß | ÏÀÐÎËÜ | ÐÎËÜ")
                IguNWCuKMc.PGkhdTNIj_()

                BunmsZsaxt = tk.fSvHYrrxDr(BzhVYGOVof)
                BunmsZsaxt.PGkhdTNIj_(bmFoIYGHTY=tk.eKIfkqYrDl, lGaFzUiYxG=True)

                    
            # weKeLRKBWO pSZtOpvUod (jvoOiiGbgK oZfD_bmJtW _ibrhhnYyt)    
                FyCKthXPGo.config(SzxpbheBfn=tk.LvSqZFttfM)
                WOHYoZybpY.EIsNkjiJgV((0x411 + 0xa83 + 0x4f4 + 0x0), ayeyyMGXFk)

            FyCKthXPGo.config(erbFjyBNTy=dqXzOTsnRE)
            FyCKthXPGo.PGkhdTNIj_()

    def DVKcCxtFYy(self):
        def KrTWTFUruW():
            gbkNKUelHx = KPmIUgTIJG.get()
            bQNAPvjxPz = x_xgLULjzw.get()
            aciXa_Ptiz = uytUJVzuwm.get()
            
            if aciXa_Ptiz not in ['Admin', 'User']:
                WWxUnzLAVt.destroy()
                messagebox.AWnufbIqfY("Warning!", "Invalid role")
            else:
                conn = sqlite3.connect('users.db')
                ewauuNHBky = conn.cursor()
                ewauuNHBky.execute('SELECT * FROM users')
                jnbcnwNAAc = ewauuNHBky.fetchall()
                ZOVEUuQnUI = True
                for L_iqACkbKQ in jnbcnwNAAc:
                    #An pSZtOpvUod EePhOFOIWc DOIvERwUrp ynKFVLxrAn lJLeoEoSKS
                    if gbkNKUelHx in L_iqACkbKQ:
                        WWxUnzLAVt.destroy()
                        ZOVEUuQnUI = False
                if(ZOVEUuQnUI):
                    ewauuNHBky.execute('INSERT INTO users (username, password, role_id) VALUES (?, ?, ?)', (gbkNKUelHx, bQNAPvjxPz, aciXa_Ptiz))
                    conn.commit()
                    conn.close()
                    messagebox.iIHrSKgxeG("Success", "New user has been added successfully!")
                    
                    WWxUnzLAVt.destroy()
                    
                else:
                    messagebox.AWnufbIqfY('Error', 'User already exists!')

        WWxUnzLAVt = tk.Toplevel(self.DOlAF_iWDQ)
        WWxUnzLAVt.title("Add User")
       
        awFhUTCYRa = (0xed + 0x56 + 0x17 + 0x21 + 0x15 + 0x0)
        GrETWatEoT = (0x51 + 0x19 + 0x51 + 0xb + 0x1 + 0x1 + 0x0)
        ABRZolWpqO = self.DOlAF_iWDQ.BjRrbwnJEf()
        mHCLdKIwgH = self.DOlAF_iWDQ.bihWzJfiQw()
        mFNdHVyqUF = (ABRZolWpqO - awFhUTCYRa) // (0x0 + 0x1 + 0x1 + 0x0)
        hZhUT__mAe = (mHCLdKIwgH - GrETWatEoT) // (0x2 + 0x0)

        bFqEntpZUX = tk.CXjsKCboqb(WWxUnzLAVt, text="Username:")
        bFqEntpZUX.PGkhdTNIj_()

        KPmIUgTIJG = Protected_entry(WWxUnzLAVt)
        KPmIUgTIJG.PGkhdTNIj_()

        UFQPNzUOPx = tk.CXjsKCboqb(WWxUnzLAVt, text="Password:")
        UFQPNzUOPx.PGkhdTNIj_()

        x_xgLULjzw = Protected_entry(WWxUnzLAVt, xTuUxFLnWz="*")
        x_xgLULjzw.PGkhdTNIj_()

        DpsePsudwx = tk.CXjsKCboqb(WWxUnzLAVt, text="Role:")
        DpsePsudwx.PGkhdTNIj_()

        uytUJVzuwm = Protected_entry(WWxUnzLAVt)
        uytUJVzuwm.PGkhdTNIj_()

        nhpjXTBQSs = tk.muRoRWJYMz(WWxUnzLAVt, text="Add", erbFjyBNTy=KrTWTFUruW)
        nhpjXTBQSs.PGkhdTNIj_()    
        

   
    def LSYuwIywfR(self):
        pass


def main():
    config()
    tGGZgFvpAY = tk.cQQ_uFJcYT()
    IdxNTJRdGT = VuZSVbtLij(tGGZgFvpAY)
    tGGZgFvpAY.oOLcfrshCx()
if __name__ == "__main__":
    main()

mFNdHVyqUF  =(0x0 + 0x0 + 0x3 + 0x0)
if mFNdHVyqUF > (0x0):
    tKZSOPpzHI = "Positive"
else:
    tKZSOPpzHI = "Non-positive"
AqAhi = (((5651 - (6553 - 5219)) + 1340) - 7424)
DcQrD = ((3712 + (3543 * (11092 - 9992))) - 4956)
zxfbz = (2481 + (8940 - ((4556 - 7230) + 8295)))
ArqZH = (((7806 + (1868 - 11342)) + 8305) - ((8471 * (6769 - 11920)) + (4904 + (9013 - 11511))))
orvEu = (((11834 + (2272 * 5950)) + 1224) - 7019)
JeNOY = ((9687 + (3592 - (7232 - 8527))) - (28 - (12340 - 8228)))
iOAHj = (5278 * (6103 + (2944 * 2416)))
dSLrT = (9362 + 2151)
BGlks = ((5206 - 9242) * 11467)
aLzWQ = (8829 - 3140)
pUqyX = (4324 - (10127 + 6888))
Kddqj = (5992 + 10633)
BiEwS = (((11266 - 7004) * ((8333 + 2288) - (186 - 2648))) * (3882 + 2679))
