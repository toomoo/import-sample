#coding: utf-8

#################################################
# Note: 色々情報あったけど、PEP*違反の話とか書いてあったのでここを記録
# https://note.com/iamhacchin/n/n8eb3efafadf9
#################################################
 
if __name__ == '__main__':
    import parent 
else:
    #from package import parent
    import pprint
    import sys
    pprint.pprint(sys.path)
    sys.path.append('../')
    pprint.pprint(sys.path)
    from package import parent


class childAnalyzer(parent.Analyzer):
    def __init__(self):
        super().__init__()
        print('childAnalyzer')


if __name__ == '__main__':
    sa = childAnalyzer()

