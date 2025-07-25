class Color:
    class EntryColor:
        PRIMARY=('#91F5C5','#084E2B')
        TEXT=('#7A0A3F',"#3484DF")
        BORDER=("#000000", "#FFFFFF")  
        #STROKE=("#000000BC", "#FFFFFFCE")
    
    class TitleColor:
        PRIMARY=('#824B40','#DC745D')
        #STROKE=("#000000BC", "#FFFFFFCE")
    
    class ResultColor:
        PRIMARY=("#838639", '#E5E619')
        #STROKE=("#000000BC", "#FFFFFFCE")

    class FrameColor:
        class ResultFrameColor:
            PRIMARY=('#23CDDC', "#120E57")
            BORDER=("#000000", "#FFFFFF") 
        class KeyboardFrameColor:
            BORDER=("#CCCACA", "#8D8B8B") 
        
        class EntryFrameColor:
            PRIMARY='transparent'

        class AppColor:
            PRIMARY=('#FFFFFF', '#000000')

    class Buttons:
        HOVER=("#7C7979", "#CEC6C6")
        #STROKE=("#000000BC", "#FFFFFFCE")
        class NumericButtons:
            PRIMARY=('#14EAEB', '#2b7bb9')
            HOVER=('#2b7bb9', '#14EAEB')
        
        class NonNumericKeyboardButtons:
            PRIMARY=("#B8B1B1", "#3A3A3A")
            Hover=("#3A3A3A", "#B8B1B1")

        class FooterButtons:
            PRIMARY='transparent'
            HOVER=("#A5AD5D", "#D3C470")
            TEXT=("#ABB2B6","#CC5500")

        class EntryButton:
            PRIMARY='transparent'
            HOVER=('#FFFFFF', "#0D5C21")
