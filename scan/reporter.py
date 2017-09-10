import xlwt;

class Reporter:
    def generate_excel(self):
        pass;
    def write_excel(self, data):
        # style0 = xlwt.easyxf('font: name Times New Roman, color-index red, bold on', num_format_str='#,##0.00')
        wb = xlwt.Workbook()
        ws = wb.add_sheet('A Test Sheet')
        titles = ['Package Name','Mtk Apps','Owner','Connect To Internet','Comments'];
        row_num = 0;
        col_num = 0;
        for title in titles:
            ws.write(row_num, col_num, title);
            col_num += 1;
        row_num = 1;
        col_num = 0;
        for pkg_name in data:
            ws.write(row_num, col_num, pkg_name);
            row_num += 1;
        wb.save('../internet_permission_pkg.xls')

    def set_style(self,name = 'Times New Roman', height = 16,bold = False):
        style = xlwt.XFStyle() # 初始化样式  
  
        font = xlwt.Font() # 为样式创建字体  
        font.name = name # 'Times New Roman'  
        font.bold = bold  
        font.color_index = 4  
        font.height = height  

        # borders= xlwt.Borders()  
        # borders.left= 6  
        # borders.right= 6  
        # borders.top= 6  
        # borders.bottom= 6  

        style.font = font  
        # style.borders = borders  

        return style
    




if __name__ == '__main__':
    test = Reporter();
    # test.set_style();
    test.write_excel();
    