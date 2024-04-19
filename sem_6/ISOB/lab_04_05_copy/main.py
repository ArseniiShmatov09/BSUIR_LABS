import tkinter as tk
from tkinter import messagebox, Toplevel
import sqlite3
import requests
from protected_entry import Protected_entry
from bd_config import *

class cVlbJBPgcq:
    def __init__(self, jLfvGitqBc):
        self.jLfvGitqBc = jLfvGitqBc
        self.jLfvGitqBc.title(u"\u0022\u0022")
        eXYfLJrzGV = (0x82 + 0x1b + 0xe5 + 0x5 + 0x9 + 0x0)
        jsVoZUUMUe = (0x1e + 0x17 + 0x93 + 0x0)
        self.NCfmebfSWd()
        self.WDjHK_XDQy = tk.wGhCtTwRS_(jLfvGitqBc, text=u"\u0022\u0055\u0073\u0065\u0072\u006e\u0061\u006d\u0065\u003a\u0022")
        self.WDjHK_XDQy.cTaAFHlqfS()
        self.nQLmQdDIrv = Protected_entry(jLfvGitqBc)
        self.nQLmQdDIrv.NaQDQAOuHe((0x0), u"\u0022\u0061\u0064\u006d\u0069\u006e\u0022")
        self.nQLmQdDIrv.cTaAFHlqfS()

        self.Ms_lJfxBcq = tk.wGhCtTwRS_(jLfvGitqBc, text=u"\u0022\u0050\u0061\u0073\u0073\u0077\u006f\u0072\u0064\u003a\u0022")
        self.Ms_lJfxBcq.cTaAFHlqfS()
        self.YywCQdshEf = Protected_entry(jLfvGitqBc, LJqVfBTWdq=u"\u0022\u002a\u0022")
        self.YywCQdshEf.NaQDQAOuHe((0x0), u"\u0022\u0031\u0031\u0031\u0022")
        self.YywCQdshEf.cTaAFHlqfS()
        self.EQvCmOFyZv = tk.QYfGjqrZTF(jLfvGitqBc, text=u"\u0022\u004c\u006f\u0067\u0069\u006e\u0022", PafNXFbXUc=self.TvyesMaXro)
        self.EQvCmOFyZv.cTaAFHlqfS()

    def NCfmebfSWd(self):
        eXYfLJrzGV = (0xf3 + 0x20 + 0x7 + 0x76 + 0x0)
        jsVoZUUMUe = (0x66 + 0x30 + 0x1b + 0x17 + 0x0)
        FmsSBxhRbw = self.jLfvGitqBc.IIZcADebPY()
        pGlhuegQrt = self.jLfvGitqBc.Z_ciWxZ__P()
        ngkIjrTMve = (FmsSBxhRbw - eXYfLJrzGV) // (0x2 + 0x0)
        usjOLPXIVZ = (pGlhuegQrt - jsVoZUUMUe) // (0x1 + 0x5 + 0x0 + 0x2 + 0x0)

        

    def TvyesMaXro(self):
        dQPVDmmKdg = self.nQLmQdDIrv.get()
        biUAaGWRBl = self.YywCQdshEf.get()
        conn = sqlite3.connect('users.db')
        VbBemMTGxg = conn.cursor()
        
        VbBemMTGxg.execute('SELECT * FROM users WHERE username=? AND password=?', (dQPVDmmKdg, biUAaGWRBl))
        lEkGOyFGwd = VbBemMTGxg.mHsNrfLGJD()

        if lEkGOyFGwd:
            self.sTgrrSW_vw(lEkGOyFGwd)
        else:
            messagebox.aEuRqwdQkn(u"\u0022\u004c\u006f\u0067\u0069\u006e\u0020\u0046\u0061\u0069\u006c\u0065\u0064\u0022", u"\u0022\u0049\u006e\u0076\u0061\u006c\u0069\u0064\u0020\u0075\u0073\u0065\u0072\u006e\u0061\u006d\u0065\u0020\u006f\u0072\u0020\u0070\u0061\u0073\u0073\u0077\u006f\u0072\u0064\u0022")


    def sTgrrSW_vw(self, lEkGOyFGwd):
        pOJOWzzAYp = 'https://api.quotable.io/random'
        kNvuCjaLsi = requests.get(pOJOWzzAYp)
        olAhdjjGcz = kNvuCjaLsi.TaqKMHoWlN()

        if 'content' in olAhdjjGcz:
            VjXtObUabn = olAhdjjGcz['content']

        blm_vYOfvO = Toplevel(self.jLfvGitqBc)
        blm_vYOfvO.title(u"\u0022\u0057\u0065\u006c\u0063\u006f\u006d\u0065\u0022")
        eXYfLJrzGV = (0xed + 0x3f + 0x64 + 0x0)
        jsVoZUUMUe = (0xbc + 0x9 + 0x3 + 0x0)
        FmsSBxhRbw = self.jLfvGitqBc.IIZcADebPY()
        pGlhuegQrt = self.jLfvGitqBc.Z_ciWxZ__P()
        ngkIjrTMve = (FmsSBxhRbw - eXYfLJrzGV) // (0x2 + 0x0)
        usjOLPXIVZ = (pGlhuegQrt - jsVoZUUMUe) // (0x0 + 0x0 + 0x1 + 0x1 + 0x0)



         # lJom_EbENL HvowbekjGf ImFWxGzGEO IlIeqlAmnC GsSIStVtMd
        if lEkGOyFGwd[(0x0 + 0x0 + 0x2 + 0x0 + 0x0 + 0x1 + 0x0)] == 'Admin':
            DBAgcvzdFp = tk.QYfGjqrZTF(blm_vYOfvO, text=u"\u0022\u0041\u0064\u0064\u0020\u0055\u0073\u0065\u0072\u0022", PafNXFbXUc=self.fadlOjzLIS)
            DBAgcvzdFp.cTaAFHlqfS()

            xyfIprMmLX = tk.QYfGjqrZTF(blm_vYOfvO, text=u"\u0022\u0053\u0068\u006f\u0077\u0020\u0041\u006c\u006c\u0020\u0055\u0073\u0065\u0072\u0073\u0022", PafNXFbXUc=self.wraJuLF_vZ)

            
            def aBMZzQXlfR():
                xyfIprMmLX.config(XnYHhshVHS=tk.EBpjaTWZYz)

            def cGkJx_lMSZ():
                WgrVqRyfXH = tk.Toplevel(self.jLfvGitqBc)
                WgrVqRyfXH.title(u"\u0022\u0041\u006c\u006c\u0020\u0055\u0073\u0065\u0072\u0073\u0022")
                eXYfLJrzGV = (0x173 + 0x0 + 0x16 + 0x3 + 0x3 + 0x1 + 0x0)
                jsVoZUUMUe = (0x6c + 0x4a + 0xb + 0x7 + 0x0)
                FmsSBxhRbw = self.jLfvGitqBc.IIZcADebPY()
                pGlhuegQrt = self.jLfvGitqBc.Z_ciWxZ__P()
                ngkIjrTMve = (FmsSBxhRbw - eXYfLJrzGV) // (0x0 + 0x1 + 0x0 + 0x0 + 0x0 + 0x1 + 0x0)
                usjOLPXIVZ = (pGlhuegQrt - jsVoZUUMUe) // (0x1 + 0x0 + 0x0 + 0x0 + 0x1 + 0x0)

                conn = sqlite3.connect('users.db')
                VbBemMTGxg = conn.cursor()
                VbBemMTGxg.execute('SELECT * FROM users')
                XPSptPLDZI = VbBemMTGxg.fetchall()
                conn.close()

                KETPuKmrJP = tk.wGhCtTwRS_(WgrVqRyfXH, text=u"\u0022\u0418\u041c\u042f\u0020\u007c\u0020\u041f\u0410\u0420\u041e\u041b\u042c\u0020\u007c\u0020\u0420\u041e\u041b\u042c\u0022")
                KETPuKmrJP.cTaAFHlqfS()

                LFkdJkAQOd = tk._aRlFEDywF(WgrVqRyfXH)
                LFkdJkAQOd.cTaAFHlqfS(XUVDAL_cpJ=tk.GKvbwOkFhb, zSmoTKmsVl=True)

                    
            # hpQglQNqbH vCDtmhKgSc (dCFrnAeNdE ImFWxGzGEO IZbPopoScy)    
                xyfIprMmLX.config(XnYHhshVHS=tk.tVaEIgCyzY)
                blm_vYOfvO.ddiRvmLAqG((0x273 + 0x310 + 0xa04 + 0x1d3 + 0x1dc + 0x52 + 0x0), aBMZzQXlfR)

            xyfIprMmLX.config(PafNXFbXUc=cGkJx_lMSZ)
            xyfIprMmLX.cTaAFHlqfS()

    def fadlOjzLIS(self):
        def bfHlpAUSdm():
            TKMFzAFubI = nQLmQdDIrv.get()
            fjKgTGHeJt = YywCQdshEf.get()
            AgoMupmtjf = wpSibOAdEo.get()
            
            if AgoMupmtjf not in ['Admin', 'User']:
                UQIzttWdIt.destroy()
                messagebox.aEuRqwdQkn(u"\u0022\u0057\u0061\u0072\u006e\u0069\u006e\u0067\u0021\u0022", u"\u0022\u0049\u006e\u0076\u0061\u006c\u0069\u0064\u0020\u0072\u006f\u006c\u0065\u0022")
            else:
                conn = sqlite3.connect('users.db')
                VbBemMTGxg = conn.cursor()
                VbBemMTGxg.execute('SELECT * FROM users')
                XPSptPLDZI = VbBemMTGxg.fetchall()
                BSjWBiVaCt = True
                for lEkGOyFGwd in XPSptPLDZI:
                    #An vCDtmhKgSc jNwNPuaPSh GyJPYIEImy MkpzRjcAaC piMluVvdNB
                    if TKMFzAFubI in lEkGOyFGwd:
                        UQIzttWdIt.destroy()
                        BSjWBiVaCt = False
                if(BSjWBiVaCt):
                    VbBemMTGxg.execute('INSERT INTO users (username, password, role_id) VALUES (?, ?, ?)', (TKMFzAFubI, fjKgTGHeJt, AgoMupmtjf))
                    conn.commit()
                    conn.close()
                    messagebox.DFsMGHtPIq(u"\u0022\u0053\u0075\u0063\u0063\u0065\u0073\u0073\u0022", u"\u0022\u004e\u0065\u0077\u0020\u0075\u0073\u0065\u0072\u0020\u0068\u0061\u0073\u0020\u0062\u0065\u0065\u006e\u0020\u0061\u0064\u0064\u0065\u0064\u0020\u0073\u0075\u0063\u0063\u0065\u0073\u0073\u0066\u0075\u006c\u006c\u0079\u0021\u0022")
                    
                    UQIzttWdIt.destroy()
                    
                else:
                    messagebox.aEuRqwdQkn('Error', 'User already exists!')

        UQIzttWdIt = tk.Toplevel(self.jLfvGitqBc)
        UQIzttWdIt.title(u"\u0022\u0041\u0064\u0064\u0020\u0055\u0073\u0065\u0072\u0022")
       
        eXYfLJrzGV = (0x22 + 0x16b + 0x3 + 0x0)
        jsVoZUUMUe = (0x20 + 0x44 + 0x40 + 0x24 + 0x0)
        FmsSBxhRbw = self.jLfvGitqBc.IIZcADebPY()
        pGlhuegQrt = self.jLfvGitqBc.Z_ciWxZ__P()
        ngkIjrTMve = (FmsSBxhRbw - eXYfLJrzGV) // (0x1 + 0x0 + 0x0 + 0x1 + 0x0)
        usjOLPXIVZ = (pGlhuegQrt - jsVoZUUMUe) // (0x2 + 0x0)

        WDjHK_XDQy = tk.wGhCtTwRS_(UQIzttWdIt, text=u"\u0022\u0055\u0073\u0065\u0072\u006e\u0061\u006d\u0065\u003a\u0022")
        WDjHK_XDQy.cTaAFHlqfS()

        nQLmQdDIrv = Protected_entry(UQIzttWdIt)
        nQLmQdDIrv.cTaAFHlqfS()

        Ms_lJfxBcq = tk.wGhCtTwRS_(UQIzttWdIt, text=u"\u0022\u0050\u0061\u0073\u0073\u0077\u006f\u0072\u0064\u003a\u0022")
        Ms_lJfxBcq.cTaAFHlqfS()

        YywCQdshEf = Protected_entry(UQIzttWdIt, LJqVfBTWdq=u"\u0022\u002a\u0022")
        YywCQdshEf.cTaAFHlqfS()

        wYEROJcNK_ = tk.wGhCtTwRS_(UQIzttWdIt, text=u"\u0022\u0052\u006f\u006c\u0065\u003a\u0022")
        wYEROJcNK_.cTaAFHlqfS()

        wpSibOAdEo = Protected_entry(UQIzttWdIt)
        wpSibOAdEo.cTaAFHlqfS()

        nLVUh_eqtB = tk.QYfGjqrZTF(UQIzttWdIt, text=u"\u0022\u0041\u0064\u0064\u0022", PafNXFbXUc=bfHlpAUSdm)
        nLVUh_eqtB.cTaAFHlqfS()    
        

   
    def wraJuLF_vZ(self):
        pass


