import datetime
import os
from PIL import Image
from io import BytesIO
from fpdf import FPDF


filePath = "output/"


if not os.path.exists(filePath):
    os.makedirs(filePath)
    

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
            self.cell(95, 5, "made with testGen",link ="https://github.com/carlosdelolmo/testGen", align='L', ln=True)
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
            self.cell(190, 5, self.title, align='C', ln=True)
            self.cell(190, 3, border='B', ln=True) # line break
        self.cell(190, 3, ln=True) # line break


    def footer(self):
        self.set_y(-20)
        page_num = self.page_no()
        self.cell(190, 0, border=True, ln=True)  # line break
        self.set_font('times', 'B', 10)
        self.set_font('times', '', 10)
        self.set_y(-20)
        self.cell(0, 10, str(page_num), align='R')
        self.set_font('times', '', 12)


class generatePDF:
    @staticmethod
    def generarTest(preguntas: dict, respuestas: dict, order: list, showAnsers: bool = False, version: int = 0, title: str = "Test"):
        pdf = FPDF('P', 'mm', 'A4', title, version)
        pdf.add_page()

        pdf.set_font('times', 'B', 12)
        pdf.set_text_color(10, 10, 10)
        now = datetime.datetime.now()
        fnow = str(now.day) + "-" + str(now.month) + "-" + str(now.year)
        pdf.set_font('times', '', 12)
        pdf.set_text_color(10, 10, 250)
        pdf.cell(190, 10, "Respuestas", ln=True)
        pdf.set_text_color(10, 10, 10)
        resp_list = list(preguntas.keys())
        i = 0
        for index in order:
            l = chr(ord('a') + respuestas[resp_list[index]])
            pdf.cell(15, 10, str(i+1)+": " + (l if showAnsers else ""), border='BTLR', align='L')
            if pdf.get_x() > 190:
                pdf.ln()
            i += 1

        pdf.ln()
        pdf.set_text_color(10, 10, 250)
        pdf.cell(190, 10, "", ln=True)
        pdf.cell(190, 10, "Preguntas", ln=True)
        pdf.set_text_color(10, 10, 10)
        interlineado = 6
        i = 1
        for index in order:
            p = resp_list[index]
            x = pdf.get_x()
            if pdf.get_y() > 250:
                pdf.add_page()
                pdf.set_x(x)
            splittedP = p.split("$")
            hasImg = len(splittedP) > 1
            if hasImg:
                img = splittedP[1]
            cleanP = splittedP[0].strip("\n")
            if hasImg:
                    if os.path.exists(img):
                        pdf.multi_cell(190, interlineado, str(i) + ". " + cleanP, 0,  align='L')
                        pdf.image(img, x = None, y = None, w = 170, h = 0, type = '', link = '')
                    else:
                        raise Exception
            else:
                pdf.multi_cell(190, interlineado, str(i) + ". " + cleanP, 0,  align='L')
            j = 1
            for r in preguntas[p]:
                pdf.set_x(15)
                l = chr(ord('a') + j - 1)
                if showAnsers and int(respuestas[p]) == j - 1:
                    pdf.set_text_color(10, 150, 10)
                    splittedR = r.split("$")
                    hasImg = len(splittedR) > 1
                    if hasImg:
                        img = splittedR[1]
                    cleanR = splittedR[0].strip("\n")
                    if hasImg:
                        if os.path.exists(img):
                            pdf.multi_cell(100, interlineado, l + ") " + cleanR, 0,  align='L')
                            pdf.image(img, x = pdf.get_x() + 20, y = None, w = 50, h = 0, type = '', link = '')
                        else:
                            raise Exception
                    else:
                        pdf.multi_cell(100, interlineado, l + ") " + cleanR, 0, align='L')
                    pdf.set_text_color(10, 10, 10)
                else:
                    splittedR = r.split("$")
                    hasImg = len(splittedR) > 1
                    if hasImg:
                        img = splittedR[1]
                    cleanR = splittedR[0].strip("\n")
                    if hasImg:
                        if os.path.exists(img):
                            pdf.multi_cell(100, interlineado, l + ") " + cleanR, 0,  align='L')
                            pdf.image(img, x = pdf.get_x() + 20, y = None, w = 50, h = 0, type = '', link = '')
                        else:
                            raise Exception
                    else:
                        pdf.multi_cell(100, interlineado, l + ") " + cleanR, 0, align='L')
                j += 1
            pdf.cell(190, interlineado, "", 0, True)
            i += 1
        # pdf.cell(190, 0, border=True, ln=True)
        # 10 190 10
        # 95, 95
        # 47.5, 47.5 = 20 + 75

        pdf.output(filePath + title + "-" + ("v"+str(version)+"-" if version is not None else "") + ("SOL-" if showAnsers else "") +  fnow + ".pdf")

