import datetime
import os
import webbrowser

from fpdf import FPDF



filePath = "/home/carlos/Escritorio/tests/"
class FPDF(FPDF):
    title: str
    version: int
    def __init__(self, a, b, c, title, version):
        super().__init__(a, b, c)
        self.title = title
        self.version = version
    def header(self):
        if self.page_no() == 1:
            self.set_font('times', 'B', 42)
            self.set_text_color(102, 0, 255)
            self.cell(95, 20, self.title, align='L', ln=True)
            self.set_font('times', 'B', 10)
            self.cell(95, 5, "made with testGen", align='L', ln=True)
            now = datetime.datetime.now()
            fnow = str(now.day) + "-" + str(now.month) + "-" + str(now.year)
            self.set_text_color(10, 10, 10)
            self.set_font('times', '', 10)
            self.set_fill_color(220, 220, 220)
            self.ln()
            self.cell(95, 7, "Estudiante:", align='L', fill=True, border='BT')
            self.cell(80, 7, "Fecha: " + fnow, align='R', fill=True, border='BT')
            self.cell(15, 7, "v: " + str(self.version), align='R', ln=True, fill=True, border='BT')
            self.set_fill_color(255,255,255)
            self.cell(190, 5, ln=True) # line break
        else:
            self.set_font('times', '', 10)
            self.set_text_color(10,10,10)
            self.cell(95, 5, self.title, align='R', ln=True)
            self.cell(190, 3, border='B', ln=True) # line break
        self.cell(190, 3, ln=True) # line break



    def footer(self):
        self.set_y(-20)
        page_num = self.page_no()
        # print(page_num, len(self.pages))
        self.cell(190, 0, border=True, ln=True)  # line break
        self.set_font('times', 'B', 10)
        self.set_font('times', '', 10)
        self.set_y(-20)
        self.cell(0, 10, str(page_num), align='R')
        self.set_font('times', '', 12)



class generatePDF:
    @staticmethod
    def generarTest(preguntas: dict, respuestas: dict, showAnsers: bool = False, version: int = 0, title: str = "Test"):
        pdf = FPDF('P', 'mm', 'A4', title, version)
        # pdf.add_font("times", "", "LinLibertine_R.ttf", uni=True)
        pdf.add_page()

        pdf.set_font('times', 'B', 12)
        pdf.set_text_color(10, 10, 10)
        # pdf.set_xy(95, 40)
        now = datetime.datetime.now()
        fnow = str(now.day) + "-" + str(now.month) + "-" + str(now.year)
        # pdf.cell(95, 7, "Fecha: " + fnow , align='R', ln=True)
        # pdf.cell(190, 0, border=True, ln=True)
        pdf.set_font('times', '', 12)
        pdf.set_text_color(10, 10, 250)
        pdf.cell(190, 10, "Respuestas", ln=True)
        pdf.set_text_color(10, 10, 10)
        resp_list = list(preguntas.keys())
        for n in range(len(resp_list)):
            l = chr(ord('a') + respuestas[resp_list[n]])
            pdf.cell(15, 10, str(n+1)+": " + (l if showAnsers else ""), border='BTLR', align='L')
            if pdf.get_x() > 190:
                pdf.ln()
        pdf.ln()
        pdf.set_text_color(10, 10, 250)
        pdf.cell(190, 10, "", ln=True)
        pdf.cell(190, 10, "Preguntas", ln=True)
        pdf.set_text_color(10, 10, 10)
        interlineado = 6
        i = 1
        for p in preguntas.keys():
            if pdf.get_y() > 250:
                pdf.add_page()
            pdf.multi_cell(100, interlineado, str(i) + ". " + p, 0,  align='L')
            j = 1
            for r in preguntas[p]:
                pdf.set_x(15)
                l = chr(ord('a') + j - 1)
                if showAnsers and int(respuestas[p]) == j - 1:
                    pdf.set_text_color(10, 150, 10)
                    pdf.multi_cell(100, interlineado, l + ") " + r, 0, align='L')
                    pdf.set_text_color(10, 10, 10)
                else:
                    pdf.multi_cell(100, interlineado, l + ") " + r, 0, align='L')
                j += 1
            pdf.cell(190, interlineado, "", 0, True)
            i += 1
        # pdf.cell(190, 0, border=True, ln=True)
        # 10 190 10
        # 95, 95
        # 47.5, 47.5 = 20 + 75

        pdf.output(filePath + title + "-" + ("v"+str(version)+"-" if version is not None else "") + ("SOL-" if showAnsers else "") +  fnow + ".pdf")