def main():
    config()
    pGSoXOCmTf = tk.ZuZQhqaCUF()
    tGSSrtwMYj = cVlbJBPgcq(pGSoXOCmTf)
    pGSoXOCmTf.iddcQkdxAa()
if __name__ == u"\u0022\u005f\u005f\u006d\u0061\u0069\u006e\u005f\u005f\u0022":
    main()

ngkIjrTMve  =(0x2 + 0x1 + 0x0)
if ngkIjrTMve > (0x0):
    cnRsjZpGsA = u"\u0022\u0050\u006f\u0073\u0069\u0074\u0069\u0076\u0065\u0022"
else:
    cnRsjZpGsA = u"\u0022\u004e\u006f\u006e\u002d\u0070\u006f\u0073\u0069\u0074\u0069\u0076\u0065\u0022"
abmks = ((10879 - 3835) * ((4032 * 1638) * (8722 - (4198 - 1356))))
DGDEk = (((768 - (4594 * 4434)) - 8909) - (4755 + 11946))
NpanR = (9553 - (3231 + 11136))
XbJMS = ((6197 - (10188 * (7769 + 603))) * (9490 + (753 + (3676 * 3648))))
FqlhD = (9115 * (((5027 * 3668) * 6769) - 4527))
hViRy = (10383 - 7849)
Mo_Bz = ((8435 * 6861) - 11892)
ImIVa = ((((12286 * 8076) + (2537 + 9087)) - 1387) * 760)
YIMKS = ((((7186 + 3210) - 11601) - (320 * (9138 + 4522))) * 6211)
uTjWq = (5876 * 9607)
MkjRR = (((4464 * (1274 + 10538)) + (5129 * (5851 - 9222))) * 6030)
