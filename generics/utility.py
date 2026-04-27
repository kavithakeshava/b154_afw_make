import  openpyxl

class Utility:

    @staticmethod
    def read_xl(xl_path,sheet_name,row,col):
        value=""
        try:
            wb=openpyxl.load_workbook(xl_path)
            value=wb[sheet_name].cell(row,col).value
            print("data from xl",value)
            wb.close()
        except Exception as e:
            print("error while reading data:",e)

        return value